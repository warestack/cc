### Lab 2: Part 2 - Introduction to NodeJS with express

By the end of this part, you will be able to:  

- Set up a basic Node.js project with Express.  
- Create simple routes and run your first web server.  
- Start and stop the server from the terminal.  

Let’s set up our very first Node.js server using Express.

1. Let's start with a fresh project. Go to your `Documents` folder (or anywhere you prefer) and create a new folder called `lab2-hello`.
2. In VSC, open a new folder.

![vsc1](assets/vsc1.png)

3. In the terminal, we need to initialize our project. In the terminal, I’ll type:

```shell
npm init -y
```
🔍 Explanation:
- `npm` → Node Package Manager, used to manage libraries (packages) in your project.
- `init` → initializes a new Node.js project in the current folder.
- `-y` → automatically answers “yes” to all setup questions (project name, version, entry point, etc.), so it skips the interactive wizard.
  👉 The result is a package.json file created in your folder.

This file:

- Stores project information (name, version, author, license, etc.).
- Tracks dependencies (packages you install with npm install).
- Can define scripts (e.g., "start": "node app.js") to run commands easily.
- Helps others (or servers) install the exact same project setup with a single npm install.

4. Next, let’s install Express, which is the framework we’ll use, and Nodemon, which will restart our server automatically whenever we make changes.

```shell
npm install express nodemon
```
> `express` → a web framework for building servers and APIs.
> `nodemon` → automatically restarts the server when you change the code.

5. Now, we need to tell Node how to start our server.

Inside the `package.json` file, adapt the scripts section to look like this, by replacing the existing script:

```
"scripts": {
  "start": "nodemon app.js"
}
```

> 💡 Note:
> scripts → a list of shortcut commands for your project.
> start → the name of the command you’ll run (npm start).
> nodemon app.js → runs your app with Nodemon, which automatically restarts the server whenever you change the code.
> In practice thi line tells Node.js how to run your app.
> It says: when you type `npm start`, run `nodemon app.js`, and if you change your code, the server restarts automatically.

![vsc2](assets/vsc2.png)

> That way, every time you run npm start, Nodemon will launch app.js and keep it running.
> Whenever you make a change in the code, Nodemon automatically restarts the server so you don’t have to stop and start it manually.

6. Now let’s create the server. Create a new file called `app.js` and in the file, you’ll start by importing `express`:

```js
const express = require('express');
const app = express();
```

Then you’ll define your first route, the home route, just `/`.

```js
app.get('/', (req, res) => {
    res.send("Hello world!");
});
```

🔍 Explanation:
`app.get('/')` → listens for a GET request at the root URL (/).
`req` → the request coming from the browser (what the user sends).
`res` → the response the server sends back.
The arrow function (req, res) => { ... } runs when the user visits the page.

Let's define a second route.

```js
app.get('/hello', (req, res) => {
    res.send("world!");
});
```

Finally, we need to make the server listen on a port. I’ll pick port `3000`.

```js
app.listen(3000);
```

🔍 Explanation:
This means: *“Start my server and wait for users to connect on port 3000”*.
It creates the server at `http://localhost:3000`. 
Based on the code, you now have two endpoints (URLs):
- `http://localhost:3000/` → sends “Hello world!” to the browser.
- `http://localhost:3000/hello` → sends “world!”.

> 💡 What is a port?
> A port is like a numbered “door” on a computer that programs use to send and receive data over a network.
> Example: websites usually use port `80` (HTTP) or `443` (HTTPS).
> If you run a Node.js app on port `3000`, you open your browser at `http://localhost:3000`.

Here is how it looks like.

![vsc3](assets/vsc3.png)

7. Go back to the terminal and type:

```shell
npm start
```

The server is now running. Open a browser (I used Google Chrome) and visit `http://localhost:3000`, you’ll see the `Hello world!` message.

Try the `http://localhost:3000/hello` endpoint too.

![hello](assets/hello.png)

8. Press click within the terminal area and then `CTRL`+`C` to stop the server.

> (Hold the `Control` key and press `C`).

🎉 That’s it, we just built our very first Express server! This small app is the foundation for building APIs and web applications.

✅ Tutorial is completed. Continue to the [next part](lab2-part3.md).
