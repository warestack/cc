###  Lab5.2: Containerising apps with Docker

#### What am I about to learn?

Today's lab session focused on containerising applications with Docker.

Lab 5.2 focuses on how to:

* Develop a simple application in your computer
* Push your code to a versioning system (GitHub)
* Pull your code to the VM
* Create an image and run the node.js app!

You will need to watch the Docker installation video (Lab 5.1) to proceed.

> Take your time; make sure you double-check the commands before you run it

1. The following video demonstrates the steps to follow in order to containerise an app using Docker and GitHub. 

[![Watch the video](https://i.ytimg.com/vi/7AmBWq0NSVE/hqdefault.jpg)](https://youtu.be/7AmBWq0NSVE)

> **You should run this tutorial on your <u>local computer</u> and your <u>GCP VM</u> :white_check_mark:**

2. To run this tutorial, you will need a GCP VM; you will have to use the docker VM that we created in the previous tutorial.

#### On your local computer

3. Open visual studio code and create a simple node.js application. Follow the video to create your project. Your `app.js` should look like the following script.

```javascript
// app.js
const express = require('express')
const app = express()

app.get('/', (req,res)=>{
    res.send('I just shipped my app to a container!')
})

app.listen(3000)
```

4. **Before you continue**, you will need to install GitHub on your local computer. Follow the following guide to download and install GitHub, then return to this tutorial.

* How to install GitHub on Windows, Mac or Linux?
  * [Installation guide for Windows, Mac and Linux users](https://github.com/git-guides/install-git)

* We introduced GitHub in lab 3, so its a good idea to recap the step-by-step guide:
  * [Lab3.2-Pushing-code-to-GitHub.md](https://github.com/steliosot/cc/blob/master/Class-3/Lab3.2-Pushing-code-to-GitHub.md)

5. In this tutorial, we will create a new private repo, so make sure you follow the steps as presented in the video. The commands include:

* Check your `git` version.

```bash
$ git --version
```

* Initialise a git in your folder. The command converts your unversioned project folder to a Git repository.

```bash
$ git init
```

* Add remote repo from git (this should be in one single line).

```bash
$ git remote add origin https://YOUR_GIT_USERNAME:YOUR_GIT_TOKEN@YOUR_GIT_REPO
```

> When you clone a repository with git clone , it automatically **creates a remote connection called origin pointing back to the cloned repository**. This is useful for developers creating a local copy of a central repository, since it provides an easy way to pull upstream changes or publish local commits.

* Add  files and folders of the current working directory to git. Don't forget the `.` that means add everything.

```bash
$ git add . 
```

* Commit the changes to the repo with a message.

```bash
$ git commit -m "Pushing my app files"
```

> The `commit` captures a snapshot of the project's currently staged changes. Committed snapshots can be thought of as “safe” versions of a project to be pushed in the repo.

* Upload the files in the repo.

```bash
$ git push -f origin master
```

> Refresh your GitHub page; your files/folders should be there now!
>
> We just uploaded our code to GitHub! :clap:
>
> Now move to your VM!

#### On your GCP VM

6. Open a terminal connection to the GCP VM. You can connect from VSC or using the SSH button (in GCP as in my case).
7. In the VM, make sure you are already logged in as docker-user (follow Lab 5.1). 

> Just as a reminder, the command is: 
>
> ```bash
> $ su - docker-user
> ```

6. Let's clone our GitHub repo, make sure you create a new token as shown in the video.

```bash
$ git clone --branch master https://<username>:<token>@repo
```

> This is a link to my private repo:
>
> ```bash
> FOR SECURITY REASONS, THE LINK IS ON MOODLE
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

12. Build an image called `lab5-image:1`

```bash
$ docker image  build -t lab5-image:1 .
```

13. Run the container `lab-container` using the `lab5-image:1` image.

```bash
$ docker container run -d --name lab-container --publish 80:3000 lab5-image:1
```

> `-d`: runs process in the background. 

14. The second part of the video, demonstrates another example of cloning a MiniFilm auth repo. 
    * Feel free to use your own repository, rather than mine. 
    * Make sure that your code works before your push to GitHub!

> This is a link to my private repo:
>
> ```
> FOR SECURITY REASONS, THE LINK IS ON MOODLE
> ```
>
> :rotating_light: Note that we push and pull `.env` files, we will see best practices on how to manage this in next classes.
>
> For the moment, make sure you don't push your `.env` file into a public repo.

14. Try to access the MiniFilm app in postman; you just created a containerised app!
15. Now, run once more the same process using your own MiniPost application.

:checkered_flag: Well done! You completed lab 5.2! 
