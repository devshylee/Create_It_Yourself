<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>회원가입</title>
    <!-- CSS 링크 수정 -->
    <link rel="stylesheet" href="${pageContext.request.contextPath}/resources/css/global.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/resources/css/sign-up.css">
    <!-- jQuery 라이브러리 추가 -->
    <script src="https://code.jquery.com/jquery-3.6.3.min.js" integrity="sha256-pvPw+upLPUjgMXY0G+8O0xUf+/Im1MZjXxxgOcBQBXU=" crossorigin="anonymous"></script>
    <script>
        function save() {
            const form = document.getElementById("register_form");
            const formData = new FormData(form);

            const jsonData = {
                memberEmail: formData.get("memberEmail"),
                memberPassword: formData.get("memberPassword"),
                memberName: formData.get("memberName"),
                memberBirthDate: formData.get("memberBirthDate"),
            };

            // 이메일 중복 확인
            fetch("/member/email-check", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ memberEmail: jsonData.memberEmail })
            })
                .then(response => response.json())
                .then(data => {
                    if (data === "no") {
                        alert("중복된 이메일이 있습니다.");
                        document.getElementById("memberEmail").focus();
                    } else {
                        // 중복되지 않은 경우 회원가입 요청
                        fetch("/member/save", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify(jsonData)
                        })
                            .then(response => response.json())
                            .then(data => {
                                if (data.success) {
                                    alert("회원 가입 성공!");
                                    location.href = "/";
                                } else {
                                    alert("회원 가입 실패!");
                                    console.log(data.error);
                                }
                            });
                    }
                })
                .catch(error => {
                    console.error("Error:", error);
                });
        }

        const emailCheck = () => {
            const email = document.getElementById("memberEmail").value;
            const checkResult = document.getElementById("check-result");

            if (email === "") {
                checkResult.innerHTML = "";
                return;
            }
            console.log("입력한 이메일", email);
            $.ajax({
                type: "post",
                url: "/member/email-check",
                data: {
                    "memberEmail": email
                },
                success: function(res) {
                    console.log("요청성공", res);
                    if (res === "ok") {
                        console.log("사용가능한 이메일");
                        checkResult.style.color = "green";
                        checkResult.innerHTML = "사용가능한 이메일";
                    } else {
                        console.log("이미 사용중인 이메일");
                        checkResult.style.color = "red";
                        checkResult.innerHTML = "이미 사용중인 이메일";
                    }
                },
                error: function(err) {
                    console.log("에러발생", err);
                }
            });
        }
    </script>
</head>

<body>
<div class="box">
    <div class="group">
        <form action="${pageContext.request.contextPath}/member/save" method="post" id="register_form" name="joinform">
            <div class="overlap">
                <div class="rectangle"></div>
                <img class="vector" src="${pageContext.request.contextPath}/resources/img/vector.svg" />
                <div class="div">
                    <div class="overlap-group">
                        <div class="rectangle-2"></div>
                        <div class="text-wrapper">
                            <input type="password" name="memberPassword" placeholder="비밀번호를 입력하세요" tabindex="3" required>
                        </div>
                        <img class="free-icon-password" src="${pageContext.request.contextPath}/resources/img/free-icon-password-4520142-1.png" />
                    </div>
                    <div class="overlap-3">
                        <div class="rectangle-2"></div>
                        <div class="text-wrapper-3">
                            <input type="text" name="memberEmail" placeholder="이메일" id="memberEmail" onblur="emailCheck()" tabindex="2" data-initial-value="" required>
                        </div>
                        <div class="check-result-wrapper">
                            <p id="check-result"></p>
                        </div>
                    </div>
                </div>
                <div class="overlap-wrapper">
                    <div class="overlap-3">
                        <div class="rectangle-2"></div>
                        <div class="text-wrapper-3">
                            <input type="text" name="memberName" placeholder="이름" tabindex="1" required>
                        </div>
                    </div>
                </div>
                <div class="overlap-group-wrapper">
                    <div class="overlap-3">
                        <div class="rectangle-2"></div>
                        <div class="text-wrapper-3">
                            <input type="text" name="memberBirthDate" placeholder="생년월일" tabindex="4" required>
                        </div>
                    </div>
                </div>
                <img class="union" src="${pageContext.request.contextPath}/resources/img/union.svg" />
                <div class="text-wrapper-4"><a href="http://localhost:8085/">CBY</a></div>
                <div class="div-wrapper">
                    <div class="overlap-4">
                        <div class="rectangle-3"></div>
                        <!-- 버튼 스타일을 CSS에서 정의 -->
                        <div class="text-wrapper-5">
                            <button type="submit" class="sign-up-button" tabindex="5">Sign up</button>
                        </div>
                    </div>
                </div>
            </div>
        </form>
    </div>
</div>
</body>

</html>
