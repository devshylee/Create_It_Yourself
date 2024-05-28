<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>내 정보</title>
    <link rel="stylesheet" href="${pageContext.request.contextPath}/resources/css/detail.css">
</head>
<body>
<div class="container">
    <header>
        <a href="http://localhost:8085/member/main" class="logo">CBY</a>
    </header>
    <h1>내 정보</h1>
    <div class="info-box">
        <table>
            <tr>
                <th>이메일</th>
                <td>${member.memberEmail}</td>
            </tr>
            <tr>
                <th>이름</th>
                <td>${member.memberName}</td>
            </tr>
            <tr>
                <th>생년월일</th>
                <td>${member.memberBirthDate}</td>
            </tr>
        </table>
        <button onclick="location.href='http://localhost:8085/member/passwordCheck'" class="edit-button">수정</button>
    </div>
</div>
</body>
</html>
