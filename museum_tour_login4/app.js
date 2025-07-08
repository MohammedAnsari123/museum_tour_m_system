const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const path = require('path');
const User = require('./models/User');
const app = express();

mongoose.connect('mongodb://localhost:27017/museumAuth', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.error(err));

app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static(path.join(__dirname, 'views')));

// Signup API
app.post('/signup', async (req, res) => {
  const { username, email, password } = req.body;
  const userExists = await User.findOne({ email });
  if (userExists) return res.json({ success: false, message: 'Email already registered.' });

  const newUser = new User({ username, email, password });
  await newUser.save();
  res.json({ success: true, message: 'Signup successful! Please login.' });
});

// Login API

app.post('/login', async (req, res) => {
  const { email, password } = req.body;
  const user = await User.findOne({ email, password });

  if (!user) {
    return res.json({ success: false, message: 'Invalid email or password.' });
  }

  res.json({ success: true, message: `Welcome back, ${user.username}!` });
});

app.get('/dashboard.html', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'dashboard.html'));
});


// app.post('/login', async (req, res) => {
//   const { email, password } = req.body;
//   const user = await User.findOne({ email, password });
//   if (!user) return res.json({ success: false, message: 'Invalid email or password.' });

//   res.json({ success: true, message: `Welcome back, ${user.username}!` });
// });

app.listen(3000, () => console.log('Server running on http://localhost:3000'));
