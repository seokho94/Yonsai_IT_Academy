var slides = document.querySelectorAll("#slides > img");
var prev = document.getElementById("prev");
var next = document.getElementById("next");

showSlides(current);
prev.onclick = prevSlide;
next.onclick = nextSlide;

function showSlides(n){
    for(let i=0; i<slides.length; i++){
        slides[i].style.display = "none";
    }
    slides[n].style.display="block";
}

function prevSlide(){
    if(current<0) current=slides.length-1;
    else current--;
}

function nextSlide(){
    if(current>slides.length) current=0;
    else current++;
}
