window.onload = function(){

  const form = document.getElementById("form");
  const logs = document.getElementById("logs");

  form.addEventListener("submit", onSearch);

  function onSearch(e){
    e.preventDefault();
    const word = form.word.value;
    searchLogs(word);
  }

  async function searchLogs(word){
    const images = await eel.export_images(word)();
    removeAllChild(logs);
    if(images == null){
      logs.append("まだ記録はありません");
      return;
    }
    appendImages(images, logs, permitSameName=true);
  }

  searchLogs("");

}
