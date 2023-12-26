import mongoose from 'mongoose'

// acess cluster in the db
const clusterSchema=new mongoose.Schema({
    readings:Number,
    device:String,
    time:String
    
});


export const Data=mongoose.model('data',clusterSchema);