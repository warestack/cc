### Lab5.1: Introduction to Docker

#### What am I about to learn?

Today's lab session focused on Docker! We will install and run the basic commands to containerise an application.

Lab 5 focuses on how to:

* Install Docker on a GCP VM
* Run the basic commands to interact with Docker containers

The following image demonstrates the MiniPost microservice architecture.

You will need to watch the following video on installing and running a Docker on the VM.

> Take your time; make sure you double-check the commands before you run it

1. The following video demonstrates the commands used in this tutorial. 

[![Watch the video](https://i.ytimg.com/vi/jS8cNtqKhyU/hqdefault.jpg)](https://youtu.be/jS8cNtqKhyU)

> **You should run this tutorial on your GCP VM :white_check_mark:**

2. To run this tutorial, you will need a GCP VM. If you don't remember creating a VM, please watch the video. For this tutorial, I used the following configuration.
   * Zone: us-central1-a
   * Machine type: e2-medium
   * HTTP traffic: On
   * HTTPS traffic: On
   * Image: [ubuntu-1804-bionic-v20220131](https://console.cloud.google.com/compute/imagesDetail/projects/ubuntu-os-cloud/global/images/ubuntu-1804-bionic-v20220131?project=lab-7-270015)
   * Size (GB): 25
3. Open a new terminal connection and run the follow the following commands. Make sure you understand the process. You don't have to memorise the commands.
4. Let's update our system.

```bash
$ sudo apt-get update

Hit:1 http://us-central1.gce.archive.ubuntu.com/ubuntu bionic InRelease
Get:2 http://us-central1.gce.archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]
...
Get:26 http://security.ubuntu.com/ubuntu bionic-security/multiverse Translation-en [4732 B]
Fetched 23.7 MB in 5s (4972 kB/s)                           
Reading package lists... Done
```

>  Note that:
>
>  * The **sudo apt-get update** command downloads package information from all configured sources.
>
>  * The sources often defined in /etc/apt/sources.list file and other files located in /etc/apt/sources.list.d/ directory. 
>
>  * So when you run the update command, it downloads the package information from the Internet. It is helpful to get info on updated packages or their dependencies.

5. We can now install Docker; make sure you type `Y` for Yes when prompted.

```bash
$ sudo apt-get install docker.io

Reading package lists... Done
Building dependency tree       
Reading state information... Done
...
Do you want to continue? [Y/n] Y
...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for ureadahead (0.100.0-21) ...
```

> Docker is now installed on our VM; we can start trying a couple of tasks.
>
> We install docker once (in a VM), then we can just use it.

6. What is the Docker version? Run the next command

```bash
$ sudo docker --version

Docker version 20.10.7, build 20.10.7-0ubuntu5~18.04.3
```

7. We can see if Docker is running using the following command.

```bash
$ sudo systemctl status docker
```

> You will need to break the command, use `ctrl` + `C`

8. Let's create a new user called docker-user. You can use this user to run our containers.

```bash
$ sudo adduser docker-user

Adding user `docker-user' ...
Adding new group `docker-user' (1003) ...
Adding new user `docker-user' (1002) with group `docker-user' ...
Creating home directory `/home/docker-user' ...
Copying files from `/etc/skel' ...
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
Changing the user information for docker-user
Enter the new value, or press ENTER for the default
        Full Name []: 
        Room Number []: 
        Work Phone []: 
        Home Phone []: 
        Other []: 
Is the information correct? [Y/n] Y
```

> Make sure you add a password, and you can leave the rest empty—type Y at the end (although you can just press enter).

9. We will need to give `sudo` access to our new `docker-user`, so let's add it to the `sudo` group.

```bash
$ sudo usermod -aG sudo docker-user
```

> If we don't add the user in the `sudo` group, we will not run `sudo` commands.

10. Now, run the following command; this will allow us to give `sudo` permissions to docker to run our commands. 

```bash
$ sudo usermod -aG docker docker-user
```

> This command ensures that our new `docker-user` can run docker commands without using the `sudo` keyword. For example, instead of running always: 
>
> ```bash
> $ sudo docker <command> 
> ```
>
> we will be able to run:
>
> ```bash
> $ docker <command>
> ```

11. Let's switch users, type the following command.

```bash
$ su - docker-user
```

> The `-` symbol allows us to switch user (`su`) and change to the target user's home directory.

12. We should be ready now! Try the following command to see if everything works fine.

```bash
$ docker
```

> You should be able to see a list of available options and commands. We can always refer to this when we need to explore using commands and options.

13. Now let us create a new container. Docker comes with a registry called **Docker Hub**. Anyone can host their Docker images on Docker Hub, so most applications and Linux distributions you’ll need will have images hosted there. Let's try the usual Hello World container!

```bash
$ docker run hello-world
```

> This command downloads the `Alpine` baseimage and creates a Docker container for the first time. It then runs the container and executes the echo command.
>
> Docker was initially unable to find the hello-world image locally, so it downloaded it from Docker Hub, the default repository. Once the image was downloaded, Docker created a container from the image and the application within the container was executed, displaying the message.
>
> There is a message in the logs...
>
> ```bash
> Hello from Docker!
> This message shows that your installation appears to be working correctly.
> ```

14. Let's move; we will now set up an Ubuntu container to install any software we like. The container will be hosted inside the GCP VM. Firstly, we will use the Docker Hub to search for an ubuntu image.

```bash
$ docker search ubuntu
```

> The script will crawl Docker Hub and return a listing of all images whose names match the search string. Go on and examine the output; we can see one ubuntu image (at the top) with more than ten thousand stars; that's the official image we will use.

15. Once you’ve identified the image you would like to use, you can download it to your computer using the `pull` subcommand. In our case, we will go for the `ubuntu` image.

```bash
$ docker pull ubuntu
```

> We just downloaded an Ubuntu image! The image is a file that we need to use to run a container (think about it as an executable file that you just need to double click to run, in the old days, we used to buy CDs with software, these were images of the same software).
>
> Note that this will download the latest ubuntu image from the official ubuntu repository, so your output could be different than mine.

16. I will clear my terminal and move forward.

```bash
$ clear	
```

17. Let's see the available docker images; we should have two, the `hello-world` and the `ubuntu` that we downloaded before.

```bash
$ docker images
```

> That's my output:
>
> ```
> REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
> ubuntu        latest    54c9d81cbb44   3 days ago     72.8MB
> hello-world   latest    feb5d9fea6a5   4 months ago   13.3kB
> ```
>
> You can use the following command to delete images:
>
> ```
> docker image rm hello-world
> ```
>
> * For the moment, do not remove it.
> * Note that if you create a container, you cannot delete the image since the image is in use. You will need to stop the container and then delete it.

18. Let's see the available running containers. Remember, a container is a running instance of an image!

```bash
$ docker ps -all
```

> This command will show you all the available containers.
>
> My output is as follows:
>
> ```bash
> CONTAINER ID   IMAGE         COMMAND    CREATED          STATUS                      PORTS     NAMES
> 039e63ad6db8   hello-world   "/hello"   15 minutes ago   Exited (0) 15 minutes ago             nice_hermann
> ```
>
> Since the **`STATUS`** is **`Exited`**, that means that my container is stopped; that's fine; we can rerun it if we like.
>
> Exited: The Docker container has exited, **usually because the process inside the container has exited**.

19. Let's delete the container; for this, you will need to use the **`CONTAINER ID`** or the container name (under the  **`NAMES`**, this is a name. that is randomly assigned, so your container name should be different). In my case, I will use the **`CONTAINER ID`**.

```bash
$ docker rm 039e63ad6db8
```

20. We will need to use the `ubuntu` image to create a new container. We can also assign a new name to the new container; I will call it `mini-ubuntu`. The combination of the `-it` switch, that gives you interactive shell access into the container.

```bash
docker run -it --name mini-ubuntu ubuntu
```

>  Great! We just created a new container, and we are actually inside the new running container. In other words, you have a small Ubuntu container running inside your Ubuntu VM. 
>
> You can run any command and install any software you like. 
>
> Try the **ls** command. 
>
> ```bash
> # ls
> 
> bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
> ```

21. Let us exit from the container and return to the VM.

```
 # exit
```

> From now on:
>
> * The dollar symbol `$`, in the terminal indicates that we are running commands in the VM.
> * The hash symbol `#` in the terminal indicates that we are running commands in the container.
>
> I exited, so now we are in the VM prompt.

22. To see all the active or inactive docker containers, we will need to run the following command.

```bash
$ docker ps -a
```

> The `mini-ubuntu` container is there, but it is not active.
>
> ```bash
> CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                      PORTS     NAMES
> 0bceff76c9ad   ubuntu    "bash"                   4 minutes ago    Exited (0) 29 seconds ago             mini-ubuntu
> ...
> ```

23. Let's start the `mini-ubuntu` container.

```bash
$ docker start mini-ubuntu
```

24. It should be up and running; let's check.

```bash
$ docker ps -a
```

> The output verifies our assumption, that the `mini-ubuntu` is now running (**`STATUS`** is **`Up`**).
>
> ```bash
> CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS     NAMES
> 0bceff76c9ad   ubuntu    "bash"                   7 minutes ago    Up 9 seconds             mini-ubuntu
> ...
> ```

25. If we want to list only the running containers, we can try the following command.

```bash
$ docker ps -all
```

> | Shorthand        | Description                                             |
> | ---------------- | ------------------------------------------------------- |
> | `--all`, `-a`    | Show all containers (default shows just running)        |
> | `--latest`, `-l` | Show the latest created container (includes all states) |
> | `--size`, `-s`   | Display total file sizes                                |
> | `--filter`, `-f` | Filter output based on conditions provided              |
>
> Explore more about the [docker ps command here](https://docs.docker.com/engine/reference/commandline/ps/).

26. Let's attach (connect) to the running container shell.

```bash
$ docker exec -it mini-ubuntu /bin/bash 
```

> So we can always connect to the shell and run any commands that we might want.

27. Let's try an alternative way of exiting from the container; try the following combination of keys:

* press `ctrl` + `c` followed by `ctrl`+`d`

> The output should look like this:
>
> ```bash
> # ^C
> # exit
> ```
>
> However, we can exit (detach) from our container using this combination of keys without stopping it.

28. Let's check if the `mini-ubuntu` is still running.

```bash
$ docker ps -all
```

> The container should be **`Up`** and running!

29. We can stop the container using the following command.

```bash
$ docker stop mini-ubuntu
```

30. And finally, let's remove the container using the the `docker rm` command ([docker rm documentation](https://docs.docker.com/engine/reference/commandline/rm/)).

```bash
$ docker rm mini-ubuntu
```

> You can only delete stopped containers; you have to force deletion if a container is running.

> | Shorthand       | Description                                             |
> | --------------- | ------------------------------------------------------- |
> | `--force`, `-f` | Force the removal of a running container (uses SIGKILL) |
>
> åand to check; the container is now deleted.

31. We learned the basic commands by now, so our next (essential) step is to create our first containerised application! First, let's try using Python.

We will need a `Python` container for this; this will come pre-installed with Python. We will use the `docker search` command ([docker search documentation](https://docs.docker.com/engine/reference/commandline/search/)).

```bash
$ docker search python
```

32. Once more, I will use the official image; it should be the one on the top called (surprisingly :laughing:) `python`.

Let us create a new container and run it; I will call it `mini-python-container` ([docker run documentation](https://docs.docker.com/engine/reference/commandline/run/)). 

```bash
docker run --name mini-python-container -it python
```

> * Then `-it` instructs Docker to allocate a pseudo-TTY connected to the container’s stdin creating an interactive `bash` shell.
>   * [TTY](https://en.wikipedia.org/wiki/Tty_(Unix)) is a subsystem in Linux and Unix that makes process management, line editing, and session management possible at the kernel level through TTY drivers.
>   * We use TTY to establish asynchronous, [bidirectional](https://en.wikipedia.org/wiki/Duplex_(telecommunications)) communication ([IPC](https://en.wikipedia.org/wiki/IPC_socket)) channel (with two ports) between two or more processes, the VM and the container.
>
> It might take a minute to complete; docker will need to download the image and run it. 
>
> Let's explore some valuable shorthands. 
>
> | Shorthand         | Description                                                  |
> | ----------------- | ------------------------------------------------------------ |
> | --interactive, -i | Keep STDIN open even if not attached                         |
> | --tty` , `-t      | Allocate a [pseudo-TTY](https://en.wikipedia.org/wiki/Pseudoterminal) |
> | --detach` , `-d   | Run container in background and print container ID           |
> | --attach` , `-a   | Attach to STDIN, STDOUT or STDERR                            |

33. Did you notice that we just downloaded and created a new python container? We are already in the Python3 interpreter!

Let's try some python! 

```python
>>> print('Hello World!')
```

> That's great! Let's exit now...

```python
>>> exit()
```

> We exited directly to the VM.

34. Let's list the containers.

```bash
$ docker ps -a
```

> It looks like we stopped our `mini-python-container`...

35. Let's start it

```bash
$ docker start mini-python-container 
```

36. Now let us create a python file called `test.py` using the `cat` command. The command allows us to create a file and set its contents.

```bash
$ echo "print('Hello from mini-python-container')" > test.py
```

37. Let's run the `ls` command to check that the 'test.py' file is there.

```bash
$ ls

test.py
```

> It looks like we have our file!

38. Let's move the file in the container and its home directory. We will need to use the `cp` command that can help you copy files and folders between a container and the local filesystem ([docker cp documentation](https://docs.docker.com/engine/reference/commandline/cp/)). 

```bash
$ docker cp test.py mini-python-container:/home
```

> Make sure you run the container, before you proceed:
>
> ```bash
> docker start mini-python-container
> ```

39. Let's run a command inside our container, using the `docker exec` command ([docker exec documentation](https://docs.docker.com/engine/reference/commandline/exec/))

```bash
$ docker exec -it  mini-python-container python /home/test.py
```

> We should see our python script output! 
>
> | Shorthand         | Description                                        |
> | ----------------- | -------------------------------------------------- |
> | --interactive, -i | Keep STDIN open even if not attached               |
> | --tty` , `-t      | Allocate a pseudo-TTY                              |
> | --detach` , `-d   | Run container in background and print container ID |
>
> * You can replace `-it` with `-d`, this will run your python script inside the running container, in the background.
>
> Congrats :clap:  you just created your first containerised application with Python!

40. Now, let's try to organise our commands; instead of running all these manual tasks one after the other, we will create a new `Dockerfile`.

* A Dockerfile is **a text document that contains all the commands a user could call on the command line to assemble an image**. 
* Using docker build, you can create an **automated build** that executes several command-line instructions in succession. 
* You will find more information on the official [Dockerfile documentation](https://docs.docker.com/engine/reference/builder/) page.

41. Let's create a new `Dockerfile` as follows.

```
pico Dockerfile
```

> Add the following commands.
>
> ```dockerfile
> FROM ubuntu:latest
> RUN apt-get update -y
> RUN apt-get install software-properties-common -y
> RUN apt-get install python3.7 -y
> ADD . /app
> WORKDIR /app
> CMD ["python3", "test.py"]
> ```
>
> Let's examine our `Dockerfile`
>
> * `FROM ubuntu:latest` :arrow_right: Use the latest ubuntu image; I will download Ubuntu and install Python manually for this example.
>
> * `RUN apt-get update -y` :arrow_right: Update the container (using `y` as Yes)
>
> * `RUN apt-get install software-properties-common -y` :arrow_right: Install the necessary packages for Python3 (e.g. software-properties-common)
>
> * `RUN apt-get install python3.7 -y` :arrow_right: Install python3.7
>
> * `ADD . /app` :arrow_right: Add all the data of the current folder (e.g. our `test.py`) to a new directory called `app` inside the containers.
>
> * `WORKDIR /app` :arrow_right: Make the`workdir` our current working directory.
>
> * `CMD ["python3", "test.py"]` :arrow_right: Run the `python3` command on  `test.py` file. (`python3 test.py`)

42. Let's build our new image; I will call it `mini-python3-image`.

```bash
$ docker build -f Dockerfile . -t mini-python3-image
```

> * The [docker build](https://docs.docker.com/engine/reference/commandline/build/) command builds an image from a `Dockerfile` and a *context*. The build’s context is the set of files at a specified location `PATH` or `URL`. The `PATH` is a directory on your local filesystem. The `URL` is a Git repository location. You can imagine downloading our Git repo using a simple command here. This is what we are about to do in lab 5.2.
>
> The command might take a minute as we will need to run all the necessary steps one after the other. Make sure you monitor the output; you might notice the different steps!
>
> Finally, our image is now ready:
>
> ```bash
> $ Successfully tagged mini-python3-image:latest
> ```
>
> Traditionally, the `Dockerfile` is called `Dockerfile` and is located in the root of the context. You use the `-f` flag with `docker build` to point to a Dockerfile anywhere in your file system.

43. Let's run it; I will create a new container called `test-python3-container`; I will still use the interactive `-it` shorthand to enter  the bash.

```bash
$ docker run --name test-python3-container -it mini-python3-image /bin/bash
```

:checkered_flag: Well done! You completed lab 5.1! 

Now move to lab 5.2!