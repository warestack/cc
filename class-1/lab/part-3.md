### Week 1 Part 3: Routes, Routers, and JSON Responses

In this tutorial, you will organise your FastAPI app using routers.

Routers help keep your code clean. Instead of placing every endpoint in `main.py`, you can move related endpoints into separate files.

#### What You Will Learn

- How to create more API routes.
- How to return JSON data.
- How to create a `routers` folder.
- How to use `APIRouter`.
- How to connect a router to `main.py`.
- How to use path parameters such as `/movies/hobbit`.

#### Part A: Start From Your Existing Project

1. Open the `week1-hello-api` folder from Part 1 in VS Code.

2. Open the VS Code terminal.

3. Activate your virtual environment if it's not already activated. 

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

4. Run the app again:

```bash
uvicorn main:app --reload
```

5. Open the browser and check:

```text
http://127.0.0.1:8000/
```

You should see your home JSON response.

#### Part B: Create a Router File

6. Stop the server with `Ctrl + C`.

7. In VS Code, create a new folder called:

```text
routers
```

8. Inside `routers`, create an empty file called:

```text
__init__.py
```

This file tells Python that `routers` is a package we can import from.

9. Inside `routers`, create a file called:

```text
movies.py
```

Your project should now look like this:

```text
week1-hello-api/
  .venv/
  main.py
  requirements.txt
  routers/
    __init__.py
    movies.py
```

10. Add this code to `routers/movies.py`:

```python
# APIRouter lets this file define routes outside main.py.
from fastapi import APIRouter

# This router will hold all movie-related endpoints.
routers = APIRouter()


# This route will become /movies after we connect it in main.py.
@routers.get("/")
def get_movies():
    return {"message": "Hello world from the movies router!"}
```

#### What Is `APIRouter`?

`APIRouter` lets us group related endpoints.

In this example, movie endpoints will live in `routers/movies.py` instead of `main.py`.

#### Part C: Connect the Router to `main.py`

11. Open `main.py`.

12. Replace the file with this code:

```python
from fastapi import FastAPI

# Import the movies router from routers/movies.py.
from routers import movies

app = FastAPI()

# Connect all routes from movies.py under the /movies URL prefix.
app.include_router(movies.router, prefix="/movies")


# Keep the home endpoint in main.py.
@app.get("/")
def home():
    return {"message": "Hello world!"}


@app.get("/hello")
def hello():
    return {"message": "world!"}
```

13. Save the file.

The important line is:

```python
app.include_router(movies.router, prefix="/movies")
```

This means:

- load the routes from `routers/movies.py`
- place them under the `/movies` URL prefix
- the route `/` inside `movies.py` becomes `/movies`

> **Quick question**
>
> The router has `@router.get("/")` and `main.py` uses `prefix="/movies"`. What full URL should you test in the browser?
>
> <details>
> <summary>Show answer</summary>
>
> ```text
> http://127.0.0.1:8000/movies
> ```
>
> </details>

14. Run the server again:

```bash
uvicorn main:app --reload
```

15. Open the browser and visit:

```text
http://127.0.0.1:8000/movies
```

You should see:

```json
{"message":"Hello world from the movies router!"}
```

#### Part D: Return Movie Data as JSON

16. Stop the server with `Ctrl + C`.

17. Open `routers/movies.py`.

18. Replace it with this code:

```python
from fastapi import APIRouter

router = APIRouter()

# This dictionary is temporary in-memory data.
# Next week we will replace this style with SQL database data.
movies = {
    "hobbit": {
        "title": "The Hobbit",
        "description": "A fantasy adventure film based on J.R.R. Tolkien's novel.",
        "year": 2012
    },
    "matrix": {
        "title": "The Matrix",
        "description": "A science fiction film about simulated reality.",
        "year": 1999
    }
}


@routers.get("/")
def get_movies():
    # Return all movie records.
    return movies


@routers.get("/{movie_id}")
def get_movie(movie_id: str):
    # movie_id comes from the URL, for example /movies/hobbit.
    # We use it as a key in the movies dictionary.
    return movies[movie_id]
```

19. Run the server:

```bash
uvicorn main:app --reload
```

20. Open:

```text
http://127.0.0.1:8000/movies
```

You should see all movies.

21. Open:

```text
http://127.0.0.1:8000/movies/hobbit
```

You should see only the Hobbit movie.

#### Understanding `/{movie_id}`

`/{movie_id}` is a path parameter.

It means the URL can contain a changing value:

- `/movies/hobbit` gives `movie_id = "hobbit"`
- `/movies/matrix` gives `movie_id = "matrix"`

Then this line reads the matching movie from the dictionary:

```python
return movies[movie_id]
```

> **Quick question**
>
> Small research task: search the web for FastAPI path parameters. What does the `{movie_id}` part of the route do?
>
> <details>
> <summary>Show answer</summary>
>
> It captures part of the URL and passes it into the function as a variable. For `/movies/hobbit`, FastAPI passes `"hobbit"` into `movie_id`.
>
> </details>

#### Part E: Handle Missing Movies

22. Try this URL:

```text
http://127.0.0.1:8000/movies/avatar
```

You will see an error because `avatar` is not in the `movies` dictionary.

23. Stop the server with `Ctrl + C`.

24. Update the import in `routers/movies.py`:

```python
from fastapi import APIRouter, HTTPException
```

25. Replace the `get_movie` function with this version:

```python
@routers.get("/{movie_id}")
def get_movie(movie_id: str):
    # .get() returns None instead of crashing if the key does not exist.
    movie = movies.get(movie_id)

    if movie is None:
        # Return a clear 404 response when the movie is missing.
        raise HTTPException(status_code=404, detail="Movie not found")

    return movie
```

26. Run the server again:

```bash
uvicorn main:app --reload
```

27. Test:

```text
http://127.0.0.1:8000/movies/avatar
```

You should now see a clearer JSON error:

```json
{"detail":"Movie not found"}
```

#### Command Summary

- `uvicorn main:app --reload` runs your FastAPI app.
- `Ctrl + C` stops the server.
- `APIRouter()` creates a router.
- `app.include_router(...)` connects a router to the main app.
- `prefix="/movies"` places router endpoints under `/movies`.
- `/{movie_id}` creates a path parameter.
- `HTTPException(status_code=404, detail="...")` returns a clear API error.

Part 3 is complete. Continue to [Homework 1](../homework/homework-1.md).
