### Lab 5

#### Exercise 1 – Docker basics: Hello Container

**Task**

Recreate the "Hello World" Docker container setup from scratch on your GCP VM:

1. Update your VM packages.

2. Install Docker and verify that it’s running.

3. Create a new user named docker-student with Docker permissions.

4. Run the official Docker hello-world image.

5. List all containers and remove the exited one.
6. Document your solution.

#### Exercise 2 – Data cleaning with Python in a Docker container

**Task**

Recreate the "Hello World" Docker container setup from scratch on your GCP VM:

1. On your VM, create a simple file called `app.py` and implement a simple script to remove duplicated data from a list. Print the results.

```python
data = [10, 20, 10, 30, 20, 40, 50, 30, 50]
...
```

2. Write a `Dockerfile` that:

- Uses Ubuntu as base image (`FROM ubuntu:latest`)
- Installs Python3
- Copies the script inside `/app`
- Runs the script automatically on startup

3. Build the image and run a container named `mini-python-app`.

4. Verify that the container outputs the print message.
5. Document your solution.

#### Exercise 3 – Containireze the MiniFillm application (lab4)

1. Containerize the MiniFilm app (implemented in Week 4).
2. Push the code to your GitHub repository.
3. Pull the repository to your VM and run the application.
4. Send me a screenshot of the running instance with a few calls from postman (no code).

> [Link to week 4](https://github.com/warestack/cc/tree/main/Class-4)

#### When you complete the tasks, document your work and send your solutions to me via MS Teams.

