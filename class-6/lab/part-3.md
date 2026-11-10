### Week 6 Part 3: Independent Docker Exercise

Use the app you built in [SQLite and Docker](sqlite-and-docker.md) and published in [Docker Hub](docker-hub.md). Spend about 20 minutes checking it independently. Work in your existing `week6-fastapi-docker` project on `lab-5`; keep the database volume from the tutorials.

Your goal is to show that the published image runs correctly and that a record created through the API survives replacing its container.

#### Task 1: Identify What Is Running

Check the running `courses-api` container, its image reference and the volume mounted at `/data`. Record your Docker Hub repository link, explicit version tag and full `repository@sha256:...` reference. Use the digest reported by your push or pull and listed in `RepoDigests`, rather than only the local image ID.

The expected image reference is `USERNAME/week6-courses-api:1`, with your Docker Hub username substituted. The named volume is `week6-courses-data`, and the runtime database URL is `sqlite:////data/courses.db`.

<details>
<summary>Hint: Which commands help identify the container and its storage?</summary>

Use `docker ps`, `docker inspect courses-api`, `docker volume inspect week6-courses-data` and the image-inspection command from the Docker Hub tutorial. The container's `Mounts` section should show the named volume mounted at `/data`.

</details>

#### Task 2: Test Successful and Rejected Requests

Use Postman or Swagger UI at `http://YOUR_VM_EXTERNAL_IP/docs`. Use `http` and your VM's current external IP.

1. Request `GET /health` and `GET /courses`; expect `200`.
2. Create a course with `POST /courses`, choosing a course code that is not already present. Supply `code`, `title` and `lecturer` with valid lengths, as in Week 3. Expect `201`.
3. Save the full returned JSON and its generated integer `id`. Retrieve that exact ID with `GET /courses/{course_id}`; expect `200` and matching values.
4. Submit the same course code again; expect `409`, and check that no extra course was created.
5. Send a course with a one-character `code` and otherwise valid fields; expect `422`.
6. Request a course ID that does not exist; expect `404`.

Choose a different course code if you repeat the exercise. Do not assume that the new record's ID is `1`.

<details>
<summary>Hint: What should the successful course response contain?</summary>

It should contain the server-generated integer `id` plus the `code`, `title` and `lecturer` you submitted. Test a record you created yourself; built-in or seeded data does not prove that your new write survived.

</details>

#### Task 3: Replace the Container and Check the Same Record

1. Capture the successful retrieval of your new course, including its ID and fields.
2. Stop and remove `courses-api`. Keep `week6-courses-data`.
3. Create a replacement container from your versioned Docker Hub image, publishing VM port `80` to container port `8000`. Pass the database configuration and mount the same named volume at `/data`.
4. Check the container and logs, then retrieve the saved course ID again. Expect `200` and the same JSON values.
5. Confirm that the replacement is a new container using the same volume. Capture the before-and-after requests, results and container identities.

Restarting the same container is a useful operational check, but it does not demonstrate replacement. Complete the stop, remove and new `docker run` sequence.

<details>
<summary>Hint: Which settings must the replacement keep?</summary>

Keep `DATABASE_URL=sqlite:////data/courses.db`, the named-volume mount `--mount type=volume,src=week6-courses-data,dst=/data`, and `-p 80:8000`. Use your `.env` file and the versioned image reference as taught in the Docker Hub tutorial. Inspect `docker ps -a` and `docker logs courses-api` if the API does not respond.

</details>

#### Optional Extension: A Visible Version 2

Change the response from `GET /` so that it visibly identifies version 2. Build and publish `USERNAME/week6-courses-api:2`, recording its digest. The Docker Hub tutorial ended with `docker logout`, so [sign back in with your token](docker-hub.md#3-sign-in-from-the-vm-using-a-token) before pushing and run `docker logout` again afterward. Replace the version-1 container with version 2 using the same database volume. Verify both the changed home response and your unchanged stored course.

Keep `:1` as your first version rather than overwriting it. This is practice for the assignment's later versioned deployment update; Kubernetes is covered in a later lab.

#### Checkpoint

Before cleanup, make sure you can show:

- A versioned Docker Hub image reference and registry digest.
- A running container using that image on the VM.
- Successful creation/retrieval and the `409`, `422` and `404` responses.
- The exact newly created record before and after container removal and replacement.
- A named volume mounted at the database location.
- A short explanation of why the database is kept outside the image and container's disposable filesystem.

#### Cleanup

Collect the evidence needed for [Homework 1](../homework/homework-1.md) before removing anything.

Stop and remove only your practice API container:

```bash
docker stop courses-api
docker rm courses-api
docker ps
```

If a container from an earlier part is still running, stop and remove that specific practice container too. Keep `week6-courses-data` if you need to finish the homework or repeat the persistence check.

When you have collected all evidence and no longer need the practice data, you may delete this specific volume:

```bash
docker volume rm week6-courses-data
```

That separate command permanently deletes the practice database. Do not remove the volume before the replacement check, and do not run a blanket cleanup against other projects.

Finally, stop `lab-5` in the GCP console. Keep the VM and its disk for later labs. Do not delete the VM or disk as part of this lab's cleanup.

Part 3 is complete. Continue to [Homework 1](../homework/homework-1.md).
