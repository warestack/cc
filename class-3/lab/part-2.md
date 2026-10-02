### Week 3 Part 2: Build a FastAPI App with SQLAlchemy

In this part, you will use the same database model inside a FastAPI app.

The important idea is this: FastAPI handles the web request, and SQLAlchemy handles the database work.

#### What You Will Learn

- How to install FastAPI in the same project.
- How to create a database dependency.
- How to return database rows from an API route.
- How to create a new database row from an API request.

#### Part A: Update the Requirements

1. Open `requirements.txt`.

2. Replace it with:

```text
fastapi==0.141.1;
uvicorn==0.52.4;
sqlalchemy;
```

3. Install:

```bash
python -m pip install -r requirements.txt
```

#### Part B: Add a Database Dependency

4. Open `database.py`.

5. Add this function at the bottom:

```python
def get_db():
    # Open a database session for one API request.
    db = SessionLocal()
    try:
        # yield gives the open session to the route function.
        yield db
    finally:
        # Always close the session after the request finishes.
        db.close()
```

This function gives a database session to FastAPI routes.

- `db = SessionLocal()` opens a session.
- `yield db` gives that session to the endpoint.
- The `finally` block closes the session after the request finishes.
- This keeps database work organised and avoids leaving connections open.

FastAPI will use this function to give each route a database session.

> **Quick question**
>
> Why do we close the database session after each request?
>
> <details>
> <summary>Show answer</summary>
>
> Because the connection is no longer needed. Closing it avoids wasting database resources.
>
> </details>

#### Part C: Create the FastAPI App

6. Create `main.py`.

7. Add:

```python
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import models
from database import engine, get_db

# Create the database tables when the app starts.
# This uses the Course model from models.py.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Week 3 SQLAlchemy API is running"}


@app.get("/courses")
def get_courses(db: Session = Depends(get_db)):
    # Depends(get_db) asks FastAPI to open a database session for this request.
    # Read all courses from the database.
    courses = db.query(models.Course).all()
    return courses


@app.get("/courses/{course_id}")
def get_course(course_id: int, db: Session = Depends(get_db)):
    # Find one course by primary key.
    # .first() returns one Course object or None.
    course = db.query(models.Course).filter(models.Course.id == course_id).first()

    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    return course


@app.post("/courses")
def create_course(course_data: dict, db: Session = Depends(get_db)):
    # This first version accepts a plain dictionary.
    # In Part 3, we will replace it with Pydantic validation.
    # The keys must match the JSON fields sent by the client.
    course = models.Course(
        code=course_data["code"],
        title=course_data["title"],
        lecturer=course_data["lecturer"]
    )

    try:
        # Add the new object to the session, then commit it to the database.
        db.add(course)
        db.commit()

        # Refresh loads database-generated values such as id.
        db.refresh(course)
        return course

    except IntegrityError:
        # If the unique course code is repeated, undo the failed transaction.
        db.rollback()
        raise HTTPException(status_code=400, detail="Course code already exists")
```

This code turns the SQLAlchemy database into a FastAPI API.

- `Depends(get_db)` gives each route a database session.
- `GET /courses` reads all rows from the `courses` table.
- `GET /courses/{course_id}` reads one row by ID and returns `404` if it does not exist.
- `POST /courses` creates a new `Course` object from the request body.
- `db.commit()` saves the new course.
- `db.refresh(course)` reloads the course so the generated `id` is available.
- `IntegrityError` is used here to catch repeated course codes.

#### Part D: Run the API

8. Run:

```bash
uvicorn main:app --reload
```

9. Open the browser:

```text
http://127.0.0.1:8000/
```

You should see:

```json
{"message":"Week 3 SQLAlchemy API is running"}
```

10. Open:

```text
http://127.0.0.1:8000/courses
```

You should see the courses from Part 1.

11. Open:

```text
http://127.0.0.1:8000/docs
```

12. Test `POST /courses` with:

```json
{
  "code": "API101",
  "title": "API Development",
  "lecturer": "Alex"
}
```

<details>
<summary>What route should you open to see all courses in the browser?</summary>

```text
http://127.0.0.1:8000/courses
```

</details>

#### Part E: Stop and Think

13. Try to create another course with the same `code`.

You should get an error because `code` is unique:

![Error](images/week3_lab_2.png "Error")

14. Stop the server with `Ctrl + C`.

Part 2 is complete. Continue to [Part 3](part-3.md).
