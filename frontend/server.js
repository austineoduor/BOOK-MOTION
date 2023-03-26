const express = require('express'). // Include ExpressJS
const app = express(). // Create an ExpressJS app
const bodyParser = require('body-parser'); // Middleware

app.use(bodyParser.urlencoded({ extended: false }));

// Route to Homepage
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/static/index.html');
});

// Route to Signin-signup Page
app.get('/signin', (req, res) => {
  res.sendFile(__dirname + '/static/signin-signup.html');
});

app.post('/signin', (req, res) => {
  // Insert Login Code Here
  let username = req.body.username;
  let password = req.body.password;
  res.send(`Username: ${username} Password: ${password}`);
});

const port = 3000 // Port we will listen on

// Start the server
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
