var express = require('express')
 , path = require('path')
 , bodyParser = require('body-parser')
 , fs = require('fs');
 var exec = require('child_process').exec;

var app = express();

// set views directory
var viewpath = __dirname + '/views/';
app.set('view engine', 'ejs');
app.use(require("express-ejs-layouts"));
app.use(express.static(path.join(__dirname, 'public')));

app.use(bodyParser.json()); // for parsing application/json
app.use(bodyParser.urlencoded({ extended: false })); // for parsing application/x-www-form-urlencoded

app.use(function(req, res, next) {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS');
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization, Content-Length, X-Requested-With');

  // intercept OPTIONS method
  if ('OPTIONS' == req.method) {
    res.send(200);
  }
  else {
    next();
  }
});

app.get('/hello', function(req,res){
  res.send({"message": "Hello there, welcome to borikanes.me"})
});

app.get('/', function(req, res){
  res.render('index')
});

app.post('/githubwebhook', function (req, res){
  var payload_body = req.body;
  if(payload_body['action'] == 'closed' && payload_body['pull_request']['merged_at'] != null){
    // Run script here
    // $PAYLOAD_HOME/payload.txt
    fs.writeFile("/home/pi/githubwebhooks/payload.txt", JSON.stringify(req.body), function(err) {
     if(err) {
        res.sendStatus(500);
         return console.log(err);
     }
     res.sendStatus(200);
   });
  }
});

app.listen(8080);
