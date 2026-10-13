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

If the command is not found, install the SQLite **command-line tools** for your operating system from the [official SQLite download page](https://www.sqlite.org/download.html). On Windows, the tools ZIP contains `sqlite3.exe`; extract it to a folder and add that folder to your `PATH`, then reopen the terminal and repeat the check. Ask your tutor if you need help.

Python includes a `sqlite3` module, but this does not install the separate `sqlite3` terminal command.

Run commands from the `week2-sqlite` folder. The commands below that begin with `sqlite3` belong in your normal terminal; SQL and commands such as `.tables` belong inside the `sqlite>` shell.

#### Part B: Create a SQL File

Instead of typing the longer setup SQL directly into the terminal, we will write the table creation and insert commands in a text file first. This makes it easier to fix mistakes before running the commands.

We will still run the smaller check commands, such as `SELECT`, `.tables`, and `.schema`, directly in the SQLite shell.

SQL statements end with a semicolon (`;`). SQLite shell commands beginning with a dot, such as `.tables` and `.quit`, do not. If the prompt changes to `...>`, SQLite is waiting for you to finish the SQL statement.

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
sqlite3 -bail university.db ".read setup_students.sql"
```

This command means:

- open or create `university.db`
- use SQLite's `.read` command to read `setup_students.sql`
- run those commands inside SQLite
- use `-bail` to stop at the first SQL error

This command works in macOS/Linux terminals and Windows PowerShell. Run the setup **once**. Running it again reports `table students already exists`; `-bail` stops before any duplicate rows are inserted.

To restart this exercise from scratch, stop any API server, delete only `university.db` from your `week2-sqlite` exercise folder, and rerun the setup. This resets the exercise data.

> **Quick question**
>
> What does `.read setup_students.sql` do?
>
> <details>
> <summary>Show answer</summary>
>
> It tells SQLite to execute the SQL commands stored in `setup_students.sql`. It is a SQLite command, so it does not depend on your terminal's input-redirection syntax.
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

You should see three rows, with IDs `1`, `2`, and `3`. Ada Lovelace starts in year `2`, Alan Turing in year `3`, and Grace Hopper in year `1`.

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

Ada Lovelace should now be in year `3`. The updated value is saved in `university.db` and will appear in Part 2.

19. Exit SQLite:

```sql
.quit
```

Part 1 is complete. Continue to [Part 2](part-2.md).
