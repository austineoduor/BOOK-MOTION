const express = require('express');
const app = express();
const port = 3000;

// Serve static files from the "public" directory
app.use(express.static('public'));

// Route for the sign-up page
app.get('/sign', (req, res) => {
  res.sendFile(__dirname + '/public/sign.html');
});

// Route for the sign-in page
app.get('/signup', (req, res) => {
  res.sendFile(__dirname + '/public/signup.html');
});

// Route for the home page
app.get('/home', (req, res) => {
  res.sendFile(__dirname + '/public/home.html');
});

// Start the server
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

