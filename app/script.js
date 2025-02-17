let users = [
    { username: "thamo", password: "thamo" }
];

const loginBtn = document.getElementById('login-btn');
const signupBtn = document.getElementById('signup-btn');
const createAccountBtn = document.getElementById('create-account-btn');
const backToLoginBtn = document.getElementById('back-to-login-btn');
const loginForm = document.getElementById('login-form');
const signupForm = document.getElementById('signup-form');
const banner = document.getElementById('banner');

function showBanner(message, isSuccess) {
    banner.textContent = message;
    banner.className = isSuccess ? 'success' : 'error';
    banner.style.display = 'block';
}

function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const user = users.find(user => user.username === username && user.password === password);

    if (user) {
        showBanner('You are logged in.', true);
    } else {
        showBanner('Login failed. Please check your credentials.', false);
    }
}

function signup() {
    const newUsername = document.getElementById('new-username').value;
    const newPassword = document.getElementById('new-password').value;

    // Check if username already exists
    if (users.some(user => user.username === newUsername)) {
        showBanner('Username already exists.', false);
    } else {
        users.push({ username: newUsername, password: newPassword });
        showBanner('You have been signed up.', true);
    }
}

loginBtn.addEventListener('click', login);
signupBtn.addEventListener('click', () => {
    loginForm.style.display = 'none';
    signupForm.style.display = 'block';
});
createAccountBtn.addEventListener('click', signup);
backToLoginBtn.addEventListener('click', () => {
    signupForm.style.display = 'none';
    loginForm.style.display = 'block';
});
