### Week 6 Part 1: Continue with Docker Containers

Build on [Week 5's Docker basics](../../class-5/lab/part-4.md). You should already have Docker installed on `lab-5` and have run the `hello-world` container. This week, explore an interactive container before packaging FastAPI.

#### What You Will Learn

- How to check Docker after restarting your VM.
- How to pull an image and open an interactive container shell.
- How to restart an existing container and remove it when finished.

#### Part A: Reconnect and Check Docker

Start `lab-5` and connect using its **SSH** button. Cloud Shell is an [optional alternative](../../class-5/lab/part-2.md#optional--connect-through-cloud-shell). [Switch to the existing `student` user](../../class-5/lab/part-2.md#5-reconnect-using-the-existing-user); do not create the user again.

```bash
hostname -s
whoami
docker --version
docker ps
```

Expect `lab-5`, `student`, a Docker version, and a container table, which may be empty. `docker ps` must work without sudo; displaying the version alone does not verify service access.

If you missed the introduction or Docker is unavailable, complete [Week 5 Part 4](../../class-5/lab/part-4.md) through its checkpoint, then return here. Keep the VM running while continuing to Part B.

#### Part B: Run an Ubuntu Container

1. Pull the Ubuntu image:

```bash
docker pull ubuntu:24.04
```

2. Run an interactive Ubuntu container:

```bash
docker run -it --name mini-ubuntu ubuntu:24.04 bash
```

You are now inside the container, not in your VM shell. `-it` provides an interactive terminal, `--name` gives the container a name, and `bash` starts its shell. The `24.04` tag selects the Ubuntu release.

If the name is already in use from an earlier attempt, inspect `docker ps -a` and reuse the existing container with `docker start -ai mini-ubuntu` instead of creating another one.

3. Run:

```bash
ls
```

4. Exit the container:

```bash
exit
```

5. Check the container:

```bash
docker ps -a
```

6. Start it again:

```bash
docker start -ai mini-ubuntu
```

The `-ai` options attach your terminal and allow input, returning you to the same container shell. Run `exit` again to return to `lab-5` and stop the container.

7. Remove the stopped practice container:

```bash
docker rm mini-ubuntu
```

Part 1 is complete. Continue to [Part 2](part-2.md).
