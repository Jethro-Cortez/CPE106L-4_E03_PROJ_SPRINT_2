// 🌗 Dark/Light Mode Toggle — Optimized
window.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.querySelector('.theme-toggle');
    if (!themeToggle) {
        console.error('⚠️ Theme toggle button not found!');
        return;
    }

    const icon = themeToggle.querySelector('i');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const storedTheme = localStorage.getItem('theme');
    const currentTheme = storedTheme || (systemPrefersDark ? 'dark' : 'light');

    // Apply initial theme
    setTheme(currentTheme);

    // 🌗 Toggle Theme on Click
    themeToggle.addEventListener('click', () => {
        const newTheme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        setTheme(newTheme);
    });

    // 🛠️ Helper Function: Apply Theme & Update Icon
    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);

        if (theme === 'dark') {
            icon.classList.replace('fa-moon', 'fa-sun');
        } else {
            icon.classList.replace('fa-sun', 'fa-moon');
        }
    }
});
