CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    year INTEGER NOT NULL
);

INSERT INTO students (name, course, year)
VALUES ('Ada Lovelace', 'Cloud Computing', 2);
INSERT INTO students (name, course, year)
VALUES ('Alan Turing', 'Artificial Intelligence', 3);

INSERT INTO students (name, course, year)
VALUES ('Grace Hopper', 'Software Engineering', 2);
