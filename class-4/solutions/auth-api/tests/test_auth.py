from datetime import datetime, timedelta, timezone

import jwt
import pytest

from security import ALGORITHM, SECRET_KEY, hash_password, verify_password

USER = {"username": "student", "email": "student@example.com", "password": "secret123"}


def test_hash_password():
    hashed = hash_password(USER["password"])
    assert hashed != USER["password"]
    assert verify_password(USER["password"], hashed)
    assert not verify_password("wrong", hashed)


def test_registration_login_and_profile(client):
    registered = client.post("/auth/register", json=USER)
    assert registered.status_code == 201
    assert set(registered.json()) == {"id", "username", "email"}
    assert client.post("/auth/register", json=USER).status_code == 409
    login = client.post("/auth/login", json=USER)
    assert login.status_code == 200
    token = login.json()["access_token"]
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert payload["sub"] == USER["email"]
    assert payload["exp"] > datetime.now(timezone.utc).timestamp()
    profile = client.get("/profile/me", headers={"Authorization": f"Bearer {token}"})
    assert profile.status_code == 200
    assert profile.json() == registered.json()


@pytest.mark.parametrize("body", [USER, {**USER, "password": "wrong"}])
def test_bad_login(client, body):
    if body["password"] == "wrong":
        client.post("/auth/register", json=USER)
    assert client.post("/auth/login", json=body).status_code == 401


def test_invalid_registration(client):
    assert client.post("/auth/register", json={**USER, "email": "invalid"}).status_code == 422


@pytest.mark.parametrize("kind", ["missing", "invalid", "expired", "no-expiry", "unknown-user", "bad-signature"])
def test_reject_token(client, kind):
    client.post("/auth/register", json=USER)
    payload = {"sub": USER["email"], "exp": datetime.now(timezone.utc) + timedelta(minutes=10)}
    if kind == "expired":
        payload["exp"] = datetime(2000, 1, 1, tzinfo=timezone.utc)
    if kind == "no-expiry":
        del payload["exp"]
    if kind == "unknown-user":
        payload["sub"] = "unknown@example.com"
    key = "other-test-signing-key-12345678901234567890" if kind == "bad-signature" else SECRET_KEY
    token = "invalid" if kind == "invalid" else jwt.encode(payload, key, algorithm=ALGORITHM)
    headers = {} if kind == "missing" else {"Authorization": f"Bearer {token}"}
    assert client.get("/profile/me", headers=headers).status_code == 401
