###  Lab5.2: Pushing code to GitHub and Docker

#### What am I about to learn?

Today's lab session focused on Docker! We will install and run the basic commands to containerise an application.

Lab 5 focuses on how to:

* Install Docker on a GCP VM
* Run the basic commands to interact with Docker containers

The following image demonstrates the MiniPost microservice architecture.

You will need to watch the following video on installing and running a Docker on the VM.

> Take your time; make sure you double-check the commands before you run it

1. The following video demonstrates the commands used in this tutorial. 

[![Watch the video](https://i.ytimg.com/vi/7AmBWq0NSVE/hqdefault.jpg)](https://youtu.be/7AmBWq0NSVE)

> **You should run this tutorial on your local computer and your GCP VM :white_check_mark:**

2. To run this tutorial, you will need a GCP VM; you will have to use the docker VM that we created in the previous tutorial.

#### On your local computer

3. Open visual studio code and create a simple node.js application. Follow the video to create a new application that looks like this:

```javascript
const express = require('express')
const res = require('express/lib/response')
const app = express()

app.get('/', (req,res)=>{
    res.send('I just shipped my app to a container!')
})

app.listen(3000)
```

4. Before you continue, you will need to install GitHub on your local computer. Follow the following guide to download and install GitHub, then return to this tutorial.

* [Installation guide for Windows, Mac and Linux users](https://github.com/git-guides/install-git)

> **<u>For Windows users</u>, please use the following step by step guide: https://phoenixnap.com/kb/how-to-install-git-windows** 
>
> * Install **git bash** and then restart your visual studio code.
>
> Then you can start a new GitBash to run the git commands as follows.
>
> ![vsc-win](images/vsc-win.png)

* It might worth to revise [Lab3.2-Pushing-code-to-GitHub.md](https://github.com/steliosot/cc/blob/master/Class-3/Lab3.2-Pushing-code-to-GitHub.md)

5. We will create a new Private repo in this tutorial, so make sure you follow the steps as presented in the video. The commands include:

* See git version.

```bash
$ git --version
```

* Initialise a git in your folder.

```bash
$ git init
```

* Add remote repo from git (this should be in one single line).

```bash
$ git remote add origin https://YOUR_GIT_USERNAME:YOUR_GIT_TOKEN@YOUR_GIT_REPO
```

* Add all files and folders.

```bash
$ git add . 
```

* Commit the changes to the repo

```bash
$ git commit -m "Pushing my app files"
```

* Upload the files in the repo

```bash
$ git push -f origin master
```

> At this moment, refresh your GitHub page; your files/folders should be there now!
>
> Now go to your VM!

#### On your GCP VM

6. Open a terminal connection to the GCP VM. You can connect from VSC or using the SSH button (in GCP).
7. In the VM, make sure you are already logged in as docker-user (from Lab 5.1). 
8. Let's clone our GitHub repo.

```bash
$ git clone --branch master https://<username>:<token>@repo
```

> This is the link to the **lab5-auth-minifilm**: 
>
> ```
> FOR SECURITY REASONS THE LINK IS ON MOODLE, PLEASE DO NOT PUBLISH THIS LINK!
> ```

9. Your repo should be now in your VM; run `ls` to check it out.

```bash
$ ls

lab5-test-app
```

10. Enter in the repo folder.

```bash
$ cd lab5-test-app
```

11. Create a new Dockerfile as follows (e.g. using `pico`)

```dockerfile
FROM alpine
RUN apk add --update nodejs npm
COPY . /src
WORKDIR /src
EXPOSE 3000
ENTRYPOINT ["node", "./app.js"]
```

> Save and exit.

12. Build the image.

```bash
$ docker image  build -t mini-test-app-image:1 .
```

13. Run the container.

```bash
$ docker container run -d --name stelios-web --publish 80:3000 mini-test-app-image:1
```

> `-d` run process in the background. 

14. Try to access your service in the browser; you just created your first containerised app!
15. Make sure you follow the second part of the video to containarise the **lab5-auth-minifilm** microservice. Please follow the steps on the video, and you might need to reuse the same steps of this tutorial (8-13) to create and run the service.

> In this example, I used Postman to interact with the service, as we did in week 4.
>
> For the moment, I made the assumption that I can push the `.env` file, as it is in my private repository, but this is a bad practice and we will need to deal with this! We will explore best practices for such (configuration) files in the next classes.

16. :checkered_flag: Well done! You completed lab 5.2!

17. Now follow the same process to containerise the MiniPost application! Can you do it in less than 5 minutes? :timer_clock: