### Week 4 Part 1: Validation Recap for User Registration

In Week 3, you used Pydantic validation for courses.

In this short recap, you will use the same idea for user registration. This time the data is more sensitive because it contains an email address and a password.

#### What You Will Learn

- How to reuse Pydantic validation for user input.
- How to validate email addresses.
- How to avoid returning passwords in API responses.
- How to test invalid data in `/docs`.

#### Part A: Create the Project

1. Create a new folder:

```text
week4-auth-api
```

2. Open it in VS Code.

3. Create and activate a virtual environment.

4. Create `requirements.txt`:

```text
fastapi==0.141.1;
uvicorn==0.52.4;
sqlalchemy;
passlib[bcrypt];
bcrypt<5;
pyasn1>=0.4.6;
python-jose[cryptography];
```

5. Install:

```bash
python -m pip install -r requirements.txt
```

#### Part B: Create a Small Validation App

6. Create `main.py`.

7. Add:

```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()


# This schema describes the data accepted by /register-preview.
# A schema is a Python class that says which fields the request body must contain.
class UserRegister(BaseModel):
    # Field adds validation rules.
    # Here, username must be between 3 and 50 characters.
    username: str = Field(min_length=3, max_length=50)

    # EmailStr checks that the value looks like an email address.
    # This needs the email-validator package.
    email: EmailStr

    # password must be at least 6 characters.
    password: str = Field(min_length=6)


@app.post("/register-preview")
def register_preview(user: UserRegister):
    # If we reach this point, validation has passed.
    # FastAPI has already converted the JSON body into a UserRegister object.
    # Do not return the password in the response.
    return {
        "username": user.username,
        "email": user.email,
        "message": "Validation passed"
    }
```

This code checks registration data before we save anything.

- `UserRegister` is the schema for the request body.
- `Field(...)` checks the length of `username` and `password`.
- `EmailStr` checks that the email looks valid.
- `register_preview()` returns only safe information.
- The password is accepted for validation, but it is not returned in the response.

8. Add `email-validator` to `requirements.txt`:

```text
email-validator
```

9. Install again:

```bash
python -m pip install -r requirements.txt
```

10. Run:

```bash
uvicorn main:app --reload
```

11. Open:

```text
http://127.0.0.1:8000/docs
```

12. Test `POST /register-preview` with:

```json
{
  "username": "stelios",
  "email": "stelios@example.com",
  "password": "secret123"
}
```

13. Now try invalid data:

```json
{
  "username": "st",
  "email": "not-an-email",
  "password": "123"
}
```

FastAPI should return validation errors.

> **Quick question**
>
> Why is it useful for FastAPI to reject bad data before it reaches our database code?
>
> <details>
> <summary>Show answer</summary>
>
> It prevents invalid or incomplete data from entering the application. This makes the API safer and easier to debug.
>
> </details>

#### Part C: Stop the Server

14. Stop the server with `Ctrl + C`.

Part 1 is complete. Continue to [Part 2](part-2.md).
