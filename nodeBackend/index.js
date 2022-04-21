const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');
const app = express();
require('dotenv').config();

// Add mysql database connection
const db = mysql.createPool({
  host: process.env.MYSQL_HOST, // the host 
  user: process.env.MYSQL_USER, // database user 
  password: process.env.MYSQL_PASSWORD, // database user password 
  database: process.env.MYSQL_DATABASE // database name 
})

// Enable cors security headers
app.use(cors())

// add an express method to parse the POST method
app.use(express.json())
app.use(express.urlencoded({ extended: true }));

// home page
app.get('/test1', (req, res) => {
  res.send('Hello World! I am from node!')
});

app.get('/getUsers', (req, res) => {
    const SelectQuery = " SELECT * FROM  users";
    db.query(SelectQuery, (err, result) => {
      res.send(result)
    })
})

app.listen('3001', () => {})