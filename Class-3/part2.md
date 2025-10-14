### Lab 3: Part 2

##### **What you’ll learn**

In this lab, you will continue building your API by connecting it to a MongoDB database using the Mongoose library.
 By the end, you’ll understand how to:

- Scaffold a Node.js project using Express.
- Organise your project with **routes** and **models**.
- Define and use a **MongoDB schema** with **Mongoose**.
- Connect your application to **MongoDB Atlas** and fetch data through API endpoints.

> 💡 **Tip:** Follow each step carefully and **double-check file names, folder structure, and syntax.**
>  Most errors happen because of typos, missing brackets, or incorrect paths.

##### Step 1: `MiniFilms` project preparation

Let’s start by setting up your Express project and preparing the structure for your API.

1. Create a folder called `minifilms` somewhere on your computer. Then, open your terminal and run the following commands.

```shell
npm init -y
```

```shell
npm install express nodemon
```

2. Edit the `package.json` file and add the following line inside the `"scripts"` section.

```js
"scripts": {
  "start": "nodemon app.js"
}
```

> This means that when you run `npm start`, it will automatically execute `nodemon app.js`, launching your server with live reloading.

3. In your project folder, create a file called `app.js` and add the following boilerplate code.

```js
// Import the Express library
const express = require('express');
const app = express();

// Root route: generic welcome + API description
app.get('/api', (req, res) => {
  res.json({ message: "Hello, world! Welcome to the API." });
});

// Start the server on port 3000
app.listen(3000);
```

4. Now start the project.

```shell
npm start	
```

> If everything is correct, you should see in your terminal:
>  ✅ `Server is running on http://localhost:3000`.
>
> Then visit `http://localhost:3000/api` in your browser — you should see this JSON:
>
> ```
> {
>   "message": "Hello, world! Welcome to the API."
> }
> ```

5. Inside your project folder, create a new folder called `routes`, and inside it, create a file named `films.js`.

```js
const express = require('express');
const router = express.Router();

const Film = require('../models/Film'); // we’ll create this model later

// More code will go here

module.exports = router;
```

> This sets up a Router as in previous lab.

5. Now open your `app.js` again and connect the `films` route. Add the following code **before** `app.listen(...)`:

```js
// Add the Films routes
const filmsRoute = require('./routes/films');
app.use('/films', filmsRoute);
```

##### Step 2: Setting up `Mongoose` library to extract data

1. Go back to you terminal, stop your server (`CTRL`+`C`) and install the following library. 

```shell
 npm install mongoose
```

> Mongoose acts as a bridge between your Node.js code and the MongoDB database. It helps you define **schemas** (data structures), enforce **validation**, and run **database queries** easily.
>
> Now we’ll connect your app to MongoDB Atlas and create a schema for storing and retrieving film data.

2. The library is now installed and we are ready to connect. We’ll build two endpoints:

- `GET /films` → to fetch all films.
- `GET /films/<film-id>` → to fetch a single film by its unique ID.

> As a reminder our database (`DBFilms`) contains a collection called `ColFilms` with documents that represent movies.

![mongo9](assets/mongo9.png)

3. In your project, create a new folder called `models`.  Inside it, create a file named `Film.js` and add the code bellow. Back in VSC, here is my structured folder.

![vsc1](assets/vsc1.png)

4. You will need to build **the same schema** using the data object in the `ColFilms`. The code is self-explanatory, you can examine it yourself.

```js
const mongoose = require('mongoose');

// Define the Film schema
const FilmSchema = new mongoose.Schema(
  {
    title: {
      type: String,
      required: true
    },
    year: {
      type: String,
      required: true
    },
    genre: {
      type: String,
      required: true
    },
    director: {
      type: String,
      required: true
    },
    rating: {
      type: Number,
      required: true
    }
  },
  {
    collection: 'ColFilms',   // Explicit collection name in MongoDB
    timestamps: true       // Adds createdAt and updatedAt fields
  }
);

// Export the model
module.exports = mongoose.model('Film', FilmSchema, 'ColFilms');
```

> Briefly:
>
> - `mongoose.Schema` → defines the shape of each film document.
> - Each key (`title`, `genre`, `rating`) has a data type and validation rules.
> - `timestamps: true` adds fields that track when each record was created and updated.
> - The `model` lets you interact with this collection directly in your routes.

5. Now we can add the database queries.

   Open `routes/films.js` and replace its content with the following:

```js
const express = require('express');
const router = express.Router();
const Film = require('../models/Film');

// GET all films
router.get('/', async (req, res) => {
  try {
    const films = await Film.find().limit(10); // limits to 10 results
    res.json(films);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// GET film by ID
router.get('/:postId', async (req, res) => {
  try {
    const film = await Film.findById(req.params.postId);
    if (!film) return res.status(404).json({ message: 'Film not found' });
    res.json(film);
  } catch (err) {
    res.status(400).json({ message: 'Invalid film ID' });
  }
});

module.exports = router;
```

> **Explanation:**
>
> - `Film.find()` → retrieves all documents from the collection.
> - `Film.findById()` → retrieves a specific document by its unique ID.
> - `.limit(10)` → ensures only 10 records are fetched at once.
> - `try...catch` → handles possible errors gracefully (e.g. if the ID is invalid).

6. Now let’s add your MongoDB connection inside `app.js`.

   Replace your previous `app.js` with this version:

```js
const express = require('express');
const mongoose = require('mongoose');

const app = express();
app.use(express.json());

// Routes
const filmsRoute = require('./routes/films');
app.use('/films', filmsRoute);

// Root route
app.get('/', (req, res) => {
  res.json({ message: 'Hello, world! Welcome to the API.' });
});

// MongoDB Atlas connection string (use your own credentials)
const MURL = 'mongodb+srv://stelios:1234@cluster0.h3mixcq.mongodb.net/DBFilms?retryWrites=true&w=majority&appName=Cluster0';

mongoose.connect(MURL)
  .then(() => console.log('Connected to MongoDB Atlas'))
  .catch(err => console.log('Connection error:', err));

app.listen(3000);

```

7. If all went well, you will be able to see all the data in the browser. 

   Start your server again:

   ```
   npm start
   ```

   Then visit:

   - `http://localhost:3000/films` → should display up to 10 film records.
   - `http://localhost:3000/films/<film-id>` → should display details for a specific film.

![data1](assets/data1.png)

8. Data per id.

![data2](assets/data2.png)

9. You can also manually insert a new film in your MongoDB Atlas collection.

   Go to `DBFilms > ColFilms` and click **Insert Document**:

```
{
  "title": "The Shawshank Redemption",
  "year": "1994",
  "genre": "Drama",
  "director": "Frank Darabont",
  "rating": 9.3
}
```

Save it and then refresh `http://localhost:3000/films` in your browser — your new movie should now appear!

✅ Well done — your MiniFilms API is live! 🎬