### Week 1 Homework 1: University API Exercise

Now build a small University API using FastAPI.

Create a new project in VS Code. Do not reuse the movie project from Lab Part 3.

Solutions are in the [solutions](../solutions/) folder.

#### Goal

Your API should support these endpoints:

- `GET /` returns a welcome page with API information.
- `GET /students` returns all students.
- `GET /students/{student_id}` returns one student by ID.
- If the student does not exist, return a `404` JSON error.

You should use:

- `main.py`
- a `routers` folder
- `routers/students.py`
- `APIRouter`
- `requirements.txt`
- `uvicorn main:app --reload`

#### Part A: Create the Project

1. Create a new folder called:

```text
week1-university-api
```

2. Open it in VS Code.

3. Open a VS Code terminal.

4. Create and activate a virtual environment.

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

5. Create a `requirements.txt` file with:

```text
fastapi==0.141.1
uvicorn==0.52.4
```

6. Install the requirements:

```bash
python -m pip install -r requirements.txt
```

#### Part B: Create the Files

Create this structure:

```text
week1-university-api/
  main.py
  requirements.txt
  routers/
    __init__.py
    students.py
```

#### Starter Boilerplate

Use this as the starting point for `main.py`:

```python
from fastapi import FastAPI

from routers import students

app = FastAPI()

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

Use this as the starting point for `routers/students.py`:

```python
from fastapi import APIRouter, HTTPException

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

#### Part C: Root Endpoint

Your root endpoint should return:

```json
{
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

#### Part D: Student Data

Use this data in `routers/students.py`:

```python
students = {
    # The keys s1, s2, and s3 are the IDs used in the URL.
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
```

#### Part E: Required Tests

Run the server:

```bash
uvicorn main:app --reload
```

Open these URLs in your browser:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/students
http://127.0.0.1:8000/students/s1
http://127.0.0.1:8000/students/s10
```

The final URL should return a `404` error with:

```json
{"detail":"Student not found"}
```

Also check student `s2`:

```text
http://127.0.0.1:8000/students/s2
```

#### Hints

In `main.py`, you will need:

```python
from fastapi import FastAPI

# Import the students router from routers/students.py.
from routers import students

app = FastAPI()

# Every route in students.py will start with /students.
app.include_router(students.router, prefix="/students")
```

In `routers/students.py`, you will need:

```python
from fastapi import APIRouter, HTTPException

# Create a router for student-related endpoints.
router = APIRouter()
```

To return one student:

```python
# Look up the student using the ID from the URL.
student = students.get(student_id)

if student is None:
    # If the ID is unknown, return a clear 404 error.
    raise HTTPException(status_code=404, detail="Student not found")

return student
```

#### Submission Checklist

Before you finish, make sure:

- Your virtual environment works.
- Your `requirements.txt` contains `fastapi` and `uvicorn`.
- `GET /` works in the browser.
- `GET /students` works in the browser.
- `GET /students/s1` works in the browser.
- `GET /students/s10` returns a `404` JSON error.
- You can explain what `/{student_id}` does.

Homework 1 is complete. Week 1 is complete.
