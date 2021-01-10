function createImageDiv(image){
  var imageDiv = document.createElement("div");
  var newImg = document.createElement("img");
  newImg.src = "data:image/jpeg;base64," + image.img;
  imageDiv.appendChild(newImg);
  imageDiv.append(`name: ${name} date: ${image.date}`);
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
