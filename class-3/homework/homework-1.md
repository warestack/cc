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
sqlalchemy
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

#### Starter Boilerplate

Use this as the starting point for `database.py`:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

Use this as the starting point for `models.py`:

```python
from sqlalchemy import Column, Integer, String

from database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
```

Use this as the starting point for `schemas.py`:

```python
from pydantic import BaseModel, ConfigDict, Field


class BookCreate(BaseModel):
    title: str = Field(min_length=2)
    author: str = Field(min_length=2)
    year: int = Field(ge=1900)


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    year: int

    model_config = ConfigDict(from_attributes=True)
```

Use this as the starting point for `main.py`:

```python
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Books API is running"}


@app.get("/books", response_model=list[schemas.BookResponse])
def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()


@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@app.post("/books", response_model=schemas.BookResponse)
def create_book(book_data: schemas.BookCreate, db: Session = Depends(get_db)):
    book = models.Book(
        title=book_data.title,
        author=book_data.author,
        year=book_data.year
    )

    db.add(book)
    db.commit()
    db.refresh(book)
    return book
```

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

Week 3 is complete.
