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
