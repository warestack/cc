### Week 3: Weekend Activity

#### Unit and API Testing with pytest

Continue your **Courses API from Part 3**, not the Books homework. In Week 2 you sent requests manually. Now you will write checks that can be repeated with one command.

#### What You Will Learn

- A **unit test** calls a small application rule directly, without HTTP or a database.
- An **API integration test** sends a request through FastAPI and checks validation, routing and database behaviour together.
- A **fixture** supplies fresh setup for a test and cleans up afterwards.
- An **assertion** states what must be true; pytest reports a failure when it is false.

#### Part A: Prepare Your Project

Stop Uvicorn and activate your Courses project's environment. Add these lines to `requirements.txt`, keeping the existing dependencies:

```text
pytest==9.1.1
httpx==0.28.1
```

Install them:

```bash
python -m pip install -r requirements.txt
```

Create a `tests` folder. Test filenames and functions start with `test_`. You do not need a running server, Google Cloud account or credentials: `TestClient` sends requests inside the Python process.

#### Part B: Test a Rule Directly

As a small practice rule, enrolment is open only **before** a closing time. At the exact closing time it is closed. This helper is a standalone exercise; it does not add an enrolment endpoint to the Courses API.

Create `rules.py`:

```python
from datetime import datetime


def enrolment_is_open(closes_at: datetime, now: datetime) -> bool:
    """Both arguments must be timezone-aware UTC timestamps."""
    return now < closes_at
```

Start with one example. Create `tests/test_rules.py`:

```python
from datetime import datetime, timedelta, timezone

from rules import enrolment_is_open


def test_enrolment_before_closing():
    closes_at = datetime(2026, 11, 1, 12, tzinfo=timezone.utc)
    now = closes_at - timedelta(seconds=1)
    assert enrolment_is_open(closes_at, now) is True
```

Run it from the project root:

```bash
python -m pytest tests/test_rules.py -q
```

Expect **1 passed**. The test arranges two times, calls the rule, and checks the result with `assert`.

Now **replace** `tests/test_rules.py` with the version below to check all three boundary cases:

```python
from datetime import datetime, timedelta, timezone

import pytest

from rules import enrolment_is_open


@pytest.mark.parametrize("seconds, expected", [(-1, True), (0, False), (1, False)])
def test_enrolment_boundary(seconds, expected):
    closes_at = datetime(2026, 11, 1, 12, tzinfo=timezone.utc)
    now = closes_at + timedelta(seconds=seconds)
    assert enrolment_is_open(closes_at, now) is expected
```

`parametrize` runs the function three times: before, exactly at and after the boundary. We pass a fixed UTC time instead of waiting or calling the real clock. This makes the test repeatable. The same technique helps you test time-based assignment rules in your own implementation.

Run:

```bash
python -m pytest tests/test_rules.py -q
```

Expect **3 passed**. Temporarily change `<` to `<=` in `rules.py`, rerun, and inspect the failing boundary case. Restore `<` and rerun. This shows that the test detects a plausible defect.

#### Part C: Make Application Setup Testable

The current `main.py` creates tables when imported. Tests must not create or change your normal `courses.db`. Separate application construction from the normal server entry point.

Create `application.py` with the complete code below. It keeps the Part 3 routes, but places them inside `create_app`, which accepts the database engine to initialise:

```python
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import schemas
import models
from database import engine, get_db

def create_app(db_engine=engine):
    models.Base.metadata.create_all(bind=db_engine)
    app = FastAPI()

    @app.get("/")
    def home():
        return {"message": "Week 3 SQLAlchemy API is running"}


    @app.get("/courses", response_model=list[schemas.CourseResponse])
    def get_courses(db: Session = Depends(get_db)):
        # response_model tells FastAPI to return a list of CourseResponse objects.
        # Read all courses from the database.
        courses = db.query(models.Course).all()
        return courses


    @app.get("/courses/{course_id}", response_model=schemas.CourseResponse)
    def get_course(course_id: int, db: Session = Depends(get_db)):
        # Find one course by primary key.
        course = db.query(models.Course).filter(models.Course.id == course_id).first()

        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")

        return course


    @app.post("/courses", response_model=schemas.CourseResponse, status_code=201)
    def create_course(course_data: schemas.CourseCreate, db: Session = Depends(get_db)):
        # course_data has already been checked by Pydantic.
        # We can use dot notation because course_data is a CourseCreate object.
        course = models.Course(
            code=course_data.code,
            title=course_data.title,
            lecturer=course_data.lecturer
        )

        try:
            db.add(course)
            db.commit()
            db.refresh(course)
            return course

        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=409, detail="Course code already exists")

    return app
```

Replace `main.py` with:

```python
from application import create_app

app = create_app()
```

Keep `database.py`, `models.py` and `schemas.py` from Parts 1–3. Normal use still runs with `uvicorn main:app --reload`. Tests import `application`, not `main`, so they can create tables only in a temporary database.

#### Part D: Give Each Test Its Own Database

Create `tests/conftest.py`:

```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from application import create_app
from database import get_db


@pytest.fixture
def app_factory(tmp_path):
    # Each test receives a different temporary directory and database.
    engine = create_engine(
        f"sqlite:///{tmp_path / 'test.db'}",
        connect_args={"check_same_thread": False},
    )
    sessions = sessionmaker(bind=engine)
    apps = []

    def make_app():
        app = create_app(engine)

        def override_db():
            with sessions() as session:
                yield session

        app.dependency_overrides[get_db] = override_db
        apps.append(app)
        return app

    yield make_app
    for app in apps:
        app.dependency_overrides.clear()
    engine.dispose()


@pytest.fixture
def client(app_factory):
    with TestClient(app_factory()) as test_client:
        yield test_client
```

