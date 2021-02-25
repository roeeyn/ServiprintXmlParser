const updateFileListUi = (filenames) => {
  const fileList = document.getElementById("file-list");

  // Delete actual list
  fileList.textContent = "";

  // Insert new file list
  filenames.forEach((filename) => {
    const itemNode = document.createElement("li");
    const textNode = document.createTextNode(filename.substring(0, 6) + "...");
    itemNode.appendChild(textNode);
    fileList.appendChild(itemNode);
  });

  // Insert submit button
  const submitBtn = document.getElementById("submit-button");
  submitBtn.classList.remove("hidden");
};

const updateInstructionsButton = (filenames) => {
  const button = document.getElementById("instructions-button");
  button.textContent = `${filenames.length} archivos seleccionados`;
};

const fileInput = document.getElementById("file-input");

fileInput.addEventListener("change", (event) => {
  const fileNames = Array.from(event.target.files).map((file) => file.name);
  updateFileListUi(fileNames);
  updateInstructionsButton(fileNames);
});
