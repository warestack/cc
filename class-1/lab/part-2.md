### Week 1 Part 2: Hello FastAPI Exercise

This is a short exercise based on [Part 1](part-1.md).

Start from zero. Close your previous VS Code project first, then create a new project in your preferred folder.

Solutions are in the [solutions](../solutions/) folder.

#### Goal

Create a new FastAPI app with two simple endpoints:

- `GET /` returns a welcome message
- `GET /about` returns information about the app

#### Part A: Close the Previous Project

1. In VS Code, close the folder from Part 1.

   Use:

```text
File > Close Folder
```

2. Create a new folder called:

```text
week1-exercise-api
```

3. Open the new folder in VS Code.

4. Open a new VS Code terminal.

#### Part B: Create the Python Environment

5. Create a virtual environment:

6. Activate the virtual environment.

7. Create the `requirements.txt` file.

8. Add:

```text
fastapi==0.141.1;
uvicorn==0.52.4;
```

9. Install the requirements.

#### Part C: Create the App

10. Create a file called:

```text
main.py
```

11. Write a FastAPI app that has these endpoints:

```text
GET /
GET /about
```

Use this boilerplate:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    # Add your return statement here.
    pass


@app.get("/about")
def about():
    # Add your return statement here.
    pass
```

The home endpoint should return:

```json
{"message": "Hello from my exercise API"}
```

The about endpoint should return:

```json
{
  "name": "Week 1 Exercise API",
  "version": "1.0.0",
  "author": "your name"
}
```

Replace `your name` with your own name.

#### Part D: Run and Test

12. Run the app.

13. Open the home endpoint in your browser.

14. Open the about endpoint.

15. Stop the server.

#### Checklist

Before you finish, make sure:

- you created a new project folder
- your virtual environment works
- `requirements.txt` contains `fastapi` and `uvicorn`
- `GET /` works in the browser
- `GET /about` works in the browser

Part 2 is complete. Continue to [Part 3](part-3.md).
