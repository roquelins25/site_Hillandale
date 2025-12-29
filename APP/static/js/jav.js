const menuItems = document.querySelectorAll(".item-menu");
const iframes = document.querySelectorAll("iframe");

menuItems.forEach(item => {
    item.addEventListener("click", () => {
        const target = item.getAttribute("data-target");

        iframes.forEach(f => f.classList.remove("active"));

        const frameToShow = document.getElementById(target);
        if (frameToShow) {
            frameToShow.classList.add("active");
        }

        menuItems.forEach(i => i.classList.remove("ativo"));
        item.classList.add("ativo");
    });
});

document.getElementById("Invoicing").classList.add("active");
