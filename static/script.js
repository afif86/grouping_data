// Function to add new row to the table
document.getElementById("add-row").addEventListener("click", addRow);

function addRow(e) {
  e.preventDefault();
  let table = document.querySelector("#dataTable tbody");
  let row = table.insertRow(0);
  let cell1 = row.insertCell(0);
  let cell2 = row.insertCell(1);
  let cell3 = row.insertCell(2);
  cell1.innerHTML = `<input type="text" class="name" name="name" placeholder="Name">`;
  cell2.innerHTML = `<input type="text" class="address" name="address" placeholder="Street, City, Country">`;
  cell3.innerHTML = `<i class="fa-solid fa-trash-can"></i>`;
}

// Function to remove row from the table
if (document.querySelector("#dataTable tbody")) {
  document.querySelector("#dataTable tbody").addEventListener("click", (e) => {
    e.preventDefault();
    if (e.target.classList.contains("fa-trash-can")) e.target.parentElement.parentElement.remove();
  });
}

// removeRow = (e) => {
//   e.preventDefault();
//   if (e.target.classList.contains("fa-trash-can")) row.deleteRow(e.parentElement.parentElement.rowIndex);
// };

// Function to upload and check the file type and size
const selectedFile = document.getElementById("file");
selectedFile.addEventListener("change", handleFiles, false);
function handleFiles() {
  const file = this.files[0];
  if (file.type == "text/csv" && file.size > 1) {
    document.querySelector(".message").style.color = "black";
    document.querySelector(".message").innerHTML = `<i class="fa-solid fa-file-circle-check" style="color:green;"></i>
    <span>&nbsp;&nbsp;Your file has been attached successfully</span>`;
  } else {
    document.querySelector(".message").style.color = "red";
    document.querySelector(".message").innerHTML = `<i class="fa-solid fa-circle-exclamation"></i>
    <b>&nbsp;&nbsp;Error:</b><span>&nbsp;Please insert a file with <b>CSV</b> extension</span>`;
  }
}

// function to get data from table (data entered by user)
const info = document.getElementById("submit-btn");
info.addEventListener("click", (e) => {
  let finalInput = [];

  // get data from table and return a json object
  document.querySelectorAll("#dataTable tbody tr").forEach((tr) => {
    let name = tr.querySelector("input.name").value;
    let address = tr.querySelector("input.address").value;
    finalInput.push({ name, address });
  });

  // check if file is uploaded or have data in table
  if (selectedFile.files.length > 0 || finalInput.length > 0) {
    // function for loading animation
    document.querySelector(".content").classList.add("loader-in");
    document.querySelector(".content").classList.remove("loader-out");

    setTimeout(() => {
      document.querySelector(".content").classList.remove("loader-in");
    }, 4000);
    setTimeout(() => {
      document.querySelector(".content").classList.add("loadr-out");
    }, 4000);

    // function to send data to server
    const formData = new FormData();
    formData.append("file", selectedFile.files[0]);
    formData.append("data", JSON.stringify(finalInput));

    fetch("/saved", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.text())
      .then((html) => {
        document.body.innerHTML = html;
      });
  } else {
    l;
  }
});
