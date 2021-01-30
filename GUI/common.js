function createImageDiv(image){
  var imageDiv = document.createElement("div");
  var newImg = document.createElement("img");
  newImg.src = image.img;
  imageDiv.appendChild(newImg);
  var infoDiv = document.createElement("div");
  infoDiv.append(`name: ${name} date: ${image.date}`);
  imageDiv.appendChild(infoDiv)
  return imageDiv;
}

function appendImages(images, div, permitSameName=false){
  for(name in images){
    for(image of images[name]){
      const imageDiv = createImageDiv(image);
      div.appendChild(imageDiv);
      if(!permitSameName) break;
    }
  }
}

function removeAllChild(parents){
  while (parents.firstChild) {
    parents.removeChild(parents.firstChild);
  }
}

eel.expose(onStartRecognization, "on_start_recognization");
function onStartRecognization(){
  //alert("start!");
}

eel.expose(onRecognized, "on_recognized");
function onRecognized(Recognizedtext){
  alert(Recognizedtext);
}
