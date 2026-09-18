const themeToggle = document.getElementById("themeToggle");


// Check saved theme
const savedTheme = localStorage.getItem("theme");

if (savedTheme === "dark") {
    document.body.classList.add("dark-mode");

    if (themeToggle) {
        themeToggle.innerHTML = "☀️";
    }
}


// Toggle theme
if (themeToggle) {

    themeToggle.addEventListener("click", function () {

        document.body.classList.toggle("dark-mode");

        if (document.body.classList.contains("dark-mode")) {

            localStorage.setItem("theme", "dark");

            themeToggle.innerHTML = "☀️";

        } else {

            localStorage.setItem("theme", "light");

            themeToggle.innerHTML = "🌙";
        }

    });

}