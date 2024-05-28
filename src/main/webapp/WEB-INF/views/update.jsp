<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>회원 정보 수정</title>
    <link rel="stylesheet" href="${pageContext.request.contextPath}/resources/css/update.css">
</head>
<body>
<div class="container">
    <header>
        <a href="http://localhost:8085/member/main" class="logo">CBY</a>
    </header>
    <h1>회원 정보 수정</h1>
    <div class="form-box">
        <form action="${pageContext.request.contextPath}/member/update" method="post" name="updateForm">
            <input type="hidden" name="id" value="${member.id}">
            <div class="form-group">
                <label for="memberEmail">이메일</label>
                <input type="text" name="memberEmail" id="memberEmail" value="${member.memberEmail}" readonly>
            </div>
            <div class="form-group">
                <label for="memberName">이름</label>
                <input type="text" name="memberName" id="memberName" value="${member.memberName}" required>
            </div>
            <div class="form-group">
                <label for="memberBirthDate">생년월일</label>
                <input type="text" name="memberBirthDate" id="memberBirthDate" value="${member.memberBirthDate}" required>
            </div>
            <div class="form-group">
                <label for="memberPassword">비밀번호</label>
                <input type="password" name="memberPassword" id="memberPassword">
            </div>
            <button type="button" onclick="update()">수정</button>
        </form>
    </div>
</div>
<script>
    const update = () => {
            document.updateForm.submit();
    }
</script>
</body>
</html>
