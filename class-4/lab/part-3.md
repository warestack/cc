### Week 4 Part 3: Protect API Routes with JWT

In this part, you will protect an API route using the JWT token from login.

#### What You Will Learn

- What a bearer token is.
- How to read the current user from a token.
- How to protect a FastAPI route.
- How to test protected routes in `/docs`.

#### Part A: Add Token Reading

1. Open `security.py`.

2. Add these imports:

```python
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError
from sqlalchemy.orm import Session

import models
from database import get_db
```

These imports add the tools needed to read and verify bearer tokens.

- `HTTPBearer` reads the `Authorization: Bearer ...` header.
- `JWTError` lets us catch invalid token problems.
- `Session` and `get_db` let us find the user in the database.
- `models` gives access to the `User` table.

3. Add this under the constants:

```python
# HTTPBearer tells FastAPI to expect an Authorization: Bearer <token> header.
bearer_scheme = HTTPBearer()
```

This creates the security dependency.

- If a route uses this dependency, FastAPI expects a bearer token.
- If no token is sent, FastAPI rejects the request before the route runs.

4. Add this function at the bottom:

```python
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db)
):
    # Extract the token value from the Authorization header.
    token = credentials.credentials

    try:
        # Decode and verify the JWT.
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # We stored the user's email in the token subject.
        email = payload.get("sub")

        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Find the user represented by the token.
    user = db.query(models.User).filter(models.User.email == email).first()

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user
```

This function finds the logged-in user from the token.

- It reads the token from the request header.
- It decodes the JWT using the same `SECRET_KEY`.
- It reads the email from the token subject, `sub`.
- It queries the database for that user.
- If anything is wrong, it returns a `401` error.
- If everything is valid, it returns the current user object.

#### Part B: Create a Protected Router

5. Create `routers/profile.py`:

```python
from fastapi import APIRouter, Depends

import models
from security import get_current_user

router = APIRouter()


@router.get("/me")
def get_profile(current_user: models.User = Depends(get_current_user)):
    # This function only runs if get_current_user returns a valid user.
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }
```

This router contains a protected route.

- `Depends(get_current_user)` means the route needs a valid token.
- If the token is missing or invalid, the function does not run.
- If the token is valid, `current_user` contains the logged-in user.
- The route returns profile information for that user.

6. Open `main.py`.

7. Update the router import:

```python
from routers import auth, profile
```

This imports both routers so `main.py` can connect them to the app.

8. Add:

```python
app.include_router(profile.router, prefix="/profile")
```

This connects the profile routes under `/profile`.

- The route `@router.get("/me")` becomes `/profile/me`.
- Because the route depends on `get_current_user`, it is protected.

#### Part C: Test Without a Token

9. Run the app:

```bash
uvicorn main:app --reload
```

10. Open:

```text
http://127.0.0.1:8000/profile/me
```

You should get an authentication error because you did not send a token.

The response should include:

```json
{"detail":"Not authenticated"}
```

#### Part D: Test With a Token in Docs

11. Open:

```text
http://127.0.0.1:8000/docs
```

12. Use `POST /auth/login` to log in.

13. Copy the `access_token` value.

14. Click the **Authorize** button at the top of the docs page.

15. Paste the token.

16. Click **Authorize**.

17. Test `GET /profile/me`.

You should see the logged-in user's profile.

> **Quick question**
>
> What does a bearer token prove to the API?
>
> <details>
> <summary>Show answer</summary>
>
> It proves that the client has a valid token created by the API. The API can decode it and identify the user.
>
> </details>

#### Completion Checklist

Before you finish, make sure:

- invalid registration data is rejected
- duplicate email registration is rejected
- login returns an access token
- `/profile/me` fails without a token
- `/profile/me` works with a valid token
- you can explain why passwords should be hashed

Part 3 is complete. Week 4 is complete.
