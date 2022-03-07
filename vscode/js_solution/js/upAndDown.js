//요소 선택 과정
var unknown = document.querySelector("#targetNumber");
var checkNumber = document.querySelector("#check_result");
var sendBtn = document.getElementById("sendData");
var resetBtn = document.getElementById("resetData");
var userChoice = document.getElementById("textData");

var target = Math.floor(Math.random()*100)+1;;
var result = "???";
checkNumber.textContent = '숫자를 입력해주세요.';

setNumber(result);
sendBtn.onclick = sendNumber;
resetBtn.onclick = resetNumber;

function setNumber(str){
    unknown.textContent = str;
}
//Up & Down 알고리즘
function upNdown(number){
    userNumber = number;
    if(userNumber < target) {
        checkNumber.textContent = 'UP!';
    }
    else if(userNumber > target) {
        checkNumber.textContent = 'DOWN!';
    }
    else {
        checkNumber.textContent = '정답입니다!';
        setNumber(target);
    }
}



//서브밋 클릭시 input data 전송
function sendNumber() {
    console.log("sendNumber 실행");
    var userData = userChoice.value
    upNdown(userData);
    userChoice.value="";
}

//리셋버튼 클릭시 랜덤 숫자 초기화
function resetNumber() {
    var random = Math.floor(Math.random()*100)+1;
    target =  random;
    setNumber(target);
}