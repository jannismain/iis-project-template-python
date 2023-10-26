// remove '@' from github mention magiclink
let mentions = document.querySelectorAll(".magiclink-gitlab.magiclink-mention");
mentions.forEach((el) => {
  el.text = el.text.replace("@", "");
});
