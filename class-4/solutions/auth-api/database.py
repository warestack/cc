from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Store users in a local SQLite file called auth.db.
DATABASE_PATH = Path(__file__).resolve().parent / "auth.db"
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

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
