from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# This creates a SQLite database file called books.db.
# sqlite:/// means "use a local SQLite file".
DATABASE_PATH = Path(__file__).resolve().parent / "books.db"
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# The engine is the connection point between SQLAlchemy and the database.
engine = create_engine(
    DATABASE_URL,
    # SQLite normally checks that one connection is used by one thread.
    # We disable that check because FastAPI can handle requests in different threads.
    connect_args={"check_same_thread": False}
)

# SessionLocal creates database sessions.
# A session is the object we use to talk to the database.
# autocommit=False means we choose when to save changes with db.commit().
# autoflush=False keeps SQLAlchemy from sending changes before we ask it to.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is used by our models.
# Every SQLAlchemy model class will inherit from this Base.
Base = declarative_base()


def get_db():
    # Open a database session for one API request.
    db = SessionLocal()
    try:
        # yield gives the open session to the route function.
        yield db
    finally:
        # Always close the session after the request finishes.
        db.close()
