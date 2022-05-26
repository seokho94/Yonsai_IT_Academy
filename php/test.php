<?php
    //한 줄 주석용
    /*
        여러 줄
        주석용
    */

    $a = 100;
    print $a;

    $b = "안녕하세요? MySQL";
    echo $b;

    $a = 123; echo gettype($a), "<br>";
    $a = 123.123; echo gettype($a), "<br>";
    $a = "MySQL"; echo gettype($a), "<br>";
    $a = true; echo gettype($a), "<br>";
    $a = array(1, 2, 3); echo gettype($a), "<br>";

    $str1 = "이것이 MySQL이다<br>"; echo $str1;
    $str2 = 'php 프로그래밍<br>'; echo $str2;
    $str3 = "select * from userTBL where userID = 'JYP' "; echo $str3;

    $a = 100;
    $b = 200;

    if($a > $b) {
        echo "a가 b보다 큽니다.";
    }
    else{
        echo "a가 b보다 작습니다.";
    }
    
?>