### Week 3: Testing Exercise Answers

Try Part F of the [testing tutorial](../lab/weekend-activity.md) first. Add these functions to `tests/test_api.py`, where `COURSE` is already defined.

```python
def test_missing_title(client):
    body = {"code": "CC101", "lecturer": "Alex"}
    response = client.post("/courses", json=body)
    assert response.status_code == 422
    assert any(error["loc"] == ["body", "title"] for error in response.json()["detail"])
    assert client.get("/courses").json() == []


def test_create_after_duplicate(client):
    assert client.post("/courses", json=COURSE).status_code == 201
    assert client.post("/courses", json=COURSE).status_code == 409
    second = {**COURSE, "code": "DB101", "title": "Databases"}
    assert client.post("/courses", json=second).status_code == 201
    rows = client.get("/courses").json()
    assert {row["code"] for row in rows} == {"CC101", "DB101"}
```

Run `python -m pytest -q`: expect **11 passed** after adding these two tests. The second test verifies recovery after a uniqueness conflict, including the stored results.

Return to [Week 3](../README.md).
