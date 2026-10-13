### Week 2 Part 3 Solutions: Books API

Use this solution after attempting the exercise. Your book choices may differ; compare the table structure, routes, and JSON response shape.

#### Project Files

```text
week2-books-api/
  setup_books.sql
  books.db
  requirements.txt
  main.py
  .venv/
```

#### `setup_books.sql`

```sql
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER NOT NULL
);

INSERT INTO books (title, author, year)
VALUES ('The Hobbit', 'J.R.R. Tolkien', 1937);
INSERT INTO books (title, author, year)
VALUES ('Nineteen Eighty-Four', 'George Orwell', 1949);
INSERT INTO books (title, author, year)
VALUES ('Frankenstein', 'Mary Shelley', 1818);
```

Save the file, then run this command once from the project folder. It works in macOS/Linux terminals and Windows PowerShell:

```bash
sqlite3 -bail books.db ".read setup_books.sql"
```

If you already created and populated `books.db` for the exercise, keep it and skip this setup. Rerunning against an existing table reports an error; `-bail` stops before inserting duplicates.

#### `requirements.txt`

```text
fastapi==0.141.1
uvicorn==0.52.4
```

Create and activate this project's virtual environment, then install the requirements as shown in [Part 2](../lab/part-2.md).

```bash
python -m pip install -r requirements.txt
```

#### `main.py`

```python
from fastapi import FastAPI
from pathlib import Path
import sqlite3

app = FastAPI()

# Find the database beside main.py, regardless of the terminal folder.
DATABASE_PATH = Path(__file__).resolve().parent / "books.db"


def get_connection():
    # Open a connection to the SQLite database file.
    # row_factory lets us access columns by name.
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


@app.get("/")
def home():
    return {"message": "Books API is running"}


@app.get("/books")
def get_books():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        # Read all rows from the books table in ID order.
        cursor.execute("SELECT * FROM books ORDER BY id")
        rows = cursor.fetchall()
    finally:
        # Close the connection even if the query fails.
        connection.close()

    # Convert each row into a dictionary
    books = []

    for row in rows:
        books.append(dict(row))

    return books
```

#### Run and Check

```bash
uvicorn main:app --reload
```

Check these URLs in your browser:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/books
```

The home endpoint returns `{"message":"Books API is running"}`. If you used the sample SQL above, `/books` returns:

```json
[
  {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
  {"id": 2, "title": "Nineteen Eighty-Four", "author": "George Orwell", "year": 1949},
  {"id": 3, "title": "Frankenstein", "author": "Mary Shelley", "year": 1818}
]
```

Stop the server with `Ctrl + C` before continuing to [Homework 1](../homework/homework-1.md).
