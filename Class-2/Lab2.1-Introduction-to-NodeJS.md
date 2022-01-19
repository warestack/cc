### Lab2.1: Introduction to Node.js

#### What am I about to learn?

Today's lab session focused on an introduction to Node.js.

Lab 2 part 1 focuses on how to:

* Install Node.js
* Create a simple application using Node.js

#### Lab 2.1: Installing and running a simple Node.js application 

You will need to watch the next video on how to install and run a Node.js app.

> Take your time, make sure you double-check the code and debug your code as you do.

1. Firstly, watch the following video.

[![Watch the video](http://img.youtube.com/vi/2xEEF_HOq4U/hqdefault.jpg)](https://youtu.be/2xEEF_HOq4U)

> You should run this tutorial on your personal computer :white_check_mark:

2. Here, you will find the commands and scripts that I created in this video. Assuming that you already installed Node.js on your personal computer, and you are already in your project folder, you can initialise a Node.js application using the following script.

```shell
$ npm init
```

> npm is the node package manager that gives us access to the online repository of Node. 

3. We need to install the `express` package and the  `nodemon` tool.

```shell
$ npm install express nodemon
```

> I can install both packages at the same time.

4. Make sure you edit the `package.json` and adapt the `scripts` key to the following value (as shown in the video).

```json
...
"scripts": {
  "start":"nodemon app.js"
}
```

5. The next script is the code for the `app.js` file.

```javascript
// 1. Import the libraries

const express = require('express')
const { restart } = require('nodemon')
const app = express()

const movieRoute = require('./routes/movies')
const userRoute = require('./routes/users')

// 2. Middleware
app.use('/movies',movieRoute)
app.use('/users',userRoute)

// 3. Create a route
app.get('/', (req,res)=> {
    res.send('You are in your home page!')
})

//4. Start the server
app.listen(3000, ()=>{
    console.log('Server is up and running...')
})
```

6. We created a `routes` directory to store our routes. Firstly, we created the `movies.js`.

```javascript
const express = require('express')
const router = express.Router()

router.get('/', (req,res)=>{
    res.send('You are in movies (router)')
})

router.get('/hobbit', (req,res)=>{
    res.send('You are in Hobbit movie!')
})

module.exports = router
```

7. Then, we created the `users.js`

```javascript
const express = require('express')
const router = express.Router()

router.get('/', (req,res)=>{
    res.send('You are in users!')
})

router.get('/stelios', (req,res)=>{
    res.send('You are in stelios home page!')
})

module.exports = router

```

8. You need to run the `npm start` to start the server.

```shell
$ npm start
```

8. Make sure you create a couple of extra routes and familiarise yourself with the Node.js code.

:checkered_flag: Well done! You completed part 1, now move to part 2 :clap: