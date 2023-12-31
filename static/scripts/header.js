form_toggle = document.querySelector("#form_toggle");
toggler = document.querySelector("#toggle");

form_toggle.addEventListener("click", () => {
  form_search = document.querySelector("#form_search");
  form_search.classList.toggle("active");
});

toggle.addEventListener("click", () => {
  header_menu = document.querySelector(".header__menu");
  header_menu.classList.toggle("active");
});
