### Lab2.2: Building the MiniFilm application <img src="images/minifilm.png" alt="a" style="zoom:10%;" />

#### What am I about to learn?

Today's lab session focused on how to build a MiniFilm application by connecting to a MongoDB database to collect data and render it to the browser.

Lab 2 part 2 focuses on how to:

* Conceptualise an application development task
* Deploy a free MongoDB instance on the MongoDB Atlas
* Create a MiniFilm application using NodeJS

#### Lab 2.2: Building the MiniFilm application with MongoDB

You will need to watch the next video on how to install and run a NodeJS app.

> Take your time, make sure you double-check the code and debug your code as you do.

1. Firstly, watch the following video.

[![Watch the video](https://i.ytimg.com/vi/TriF0rcEeHs/hqdefault.jpg)](https://youtu.be/TriF0rcEeHs)

> You should run this tutorial on your personal computer :white_check_mark:

2. Here, you will find the commands and scripts that I created in this video. Assuming that you already installed NodeJS on your personal computer, and you are already in your project folder, you can initialise a NodeJS application using the following script.

```shell
$ npm init
```

> npm is the node package manager that gives us access to the online repository of Node. 

3. For this tutorial, we need to install the `express` package, the  `nodemon` tool and the `mongoose` driver to connect to the MongoDB cluster.

```shell
$ npm install express nodemon mongoose
```

> I can install both packages at the same time.

4. Make sure you edit the `package.json` and adapt the `scripts` key to the following value (as shown in the video).

```json
...
"scripts": {
  "start":"nodemon app.js"
}
```

5. You will need to create a new MongoDB collection using the MongoDB atlas. Watch the video on how to connect and deploy your first MongoDB cluster.

> [Link](https://www.mongodb.com/cloud/atlas/lp/try2?utm_source=google&utm_campaign=gs_emea_united_kingdom_search_core_brand_atlas_desktop&utm_term=mongodb%20atlas%20login&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=12212624581&adgroup=115749705303&gclid=CjwKCAiA55mPBhBOEiwANmzoQrRYt9_LM38WefyAApthSkD3j0I_soqf9RiNSKQnr2YL9oaLhXJEEhoChb4QAvD_BwE) to connect to the MongoDB cluster.

6. This is an example of the data model that we insert in Mongo and we build in NodeJS. The data is in JSON format.

```json
{
  "film_id":"1001",
  "film_name":"Umbrella",
  "film_type":"Animated Short Film",
  "film_year":"2021",
  "film_link":"https://youtu.be/Bl1FOKpFY2Q"
}
```

5. The next script is the code for the `app.js` file.

```javascript
const express = require('express')
const app = express()

const mongoose = require('mongoose')

const filmsRoute = require('./routes/films')

app.use('/films',filmsRoute)

app.get('/', (req,res)=>{
    res.send('Homepage')
})

// You will need to update the username and password, there are the credentials that you 
// created in MongoDB

const MURL = 'mongodb+srv://username:passwors@cluster0.h0tys.mongodb.net/MiniFilms?retryWrites=true&w=majority'

mongoose.connect(MURL, ()=>{
    console.log('Your mongoDB connector is on...')
})

app.listen(3000, ()=>{
    console.log('Your server is up and running...')
})
```

6. We created the `films.js` file inside a new `routes` folder.

```javascript
const express = require('express')
const router = express.Router()

const Film = require('../models/Film')

router.get('/', async (req,res) =>{ 
    try{
        const films = await Film.find() // .limit(5)
        res.send(films)
    }catch(err){
        res.send({message:err})
    }
})

router.get('/:filmId', async(req,res)=>{
    try{
        const filmById = await Film.findById(req.params.filmId)
        res.send(filmById)
    }catch(err){
        res.send({message:err})
    }
})

module.exports = router
```

7. Then, we created the a new model called `Film.js` inside the new `models` folder.

```javascript
const mongoose = require('mongoose')

const FilmSchema = mongoose.Schema({
    film_name:{
        type:String
    },
    film_type:{
        type:String
    },
    film_year:{
        type:String
    },
    film_link:{
        type:String
    }
})

module.exports = mongoose.model('films',FilmSchema)
```

8. You need to run the `npm start` to start the server.

```shell
$ npm start
```

9. Make sure you create a couple of extra routes and familiarise yourself with the NodeJS code.

:checkered_flag: Well done! You completed part 1, now move to part 2 :clap: