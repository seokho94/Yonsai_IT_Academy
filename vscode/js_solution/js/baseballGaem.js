var target = Math.floor(Math.random()*100)+1;

while(true){
    var userNumber = prompt("숫자를 입력해주세요.");
    if(userNumber < target) alert("up");
    else if(userNumber > target) alert("down");
    else {
        alert("맞혔습니다.");
        break;
    }
}