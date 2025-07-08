// Simulate local storage for demonstration (no real security!)
let users = JSON.parse(localStorage.getItem('users')) || [];

// Signup Form
const signupForm = document.getElementById('signupForm');
if (signupForm) {
  signupForm.addEventListener('submit', function(e) {
    e.preventDefault();
    const username = document.getElementById('signupUsername').value.trim();
    const email = document.getElementById('signupEmail').value.trim();
    const password = document.getElementById('signupPassword').value.trim();
    const message = document.getElementById('signupMsg');

    const existingUser = users.find(user => user.email === email);
    if (existingUser) {
      message.innerText = 'Email already registered.';
    } else {
      users.push({ username, email, password });
      localStorage.setItem('users', JSON.stringify(users));
      message.style.color = 'green';
      message.innerText = 'Signup successful! Please login.';
      setTimeout(() => window.location.href = 'login.html', 1500);
    }
  });
}

// Login Form
const loginForm = document.getElementById('loginForm');
if (loginForm) {
  loginForm.addEventListener('submit', function(e) {
    e.preventDefault();
    const email = document.getElementById('loginEmail').value.trim();
    const password = document.getElementById('loginPassword').value.trim();
    const message = document.getElementById('loginMsg');

    const user = users.find(user => user.email === email && user.password === password);
    if (user) {
      message.style.color = 'green';
      message.innerText = 'Login successful!';
      setTimeout(() => window.location.href = 'dashboard.html', 1000);
    } else {
      message.innerText = 'Invalid email or password.';
    }
  });
}
