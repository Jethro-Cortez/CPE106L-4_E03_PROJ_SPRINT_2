// 🚀 Login Form Validation
document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("login-form");

    loginForm.addEventListener("submit", (e) => {
        const username = document.getElementById("username").value.trim();
        const password = document.getElementById("password").value.trim();

        if (username === "" || password === "") {
            e.preventDefault();
            alert("Both fields are required! ❗");
        }
    });
});

// 🚀 Registration Form Validation
document.addEventListener("DOMContentLoaded", () => {
    const registerForm = document.getElementById("register-form");

    registerForm.addEventListener("submit", (e) => {
        const username = document.getElementById("username").value.trim();
        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value;
        const confirmPassword = document.getElementById("confirm_password").value;

        if (!username || !email || !password || !confirmPassword) {
            e.preventDefault();
            alert("All fields are required! ❗");
        } else if (password !== confirmPassword) {
            e.preventDefault();
            alert("Passwords do not match! ⚠️");
        }
    });
});

// 👑 Admin Registration Form Validation
document.addEventListener("DOMContentLoaded", () => {
    const adminForm = document.getElementById("admin-register-form");

    adminForm.addEventListener("submit", (e) => {
        const secretKey = document.getElementById("secret_key").value.trim();
        const username = document.getElementById("username").value.trim();
        const password = document.getElementById("password").value;
        const confirmPassword = document.getElementById("confirm_password").value;

        // 🔒 Replace with your real secret key in the backend
        const VALID_SECRET_KEY = "sinigangmix"; 

        if (!secretKey || !username || !password || !confirmPassword) {
            e.preventDefault();
            alert("All fields are required! ❗");
        } else if (secretKey !== VALID_SECRET_KEY) {
            e.preventDefault();
            alert("Invalid Secret Key! ⚠️");
        } else if (password !== confirmPassword) {
            e.preventDefault();
            alert("Passwords do not match! ⚠️");
        }
    });
});
