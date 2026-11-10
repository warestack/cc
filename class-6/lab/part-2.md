# Week 6 Part 2 — Containerize a FastAPI app

Previous: [Docker containers](part-1.md) · [Week 6 overview](../README.md) · Next: [SQLite and Docker](sqlite-and-docker.md)

Build a small FastAPI image and run it on your existing `lab-5` VM. All terminal commands below run in the **VM's SSH terminal as `student`**. Browser and Postman checks run on your own computer, using the VM's current external IP from [Part 1](part-1.md).

## 1. Create the application

Start from your home directory:

```bash
cd ~
mkdir week6-fastapi-docker
cd week6-fastapi-docker
pwd
```

Expect `/home/student/week6-fastapi-docker`. If the folder already exists, inspect it and reuse your earlier work rather than deleting it. This project does not need a virtual environment on the VM: the Dockerfile will install Python packages inside the image.

Create `requirements.txt` with pico:

```bash
pico requirements.txt
```

Add the same package versions used in earlier labs:

```text
fastapi==0.141.1
uvicorn==0.52.4
```

Save with **Ctrl+O → Enter**, then exit with **Ctrl+X**. Create `main.py`:

```bash
pico main.py
```

Add and save:

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

`GET /` returns a welcome message. `GET /health` provides a simple check that the API is alive. This is normal FastAPI code; Docker changes how it is packaged and started.

## 2. Exclude local files before building

Create `.dockerignore` in this project folder:

```bash
pico .dockerignore
```

Add and save:

```text
.venv/
venv/
.git/
__pycache__/
*.py[cod]
.env
.env.*
!.env.example
*.db
*.db-*
*.sqlite
*.sqlite-*
*.sqlite3
*.sqlite3-*
data/
```

A [`.dockerignore` file](https://docs.docker.com/build/concepts/context/#dockerignore-files) excludes matching files from the build context. It keeps local environments, Git history, real environment files, SQLite databases and their journal files, and runtime data out of the build. The exception permits a deliberately non-secret `.env.example` containing placeholders. A `.gitignore` file does not replace `.dockerignore`.

This tiny app has no secrets or database yet. Establish the exclusions now, before the later database and Docker Hub tutorials.

## 3. Write the Dockerfile

Create a file named exactly `Dockerfile`, with a capital `D` and no extension:

```bash
pico Dockerfile
```

Add and save:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

| Instruction | Purpose |
| --- | --- |
| `FROM python:3.12-slim` | Start from the official Python image with the `3.12-slim` tag. |
| `WORKDIR /app` | Create and use `/app` inside the image. |
| `COPY requirements.txt .` and `RUN pip install ...` | Copy and install the dependencies before copying application code, so Docker can reuse this layer when only the code changes. |
| `COPY main.py .` | Copy the one application file this example needs. |
| `EXPOSE 8000` | Document the container's application port; it does not publish the port. |
| `CMD [...]` | Start Uvicorn when a container using this image starts. |

`--host 0.0.0.0` makes Uvicorn listen on the container's network interfaces. Listening only on `127.0.0.1` inside the container would prevent Docker's published port from reaching it. Do not use development auto-reload for this container.

## 4. Build the image

From `~/week6-fastapi-docker`, run:

```bash
docker build -t week6-fastapi-app:1 .
docker images
```

The final `.` selects the current project folder as the build context. `week6-fastapi-app` is the image name and `1` is its tag. You should see that image in the list. If the build fails, read the first error and check your filenames and file contents before continuing.

## 5. Run and check the container on the VM

Inspect existing containers first:

```bash
docker ps -a
```

Use VM port `80` for one lab web container at a time. If you are repeating this part, stop and remove your earlier `week6-api` using Section 8 before creating another with that name.

```bash
docker run -d --name week6-api -p 80:8000 week6-fastapi-app:1
docker ps
docker logs week6-api
```

`-d` runs in the background, `--name` names the container, and `-p 80:8000` publishes **VM port 80 → container port 8000**. The existing Google Cloud HTTP rule allows traffic to VM port 80. No rule for VM port 8000 is needed. See [Docker's port-publishing explanation](https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/).

Check the API from the **VM terminal**:

```bash
curl -i http://127.0.0.1/health
```

Expect an HTTP `200` response and:

```json
{"status":"ok"}
```

If `curl` is not installed, run `sudo apt update` and then `sudo apt install curl`, and repeat the check. If the app is still starting, inspect its logs and retry. Here `127.0.0.1` means the VM because the command runs in its SSH terminal.

## 6. Test from your computer

In your computer's browser, replace `YOUR_VM_EXTERNAL_IP` with the VM's **current** external IP:

| URL | Expected result |
| --- | --- |
| `http://YOUR_VM_EXTERNAL_IP/` | HTTP `200` and the welcome message. |
| `http://YOUR_VM_EXTERNAL_IP/health` | HTTP `200` and `{"status":"ok"}`. |
| `http://YOUR_VM_EXTERNAL_IP/docs` | FastAPI's interactive API documentation. |

Use `http`, without `https` or `:8000`: Docker publishes the app on HTTP's default port `80`. Your laptop's `127.0.0.1` refers to your laptop, so use the VM's external IP in its browser.

In Postman on your computer, send `GET` requests to the first two URLs. Confirm both the `200` status and their JSON bodies. Save any screenshot you need for your lab notes before cleanup.

## 7. Diagnose a failed check

| Symptom | What to check |
| --- | --- |
| Container is absent from `docker ps` | Run `docker ps -a` to find stopped containers, then `docker logs week6-api` to read the application error. |
| Name `week6-api` is already in use | Inspect the old container. If it is your earlier attempt, stop it if running and remove it before repeating `docker run`. A stopped container still reserves its name. |
| Host port 80 is already allocated | Inspect `docker ps` for your previous lab web container. Stop only that container before retrying. If no container explains the conflict, ask the tutor to help identify the host process using port 80. |
| VM-side curl works but your computer cannot connect | Check the current external IP, `http` URL, and the VM's existing Allow HTTP setting. The working local request confirms the app and Docker port mapping respond on the VM. |
| VM-side curl fails | Check container status and logs first. Confirm Uvicorn uses `0.0.0.0:8000` and the run command uses `-p 80:8000`. |

If a failed `docker run` leaves a `Created` or stopped container behind, remove that failed `week6-api` after inspection before retrying. If you edit the source, rebuild the image, stop/remove the old container, and run a new one; editing the host file does not change code already copied into an image.

## 8. Stop and remove this container

Run in the VM terminal:

```bash
docker stop week6-api
docker rm week6-api
docker ps -a
```

Confirm `week6-api` is gone and VM port 80 is free for the next tutorial. Keep the `week6-fastapi-app:1` image and project files; removing a container does not remove its image.

### Checkpoint

- [ ] The project has `main.py`, `requirements.txt`, `.dockerignore`, and `Dockerfile`.
- [ ] The image builds and the container starts successfully.
- [ ] VM-side curl, your browser, and Postman return the expected responses.
- [ ] You can explain the host/container port mapping and the purpose of `.dockerignore`.
- [ ] You stopped and removed `week6-api` before continuing.

Continue to [SQLite and Docker](sqlite-and-docker.md). Keep the VM running while you continue; stop it in the Cloud Console if pausing.
