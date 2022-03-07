//요소 선택 과정
var unknown = document.querySelector("#targetNumber");
var sendBtn = document.getElementById("sendData");
var resetBtn = document.getElementById("resetData");

var target = Math.floor(Math.random()*100)+1;;
var result = target;

setNumber(result);
upNdown();
sendBtn.onclick = sendNumber;
resetBtn.onclick = resetNumber;

function setNumber(string){
    unknown.textContent = result;
}
//Up & Down 알고리즘
function upNdown(number){
    // if(userNumber < target) alert("up");
    // else if(userNumber > target) alert("down");
    // else {
    //     alert("맞혔습니다.");
    //     result = target;
    //     unknown.textContent = result;
    //     break;
    // }
}



//서브밋 클릭시 input data 전송
function sendNumber() {
    var userData = document.getElementById("#textData");
    upNdown(userData);
}

//리셋버튼 클릭시 랜덤 숫자 초기화
function resetNumber() {
    var random = Math.floor(Math.random()*100)+1;
    target =  random;
    setNumber(target);
}