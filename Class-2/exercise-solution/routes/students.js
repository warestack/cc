// routes/students.js
const express = require('express');
const router = express.Router();

const students = {
  s1: {
    name: 'John Smith',
    studentId: 'S12345',
    major: 'Computer Science',
    year: 2
  },
  s2: {
    name: 'Maria Garcia',
    studentId: 'S54321',
    major: 'Mathematics',
    year: 3
  },
  s3: {
    name: 'Ali Khan',
    studentId: 'S77777',
    major: 'Data Science',
    year: 1
  }
};

// --- Routes ---

router.get('/', (req, res) => {
  res.json(students);
});

router.get('/:id', (req, res) => {
  const student = students[req.params.id]; // direct key access

  if (!student) {
    return res.status(404).json({ error: 'Student not found' });
  }

  res.json(student);
});

module.exports = router;