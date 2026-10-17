### Week 4 Reference Solution

Attempt Parts 1–3 and Homework 1 before comparing with the [complete authentication project](auth-api/). This example provides registration, login and a protected profile; it is not a Piazza solution.

#### Run the App

Copy `auth-api` into your own working area. Create and activate a virtual environment as shown in the [welcome page](../lab/welcome.md), then install:

```bash
python -m pip install -r requirements.txt
```

Set `JWT_SECRET` in your terminal following [Part 2](../lab/part-2.md). Use your own generated secret, keep it private and reuse it across restarts. Then run:

```bash
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs`. Register (`201`), log in (`200`), paste the token into **Authorize**, and call `/profile/me` (`200`). Repeat registration (`409`), try a wrong password (`401`), and clear authorisation before calling the profile again (`401`). Invalid registration input returns `422`.

Users persist in `auth.db` beside `database.py`. Passwords are stored as Argon2 hashes and tokens expire after 30 minutes. If you used an earlier lab version with bcrypt hashes, use a fresh practice project/database for this solution; it is not a hash migration tool.

#### Automated Checks

Stop Uvicorn and run:

```bash
python -m pytest -q
```

The reference solution extends the three starting tests in [Homework 1](../homework/homework-1.md). Expect **11 passed**, covering hashing, registration/login/profile, rejected credentials, invalid input and missing, invalid, expired or incomplete tokens. Tests use a temporary database and a test-only signing secret; they do not require your real secret or cloud credentials. Read the tests alongside the [Week 3 testing tutorial](../../class-3/lab/weekend-activity.md).

These checks are examples to learn from. Design your own tests for the assignment's full requirements. Continue to [Homework 2](../homework/homework-2.md) to publish your practice project, then complete the architecture activity.
