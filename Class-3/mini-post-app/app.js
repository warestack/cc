const express = require('express')
const app = express()

const mongoose =require('mongoose')
require('dotenv/config')

const bodyParser = require('body-parser')
const postsRoute = require('./routes/posts')

app.use(bodyParser.json())
app.use('/posts',postsRoute)

app.get('/', (req,res) =>{
    res.send('Homepage')
})

mongoose.connect(MURL).then(() => { console.log('Your mongoDB connector is on...')})

app.listen(3000, ()=>{
    console.log('Server is up and running...')
})
