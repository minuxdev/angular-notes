const form = document.forms["article"];
form.addEventListener("submit", (e) => {
  e.preventDefault();
  uploader();
});

function hideInputs() {
  const i = document.querySelector("#thumbnail-clear_id");
  const a = document.querySelector(".input__group a");
  const label = document.querySelector('[for="thumbnail-clear_id"]');
  i.style.display = "none";
  a.style.display = "none";
  label.style.display = "none";
}

async function configLoader() {
  const response = await fetch("/firebase/configuration/file/");
  const json = await response.json();
  const firebase_config = await json.firebase_config;

  firebase = firebase.initializeApp(firebase_config);
}

async function uploader() {
  const file = document.querySelector("#id_thumbnail").files[0];
  if (!file) form.submit();

  if (file && file.size > 1 * 1024 * 1024) {
    alert("File cannot be greater than 1Mb");
    return;
  }
  const ref = firebase.storage().ref();
  const name = `${new Date()}-${file.name}`;

  const task = await ref.child("images/" + name).put(file);
  const snapshot = await task;
  const url = await snapshot.ref.getDownloadURL();
  const el = document.querySelector("#thumbnail");
  el.value = url;
  form.submit();
}

configLoader();
hideInputs();
