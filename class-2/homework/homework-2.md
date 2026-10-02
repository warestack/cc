### Week 2 Homework 2: Test APIs with Postman

In this homework exercise, you will use Postman to make API calls to your FastAPI app.

Postman is an API client. It lets you send requests such as `GET`, `POST`, `PATCH`, and `DELETE` without writing code.

#### What You Will Learn

- How to download Postman.
- How to send a `GET` request.
- How to send a `POST` request with JSON.
- How to send a `PATCH` request.
- How to send a `DELETE` request.
- How to read the response status code and JSON body.

#### Part A: Download Postman

1. Open the official Postman download page:

```text
https://www.postman.com/downloads/
```

Use the official Postman site only.

2. Download the desktop app for your operating system.

Postman supports Windows, macOS, and Linux. The official installation guide says to download the latest desktop app from the Postman download page and choose the option for your operating system.

3. Install and open Postman.

You may be asked to create or sign in to a Postman account. Follow the screen instructions.

#### Part B: Start Your API

4. Open your `week2-notes-crud` project in VS Code.

5. Activate your virtual environment.

6. Run the API:

```bash
uvicorn main:app --reload
```

Keep the server running while you use Postman.

#### Part C: Send a GET Request

7. In Postman, create a new request.

8. Set the method to:

```text
GET
```

9. Enter this URL:

```text
http://127.0.0.1:8000/notes
```

10. Click **Send**.

You should see a JSON response. If there are no notes yet, you may see:

```json
[]
```

#### Part D: Send a POST Request

11. Create a new request.

12. Set the method to:

```text
POST
```

13. Enter this URL:

```text
http://127.0.0.1:8000/notes
```

14. Open the **Body** tab.

15. Select **raw**.

16. Change the body type to **JSON**.

17. Add this JSON:

```json
{
  "title": "Postman note",
  "text": "I created this note using Postman."
}
```

18. Click **Send**.

You should see a response with an `id`, `title`, and `text`.

#### Part E: Send a PATCH Request

19. Create a new request.

20. Set the method to:

```text
PATCH
```

21. Enter this URL:

```text
http://127.0.0.1:8000/notes/1
```

If your note has a different ID, replace `1` with your note ID.

22. Open the **Body** tab.

23. Select **raw** and **JSON**.

24. Add this JSON:

```json
{
  "title": "Updated from Postman"
}
```

25. Click **Send**.

You should see the updated note.

#### Part F: Send a DELETE Request

26. Create a new request.

27. Set the method to:

```text
DELETE
```

28. Enter this URL:

```text
http://127.0.0.1:8000/notes/1
```

If your note has a different ID, replace `1` with your note ID.

29. Click **Send**.

You should see:

```json
{"message":"Note deleted"}
```

30. Send `GET /notes` again to check that the note is gone.

#### Part G: Stop the Server

31. Go back to the VS Code terminal.

32. Stop the server with:

```text
Ctrl + C
```

#### Checklist

Before you finish, make sure:

- Postman is installed.
- `GET /notes` works in Postman.
- `POST /notes` creates a note.
- `PATCH /notes/{note_id}` updates a note.
- `DELETE /notes/{note_id}` deletes a note.
- You can find the response status code in Postman.

Homework 2 is complete. Week 2 is complete.
