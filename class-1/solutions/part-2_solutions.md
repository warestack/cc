### Week 1 Part 2 Solutions: Hello FastAPI Exercise

Use these solutions only after you have tried the exercise.

#### `requirements.txt`

```text
fastapi==0.141.1
uvicorn==0.52.4
```

#### `main.py`

```python
from fastapi import FastAPI

# Create the FastAPI app object.
app = FastAPI()


@app.get("/")
def home():
    # Return JSON for the home endpoint.
    return {"message": "Hello from my exercise API"}


@app.get("/about")
def about():
    # Return simple information about this API.
    return {
        "name": "Week 1 Exercise API",
        "version": "1.0.0",
        "author": "your name"
    }
```

Replace `your name` with your own name.

#### Commands

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

On Windows, use:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

#### Browser Tests

```text
http://127.0.0.1:8000/
```

```text
http://127.0.0.1:8000/about
```
