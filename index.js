import express from 'express';
import mongoose from'mongoose';
import {PORT,MONGO_URL} from './config.js'
import {Data} from './models/datamodel.js'
import dataRoute from './Routes/dataRoute.js'
import cors from 'cors';


const app=express();

app.use(express.json());



app.get("/",async (req,res)=>{
    try{
        const data=await Data.find({});
        return res.status(200).send(data);
    }
    catch(err){
        console.log(err.message);
        res.send(err);
    }
})

app.use(cors());
app.use('/data',dataRoute)

const connectstr=MONGO_URL
mongoose.connect(connectstr).then(()=>{
    console.log("Connected to DB");
    app.listen(PORT,() => console.log(`Server is running on port ${PORT}`));
}).catch(err=>{
    console.log(err);
});





 