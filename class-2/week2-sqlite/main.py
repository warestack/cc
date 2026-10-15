from fastapi import FastAPI
from pathlib import Path
import sqlite3

app = FastAPI()


# Check where you are connecting! Ask yourself: "Which one is my database?"
# The students table lives in university.db, created in Part 1 by setup_students.sql.
# Careful: sqlite3.connect() silently CREATES an empty file if this path does not
# exist, so a wrong filename shows up later as "no such table", not "file not found".
DB_PATH = Path(__file__).parent / "university.db"


def get_connection():
    connection = sqlite3.connect(DB_PATH)
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
        cursor.execute("select * from students")
        students = cursor.fetchall()

    finally:
        connection.close()

    return students
