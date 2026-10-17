### Week 3 Homework 1: SQLAlchemy Exercise

In this exercise, you will create a new SQLAlchemy API from zero.

Use Part 1, Part 2, and Part 3 if you struggle.

#### Task

Create a FastAPI application for books.

Your project folder should be called:

```text
week3-books-api
```

Open this folder in VS Code and use the VS Code terminal.

Create and activate a virtual environment.

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

#### Requirements

Create these files:

```text
requirements.txt
database.py
models.py
schemas.py
main.py
```

Your `requirements.txt` should contain:

```text
fastapi==0.141.1
uvicorn==0.52.4
sqlalchemy==2.0.55
```

Install the requirements:

```bash
python -m pip install -r requirements.txt
```

#### Database

Create a SQLite database file called:

```text
books.db
```

Create a SQLAlchemy model called `Book`.

The table should be called:

```text
books
```

The table should have:

- `id`
- `title`
- `author`
- `year`

#### Validation

Create a Pydantic schema called `BookCreate`.

Use validation rules:

- `title` must have at least 2 characters.
- `author` must have at least 2 characters.
- `year` must be greater than or equal to 1900.

#### API Routes

Create these routes:

```text
GET /
GET /books
GET /books/{book_id}
POST /books
```

The home route should return:

```json
{"message":"Books API is running"}
```

#### Build Your Solution

Use the Courses API from Parts 1–3 as a guide. Build the database path relative to `database.py`, as in Part 1, and give each request its own session using `get_db`. Return `201` when a book is created, `404` for a missing book and `422` for invalid input. Use a response schema containing `id`, `title`, `author` and `year`.

Attempt the exercise before checking the [complete reference files](../solutions/books-api/).

#### Test

Run the app with Uvicorn.

```bash
uvicorn main:app --reload
```

First open:

```text
http://127.0.0.1:8000/docs
```

Test:

- create a valid book
- create an invalid book with a short title
- get all books
- get one book by id
- try to get a book id that does not exist

Then test everything again in Postman.

In Postman, create requests for:

```text
GET http://127.0.0.1:8000/books
GET http://127.0.0.1:8000/books/1
POST http://127.0.0.1:8000/books
```

For the `POST` request, use **Body**, then **raw**, then **JSON**.

Send valid data:

```json
{
  "title": "Clean Code",
  "author": "Robert Martin",
  "year": 2008
}
```

Also send invalid data to check that validation works:

```json
{
  "title": "A",
  "author": "B",
  "year": 1800
}
```

#### Checklist

Before you finish, make sure:

- the app starts without errors
- SQLAlchemy creates the `books` table
- valid books can be inserted
- invalid data is rejected
- missing books return `404`
- all routes were tested in Postman
- you can explain the difference between a SQLAlchemy model and a Pydantic schema

After attempting the exercise, compare with the [Books reference solution](../solutions/README.md). Then return to your Courses project for the [weekend testing tutorial](../lab/weekend-activity.md).
