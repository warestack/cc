#### Lab 3 – MongoDB & Node.js REST API Development

This lab series introduces how to build a **Node.js + MongoDB** application from the ground up — starting with a cloud database, then connecting it through Express and Mongoose, and finally creating a full REST API with CRUD operations.

The lab is divided into three main parts:

#### Part 1 – MongoDB Cloud Setup

You’ll learn how to:

- Create and configure a MongoDB Atlas account.
- Deploy your first database cluster using the free plan.
- Add collections and documents (`DBFilms` → `ColFilms`).
- Obtain and configure your database connection string for Node.js.

📄 See file: [part 1.md](part 1.md)

#### Part 2 – Connecting Node.js to MongoDB

You’ll continue by developing a small API called MiniFilms, connecting it to the MongoDB database using the Mongoose library.

You’ll learn how to:

- Scaffold an Express project.
- Organize your project with routes and models.
- Define a Mongoose schema for films.
- Fetch and display data from your MongoDB Atlas cluster.

📄 See file: [part 2.md](part 2.md)

#### Part 3 – Building the MiniPost REST Microservice

You’ll create a fully functional CRUD microservice called MiniPost that performs:

- Create, Read, Update, Delete operations
- Connection to MongoDB Atlas via Mongoose
- Route handling with Express
- Environment configuration using dotenv

📄 See file: [part 3.md](part 3.md)
