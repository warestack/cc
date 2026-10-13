### Welcome to Week 2

In Week 1, your APIs returned data written directly in Python. This week, you will store data in **SQLite** and read it through a FastAPI application. You will then create, read, update, and delete notes using API requests.

#### Before You Begin

Complete [Week 1](../../class-1/README.md) first. You should be comfortable creating a project folder, activating a virtual environment, running Uvicorn, and testing GET endpoints.

You will use Python 3.10 or later and VS Code again. If you need a reminder, revisit the [Week 1 welcome page](../../class-1/lab/welcome.md). Part 1 will help you check and install the SQLite command-line tools.

#### What Is SQLite?

**SQLite** is a database that stores your data in a file. Changes made to an in-memory dictionary are lost when the application restarts; changes saved to a SQLite database remain available. The original values written in your Python code can still be recreated each time it starts.

You will use **SQL (Structured Query Language)** to create tables and work with their rows. Python's `sqlite3` module lets your API run SQL commands against the database.

#### What You Will Build

- Parts 1–2: a student database and an API that reads its records.
- Part 3: an independent books database and API exercise.
- Homework 1: a guided Notes CRUD API.
- Homework 2: tests of the Notes API using Postman.
- Submission: a public repository shared in Teams for feedback.
- Weekend Activity: a 200–300 word blog about cloud infrastructure and AI.

Keep each new project in its own folder and create its own virtual environment. Part 2 continues the Part 1 project; Homework 2 continues the Homework 1 project.

#### Ready to Begin?

Proceed to [Part 1: Create a Local SQLite Database](part-1.md).
