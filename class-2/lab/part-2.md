### Week 2 Part 2: Show SQLite Data with FastAPI

In this part, you will create a small FastAPI app that reads data from the SQLite database you created in Part 1.

#### What You Will Learn

- How to connect Python to SQLite.
- How to read database rows in Python.
- How to return database data from a FastAPI endpoint.
- How to show SQLite data in the browser.

#### Part A: Create the FastAPI Project Files

1. Stay inside the `week2-sqlite` folder.

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
fastapi==0.141.1;
uvicorn==0.52.4;
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
import sqlite3

app = FastAPI()


def get_connection():
    # Open a connection to the SQLite database file.
    # row_factory lets us access columns by name.
    connection = sqlite3.connect("university.db")
    connection.row_factory = sqlite3.Row
    return connection


@app.get("/")
def home():
    return {"message": "University API is running"}


@app.get("/students")
def get_students():
    connection = get_connection()
    cursor = connection.cursor()

    # Read all rows from the students table.
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    connection.close()

    # Convert each row into a dictionary
    students = []

    for row in rows:
        students.append(dict(row))

    return students
```

#### What Is Happening?

- `sqlite3.connect("university.db")` opens the database file.
- `cursor.execute(...)` runs a SQL command.
- `fetchall()` reads all matching rows.
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

You should see the students you inserted in Part 1.

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

Part 2 is complete. Continue to [Part 3](part-3.md)
