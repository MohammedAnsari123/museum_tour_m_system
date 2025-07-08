document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    const message = document.getElementById('message');

    // Hardcoded demo credentials
    const validUser = 'admin';
    const validPass = '12345';

    if (username === validUser && password === validPass) {
        message.style.color = 'green';
        message.innerText = 'Login Successful!';
        setTimeout(() => {
            window.location.href = 'dashboard.html';  // redirect (optional)
        }, 1000);
    } else {
        message.style.color = 'red';
        message.innerText = 'Invalid Username or Password';
    }
});
