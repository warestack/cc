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

For installation steps specific to your system, follow the [official Postman installation guide](https://learning.postman.com/docs/getting-started/installation/install-app/).

Use the **desktop app** for this homework so you can send requests directly to your local API at `127.0.0.1`.

3. Install and open Postman.

You may be asked to create or sign in to a Postman account. Follow the screen instructions.

#### Watch the Basics First

Watch [How to Send Your First API Request in Postman](https://www.youtube.com/watch?v=2oOSnxZ28fA), published on **Postman's official YouTube channel** (about 9 minutes).

Focus on creating a request, sending a GET request, and reading the JSON response. The video demonstrates a different API; for this homework, use your Notes API and the URLs below.

The video uses an earlier Postman interface, so some buttons may look different. The [current official quick-start guide](https://learning.postman.com/docs/getting-started/quick-start) provides an up-to-date reference.

#### Part B: Start Your API

4. Open your `week2-notes-crud` project in VS Code.

5. Activate your virtual environment.

6. Run the API:

```bash
uvicorn main:app --reload
```

Keep the server running while you use Postman. If the API is already running, skip the second start command. An `Address already in use` error means another process is using port `8000`.

#### Part C: Send a GET Request

7. In Postman, open a new HTTP request tab using **Add** (the **+** button) in the workbench.

8. Set the method to:

```text
GET
```

9. Enter this URL:

```text
http://127.0.0.1:8000/notes
```

10. Click **Send**.

Expect status **200** and a JSON list. If there are no notes yet, you may see:

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

Expect status **201** and a response with an `id`, `title`, and `text`. Copy the returned `id` for the next requests. IDs do not restart at `1` when notes are deleted, so do not assume your new note has ID `1`.

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

Replace `1` with the exact `id` returned by your POST request.

22. Open the **Body** tab.

23. Select **raw** and **JSON**.

24. Add this JSON:

```json
{
  "title": "Updated from Postman"
}
```

25. Click **Send**.

Expect status **200** and the updated note. The original text should remain unchanged because you sent only a title.

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

Replace `1` with the exact `id` returned by your POST request.

29. Click **Send**.

Expect status **200** and:

```json
{"message":"Note deleted"}
```

30. Send `GET /notes` again to check that this note is gone. Other notes may still be listed. Also request the deleted ID with `GET /notes/{note_id}`; expect **404** and `{"detail":"Note not found"}`.

#### Part G: Stop the Server

31. Go back to the VS Code terminal.

32. Stop the server with:

```text
Ctrl + C
```

#### Troubleshooting

- **Connection refused / could not send request:** check that Uvicorn is running and the URL uses `http://127.0.0.1:8000`.
- **`422` after POST:** check that the body is set to raw JSON and contains both `title` and `text` as strings.
- **`404` after PATCH or DELETE:** use the ID from your POST response and check that the note has not already been deleted.

#### Submission Checklist

Before you finish, make sure:

- Postman is installed.
- `GET /notes` works in Postman.
- `POST /notes` creates a note.
- `PATCH /notes/{note_id}` updates a note.
- `DELETE /notes/{note_id}` deletes a note.
- You can find the response status code in Postman.

Homework 2 is complete. Follow the [homework submission instructions](submission.md) to share your public repository in Teams for feedback, then complete the [Weekend Activity: Cloud and AI](../lab/weekend-activity.md).
