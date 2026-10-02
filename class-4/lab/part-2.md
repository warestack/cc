### Week 4 Part 2: Users, Passwords, and Login

In this part, you will create users, hash passwords, and build a login endpoint.

#### What You Will Learn

- How to create a user table.
- Why passwords must be hashed.
- How to register a user.
- How to verify a password during login.
- How to create a JWT access token.

#### Part A: Create Database Files

1. Create `database.py`:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Store users in a local SQLite file called auth.db.
DATABASE_URL = "sqlite:///./auth.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    # Open one database session for the request.
    db = SessionLocal()
    try:
        yield db
    finally:
        # Close it after the request finishes.
        db.close()
```

This file prepares the database connection for the authentication API.

- `auth.db` is the SQLite file that will store users.
- `engine` connects SQLAlchemy to the SQLite database.
- `SessionLocal` creates sessions for database work.
- `Base` is used by the `User` model.
- `get_db()` gives each API request its own database session and closes it afterwards.

2. Create `models.py`:

```python
from sqlalchemy import Column, Integer, String

from database import Base


# User describes the users table.
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)

    # Each email must be unique because users log in with email.
    email = Column(String, unique=True, index=True, nullable=False)

    # Store the hashed password, never the original password.
    hashed_password = Column(String, nullable=False)
```

This model creates the `users` table.

- `id` uniquely identifies each user.
- `username` stores the display name.
- `email` is unique because users log in with their email address.
- `hashed_password` stores the password hash, not the original password.

#### Part B: Create Auth Schemas

3. Create `schemas.py`:

```python
from pydantic import BaseModel, ConfigDict, EmailStr, Field


# Request body for registration.
class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=6)


# Request body for login.
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Response body for a user.
# Notice that the password is not included.
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


# Response body returned after login.
class TokenResponse(BaseModel):
    access_token: str
    token_type: str
```

These schemas describe the data that enters and leaves the auth API.

- `UserCreate` is used for registration.
- `UserLogin` is used for login.
- `UserResponse` is returned after registration and does not include the password.
- `TokenResponse` is returned after login and contains the JWT access token.
- `ConfigDict(from_attributes=True)` lets Pydantic read data from SQLAlchemy user objects.

#### Part C: Create Security Helpers

4. Create `security.py`:

```python
from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext

# In a real app, this should come from an environment variable.
SECRET_KEY = "change-this-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# passlib manages password hashing and verification.
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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
```

This file handles passwords and tokens.

- `hash_password()` turns a plain password into a hash before storing it.
- `verify_password()` checks a login password against the stored hash.
- `create_access_token()` creates a signed JWT.
- The token stores a small piece of user information and an expiry time.

> [!WARNING]
>
> The `SECRET_KEY` here is only for the lab. In a real application, secrets must not be hard-coded in source code.

#### Part D: Create Auth Routes

5. Create a folder:

```text
routers
```

6. Inside `routers`, create an empty file:

```text
__init__.py
```

7. Create `routers/auth.py`:

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db
from security import create_access_token, hash_password, verify_password

router = APIRouter()


@router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check whether another user already has this email.
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()

    if existing_user is not None:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create a database user.
    # The password is hashed before it is stored.
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    # Save the new user and reload it so the generated ID is available.
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.post("/login", response_model=schemas.TokenResponse)
def login(user_login: schemas.UserLogin, db: Session = Depends(get_db)):
    # Find the user by email.
    user = db.query(models.User).filter(models.User.email == user_login.email).first()

    if user is None:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    # Compare the submitted password with the stored hash.
    if not verify_password(user_login.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    # Put the user's email in the token subject.
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
```

This router contains the registration and login endpoints.

- `POST /auth/register` checks for duplicate emails, hashes the password, and stores the user.
- `response_model=schemas.UserResponse` prevents the hashed password from being returned.
- `POST /auth/login` finds the user by email.
- `verify_password(...)` checks the submitted password.
- If the login is correct, the API returns a bearer token.

#### Part E: Connect the App

8. Replace `main.py` with:

```python
from fastapi import FastAPI

import models
from database import engine
from routers import auth

# Create the users table if it does not exist.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# All auth routes start with /auth.
app.include_router(auth.router, prefix="/auth")


@app.get("/")
def home():
    return {"message": "Week 4 auth API is running"}
```

This file starts the FastAPI app and connects the routers.

- `create_all(...)` creates the `users` table if needed.
- `app.include_router(auth.router, prefix="/auth")` places the auth routes under `/auth`.
- The home route is a simple check that the API is running.

9. Run:

```bash
uvicorn main:app --reload
```

10. Open:

```text
http://127.0.0.1:8000/docs
```

11. Test `POST /auth/register`.

Use:

```json
{
  "username": "stelios",
  "email": "stelios@example.com",
  "password": "secret123"
}
```

12. Test `POST /auth/login` with the same email and password.

You should receive:

```json
{
  "access_token": "...",
  "token_type": "bearer"
}
```
![login](images/week4_lab_2.png "login")

> **Quick question**
>
> Why do we store `hashed_password` instead of the original password?
>
> <details>
> <summary>Show answer</summary>
>
> If the database is leaked, hashed passwords are much safer than plain text passwords.
>
> </details>

Part 2 is complete. Continue to [Part 3](part-3.md).
