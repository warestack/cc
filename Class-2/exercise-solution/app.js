// Import the Express library
const express = require('express')
const app = express()

// 1. Import the movies router
const studentsRoute = require('./routes/students');

// 2. Use the router
app.use('/students', studentsRoute);

// Root: generic welcome + API description
app.get('/', (req, res) => {
  res.json({
    name: 'University API',
    version: '1.0.0',
    description: 'A simple API to fetch university student data.',
    endpoints: {
      root: 'GET /',
      allStudents: 'GET /students',
      student1: 'GET /sid'
    }
  });
});

// Start the server on port 3000
app.listen(3000)