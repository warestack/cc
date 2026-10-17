from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db
from security import create_access_token, hash_password, verify_password

router = APIRouter()


@router.post("/register", response_model=schemas.UserResponse, status_code=201)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check whether another user already has this email.
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()

    if existing_user is not None:
        raise HTTPException(status_code=409, detail="Email already registered")

    # Create a database user.
    # The password is hashed before it is stored.
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    # Save the new user and reload it so the generated ID is available.
    db.add(db_user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Email already registered")
    db.refresh(db_user)
    return db_user


@router.post("/login", response_model=schemas.TokenResponse)
def login(user_login: schemas.UserLogin, db: Session = Depends(get_db)):
    # Find the user by email.
    user = db.query(models.User).filter(models.User.email == user_login.email).first()

    if user is None:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # Compare the submitted password with the stored hash.
    if not verify_password(user_login.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # Put the user's email in the token subject.
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
