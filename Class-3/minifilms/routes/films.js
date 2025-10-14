const express =require('express')
const router = express.Router()


// GET 1 (Read all)
router.get('/', async(req,res) =>{
    try{
        const getFilms = await Film.find().limit(10)
        res.send(getFilms)
    }catch(err){
        res.send({message:err})
    }
})

// GET 2 (Read by ID)
router.get('/:postId', async(req,res) =>{
    try{
        const getFilmById = await Film.findById(req.params.postId)
        res.send(getFilmById)
    }catch(err){
        res.send({message:err})
    }
})

module.exports = router