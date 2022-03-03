var numbers = new Array(10);
for(let i=0; i<numbers.length; i++){
    numbers[i] = Math.floor(Math.random()*10)%10;
}
bubble(numbers);

function bubble(Array) {
    var arr = Array;
    var index = 0;
    var n = arr.length;
    var count = 1;
    console.log("초기 배열 상태 : ");
    
    for(let i=0; i<arr.length; i++){
        console.log(arr[i]+ " ");
    }

    console.log("<br>");

    while(n!=2){
        if(arr[index] > arr[index+1]){
            var temp = arr[index+1];
            arr[index+1] = arr[index];
            arr[index] = temp;
        }

        index++;
        if(index==n-2){
            index = 0;
            console.log(count + "회전 결과 : ");
            for(let i=0; i<arr.length; i++){
                console.log(arr[i]+" ");
            }
            console.log("<br>");
        }
    }
}