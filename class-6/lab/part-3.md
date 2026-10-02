### Week 6 Part 3: Docker Exercise

In this exercise, you will containerize a small FastAPI API from zero.

Use Part 1 and Part 2 if you struggle.

#### Task

Create a new project folder:

```text
week6-courses-container
```

Create these files:

```text
requirements.txt
main.py
Dockerfile
```

#### Starter Files

Your `requirements.txt` should contain:

```text
fastapi==0.141.1
uvicorn==0.52.4
```

This installs the same FastAPI and Uvicorn versions used in the earlier labs.

Your `main.py` can start with:

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

courses = {
    "c1": {
        "title": "Cloud Computing",
        "level": "Year 2"
    },
    "c2": {
        "title": "Databases",
        "level": "Year 2"
    }
}


@app.get("/")
def home():
    return {"message": "Courses API is running inside Docker"}


@app.get("/courses")
def get_courses():
    return courses


@app.get("/courses/{course_id}")
def get_course(course_id: str):
    course = courses.get(course_id)

    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    return course
```

This code creates a small FastAPI API.

- `courses` is temporary in-memory data.
- `GET /` checks that the API is running.
- `GET /courses` returns all courses.
- `GET /courses/{course_id}` returns one course from the dictionary.
- `HTTPException` returns a clear `404` response when the course ID is unknown.

Your `Dockerfile` can start with:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

This Dockerfile packages the FastAPI app.

- It starts from a Python image.
- It installs the packages from `requirements.txt`.
- It copies your API code into the image.
- It starts Uvicorn when the container runs.

#### API Requirements

Your FastAPI app should have these routes:

```text
GET /
GET /courses
GET /courses/{course_id}
```

Use this data:

```python
courses = {
    "c1": {
        "title": "Cloud Computing",
        "level": "Year 2"
    },
    "c2": {
        "title": "Databases",
        "level": "Year 2"
    }
}
```

If a course does not exist, return:

```json
{"detail":"Course not found"}
```

with status code `404`.

<details>
<summary>Which FastAPI class can return a `404` error?</summary>

```python
HTTPException
```

</details>

#### Docker Requirements

Your Docker image should be called:

```text
week6-courses-api:1
```

Your container should be called:

```text
courses-api
```

Run the container so the API is available on VM port `80`.

<details>
<summary>Which Docker option maps a VM port to a container port?</summary>

```bash
-p
```

</details>

#### Required Tests

Test these URLs in your browser:

```text
http://YOUR_VM_EXTERNAL_IP/
http://YOUR_VM_EXTERNAL_IP/courses
http://YOUR_VM_EXTERNAL_IP/courses/c1
http://YOUR_VM_EXTERNAL_IP/courses/c10
```

Then test the same URLs in Postman.

#### Cleanup

When you finish, stop and remove the container.

Also check that no unnecessary containers are still running:

```bash
docker ps
```

When you finish the lab, go back to the GCP dashboard and stop your VM.

You can switch it on again when you need it.

#### Checklist

Before you finish, make sure:

- the Docker image builds successfully
- the container starts successfully
- the API works in the browser
- the API works in Postman
- unknown course IDs return `404`
- you can explain the difference between an image and a container
- your VM is stopped when you no longer need it

Part 3 is complete. Continue to [Homework 1](../homework/homework-1.md).
