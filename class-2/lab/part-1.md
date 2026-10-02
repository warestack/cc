### Week 2 Part 1: Create a Local SQLite Database

Web applications often need to store and retrieve data, such as users, products or orders. SQL allows our application to communicate with a database so that this data can be saved, searched, updated, and deleted using commands.

In this part, you will create a small SQLite database locally and practise basic SQL commands.

SQLite stores the database in a normal file. This is useful for learning because we do not need to install or manage a separate database server.

#### What You Will Learn

- How to run SQLite from the terminal.
- How to write SQL commands in a `.sql` file.
- How to create a table and insert data.
- How to read data with `SELECT`.

#### Part A: Create a Project Folder and Check SQLite

1. Open **Visual Studio Code**.

2. Open a new project folder.

   Name it:

```text
week2-sqlite
```

3. Open a new VS Code terminal.

4. Check if SQLite is available:

```bash
sqlite3 --version
```

If you see a version number, SQLite is ready.

If the command is not found, ask for help before continuing.

#### Part B: Create a SQL File

Instead of typing the longer setup SQL directly into the terminal, we will write the table creation and insert commands in a text file first. This makes it easier to fix mistakes before running the commands.

We will still run the smaller check commands, such as `SELECT`, `.tables`, and `.schema`, directly in the SQLite shell.

5. Create a new file called:

```text
setup_students.sql
```

6. Examine and add this SQL code:

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    year INTEGER NOT NULL
);

INSERT INTO students (name, course, year)
VALUES ('Ada Lovelace', 'Cloud Computing', 2);

INSERT INTO students (name, course, year)
VALUES ('Alan Turing', 'Computer Science', 3);

INSERT INTO students (name, course, year)
VALUES ('Grace Hopper', 'Software Engineering', 1);
```

* This SQL code first creates a table called `students` with four columns: a unique `id`, the student's `name`, their `course`, and their `year` of study. `PRIMARY KEY AUTOINCREMENT` automatically gives each student a unique ID, while `NOT NULL` means that a value must be provided.

* The three `INSERT` statements then add three students to the table: Ada Lovelace, Alan Turing, and Grace Hopper.

7. Save the file.

#### Part C: Create the Database from the SQL File

8. Run the SQL file and create the database:

```bash
sqlite3 university.db < setup_students.sql
```

This command means:

- open or create `university.db`
- read the SQL commands from `setup_students.sql`
- run those commands inside SQLite

> **Quick question**
>
> What does the `< setup_students.sql` part do?
>
> <details>
> <summary>Show answer</summary>
>
> It sends the contents of `setup_students.sql` into SQLite, as if you typed those SQL commands into the SQLite shell.
>
> </details>

9. Check that the database file exists in the explorer.

#### Part D: Open SQLite and Check the Data

10. Open the database:

```bash
sqlite3 university.db
```

Your terminal is now inside the SQLite shell. The prompt usually changes to:

```text
sqlite>
```

11. Show the tables in the database:

```sql
.tables
```

You should see:

```text
students
```

12. Look at the table structure:

```sql
.schema students
```

13. Make the output easier to read:

```sql
.headers on
.mode column
```

> **Quick question**
>
> What do `.headers on` and `.mode column` change?
>
> <details>
> <summary>Show answer</summary>
>
> They only change how SQLite displays results in the terminal. They do not change the database data.
>
> </details>

14. Read all students:

```sql
SELECT * FROM students;
```

#### Part E: Basic Queries

15. Select only names:

```sql
SELECT name FROM students;
```

16. Select students in year 2:

```sql
SELECT * FROM students WHERE year = 2;
```

17. Update one row:

```sql
UPDATE students
SET year = 3
WHERE name = 'Ada Lovelace';
```

18. Check the update:

```sql
SELECT * FROM students;
```

19. Exit SQLite:

```sql
.quit
```

Part 1 is complete. Continue to [Part 2](part-2.md).
