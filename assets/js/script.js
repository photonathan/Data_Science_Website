function myFunction() {
  var x = document.getElementById("myDIV");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

var navLink = document.getElementById("nav");
var aboutDiv = document.querySelector(".about");
var photos = document.querySelectorAll("img");
navLink.addEventListener("click", function() {
  if(aboutDiv.style.display === "none") {
    aboutDiv.style.display = "block";
    navLink.textContent = "Home";
    for (var i=0; i < photos.length; i++){
      photos[i].style.display = "none";
    }
  } else {
    aboutDiv.style.display = "none";
    navLink.textContent = "About";
    for (var i=0; i < photos.length; i++){
      photos[i].style.display = "block";
    }
  }
});
