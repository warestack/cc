### Week 6: Docker, SQLite and Docker Hub

Build on [Week 5's Docker introduction](../class-5/lab/part-4.md) to package FastAPI, keep SQLite data when a container is replaced, and publish a versioned image to Docker Hub.

#### Two-Hour Lab Route

Complete the work in this order. The SQLite and Docker Hub tutorials come before the independent exercise at the existing Part 3 link.

| Activity | Time | Outcome |
| --- | ---: | --- |
| [Part 1: Continue with Docker Containers](lab/part-1.md) | 10 minutes | Reconnect to `lab-5`, check Docker and explore an Ubuntu container. |
| [Part 2: Containerize a FastAPI App](lab/part-2.md) | 25 minutes | Build and run a small FastAPI image. |
| [SQLite and Docker](lab/sqlite-and-docker.md) | 30 minutes | Extend the app with SQLAlchemy and keep its database in a named volume. |
| [Docker Hub](lab/docker-hub.md) | 25 minutes | Tag, publish, pull and run your image; record its registry digest. |
| [Part 3: Independent Docker Exercise](lab/part-3.md) | 20 minutes | Verify the published API and prove that a new record survives container replacement. |
| [Cleanup](lab/part-3.md#cleanup) | 10 minutes | Collect evidence, remove practice containers and stop the VM. |

Then complete [Homework 1](homework/homework-1.md): a short reflection and the practical evidence checklist. The visible version-2 update is optional extension work.

#### Before You Start

- You need the existing `lab-5` VM, its `student` user, Docker access and the VM's HTTP firewall rule from Week 5.
- If you missed Docker installation or the `hello-world` checkpoint, complete [Week 5 Part 4](../class-5/lab/part-4.md) first.
- Review [Week 3's SQLAlchemy API](../class-3/lab/part-2.md) if needed. This week applies those database ideas to containers; SQLite does not need a separate database container.
- Create a Docker Hub account for the publishing tutorial. Use your own Docker Hub username in image references.

Use the same `week6-fastapi-docker` project throughout the guided tutorials. The first image is `week6-fastapi-app:1`; after adding SQLite, build `week6-courses-api:1`. Publish it as `USERNAME/week6-courses-api:1`. The final container is `courses-api`, with volume `week6-courses-data` mounted at `/data`.

#### Connection to the Assignment

These are practice tasks using a Courses API. They prepare you for the assignment's [Docker, Docker Hub and persistent-storage requirements](../assignment/03-testing-and-deployment.md#containerisation-requirements). Follow the assignment brief separately for Piazza, authentication, testing and later GKE deployment. This lab and its homework add no assignment marks.

Week 7 introduces Kubernetes. For the assignment's GKE deployment, Kubernetes will pull a versioned image from the registry, supply runtime configuration, and mount persistent storage at the database path. A PersistentVolumeClaim takes the place of this VM's local named volume; the data in `week6-courses-data` does not automatically move to GKE. The same configuration approach supplies the coursework's JWT secret, which must stay consistent across application replacement. Authentication remains covered by Week 4 and the assignment brief.

> [!WARNING]
>
> Capture your evidence before cleanup. Keep the named volume until you have verified persistence. Stop your containers and stop `lab-5` when finished, keeping its disk for later labs. Running cloud resources can spend your coupon credit.
