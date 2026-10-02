### Week 6 Part 2: Containerize a FastAPI App

In this part, you will create a small FastAPI app and run it inside a Docker container.

You will do this on your GCP VM.

#### What You Will Learn

- What a `Dockerfile` is.
- How to build a Docker image.
- How to run a container from your image.
- How to publish a container port.
- How to test the container in the browser and in Postman.

#### Part A: Create a New Project

1. Create a new folder:

```bash
mkdir week6-fastapi-docker
```

2. Move into it:

```bash
cd week6-fastapi-docker
```

3. Create `requirements.txt`:

```bash
pico requirements.txt
```

4. Add:

```text
fastapi==0.141.1
uvicorn==0.52.4
```

Save and exit.

5. Create `main.py`:

```bash
pico main.py
```

6. Add:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello from FastAPI inside Docker"}


@app.get("/health")
def health():
    return {"status": "ok"}
```

This is the FastAPI app that will run inside the container.

- `app = FastAPI()` creates the API application.
- `GET /` is a simple route to prove the app is running.
- `GET /health` is a common route used to check whether an API is alive.
- The code is still normal FastAPI code. Docker changes how we package and run it.

#### Part B: Create the Dockerfile

7. Create a file called `Dockerfile`:

```bash
pico Dockerfile
```

8. Add:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Save and exit.

This file tells Docker how to build the container image.

- `FROM python:3.12-slim` starts with a small Python environment.
- `WORKDIR /app` creates and uses `/app` as the project folder inside the image.
- `COPY requirements.txt .` copies only the dependency list first.
- `RUN pip install ...` installs the Python packages inside the image.
- `COPY . .` copies the FastAPI code into the image.
- `EXPOSE 8000` documents that the app uses port `8000` inside the container.
- `CMD ...` is the command that runs when the container starts.

#### What Is Happening?

- `FROM python:3.12-slim` starts from a small Python image.
- `WORKDIR /app` sets the folder inside the container.
- `COPY requirements.txt .` copies the requirements first.
- `RUN pip install ...` installs FastAPI and Uvicorn.
- `COPY . .` copies the app code.
- `EXPOSE 8000` documents the app port.
- `CMD ...` starts the FastAPI app.

<details>
<summary>Why do we use `--host 0.0.0.0` inside Docker?</summary>

Because the app must listen on all network interfaces inside the container. If it only listens on `127.0.0.1`, it may not be reachable from outside the container.

</details>

#### Part C: Build the Image

9. Build the image:

```bash
docker build -t week6-fastapi-app:1 .
```

Do not forget the final `.`.

The dot means: use the current folder as the build context.

The build command creates an image called `week6-fastapi-app` with version tag `1`.

- An image is the packaged version of your app.
- The image contains Python, the installed packages, and your FastAPI code.
- Docker can create containers from this image.

10. Check the image:

```bash
docker images
```

#### Part D: Run the Container

11. Run the container:

```bash
docker run -d --name week6-api -p 80:8000 week6-fastapi-app:1
```

This means:

- `-d` runs the container in the background.
- `--name week6-api` gives the container a clear name.
- `-p 80:8000` connects VM port `80` to container port `8000`.

12. Check the running container:

```bash
docker ps
```

13. Open the browser using your VM external IP:

```text
http://YOUR_VM_EXTERNAL_IP/
```

Remember to use `http`, not `https`.

14. Open:

```text
http://YOUR_VM_EXTERNAL_IP/health
```

The container is now running your FastAPI app.

- Uvicorn runs inside the container on port `8000`.
- Docker publishes it on VM port `80`.
- In the browser, you use the VM external IP because the container is running on the VM.

> **Quick question**
>
> Why do we use port `80` in the browser, but Uvicorn runs on port `8000`?
>
> <details>
> <summary>Show answer</summary>
>
> Docker maps VM port `80` to container port `8000` using `-p 80:8000`.
>
> </details>

#### Part E: Test in Postman

15. Open Postman on your computer.

16. Send:

```text
GET http://YOUR_VM_EXTERNAL_IP/
```

17. Send:

```text
GET http://YOUR_VM_EXTERNAL_IP/health
```

Both requests should return JSON.

#### Part F: Stop and Remove the Container

18. Stop the container:

```bash
docker stop week6-api
```

19. Remove it:

```bash
docker rm week6-api
```

20. Check:

```bash
docker ps -a
```

Part 2 is complete. Continue to [Part 3](part-3.md).
