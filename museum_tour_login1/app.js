const express = require('express');
const mongoose = require('mongoose');
const path = require('path');
const bodyParser = require('body-parser');
const User = require('./models/User');
const app = express();

// MongoDB Connection
mongoose.connect('mongodb://localhost:27017/museumDB', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.log(err));

app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.urlencoded({ extended: true }));

// Serve Login Page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'login.html'));
});

// Handle Login Request
app.post('/login', async (req, res) => {
    const { email, password } = req.body;

    const user = await User.findOne({ email, password });

    if (user) {
        res.json({ success: true, message: "Login Successful" });
    } else {
        res.json({ success: false, message: "Invalid Email or Password" });
    }
});

// Example Dashboard Route
app.get('/dashboard', (req, res) => {
    res.send('<h1>Welcome to Museum Dashboard</h1>');
});

// Start Server
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
