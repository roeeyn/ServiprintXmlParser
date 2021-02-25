const fileInput = document.getElementById("file-input");

fileInput.addEventListener("change", (event) => {
  const fileNames = Array.from(event.target.files).map((file) => file.name);
  console.log(fileNames);
});
