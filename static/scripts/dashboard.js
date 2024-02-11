function deleteArticleConfirmation() {
  const topic = document.querySelector("[data-topic]").dataset.topic;
  const slug = document.querySelector("[data-slug]").dataset.slug;
  const answer = confirm("Do you want to delete this article?\n\n" + topic);
  if (!answer) return;
  const url = `/article/delete/${slug}/`;
  console.log(url);
  fetch(url);
  window.location.reload();
}

function deleteCategoryConfirmation() {
  const pk = document.querySelector("[data-pk]").dataset.pk;
  const name = document.querySelector("[data-name]").dataset.name;
  const answer = confirm("Do you want to delete this category?\n\n" + name);
  if (!answer) return;
  const url = `/categories/delete/${pk}/`;
  console.log(url);
  fetch(url).then((response) => response);
  //window.location.reload();
}

const toggleBars = document.querySelector("[data-toggler]");
console.log(toggleBars);
