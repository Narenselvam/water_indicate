import express from 'express';
import mongoose from'mongoose';
import {PORT,MONGO_URL} from './config.js'


const app=express();

app.use(express.json());

const connectstr=MONGO_URL
mongoose.connect(connectstr).then(()=>{
    console.log("Connected to DB");
    app.listen(PORT,() => console.log(`Server is running on port ${PORT}`));
}).catch(err=>{
    console.log(err);
});

// acess cluster in the db
const clusterSchema=new mongoose.Schema({
    readings:Number,
    device:String,
    time:String

});

const Data=mongoose.model('data',clusterSchema);

app.post('/data',async (req,res)=>{
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
}

)