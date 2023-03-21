async function getMeme() {
  let data = await (await fetch("https://meme-api.com/gimme")).json();
  console.log(data.url);
  document.getElementById("meme").src = data.url;
}
getMeme();
