### Welcome to Week 3

In Week 3, rebuild your database API using SQLAlchemy, validate requests with Pydantic, and automate checks with pytest.

#### Before You Begin

Complete [Week 2](../../class-2/README.md) first. Use Python 3.10 or later and VS Code. Keep this week's project separate from previous work.

Create and open `week3-sqlalchemy-api` in VS Code. Run all commands from that project folder.

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

If activation is blocked, use the guidance in [Week 1 Part 1](../../class-1/lab/part-1.md). Part 1 provides the dependency list. Use the same environment throughout Parts 1–3; stop Uvicorn with `Ctrl + C` before changing projects.

#### What You Will Build

- Parts 1–3: a Courses API with persistent SQLite data and validation.
- Homework: a separate Books API to practise the same approach.
- Weekend: unit and API tests for the Courses API, with an isolated database.

The testing tutorial prepares you for the assignment's testing requirements. It demonstrates techniques, not a complete Piazza solution.

#### Keep Your Repository Clean

Exclude `.venv/`, `__pycache__/`, `.pytest_cache/`, `*.db` and `.env` in your project's `.gitignore`. Commit source, dependencies and tests; never passwords, tokens or signing secrets.

#### Ready to Begin?

Proceed to [Part 1](part-1.md). After trying the work, use the [reference solutions](../solutions/README.md) to compare and troubleshoot.
