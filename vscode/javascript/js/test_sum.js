var sumDisplay = document.querySelector('#result');
    var sum = 0;
    for(var i=1; i < 6; i++){
        sum += i;
    }
    
    sumDisplay.innerHTML("1부터 5까지 더하면 " + sum);

