const express = require('express')
const router = express.Router()

const Film = require('../models/Film')
const verifyToken = require('../verifyToken')

router.get('/', verifyToken, async(req,res) =>{
    try{
        const films = await Film.find()
        res.send(films)
    }catch(err){
        res.status(400).send({message:err})
    }
})

module.exports = router