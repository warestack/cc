# Part 4 — Docker basics: install and run a container

Previous: [Linux basics](part-3.md) · [Week 5 overview](../README.md) · Next: [Exercise 1](exercise-1.md)

Install Docker on your existing `lab-5` VM and run a small test container. This is the first Docker tutorial; in [Week 6](../../class-6/README.md), you will explore an interactive Ubuntu container and build and run your own FastAPI container.

## 1. Understand images and containers

Docker runs applications in containers, keeping their files and processes separate from the host's usual environment.

| Term | Meaning in this lab |
| --- | --- |
| Host | Your Ubuntu VM, `lab-5`, where Docker is installed. |
| Image | A packaged application and the files it needs; a template for creating containers. |
| Container | An instance created from an image. It can be running or stopped. |

A container shares the host's Linux kernel; it is not another full VM. Several containers can be created from the same image.

## 2. Check your VM and user

Continue inside the SSH session on `lab-5` as `student`. If you paused, start the VM, reconnect with its **SSH** button, and [switch to the existing lab user](part-2.md#5-reconnect-using-the-existing-user). Run:

```bash
hostname -s
whoami
```

Expect `lab-5` and `student`. Run the following commands on this VM, not directly in Cloud Shell, on your laptop, or on `lab-5-exercise`.

## 3. Install and start Docker

Use Ubuntu's [`docker.io` package](https://packages.ubuntu.com/noble/docker.io), the same package used in the course's Docker material:

```bash
sudo apt update
sudo apt install docker.io
sudo systemctl enable --now docker
sudo systemctl is-active docker
docker --version
```

Run each command separately. Confirm the installation with `Y` if asked. `apt update` refreshes package lists; `apt install` installs Docker and its dependencies. If Docker is already installed, APT reports that instead.

`systemctl enable --now docker` starts the Docker service now and enables it at boot. `is-active` should print `active`. The version command checks that the Docker command is installed; it does not prove your user can access the running service.

## 4. Give your lab user access

While still logged in as `student`, run:

```bash
sudo usermod -aG docker "$USER"
```

`$USER` expands to your current username, `student`. `-aG` adds the group without removing existing group memberships, including `sudo`.

> [!WARNING]
> Membership of the `docker` group grants root-level control of this VM. Treat it like administrator access. See [Docker's Linux post-installation guidance](https://docs.docker.com/engine/install/linux-postinstall/).

Start a fresh login shell so it picks up the new group membership:

```bash
su - student
```

Enter the existing `student` password when asked; no characters appear as you type. Then check:

```bash
whoami
id -nG
docker ps
```

Expect `student`, a group list containing `docker`, and a container table, which may be empty. Unlike `docker --version`, `docker ps` verifies access to the Docker service without sudo.

If you see a permission error, check your username and group list, then reconnect and switch to the existing `student` user again. If Docker cannot connect to the service, check `sudo systemctl status docker`; press `q` if a status pager opens.

## 5. Run your first container

```bash
docker run --name lab5-hello hello-world
```

On its first run, Docker downloads the `hello-world` image from Docker Hub, creates a container named `lab5-hello`, and runs its program. Look for:

```text
Hello from Docker!
```

The program prints its message and exits. Returning to the terminal is expected: this container is not a web server and does not stay running. No inbound web port or Docker Hub account is needed for this step.

## 6. Inspect and clean up

```bash
docker images
docker ps
docker ps -a
```

- `docker images` lists downloaded images, including `hello-world`.
- `docker ps` lists only running containers, so `lab5-hello` should be absent.
- `docker ps -a` includes stopped containers; `lab5-hello` should show `Exited (0)`, meaning its program completed successfully.

> **Quick question**
>
> Why can `hello-world` appear in `docker images` when `docker ps` has no containers listed?

<details>
<summary>Show answer</summary>

The image remains available after the program finishes. `docker ps` shows only running containers; `docker ps -a` also shows the stopped container created from that image.

</details>

Remove only the test container and verify it is gone:

```bash
docker rm lab5-hello
docker ps -a
```

The image remains, so you can reuse it. If repeating the tutorial produces a name-conflict error, inspect the existing `lab5-hello` with `docker ps -a` and complete this cleanup before running it again. Each `docker run` creates a new container.

### Checkpoint

- [ ] Docker is installed on `lab-5` and the service is active.
- [ ] `student` can run `docker ps` without sudo.
- [ ] The test container printed `Hello from Docker!` and exited successfully.
- [ ] You can explain the difference between an image and a container.
- [ ] You removed the test container and kept Docker installed for Week 6.

**Stop `lab-5` before moving to the separate exercise VM.** In **Compute Engine → VM instances**, select only `lab-5`, choose **Stop**, and wait for **Stopped**. Closing SSH does not stop the VM. Keep its boot disk, user, and installed software for Week 6; retained disks can still incur storage charges.

Continue to [Exercise 1 — Create a VM independently](exercise-1.md). Dockerfiles, building images, publishing ports, and running FastAPI follow in Week 6.
