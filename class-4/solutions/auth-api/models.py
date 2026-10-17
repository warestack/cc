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
