<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>비밀번호 재설정 요청</title>
    <link rel="stylesheet" type="text/css" href="${pageContext.request.contextPath}/resources/css/reset.css">
    <style>
        /* 여기에 CSS 스타일링을 추가할 수 있습니다. */
    </style>
</head>
<body>
<div class="container">
    <h2>비밀번호 재설정 요청</h2>
    <form action="${pageContext.request.contextPath}/member/resetPassword" method="post">
        <label for="email">이메일 주소</label>
        <input type="email" id="email" name="email" required>
        <button type="submit">비밀번호 재설정 링크 보내기</button>
    </form>
</div>
</body>
</html>
