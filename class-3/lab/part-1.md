### Week 3 Part 1: Create a Local SQLite Database with SQLAlchemy

In Week 2, you used SQLite directly. In this part, you will use SQLAlchemy to create and use a SQLite database from Python.

SQLAlchemy is a Python library that helps us work with databases. Instead of writing SQL commands everywhere, we can create Python classes that represent database tables.

#### What You Will Learn

- What an ORM is.
- How a SQLAlchemy model represents a table.
- How to create a local SQLite database.
- How to insert and read data using a session.

#### Part A: Open a New Project Folder

1. Close your previous project in VS Code.

2. Create a new folder:

```text
week3-sqlalchemy-api
```

3. Open this folder in VS Code.

4. Create and activate a virtual environment.

5. Create `requirements.txt`:

```text
sqlalchemy
```

6. Install the requirements:

```bash
python -m pip install -r requirements.txt
```

#### Part B: Create the Database Code

7. Create `database.py`.

8. Add:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# This creates a SQLite database file called courses.db.
# sqlite:/// means "use a local SQLite file".
DATABASE_URL = "sqlite:///./courses.db"

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
```

This code creates the database connection setup.

- `DATABASE_URL` tells SQLAlchemy which database file to use.
- `engine` is the object that connects SQLAlchemy to SQLite.
- `SessionLocal` creates database sessions. A session is used to read and write data.
- `Base` is the parent class for our database models.

> **Quick question**
>
> What file will be created by this database connection?
>
> <details>
> <summary>Show answer</summary>
>
> A local SQLite file called `courses.db`.
>
> </details>

#### Part C: Create a Model

9. Create `models.py`.

10. Add:

```python
from sqlalchemy import Column, Integer, String

from database import Base


# Course is a Python class, but SQLAlchemy maps it to the courses table.
class Course(Base):
    # This is the table name that will be created in SQLite.
    __tablename__ = "courses"

    # id is the primary key. SQLite will generate it automatically.
    id = Column(Integer, primary_key=True, index=True)

    # code must be unique, so two courses cannot use the same code.
    code = Column(String, unique=True, nullable=False)

    # nullable=False means this column is required.
    title = Column(String, nullable=False)
    lecturer = Column(String, nullable=False)
```

This code defines the shape of the `courses` table using Python.

- `Course` is a model class.
- `__tablename__ = "courses"` means the table will be called `courses`.
- Each `Column(...)` becomes one column in the database table.
- `primary_key=True` marks `id` as the unique identifier for each row.
- `unique=True` prevents two courses from having the same course code.
- `nullable=False` means the column must have a value.

In this model:

- `__tablename__` is the table name.
- `id` is the primary key.
- `code`, `title`, and `lecturer` are text columns.
- `nullable=False` means the value is required.
- `unique=True` means the course code cannot be repeated.

<details>
<summary>What is the table name created by this model?</summary>

```text
courses
```

</details>

#### Part D: Create and Seed the Database

11. Create `seed.py`.

12. Add:

```python
import models
from database import SessionLocal, engine

# Create all tables described by the models.
# If the courses table does not exist yet, this line creates it.
models.Base.metadata.create_all(bind=engine)

# Open a database session.
# We use this session to add, query, commit, and close database work.
db = SessionLocal()

try:
    courses = [
        models.Course(code="CC101", title="Cloud Computing", lecturer="Stelios"),
        models.Course(code="DB101", title="Databases", lecturer="Maria"),
    ]

    for course in courses:
        # Check by course code first so running seed.py twice does not add duplicates.
        existing_course = (
            db.query(models.Course)
            .filter(models.Course.code == course.code)
            .first()
        )

        if existing_course is None:
            db.add(course)

    # commit() saves the pending inserts to courses.db.
    db.commit()

    print("Database created and courses checked.")

finally:
    # Always close the session when the database work is finished.
    db.close()
```

This script creates the table and inserts starter data.

- `create_all(...)` creates the table if it does not exist.
- `SessionLocal()` opens a session so Python can work with the database.
- `db.query(...).filter(...).first()` checks whether a course already exists.
- `db.add(course)` prepares a new row to be inserted.
- `db.commit()` saves the changes.
- `db.close()` closes the database session.

13. Run:

```bash
python seed.py
```

You should see:

```text
Database created and courses checked.
```

#### Part E: Read the Data

14. Create `read_courses.py`.

15. Add:

```python
import models
from database import SessionLocal

db = SessionLocal()

try:
    # Query the Course model. SQLAlchemy translates this into SELECT * FROM courses.
    courses = db.query(models.Course).all()

    for course in courses:
        print(course.id, course.code, course.title, course.lecturer)

finally:
    db.close()
```

This script reads rows from the database.

- `db.query(models.Course).all()` asks for all courses.
- Each result is a `Course` object, so we can use `course.code`, `course.title`, and `course.lecturer`.
- The `finally` block closes the session even if something goes wrong.

16. Run:

```bash
python read_courses.py
```

You should see the courses printed in the terminal.

> **Quick question**
>
> What does `db.query(models.Course).all()` do?
>
> <details>
> <summary>Show answer</summary>
>
> It asks SQLAlchemy to select all rows from the `courses` table and return them as `Course` objects.
>
> </details>

#### Part F: Stop and Check

17. Make sure your folder now contains:

```text
database.py
models.py
seed.py
read_courses.py
requirements.txt
courses.db
```

Part 1 is complete. Continue to [Part 2](part-2.md).
