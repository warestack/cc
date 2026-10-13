### Week 2 Homework 1: Simple CRUD with FastAPI and SQLite

In this homework exercise, you will build a simple CRUD API using FastAPI and SQLite.

CRUD means:

- Create
- Read
- Update
- Delete

Most database-backed applications use these four actions. For example, a notes app needs to create a note, read notes, edit a note, and delete a note.

We will use a small `notes` table to keep the example simple.

#### What You Will Learn

- How to create rows from an API request.
- How to read rows from SQLite.
- How to update rows.
- How to delete rows.
- How to test non-GET endpoints using FastAPI docs.

#### Part A: Create a New Project

1. Create a new folder called:

```text
week2-notes-crud
```

2. Open it in VS Code.

3. Open a new VS Code terminal.

4. Create and activate a virtual environment.

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

5. Create `requirements.txt`:

```text
fastapi==0.141.1
uvicorn==0.52.4
```

6. Install the requirements.

```bash
python -m pip install -r requirements.txt
```

7. Create `main.py`.

#### Before You Add the Code

This is a guided example. Read the code, run it, then complete the testing tasks below using your own note content.

| Action | HTTP method and path | Successful response |
| --- | --- | --- |
| Create | `POST /notes` | `201` and the new note |
| Read all | `GET /notes` | `200` and a list of notes |
| Read one | `GET /notes/{note_id}` | `200` and one note |
| Update selected fields | `PATCH /notes/{note_id}` | `200` and the updated note |
| Delete | `DELETE /notes/{note_id}` | `200` and a confirmation |

**Status codes:** `200` means OK, `201` means Created, `404` means Not Found, and `422` means the request failed validation.

`BaseModel` comes from Pydantic, which FastAPI installs as a dependency. `NoteCreate` describes the JSON request body: both fields are required strings. `NoteUpdate` allows a partial update, so either field may be omitted. In this simple example, an omitted field or an explicit `null` leaves its existing value unchanged.

SQL placeholders (`?`) pass values separately from the SQL command. This avoids treating user input as SQL. `(note_id,)` is a tuple containing one value. `connection.commit()` saves database changes; `lastrowid` gives the ID of the row just inserted.

#### Part B: Add the CRUD API

8. Add this code to `main.py`:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import sqlite3

app = FastAPI()

DATABASE_PATH = Path(__file__).resolve().parent / "notes.db"


class NoteCreate(BaseModel):
    title: str
    text: str


class NoteUpdate(BaseModel):
    title: str | None = None
    text: str | None = None


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            text TEXT NOT NULL
        )
        """
    )
    connection.commit()
    connection.close()


create_table()


@app.get("/")
def home():
    return {"message": "Notes API is running"}


@app.get("/notes")
def get_notes():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM notes ORDER BY id")
    rows = cursor.fetchall()
    connection.close()
    return [dict(row) for row in rows]


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    row = cursor.fetchone()
    connection.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Note not found")

    return dict(row)


@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO notes (title, text) VALUES (?, ?)",
        (note.title, note.text)
    )
    connection.commit()
    note_id = cursor.lastrowid
    connection.close()
    return {"id": note_id, "title": note.title, "text": note.text}


@app.patch("/notes/{note_id}")
def update_note(note_id: int, note: NoteUpdate):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    existing = cursor.fetchone()

    if existing is None:
        connection.close()
        raise HTTPException(status_code=404, detail="Note not found")

    new_title = note.title if note.title is not None else existing["title"]
    new_text = note.text if note.text is not None else existing["text"]

    cursor.execute(
        "UPDATE notes SET title = ?, text = ? WHERE id = ?",
        (new_title, new_text, note_id)
    )
    connection.commit()
    connection.close()

    return {"id": note_id, "title": new_title, "text": new_text}


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    existing = cursor.fetchone()

    if existing is None:
        connection.close()
        raise HTTPException(status_code=404, detail="Note not found")

    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    connection.commit()
    connection.close()

    return {"message": "Note deleted"}
```

#### Part C: Run and Test

9. Run the app:

```bash
uvicorn main:app --reload
```

10. Open FastAPI docs:

```text
http://127.0.0.1:8000/docs
```

11. Expand `POST /notes` in `/docs`, click **Try it out**, replace the example request body with the JSON below, and click **Execute**:

```json
{
  "title": "First note",
  "text": "This note is stored in SQLite."
}
```

The response should have status **201** and include the created note's `id`. Record that ID; use it in all following requests. The app creates `notes.db` beside `main.py` on startup, and notes persist between server restarts.

12. Open in the browser:

```text
http://127.0.0.1:8000/notes
```

You should see your note.

13. In `/docs`, expand `GET /notes/{note_id}`, click **Try it out**, enter the ID returned by `POST`, and click **Execute**. Expect `200` and that note.

14. Test `PATCH /notes/{note_id}` with the same ID and this JSON body:

```json
{"title": "Updated first note"}
```

Expect `200`. The title changes and the text stays the same. Repeat using your own note content and update only the `text` field.

15. Stop the server with `Ctrl + C`, restart it, and read the note again. Its changes should still be present.

16. Test `DELETE /notes/{note_id}` with the same ID. Expect `200` and `{"message":"Note deleted"}`. Read that ID again; expect `404` and `{"detail":"Note not found"}`.

17. Choose an ID that is absent from `GET /notes`, such as `9999`. Send `PATCH /notes/9999` with `{"title":"Missing note test"}`, then `DELETE /notes/9999`; both should return `404`. Send `POST /notes` with `{"title":"Incomplete note"}` and no text; expect `422`, meaning the request body did not match the required model.

18. Stop the server with `Ctrl + C` before starting Homework 2. If it is already running when you return, use that server rather than starting a second one on port `8000`.

#### Submission Checklist

Before you finish, make sure:

- `GET /notes` returns notes
- `GET /notes/{note_id}` returns one note
- `POST /notes` creates a note
- `PATCH /notes/{note_id}` updates a note
- `DELETE /notes/{note_id}` deletes a note
- missing notes return a `404` error

If PowerShell blocks activation, refer to [Week 1's activation instructions](../../class-1/lab/part-1.md). If you see `Address already in use`, stop the earlier server.

Homework 1 is complete. Continue to [Homework 2](homework-2.md).
