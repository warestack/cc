# Tutorial 3 — SQLite data that survives container replacement

Previous: [Build a FastAPI image](part-2.md) · [Week 6 overview](../README.md) · Next: [Docker Hub](docker-hub.md)

Extend your FastAPI project with the Courses data model from Week 3. Create a record through the API, then test what happens when its container is stopped, removed, and replaced. Allow about 30 minutes.

Run commands **on `lab-5` as `student`**. Use the existing `~/week6-fastapi-docker` project. Part 2 should have stopped and removed `week6-api`, freeing VM port 80. Check `docker ps` before continuing: only one of our web containers can publish that port at a time.

## 1. Understand where SQLite runs

SQLite is embedded in the application process. Python includes its SQLite driver; SQLAlchemy uses that driver to read and write a database file. You do not need another database container, a database password, or an inbound database port. See [SQLite's serverless architecture](https://www.sqlite.org/serverless.html).

| Location | What happens to the database? |
| --- | --- |
| Inside a container's writable filesystem | It survives stopping and starting that same container. Removing the container removes its writable filesystem. |
| In a named Docker volume mounted into the container | The volume and records remain when the container is removed. A replacement must mount the same volume to use them. |
| In a Docker Hub image | Images distribute the application. Keep live databases and personal data out of the build context and image. |

A volume is stored on the Docker host. Our volume will survive container replacement and stopping this VM, while its disk is retained. It is not automatically copied to another VM or uploaded to Docker Hub. See [Docker's volume lifecycle](https://docs.docker.com/engine/storage/volumes/#a-volumes-lifecycle).

## 2. Add the database dependency

```bash
cd ~/week6-fastapi-docker
pico requirements.txt
```

Replace the dependency list with the same application versions used in the earlier labs:

```text
fastapi==0.141.1
uvicorn==0.52.4
sqlalchemy==2.0.55
```

Docker will install these packages when you rebuild the image. No system-wide Python package installation on the VM is needed.

## 3. Replace the small API with the Courses example

Open `pico main.py`, replace the earlier two-route example with the complete code below, then save with **Ctrl+O → Enter** and exit with **Ctrl+X**. The Courses API is teaching practice, separate from the Piazza coursework.

```python
import os
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, declarative_base, sessionmaker


# Docker supplies this setting at runtime. Local Python runs use courses.db.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./courses.db")
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    lecturer = Column(String, nullable=False)


class CourseCreate(BaseModel):
    code: str = Field(min_length=2, max_length=20)
    title: str = Field(min_length=3, max_length=100)
    lecturer: str = Field(min_length=2, max_length=80)


class CourseResponse(CourseCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    engine.dispose()


app = FastAPI(lifespan=lifespan)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Courses API version 1"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/courses", response_model=list[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    return db.query(Course).order_by(Course.id).all()


@app.get("/courses/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.get(Course, course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@app.post("/courses", response_model=CourseResponse, status_code=201)
def create_course(course_data: CourseCreate, db: Session = Depends(get_db)):
    course = Course(**course_data.model_dump())
    try:
        db.add(course)
        db.commit()
        db.refresh(course)
        return course
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Course code already exists")
```

SQLAlchemy maps `Course` to a table, while Pydantic checks request bodies and shapes responses. Each request gets a database session that closes afterward. `db.commit()` saves a row; `db.rollback()` clears a failed transaction. Startup creates missing tables without deleting or reseeding existing records. Revisit [Week 3's SQLAlchemy tutorial](../../class-3/lab/part-2.md) if these ideas need a recap.

## 4. Configure the database path and rebuild

Create `pico .env.example` containing:

```dotenv
DATABASE_URL=sqlite:////data/courses.db
```

Four slashes select an **absolute Linux path**, `/data/courses.db`. The three-slash local default in the code uses `courses.db` relative to the current working directory. See [SQLAlchemy's SQLite connection strings](https://docs.sqlalchemy.org/en/20/dialects/sqlite.html#connect-strings).

Make a working configuration file:

```bash
cp .env.example .env
```

If you are repeating the tutorial and `.env` already exists, inspect it before replacing it. This lab setting contains no secret. In coursework, keep real secrets in your private runtime configuration and use placeholders in examples. `--env-file` makes Docker supply these settings; the Python code does not automatically load `.env`.

Keep the `.dockerignore` from Part 2. It must exclude `.env`, database files and their sidecars, and runtime data. Allow `.env.example` in Git as the documented example. It is not used to bake settings into this image.

Replace `pico Dockerfile` with:

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /data
COPY main.py .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

`/data` must exist before SQLite creates its file. We will mount that directory, keeping the database and any SQLite journal files together. Leave out a Dockerfile `VOLUME` instruction for this comparison: we will explicitly choose when to attach a volume.

```bash
docker build -t week6-courses-api:1 .
```

## 5. Test storage without a volume

Start with an ordinary container filesystem:

```bash
docker run -d --name courses-api -p 80:8000 --env-file .env week6-courses-api:1
docker ps -a
docker logs courses-api
curl -i http://127.0.0.1/health
```

Wait for Uvicorn's startup message before sending requests; if a request runs too early, retry it after checking the logs. Create a temporary course:

```bash
curl -i -X POST http://127.0.0.1/courses \
  -H 'Content-Type: application/json' \
  -d '{"code":"TEMP-CC","title":"Temporary course","lecturer":"Example Tutor"}'
curl -i http://127.0.0.1/courses
```

Expect `201 Created`, a generated integer `id`, and the saved row in the list. Now stop and restart **the same container**:

```bash
docker stop courses-api
docker start courses-api
docker logs courses-api
curl -i http://127.0.0.1/courses
```

After startup, the row is still there. Stopping does not remove this container's writable filesystem. Record the result, then remove the container and create a replacement without a mount:

```bash
docker stop courses-api
docker rm courses-api
docker run -d --name courses-api -p 80:8000 --env-file .env week6-courses-api:1
docker logs courses-api
curl -i http://127.0.0.1/courses
```

After startup, expect `200 OK` with `[]`: the new container has a new database. The image contains the code, not the record created while the old container was running.

```bash
docker stop courses-api
docker rm courses-api
```

## 6. Store the database in a named volume

```bash
docker volume create week6-courses-data
docker run -d --name courses-api -p 80:8000 --env-file .env \
  --mount type=volume,source=week6-courses-data,target=/data \
  week6-courses-api:1
docker logs courses-api
```

If the named volume already exists, Docker reuses it and earlier rows can reappear. Choose a new course code for your evidence rather than deleting an existing volume. Wait for startup, then create a course that you want to keep:

```bash
curl -i -X POST http://127.0.0.1/courses \
  -H 'Content-Type: application/json' \
  -d '{"code":"CC26","title":"Cloud Computing","lecturer":"Example Tutor"}'
```

Record the returned `id`, `code`, `title`, and `lecturer`. Set this shell variable to **the actual returned ID**; `1` is an example for a fresh database:

```bash
COURSE_ID=1
curl -i "http://127.0.0.1/courses/$COURSE_ID"
docker inspect courses-api --format '{{json .Mounts}}'
docker volume inspect week6-courses-data
```

Expect `200 OK` with your row. The mount inspection should identify volume `week6-courses-data` at `/data`. Collect this **before replacement** evidence.

```bash
docker stop courses-api
docker rm courses-api
docker run -d --name courses-api -p 80:8000 --env-file .env \
  --mount type=volume,source=week6-courses-data,target=/data \
  week6-courses-api:1
docker logs courses-api
curl -i "http://127.0.0.1/courses/$COURSE_ID"
```

After startup, expect the identical row and ID. This is persistence evidence because the container was removed and replaced. A successful restart alone would not distinguish the two storage approaches.

## 7. Check successful and rejected requests

Repeat the `CC26` POST body above against the same database: expect `409 Conflict` (or use your actual saved code if you changed it). Also try:

```bash
curl -i http://127.0.0.1/courses/999999
curl -i -X POST http://127.0.0.1/courses \
  -H 'Content-Type: application/json' \
  -d '{"code":"X","title":"A","lecturer":"B"}'
```

Expect `404 Not Found` for the missing ID and `422 Unprocessable Entity` for the short fields. Confirm `GET /courses` still returns the saved data afterward.

Use Postman on your computer to repeat the checks through `http://YOUR_VM_EXTERNAL_IP`. Use your VM's current external IP and **HTTP**, with no `:8000` suffix. Browser users can inspect `http://YOUR_VM_EXTERNAL_IP/docs`; Postman can send the POST body as raw JSON with `Content-Type: application/json`.

### Checkpoint and next step

- [ ] Explain the different results of stopping and removing a container.
- [ ] Create a course (`201`), retrieve it (`200`), and verify `404`, `409`, and `422` responses.
- [ ] Capture the same row before and after replacement using `week6-courses-data`.
- [ ] Keep runtime configuration and database files out of the image.

Keep the named volume and the saved row for [Tutorial 4 — Docker Hub](docker-hub.md). It will replace this container with one created from your published image. If pausing, stop the container and then stop `lab-5` in Compute Engine; keep the VM's disk. When returning, start the VM, reconnect as `student`, enter this project folder, and start `courses-api`. Reset `COURSE_ID` from your notes if the SSH shell is new.

The [independent exercise](part-3.md) includes final cleanup after evidence collection. Removing the named volume is a separate, deliberate deletion of its records.
