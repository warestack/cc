### Week 2 Part 2: Show SQLite Data with FastAPI

In this part, you will create a small FastAPI app that reads data from the SQLite database you created in Part 1.

#### What You Will Learn

- How to connect Python to SQLite.
- How to read database rows in Python.
- How to return database data from a FastAPI endpoint.
- How to show SQLite data in the browser.

#### Part A: Create the FastAPI Project Files

1. Stay inside the `week2-sqlite` folder. Complete Part 1 first and check that `university.db` and `setup_students.sql` are present.

2. Create a virtual environment:

```bash
python3 -m venv .venv
```

On Windows, use:

```powershell
python -m venv .venv
```

3. Activate the virtual environment.

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

4. Create a file called:

```text
requirements.txt
```

5. Add:

```text
fastapi==0.141.1
uvicorn==0.52.4
```

6. Install the requirements:

```bash
python -m pip install -r requirements.txt
```

7. Create a file called:

```text
main.py
```

#### Part B: Read from SQLite

8. Add this code to `main.py`:

```python
from fastapi import FastAPI
from pathlib import Path
import sqlite3

app = FastAPI()

# Find the database beside main.py, regardless of the terminal folder.
DATABASE_PATH = Path(__file__).resolve().parent / "university.db"


def get_connection():
    # Open a connection to the SQLite database file.
    # row_factory lets us access columns by name.
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


@app.get("/")
def home():
    return {"message": "University API is running"}


@app.get("/students")
def get_students():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        # Read all rows from the students table in ID order.
        cursor.execute("SELECT * FROM students ORDER BY id")
        rows = cursor.fetchall()
    finally:
        # Close the connection even if the query fails.
        connection.close()

    # Convert each row into a dictionary
    students = []

    for row in rows:
        students.append(dict(row))

    return students
```

#### What Is Happening?

- `Path(__file__)` finds the location of `main.py`; `DATABASE_PATH` points to the database beside it.
- `sqlite3.connect(DATABASE_PATH)` opens that database file.
- `cursor.execute(...)` runs a SQL command.
- `fetchall()` reads all matching rows.
- `ORDER BY id` displays rows in ID order.
- `finally` closes the connection whether the query succeeds or raises an error.
- `dict(row)` converts each row into JSON-friendly data.

> **Quick question**
>
> Why do we use `connection.row_factory = sqlite3.Row`?
>
> <details>
> <summary>Show answer</summary>
>
> It lets Python read columns by name, such as `name` and `course`, instead of only by position.
>
> </details>

#### Part C: Run and Test

9. Run the app:

```bash
uvicorn main:app --reload
```

10. Open the home endpoint:

```text
http://127.0.0.1:8000/
```

You should see:

```json
{"message":"University API is running"}
```

11. Open the students endpoint:

```text
http://127.0.0.1:8000/students
```

You should see a JSON **list** of three student objects. Ada's year should be `3` after the update in Part 1. For example, the first object is:

```json
{"id": 1, "name": "Ada Lovelace", "course": "Cloud Computing", "year": 3}
```

The SQL rows are stored in SQLite; the API converts them into JSON for the client.

> **Quick question**
>
> Where is the API getting the student data from?
>
> <details>
> <summary>Show answer</summary>
>
> It reads the data from the `students` table inside `university.db`.
>
> </details>

12. Stop the server with:

```text
Ctrl + C
```

#### Troubleshooting

- **`no such table: students`:** confirm that you ran Part 1's setup against the `university.db` beside `main.py`. SQLite can create an empty file when the expected database is missing; a file existing does not mean it contains your table.
- **`Address already in use`:** stop the previous server with `Ctrl + C` before starting another on port `8000`.
- **`uvicorn` not found:** activate this project's `.venv` and install its requirements.
- **PowerShell blocks activation:** use the process-scoped activation instructions in [Week 1 Part 1](../../class-1/lab/part-1.md).

Part 2 is complete. Continue to [Part 3](part-3.md).
