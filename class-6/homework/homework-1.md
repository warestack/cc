### Week 6 Homework 1: Docker Practice and Reflection

Finish the [independent exercise](../lab/part-3.md), then post a 150–200-word reflection and practical evidence in the Teams collaboration space. This is formative practice for feedback and adds no assignment marks. Use the Week 6 Courses API, keeping your assessed Piazza solution separate.

#### Practical Evidence

Include a link to your Docker Hub repository, the explicit versioned image reference, and its registry digest. Publishing, pulling and running your image are required practice this week; use the [Docker Hub tutorial](../lab/docker-hub.md).

Attach a small set of labelled screenshots or terminal/request excerpts showing:

- Your versioned image running as `courses-api` on the GCP VM, with `week6-courses-data` mounted at `/data`.
- A successful API request through the VM's external address and a new course created with `201`.
- Duplicate course code `409`, invalid input `422`, and missing course `404` responses.
- Retrieval of that same newly created course before and after removing and replacing the container. Show its ID and matching fields, plus the different container identities. Keep the same named volume during replacement.

Captions should identify the request or command, its result and what it demonstrates. A running-container screenshot alone does not prove that the API works or that data persisted. Use your actual results and briefly identify anything unfinished.

#### Practice README

Add a short `README.md` to your `week6-fastapi-docker` project. Include:

- What the practice API does and the required software.
- Commands to build, tag, publish, pull and run the image.
- Your Docker Hub image reference and digest.
- The runtime database setting and the named volume mounted at `/data`.
- How to test the API, replace its container while preserving the database, and clean up afterwards.

Keep the Dockerfile, `.dockerignore`, pinned dependency file and `.env.example` with your practice project. Check that the image excludes database files and real `.env` files. Your example configuration must use placeholders for any secrets. Share the practice repository link or attach the README for feedback; do not upload the database or your assessed Piazza implementation to Teams.

#### Reflection: 150–200 Words

Explain in your own words:

- The difference between an image and a container.
- How Docker Hub helps another machine obtain your packaged API, and how a version tag differs from a registry digest.
- Why your SQLite file belongs in a volume and what happened to your record when you replaced the container.
- One reason Docker helps with cloud deployment and one limitation or problem you observed.

The README, image reference, captions and evidence are separate from the reflection's word count.

#### Optional Extension

Complete the [visible version-2 update](../lab/part-3.md#optional-extension-a-visible-version-2). Record the new tag and digest, show the changed home response, and verify that the same course remains stored. This extension is optional and adds no assignment marks.

#### Before You Finish

Collect evidence before cleanup. Follow the [lab cleanup steps](../lab/part-3.md#cleanup), keeping the named volume until your persistence check is complete. Stop `lab-5` when finished and keep its disk for later labs.

Do not share passwords, tokens, real secrets, `.env` files or database files in Teams, screenshots, public images or repositories. Keep `.env.example` safe to share.
