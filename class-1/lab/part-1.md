### Week 1 Part 1: Create Your First FastAPI App

Welcome to the cloud! Today, we will start by building a small web application, a typical starting point for many cloud-based systems. 

This tutorial will guide you through creating your first FastAPI project in VS Code, step by step, and testing it directly in your browser.

#### What You Will Learn

- How to create a new FastAPI project.
- How to create and activate a virtual environment.
- How to use `requirements.txt`.
- How to run a FastAPI app with Uvicorn.
- How to test API endpoints in the browser.

#### Part A: Create a New Project in VS Code

1. Open **Visual Studio Code**.

2. Create a new folder somewhere easy to find, for example in `Documents`.

   Name the folder:

```text
week1-hello-api
```

3. In VS Code, open the folder:

   **File > Open Folder**

4. Open a terminal inside VS Code:

   **Terminal > New Terminal**

5. Check that you are inside the project folder.

On Mac, you can use:

```bash
pwd
```

On Windows PowerShell, you can also use:

```powershell
Get-Location
```

#### Part B: Create a Virtual Environment

A **venv (virtual environment)** is an isolated Python environment created for a specific project. It allows each project to have its own libraries and package versions without affecting other Python projects on your computer.

6. Create a virtual environment:

```bash
python3 -m venv .venv
```

On Windows, use one of these if `python3` does not work:

```powershell
python -m venv .venv
py -m venv .venv
```

7. Activate the virtual environment.

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

When the environment is active, you should see `(.venv)` at the start of the terminal line.

> **Quick question**
>
> Do we need to create a separate virtual environment for each Python project folder?
>
> <details>
> <summary>Show answer</summary>
> Yes. It is good practice to create one virtual environment for each project. This keeps each project’s dependencies and package versions isolated from other projects.
>
> *So, make sure you memorise these commands, as you will use them very often.*
>
> </details>

#### Part C: Create `requirements.txt`

8. Create a new file in VS Code called:

```text
requirements.txt
```

9. Add these lines:

```text
fastapi==0.141.1;
uvicorn==0.52.4;
```

10. Save the file.

> `requirements.txt` is a list of packages needed by the project. It helps everyone install the same dependencies.

11. Install the packages:

```bash
python -m pip install -r requirements.txt
```

12. Check the installed packages:

```bash
python -m pip list
```

You should see `fastapi` and `uvicorn`.

#### Part D: Create the FastAPI App

13. Create a new file called:

```text
main.py
```

14. Add this code:

```python
# Import FastAPI, the framework we use to build the API.
from fastapi import FastAPI

# Create the FastAPI application object.
# Uvicorn will run this object.
app = FastAPI()


# This endpoint runs when the browser opens http://127.0.0.1:8000/
@app.get("/")
def home():
    # Returning a dictionary sends JSON back to the browser.
    return {"message": "Hello world!"}


# This endpoint runs when the browser opens http://127.0.0.1:8000/hello
@app.get("/hello")
def hello():
    return {"message": "world!"}
```

15. Save the file.

#### What Is Happening in This Code?

- `FastAPI` creates the API application.
- `app = FastAPI()` creates one app object.
- `@app.get("/")` creates a GET endpoint for `/`.
- `@app.get("/hello")` creates a GET endpoint for `/hello`.
- `return {"message": "Hello world!"}` sends JSON back to the browser.

#### Part E: Run the API

16. Run the app from the VS Code terminal:

```bash
uvicorn main:app --reload
```

This means:

- `uvicorn` runs the server.
- `main` is the Python file `main.py`.
- `app` is the FastAPI object inside `main.py`.
- `--reload` restarts the server automatically when you save code changes.

17. Open your browser and visit:

```text
http://127.0.0.1:8000/
```

You should see:

```json
{"message":"Hello world!"}
```

18. Visit the second endpoint:

```text
http://127.0.0.1:8000/hello
```

You should see:

```json
{"message":"world!"}
```

#### What Is a Port?

A port is like a numbered door on your computer.

FastAPI is running on port `8000`, so the browser uses:

```text
http://127.0.0.1:8000
```

`127.0.0.1` means your own computer. It is also called `localhost`.

> **Quick question**
>
> Can you have two FastAPI applications running on port `8000` at the same time?
>
> <details>
> <summary>Show answer</summary>
> **No.** Only one application can normally use a specific port at a time. To run two FastAPI applications simultaneously, use different ports, for example 8000 and 8001.
> 
> </details>

#### Part F: Stop the Server

19. Go back to the VS Code terminal.

20. Press:

```text
Ctrl + C
```

This stops the server.

Part 1 is complete. Continue to [Part 2](part-2.md).
