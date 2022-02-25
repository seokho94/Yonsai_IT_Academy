var Autoslides = document.querySelectorAll("#slides > img");
var n =0;
AutoSlideShows();

function AutoSlideShows(){
    // console.log("실행중?");
    for(let i=0; i<Autoslides.length; i++) Autoslides[i].style.display = "none";

    Autoslides[n].style.display = "block";
    n++;
    n%=Autoslides.length;
    setTimeout(AutoSlideShows,2000);
}