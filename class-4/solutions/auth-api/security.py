from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session

import models
from database import get_db
from datetime import datetime, timedelta, timezone

import os

import jwt
from pwdlib import PasswordHash

# Read the same secret on each restart; never commit its value.
SECRET_KEY = os.environ["JWT_SECRET"]
if len(SECRET_KEY) < 32:
    raise RuntimeError("JWT_SECRET must contain at least 32 characters")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# pwdlib uses Argon2 to hash and verify passwords.
password_context = PasswordHash.recommended()


def hash_password(password: str) -> str:
    # Convert a plain password into a secure hash.
    return password_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Check whether a plain password matches the stored hash.
    return password_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    # Copy the data we want to place inside the token.
    to_encode = data.copy()

    # Add an expiry time so the token is not valid forever.
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    # Sign and return the JWT.
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# HTTPBearer tells FastAPI to expect an Authorization: Bearer <token> header.
bearer_scheme = HTTPBearer(auto_error=False)

def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    db: Session = Depends(get_db)
):
    if credentials is None:
        raise HTTPException(status_code=401, detail="Not authenticated")

    # Extract the token value from the Authorization header.
    token = credentials.credentials

    try:
        # Decode and verify the JWT.
        payload = jwt.decode(
            token, SECRET_KEY, algorithms=[ALGORITHM],
            options={"require": ["exp", "sub"]}
        )

        # We stored the user's email in the token subject.
        email = payload.get("sub")

        if not isinstance(email, str) or not email:
            raise HTTPException(status_code=401, detail="Invalid token")

    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Find the user represented by the token.
    user = db.query(models.User).filter(models.User.email == email).first()

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user
