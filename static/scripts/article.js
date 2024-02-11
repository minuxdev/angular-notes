const articleForm = document.forms["article"];
const iframe = document.querySelector("[role=Applicatioin]");
//const articleBody = iframe.contentWindow.document.querySelector("#tinymce");
var myContent = tinymce.activeEditor.getContent();
console.log(myContent);
