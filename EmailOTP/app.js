dotenv.config();

const express= require("express");
const bcrypt =require("brypt")
const jwt=require("jsonwebtoken");
const pg=require("pg");
const dotenv=require("dotenv");

const app=express();
const port=process.env.PORT ||4000;

const poll= new pg.Pool({
    user:process.env.DB_USER,
    password:process.env.DB_PASSWORD,
    host:process.env.DB_HOST,
    port:process.env.DB_PORT,
    database:process.env.DB_NAME,
    
})

app.use(express.json());

app.post("/register",async(req,res)=>{
    try{

    }catch{
        
    }
})
