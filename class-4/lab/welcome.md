### Welcome to Week 4

In Week 4, validate registration data, hash passwords and protect API routes with expiring JWTs. Then explain the architecture of your planned final application.

#### Before You Begin

Complete [Week 3](../../class-3/README.md) first. Use Python 3.10 or later and VS Code. Keep this week's project separate from previous work.

Create and open `week4-auth-api` in VS Code. Run all commands from that project folder.

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

- Part 1: a temporary registration-validation preview.
- Parts 2–3: replace the preview with a persistent authentication API and protected profile route.
- Homework 1: automated checks for your authentication API.
- Homework 2: a new GitHub repository containing your practice app, tests and README.
- Weekend: a diagram and explanation of your planned final backend.

Google Cloud access will be provided in Class 4. This week's API runs locally; cloud credentials are not needed. Containerisation and Kubernetes teaching will be completed by Week 7.

#### Keep Your Repository Clean

Exclude `.venv/`, `__pycache__/`, `.pytest_cache/`, `*.db` and `.env` in your project's `.gitignore`. Commit source, dependencies and tests; never passwords, tokens or signing secrets.

#### Ready to Begin?

Proceed to [Part 1](part-1.md). After trying the work, use the [reference solutions](../solutions/README.md) to compare and troubleshoot.
