<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Check</title>
    <link rel="stylesheet" href="${pageContext.request.contextPath}/resources/css/update.css">
</head>
<body>
<div class="container">
    <header>
        <a href="http://localhost:8085/member/main" class="logo">CBY</a>
    </header>
    <h1>내프로필 수정</h1>
    <div class="form-box">
        <form action="${pageContext.request.contextPath}/member/passwordCheck" method="post">
            <div class="form-group">
                <input type="password" name="password" id="password" placeholder="비밀번호를 입력하세요" required>
            </div>
            <input type="hidden" name="id" value="${member.id}">
            <button type="submit">확인</button>
        </form>
    </div>
</div>
</body>
</html>
