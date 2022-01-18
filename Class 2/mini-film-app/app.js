const express = require('express')
const app = express()

const mongoose = require('mongoose')

const filmsRoute = require('./routes/films')

app.use('/films',filmsRoute)

app.get('/', (req,res)=>{
    res.send('Homepage')
})

const MURL = 'mongodb+srv://username:passwors@cluster0.h0tys.mongodb.net/MiniFilms?retryWrites=true&w=majority'

mongoose.connect(MURL, ()=>{
    console.log('Your mongoDB connector is on...')
})

app.listen(3000, ()=>{
    console.log('Your server is up and running...')
})