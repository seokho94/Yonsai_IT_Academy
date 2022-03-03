for(var i=2; i<20; i++){
    document.write("<div>");
    document.write("<h3>" + i + "단</h3>");
    for(var j=1; j<20; j++){
        document.write(i + " X " + j + " = " + i * j + "<br>");
    }
    document.write("</div>");
}