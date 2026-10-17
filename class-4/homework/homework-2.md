### Week 4 Homework 2: Publish Your Practice Project

Publish your Week 4 authentication API and tests in a **new public GitHub repository**, for example `week4-auth-api`. Use the Git and GitHub process you practised in [Week 1](../../class-1/lab/weekend-activity.md).

This prepares you to maintain the code, tests and instructions for the assignment. Use your lab project here; keep your assessed Piazza work in its own repository.

#### Part A: Prepare Your Files

Complete [Homework 1](homework-1.md). Add a `.gitignore` before committing:

```gitignore
.venv/
__pycache__/
.pytest_cache/
*.pyc
*.db
.env
```

Include the Python files, `routers/`, `tests/`, `requirements.txt` and a basic `README.md`. In the README, explain:

- What the application does and which Python version it needs.
- How to create an environment and install dependencies.
- How to generate and set `JWT_SECRET`, using placeholders rather than your actual secret.
- How to start the server and use `/docs` to register, log in and access `/profile/me`.
- How to run pytest, and a short summary of the results.
- That SQLite creates `auth.db` locally and the tests use a separate temporary database.

#### Part B: Create the Repository and Push

1. Create an **empty public repository** on GitHub. Leave GitHub's README, `.gitignore` and licence initialisation options unchecked.
2. Initialise Git in your own `week4-auth-api` project folder, connect it to the new repository, commit and push using the Week 1 process. Do not initialise or change the class teaching repository.
3. Use a descriptive commit message, such as `Add authentication API and tests`. Continue committing and pushing meaningful improvements as you work.
4. Open the repository on GitHub. Check that your code, tests and README are visible, and that `.venv`, databases and secrets are absent.

> **Clarification:** `.gitignore` does not remove files already tracked by Git. Check the files you are committing before you push. If unsure, ask in the lab.

#### Part C: Check and Share

Clone your new repository into a separate folder. Follow its README to install dependencies, run the tests and start the app. This checks that someone else can reproduce your work without your original environment or database.

Post the repository link in the Teams **Lab Exercises and Solutions** channel used in Week 1. Include your test summary and one question or improvement you would like feedback on. Never post tokens or signing secrets.

This practice homework adds no assignment marks. The assignment has its own repository, development-history and submission requirements.

Continue to the [weekend architecture activity](../lab/weekend-activity.md).
