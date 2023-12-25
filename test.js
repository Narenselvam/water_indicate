import { createRequire } from 'module';

const require = createRequire(import.meta.url);
const dotenv = require('dotenv').config();
import { config } from 'dotenv';
dotenv.config({path:'./config.env'})
console.log(process.env.PORT);