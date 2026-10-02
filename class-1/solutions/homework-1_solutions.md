### Week 1 Homework 1 Solutions: University API Exercise

Use these solutions only after you have tried the exercise.

#### `requirements.txt`

```text
fastapi==0.141.1
uvicorn==0.52.4
```

#### `main.py`

```python
from fastapi import FastAPI

# Import the students router from routers/students.py.
from routers import students

app = FastAPI()

# Every route in students.py will start with /students.
app.include_router(students.router, prefix="/students")


@app.get("/")
def home():
    return {
        "name": "University API",
        "version": "1.0.0",
        "description": "A simple API to fetch university student data.",
        "endpoints": {
            "root": "GET /",
            "all_students": "GET /students",
            "student_by_id": "GET /students/s1"
        }
    }
```

#### `routers/__init__.py`

```python
# This file allows Python to import modules from the routers folder.
```

#### `routers/students.py`

```python
from fastapi import APIRouter, HTTPException

# Create a router for student-related endpoints.
router = APIRouter()

students = {
    "s1": {
        "name": "John Smith",
        "student_id": "S12345",
        "major": "Computer Science",
        "year": 2
    },
    "s2": {
        "name": "Maria Garcia",
        "student_id": "S54321",
        "major": "Mathematics",
        "year": 3
    },
    "s3": {
        "name": "Ali Khan",
        "student_id": "S77777",
        "major": "Data Science",
        "year": 1
    }
}


@router.get("/")
def get_students():
    return students


@router.get("/{student_id}")
def get_student(student_id: str):
    student = students.get(student_id)

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student
```

#### Browser Tests

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/students
http://127.0.0.1:8000/students/s1
http://127.0.0.1:8000/students/s10
```
