function uploadFile(form) {
	const formData = new FormData(form);
	var oOutput = document.getElementById("static_file_response");
	var oReq = new XMLHttpRequest();
	oReq.open("POST", "upload_static_file", true);
	oReq.onload = function (oEvent) {
		if (oReq.status == 200) {
			console.log(oReq.response);
		} else {
		}
	};

	console.log("Sending file!");
	oReq.send(formData);
}

function getImgData() {
	let files = file.files[0];

	if (files) {
		const fileReader = new FileReader();
		fileReader.readAsDataURL(files);
		fileReader.addEventListener("load", function () {
			imgPreview.style.display = "block";

			imgPreview.innerHTML =
				`<img src="${this.result}"  height="100px"/>`;
		});
	}
}
const inpFile = document.getElementById("file");
const btnUpload = document.getElementById("upload-button");
const imgPreview = document.getElementById("img-preview");

inpFile.addEventListener("change", function () {
	getImgData();
});

// function previewImages() {

//     var preview = document.getElementById("preview");
    
//     if (this.files) {
//       [].forEach.call(this.files, readAndPreview);
//     }
  
//     function readAndPreview(file) {
  
//       // Make sure `file.name` matches our extensions criteria
//       if (!/\.(jpe?g|png|gif)$/i.test(file.name)) {
//         return alert(file.name + " is not an image");
//       } // else...
      
//       var reader = new FileReader();
      
//       reader.addEventListener("load", function() {
//         var image = new Image();
//         image.height = 100;
//         image.title  = file.name;
//         image.src    = this.result;
//         preview.appendChild(image);
//       });
      
//       reader.readAsDataURL(file);
      
//     }
  
//   }
  
//   document.getElementById("file-input").addEventListener("change", previewImages);