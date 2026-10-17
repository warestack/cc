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
