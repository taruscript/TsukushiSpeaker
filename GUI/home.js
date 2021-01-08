window.onload = function(){

  const form = document.getElementById("form");
  const resultdiv = document.getElementById("result");

  form.addEventListener("submit", search_image);

  async function search_image(e){
    e.preventDefault();
    const word = form.word.value;
    const images = await eel.export_images(word)();
    removeAllChild(resultdiv);
    if(images == null){
      resultdiv.append("該当する記録は見つかりませんでした");
      return;
    }
    appendImages(images, resultdiv);
  }

}
