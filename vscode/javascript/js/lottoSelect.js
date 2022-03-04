var lottoDisplay = document.querySelector("#parContent");
select_Numbers();

function select_Numbers() {
    var lottoNumber = new Array(6);
    var index =0;
    //중복 값을 제외한 번호 추출
    while(index<6){
        var number = Math.floor(Math.random()*100)%45+1;
        if(checkOverlap(lottoNumber, number)){
            lottoNumber[index] = number;
            index++;
        }
    }
    index = 0;
    var n = lottoNumber.length;

    //lottoNumber 오름차순 정렬
    while(n!=1){
        if(lottoNumber[index]>lottoNumber[index+1]){
            var temp = lottoNumber[index+1];
            lottoNumber[index+1] = lottoNumber[index];
            lottoNumber[index] = temp;
        }
        index++;
        if(index === (n-1)){
            n--;
            index=0;
        }
    }
    
    //#result에 배열 요소 출력
    for(let i=0; i<lottoNumber.length; i++){
        matchBall(lottoNumber[i]);
    }
}

//중복값 확인
function checkOverlap(arr, n){
    var checkSign = true;
    for(let i=0; i<arr.length; i++){
        if(arr[i]===n) {
            checkSign = false;
            return checkSign;
        }
    }
    return checkSign;
}

//로또 번호 요소 생성
function matchBall(n){
    var ball = document.createElement('div');
    var ballNumber = document.createTextNode(n);
    ball.style.borderRadius = "50%";
    ball.style.width = "40px";
    ball.style.height = "40px";
    ball.style.color = "white";
    ball.style.fontSize = "20px";
    ball.style.lineHeight = "40px";
    if(n<=10) ball.style.backgroundColor = "#fcc43d";
    else if(n>10 && n<=20) ball.style.backgroundColor = "#8cc6e7";
    else if(n>20 && n<=30) ball.style.backgroundColor = "#f18d80";
    else if(n>30 && n<=40) ball.style.backgroundColor = "#aca7de";
    else ball.style.backgroundColor = "#6bce9e";
    ball.appendChild(ballNumber);
    ball.className = 'lottoBall';
    lottoDisplay.appendChild(ball);
}