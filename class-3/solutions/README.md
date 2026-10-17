### Week 3 Reference Solutions

Attempt the activities first. These are teaching examples, not Piazza assignment solutions.

- [Courses API](courses-api/): the completed Parts 1–3 application, refactored as shown in the weekend tutorial, plus nine tests.
- [Books API](books-api/): complete homework files to compare with your own model, schemas and routes.
- [Testing exercise answers](testing-exercises.md): the two additional tests to try yourself first.

#### Run a Solution

Copy either project folder to your own working area and open it in VS Code. Create and activate its own virtual environment as shown in the [welcome page](../lab/welcome.md), then run:

```bash
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs`. Courses use `courses.db`; books use `books.db`, beside their `database.py`. Both start empty unless you add records. In the Courses project, you can run `python seed.py` and `python read_courses.py` to revisit Part 1. Running the seed twice must not duplicate rows.

Check creation (`201`), retrieval (`200`), missing IDs (`404`) and invalid input (`422`). Courses also reject duplicate codes (`409`). The Books exercise deliberately accepts only years from 1900 onwards; this is a practice constraint, not a rule about all books.

Stop Uvicorn. In the Courses folder, run:

```bash
python -m pytest -q
```

Expect **9 passed**. The isolated tests do not use or modify your normal database. Add the two exercise answers to reach 11 cases. No cloud access is needed.

Return to [Week 3](../README.md).
