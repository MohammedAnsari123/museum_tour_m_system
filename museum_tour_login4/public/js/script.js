// Signup Handler
const signupForm = document.getElementById('signupForm');
if (signupForm) {
  signupForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    const username = document.getElementById('username').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();

    const res = await fetch('/signup', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ username, email, password })
    });

    const data = await res.json();
    document.getElementById('signupMsg').innerText = data.message;
    if (data.success) setTimeout(() => window.location.href = '/login.html', 1500);
  });
}

// Login Handler
const loginForm = document.getElementById('loginForm');
if (loginForm) {
  loginForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();

    const res = await fetch('/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();
    const message = document.getElementById('loginMsg');
    message.innerText = data.message;

    if (data.success) {
      message.style.color = 'green';
      setTimeout(() => {
        window.location.href = '/dashboard.html';   // Redirect here ✅
      }, 1000);
    } else {
      message.style.color = 'red';
    }
  });
}
