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