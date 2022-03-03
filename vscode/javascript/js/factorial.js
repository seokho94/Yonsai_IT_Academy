var facDisplay = document.querySelector("#result");
var n = prompt("숫자를 입력하세요.");
var nFact = 1;
var i = 2;
var calProcess = String(nFact);

while(i <= n) {
    nFact *=i;
    calProcess = calProcess + " X " + String(i);
    i++;
}

facDisplay.innerHTML = n + "! = " + calProcess + " = " + nFact;