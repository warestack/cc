### Week 2 Part 3: SQLite and FastAPI Exercise

This exercise is based on [Part 1](part-1.md) and [Part 2](part-2.md).

Create a new project from zero. Do not reuse the `week2-sqlite` project.

#### Goal

Create a small database and API for books.

Your API should support:

- `GET /` returns a welcome message
- `GET /books` returns all books from SQLite

#### Part A: Create the Database

1. Create a new folder called:

```text
week2-books-api
```

2. Open it in VS Code.

3. Open a new VS Code terminal.

4. Create and open a SQLite database called:

```text
books.db
```

5. Create a table called `books` with these columns:

- `id`
- `title`
- `author`
- `year`

6. Insert at least three books.

7. Use `SELECT * FROM books;` to check your data.

8. Exit SQLite.

#### Part B: Create the FastAPI App

9. Create and activate a virtual environment.

10. Create `requirements.txt` with:

```text
fastapi==0.141.1
uvicorn==0.52.4
```

11. Install the requirements.

12. Create `main.py`.

13. Create a FastAPI app that connects to `books.db`.

14. Add:

```text
GET /
GET /books
```

#### Part C: Test

15. Run the app with Uvicorn.

16. Open:

```text
http://127.0.0.1:8000/
```

17. Open:

```text
http://127.0.0.1:8000/books
```

18. Stop the server.

#### Checklist

Before you finish, make sure:

- `books.db` exists
- the `books` table exists
- at least three books are inserted
- `GET /` works
- `GET /books` returns your database rows

Part 3 is complete. Continue to [Homework 1](../homework/homework-1.md).
