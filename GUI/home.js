const form = document.getElementById("form");
const resultdiv = document.getElementById("result");
async function search_image(e){
  e.preventDefault();
  const word = form.word.value;
  const images = await eel.export_image(word)();
  while (resultdiv.firstChild) {
    resultdiv.removeChild(resultdiv.firstChild);
  }
  console.log(images);
  if(images == null){
    resultdiv.append("該当する記録は見つかりませんでした");
    return;
  }
  for(name in images){
    const image = images[name]
    var newDiv = document.createElement("div");
    var newImg = document.createElement("img");
    newImg.src = "data:image/jpeg;base64," + image.img;
    newDiv.appendChild(newImg);
    newDiv.append(`name: ${name} date: ${image.date}`);
    resultdiv.appendChild(newDiv);
  }
}
form.addEventListener("submit", search_image);
