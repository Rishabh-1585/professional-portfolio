const searchInput = document.getElementById("projectSearch");
const filterButtons = document.querySelectorAll(".project-filter");
const projectItems = document.querySelectorAll(".project-item");

let currentFilter = "all";


function filterProjects() {

    const searchText = searchInput.value.toLowerCase().trim();

    projectItems.forEach(function (project) {

        const technologies =
            project.dataset.technologies.toLowerCase();

        const title =
            project.querySelector(".card-title").textContent.toLowerCase();

        const description =
            project.querySelector(".card-text").textContent.toLowerCase();


        const matchesFilter =
            currentFilter === "all" ||
            technologies.includes(currentFilter);


        const matchesSearch =
            title.includes(searchText) ||
            description.includes(searchText) ||
            technologies.includes(searchText);


        if (matchesFilter && matchesSearch) {
            project.style.display = "";
        } else {
            project.style.display = "none";
        }

    });
}


/* Filter Buttons */

filterButtons.forEach(function (button) {

    button.addEventListener("click", function () {

        currentFilter = button.dataset.filter;

        filterButtons.forEach(function (btn) {
            btn.classList.remove("active");
            btn.classList.remove("btn-dark");
            btn.classList.add("btn-outline-dark");
        });

        button.classList.add("active");
        button.classList.remove("btn-outline-dark");
        button.classList.add("btn-dark");

        filterProjects();

    });

});


/* Search */

if (searchInput) {

    searchInput.addEventListener("input", function () {
        filterProjects();
    });

}