var session = prompt("관심 세션을 선택해 주세요. 1-마케팅, 2-개발, 3-디자인", "1");
var divArea = document.querySelector('#result');

switch(session) {
    case "1" : divArea.innerHTML=("<p>마케팅 세션은 <strong>201호</strong>에서 진행됩니다.</p>");
    break;
    case "2" : divArea.innerHTML=("<p>개발 세션은 <strong>203호</strong>에서 진행됩니다.</p>");
    break;
    case "3" : divArea.innerHTML=("<p>디자인 세션은 <strong>205호</strong>에서 진행됩니다.</p>");
    break;

    default: alert("잘못 입력했습니다.");
}