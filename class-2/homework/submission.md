### Week 2: Share Your Homework for Feedback

After completing [Homework 1](homework-1.md) and [Homework 2](homework-2.md), share your Notes CRUD API with the class.

#### Publish Your Project

1. Prepare your `week2-notes-crud` project and create an empty **public GitHub repository**, as you practised in [Week 1's Weekend Activity](../../class-1/lab/weekend-activity.md). Leave GitHub's README, `.gitignore`, and licence initialisation options unchecked; you will add your files locally.
2. Include `main.py`, `requirements.txt`, `.gitignore`, and a `README.md` explaining how to create the virtual environment, install the packages, run the API, and test each endpoint.
3. Add these rules to `.gitignore` before committing:

   ```gitignore
   .venv/
   __pycache__/
   *.pyc
   *.db
   .env
   ```

   The app creates `notes.db` on startup. Other students should create their own database by running the app; your local database and virtual environment do not need to be uploaded.

4. In your README, summarise your tests: creating a note, reading it, updating one field, deleting it, and requesting a missing note. Include the observed response status codes.
5. Commit your project files with a clear message, then push them to the public repository. Open it on GitHub and check that the required files are visible and your `.venv` folder and `notes.db` are excluded.

#### Post in Teams

Post your **repository link** in [Lab Exercises and Solutions](https://teams.microsoft.com/l/channel/19%3A7cb8bd3bc3084d559fd93a5d1372c6f4%40thread.tacv2/Lab%20Exercises%20and%20Solutions?groupId=0f8f51d6-f7ce-4a6e-beeb-249bd6aca600&tenantId=89d07f47-d258-463c-8700-635ffaeca38e).

Use the heading **Week 2 Homework: Notes CRUD API**. Include a brief description of your API, what you tested, and any questions or difficulties you would like feedback on.

Everyone is encouraged to review each other's code, follow the README, and leave helpful comments in the relevant Teams thread. Keep feedback respectful and specific.

Continue to the [Weekend Activity: Cloud and AI](../lab/weekend-activity.md).
