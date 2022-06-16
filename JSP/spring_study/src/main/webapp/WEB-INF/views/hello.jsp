<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h2>hello World</h2>
	<hr>
	현재 날짜와 시간은 <%=java.time.LocalDateTime.now() %>
	<hr>
	메시지 : ${msg }
</body>
</html>