pytest discovers fixtures in `conftest.py`. `tmp_path` supplies a different directory for every test. `dependency_overrides` redirects `get_db` to the test database; passing an engine to `create_app` alone would not redirect request sessions. Cleanup clears the overrides and releases connections.

`app_factory` can make two application instances sharing one temporary file **within a single test**. Other tests still receive different files.

#### Part E: Test Requests and Stored Results

Start with one API check. Create `tests/test_api.py`:

```python
def test_starts_empty(client):
    response = client.get("/courses")
    assert response.status_code == 200
    assert response.json() == []
```

The `client` argument asks pytest for the fixture from `conftest.py`; you do not call the fixture yourself. Run:

```bash
python -m pytest tests/test_api.py -q
```

Expect **1 passed**. This test sends a request and checks both the status code and returned JSON.

Now **replace** `tests/test_api.py` with these six examples:

```python
from fastapi.testclient import TestClient

COURSE = {"code": "CC101", "title": "Cloud Computing", "lecturer": "Alex"}


def test_create_and_retrieve(client):
    created = client.post("/courses", json=COURSE)
    assert created.status_code == 201
    body = created.json()
    assert body == {"id": body["id"], **COURSE}
    assert isinstance(body["id"], int)
    fetched = client.get(f"/courses/{body['id']}")
    assert fetched.status_code == 200
    assert fetched.json() == body
    assert client.get("/courses").json() == [body]


def test_duplicate_does_not_add_row(client):
    assert client.post("/courses", json=COURSE).status_code == 201
    duplicate = client.post("/courses", json=COURSE)
    assert duplicate.status_code == 409
    assert duplicate.json()["detail"] == "Course code already exists"
    assert len(client.get("/courses").json()) == 1


def test_invalid_input_does_not_add_row(client):
    response = client.post("/courses", json={**COURSE, "code": "X"})
    assert response.status_code == 422
    assert any(error["loc"] == ["body", "code"] for error in response.json()["detail"])
    assert client.get("/courses").json() == []


def test_missing_course(client):
    response = client.get("/courses/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Course not found"}


def test_starts_empty(client):
    # This remains true even when other tests have created courses.
    assert client.get("/courses").json() == []


def test_data_survives_new_application(app_factory):
    with TestClient(app_factory()) as first:
        created = first.post("/courses", json=COURSE)
        assert created.status_code == 201
        body = created.json()
    # A second app and new sessions use the same file within this test.
    with TestClient(app_factory()) as restarted:
        assert restarted.get(f"/courses/{body['id']}").json() == body
```

These checks cover successful creation/retrieval, duplicates (`409`), invalid input (`422`), missing records (`404`), isolation and persistence across application instances. Notice that they check returned data and database effects, not just status codes.

> **Clarification:** The persistence test creates a new app with new sessions using the same file. It does not prove recovery after a real process crash or Kubernetes Pod replacement; the assignment asks for deployment evidence separately.

Your project should now contain:

```text
week3-sqlalchemy-api/
  application.py
  main.py
  database.py
  models.py
  schemas.py
  rules.py
  requirements.txt
  tests/
    conftest.py
    test_rules.py
    test_api.py
```

Keep the seed/read scripts from Part 1; tests do not need to run them.

#### Part F: Run, Interpret and Extend

From the project root, run the whole suite:

```bash
python -m pytest -q
```

Expect **9 passed**: three unit cases and six API tests. Warnings are reported separately from test failures; check the final passed/failed summary. Run it again; the result should be the same and your normal `courses.db` should be unchanged. Use `python -m pytest -v` to see test names. If a test fails, read the failing assertion, compare expected and actual values, and fix the cause rather than weakening the assertion.

Add two more API tests yourself:

1. Omit `title`: expect `422` and no new course.
2. After a rejected duplicate, create a different course: expect `201` and two stored courses. This checks that a failed request does not prevent later writes.

Try these before opening the [exercise answers](../solutions/testing-exercises.md). With both added, expect **11 passed**.

#### Checklist and Assignment Connection

- Explain the difference between the three direct unit cases and the API tests.
- Show that tests start with fresh data and do not depend on their execution order.
- Explain the boundary failure you deliberately introduced and fixed.
- Record the command, results and one limitation in your lab README.

For Piazza, apply these techniques to your own rules and endpoints. After Week 4, extend them to authentication failures and protected routes. Use the assignment's [testing requirements](../../assignment/03-testing-and-deployment.md) to plan coverage; this small lab suite does not cover the full assignment. Test counts alone do not demonstrate quality.

#### Troubleshooting

- **Import error:** run from the project root using `python -m pytest`, with the correct environment active.
- **No tests collected:** check filenames and function names start with `test_`.
- **Wrong status code:** confirm you completed Part 3 and use the application code above.
- **Unexpected existing rows:** check the `get_db` override and import `application`, not `main`, in tests.

Further reading: [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/) and [dependency overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/).

Compare with the [runnable reference solution](../solutions/README.md), then [share your work for feedback](../homework/submission.md).
