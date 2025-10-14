const express = require('express');
const mongoose = require('mongoose');

const app = express();
app.use(express.json());

// routes
const filmsRoute = require('./routes/films');
app.use('/films', filmsRoute);

// root
app.get('/', (req, res) => {
  res.json({ message: 'Hello, world! Welcome to the API.' });
});

// ✅ Use your exact Atlas URL (copy from Atlas → Connect → Drivers)
const MURL = 'mongodb+srv://stelios:1234@cluster0.h3mixcq.mongodb.net/DBFilms?retryWrites=true&w=majority&appName=Cluster0';

// Connect (no deprecated options) and start server after success
mongoose.connect(MURL);


app.listen(3000, () => console.log('Server running on http://localhost:3000'));