### Week 4 Homework 1: Test Your Authentication API

Continue your `week4-auth-api` project after Part 3. Reuse the approach from the [Week 3 testing tutorial](../../class-3/lab/weekend-activity.md): test a helper directly, then send API requests with `TestClient`.

#### Part A: Prepare the App for Tests

Stop Uvicorn and activate this project's environment. Add these lines to `requirements.txt`, keeping its existing contents, then run `python -m pip install -r requirements.txt`:

```text
pytest==9.1.1
httpx==0.28.1
```

As in Week 3, separate application setup so tests create only their own database. Create `application.py`:

```python
from fastapi import FastAPI

import models
from database import engine
from routers import auth, profile


def create_app(db_engine=engine):
    models.Base.metadata.create_all(bind=db_engine)
    app = FastAPI()
    app.include_router(auth.router, prefix="/auth")
    app.include_router(profile.router, prefix="/profile")

    @app.get("/")
    def home():
        return {"message": "Week 4 auth API is running"}

    return app
```

Replace `main.py` with:

```python
from application import create_app

app = create_app()
```

Keep your other files unchanged. Normal use still runs with `uvicorn main:app --reload` after setting your own `JWT_SECRET` as shown in Part 2.

#### Part B: Create an Isolated Test Client

Create a `tests` folder and add `tests/conftest.py`:

```python
import os

# Set a test-only secret before importing application/security.
os.environ["JWT_SECRET"] = "test-only-secret-not-for-deployment-123456789"

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from application import create_app
from database import get_db


@pytest.fixture
def client(tmp_path):
    engine = create_engine(
        f"sqlite:///{tmp_path / 'auth-test.db'}",
        connect_args={"check_same_thread": False},
    )
    sessions = sessionmaker(bind=engine)
    app = create_app(engine)

    def override_db():
        with sessions() as session:
            yield session

    app.dependency_overrides[get_db] = override_db
    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.clear()
        engine.dispose()
```

Each test receives a fresh temporary SQLite database. The override sends request sessions to it. The test-only secret is set before importing the app and never used to run your normal application. Tests import `application`, not `main`, so they do not create or modify `auth.db`.

#### Part C: Start with Three Tests

Create `tests/test_auth.py`:

```python
from security import hash_password, verify_password

USER = {"username": "student", "email": "student@example.com", "password": "secret123"}


def test_password_hash():
    hashed = hash_password(USER["password"])
    assert hashed != USER["password"]
    assert verify_password(USER["password"], hashed)
    assert not verify_password("wrong", hashed)


def test_login_and_profile(client):
    registered = client.post("/auth/register", json=USER)
    assert registered.status_code == 201
    assert set(registered.json()) == {"id", "username", "email"}
    login = client.post("/auth/login", json=USER)
    assert login.status_code == 200
    token = login.json()["access_token"]
    profile = client.get("/profile/me", headers={"Authorization": f"Bearer {token}"})
    assert profile.status_code == 200
    assert profile.json() == registered.json()


def test_profile_requires_token(client):
    response = client.get("/profile/me")
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}
```

From the project root, run:

```bash
python -m pytest -q
```

Expect **3 passed**. The first is a unit test of the password helper; the other two are API integration tests. No server, real signing secret or cloud credentials are needed.

#### Part D: Add Your Own Checks

Add tests for duplicate registration (`409`), wrong-password login (`401`) and invalid registration data (`422`). Check the response data as well as the status where useful. Each test must create any users it needs rather than relying on another test.

After trying them, compare with the [reference solution](../solutions/README.md), which includes further examples for invalid and expired tokens. Your test count will depend on which examples you add.

Add the pytest command and a short result summary to your README. Continue to [Homework 2: Publish Your Practice Project](homework-2.md).
