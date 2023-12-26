import Express from 'express';
import {Data} from '../models/datamodel.js'

const router = Express.Router();

//data

router.post('/data',async (req,res)=>{
    try{
        const newData={
            readings:req.body.readings,
            device:req.body.device,
            time:req.body.time
        }
       const data=await Data.create(newData);
       console.log(data);
       return res.status(201).send(data);
    }catch(err){
        console.log(err.message);
        res.send(err);
    }
})



//latest data
router.get("/latest", async (req, res) => {
    try {
        const data = await Data.find().sort({_id: -1}).limit(1);
        return res.status(200).send(data);
    } catch (err) {
        console.log(err.message);
        res.send(err);
    }
 });

 export default router;