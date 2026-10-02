### Week 6 Part 1: Install Docker and Run Your First Containers

In this part, you will install Docker on the GCP VM you created in Week 5 and run your first containers.

Use the `lab-5` VM and your Week 5 lab user. Do not use the default temporary user if you created a separate lab user.

#### What You Will Learn

- What Docker is.
- What an image is.
- What a container is.
- How to install Docker on Ubuntu.
- How to run and inspect containers.

#### Part A: Start Your VM

1. Go to the GCP dashboard.

2. Start your `lab-5` VM.

3. Connect to the VM using SSH.

4. Switch to your lab user if you are not already using it.

<details>
<summary>How can you check which user you are?</summary>

```bash
whoami
```

</details>

#### Part B: Install Docker

5. Update the package list:

```bash
sudo apt update
```

6. Install Docker:

```bash
sudo apt install -y docker.io
```

7. Start Docker:

```bash
sudo systemctl enable --now docker
```

8. Check the Docker version:

```bash
sudo docker --version
```

9. Check that Docker is running:

```bash
sudo systemctl status docker
```

If the status screen opens, press `q` to return to the terminal.

> **Quick question**
>
> What does `sudo apt update` do before installing Docker?
>
> <details>
> <summary>Show answer</summary>
>
> It downloads the latest package information, so Ubuntu knows what software versions are available.
>
> </details>

#### Part C: Allow Your User to Run Docker

10. Add your current user to the `docker` group:

```bash
sudo usermod -aG docker $USER
```

11. Apply the group change:

```bash
newgrp docker
```

12. Run:

```bash
docker --version
```

If this works without `sudo`, your user can run Docker commands.

> [!WARNING]
>
> Users in the `docker` group can control Docker on the machine. Treat this like administrator access.

<details>
<summary>Why did we add the user to the `docker` group?</summary>

So we can run commands like `docker ps` and `docker run` without typing `sudo` every time.

</details>

#### Part D: Run Hello World

13. Run Docker's test container:

```bash
docker run hello-world
```

You should see a message starting with:

```text
Hello from Docker!
```

This means Docker downloaded an image and created a container from it.

#### Part E: Images and Containers

An **image** is like a template or package.

A **container** is a running or stopped instance of an image.

14. Show downloaded images:

```bash
docker images
```

15. Show all containers:

```bash
docker ps -a
```

<details>
<summary>What is the difference between `docker images` and `docker ps -a`?</summary>

`docker images` shows image templates. `docker ps -a` shows containers that were created from images.

</details>

#### Part F: Run an Ubuntu Container

16. Pull the Ubuntu image:

```bash
docker pull ubuntu
```

17. Run an interactive Ubuntu container:

```bash
docker run -it --name mini-ubuntu ubuntu
```

You are now inside the container.

18. Run:

```bash
ls
```

19. Exit the container:

```bash
exit
```

20. Check the container:

```bash
docker ps -a
```

21. Start it again:

```bash
docker start mini-ubuntu
```

22. Stop it:

```bash
docker stop mini-ubuntu
```

Part 1 is complete. Continue to [Part 2](part-2.md).
