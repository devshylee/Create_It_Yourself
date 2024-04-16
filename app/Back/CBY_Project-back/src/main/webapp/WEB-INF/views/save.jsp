<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="${pageContext.request.contextPath}/resources/css/globals.css" />
    <link rel="stylesheet" href="${pageContext.request.contextPath}/resources/css/sign-up.css" />
    <!-- <link rel="stylesheet" href="sigh-up.js" /> -->

    <script>
        function test() {
            const form = document.getElementById("register_form");
            const formData = new FormData(form);

            const jsonData = {
                memberEmail: formData.get("memberEmail"),                       //이메일
                memberPassword: formData.get("memberPassword"),                 //패스워드
                memberName: formData.get("memberName"),                         //이름
                memberBirthDate: formData.get("memberBirthDate"),     //생년월일
            };

            // JSON 데이터를 사용하여 API 호출
            fetch("/member/save", {
                method: "POST",
                body: JSON.stringify(jsonData),
            })
                .then((response) => response.json())
                .then((data) => {
                    // ...
                    // API 응답 처리
                    if (data.success) {
                        alert("회원 가입 성공!");
                        location.href = "/";
                    } else {
                        alert("회원 가입 실패!");
                        console.log(data.error);
                    }
                });
        }

        document.addEventListener("DOMContentLoaded", function () {
            const signUpButton = document.querySelector('input[type="submit"][value="Sign-up"]');

            signUpButton.addEventListener('click', function (event) {
                test();
            });
        });
    </script>
</head>

<body>

<!-- <form action="/member/register" method="post" id="register_form">

    <input type="text" name="memberName" placeholder="이름">
    <input type="text" name="memberId" placeholder="아이디">
    <input type="text" name="memberPassword" placeholder="비밀번호">
    <input type="text" name="memberBirthDate" placeholder="생년월일">
    <input type="text" name="memberMobile" placeholder="전화번호">
    <input type="text" name="memberEmail" placeholder="이메일" id="memberEmail" onblur="emailCheck()">
    <p id="check-result"></p>
    <input type="submit" value="회원가입">
  </form>
-->

<div class="box">
    <div class="group">
        <form action="${pageContext.request.contextPath}/member/save" method="post" id="register_form">
            <div class="overlap">
                <div class="rectangle"></div>
                <img class="vector" src="${pageContext.request.contextPath}/resources/img/vector.svg" />
                <div class="div">
                    <div class="overlap-group">
                        <div class="rectangle-2"></div>
                        <div class="text-wrapper"><input type="text" name="memberPassword" placeholder="비밀번호를 입력하세요"
                                                         value="testPw1"></div>
                        <img class="free-icon-password" src="${pageContext.request.contextPath}/resources/img/free-icon-password-4520142-1.png" />
                    </div>
                    <div class="overlap-3">
                        <div class="rectangle-2"></div>
                        <div class="text-wrapper-3"><input type="text" name="memberEmail" placeholder="이메일" id="memberEmail"
                                                           onblur="emailCheck()"> </div>
                    </div>
                </div>
                <div class="overlap-wrapper">
                    <div class="overlap-3">
                        <div class="rectangle-2"></div>
                        <div class="text-wrapper-3"><input type="text" name="memberName" placeholder="이름" value="testName1"></div>
                    </div>
                </div>
                <div class="overlap-group-wrapper">
                    <div class="overlap-3">
                        <div class="rectangle-2"></div>
                        <div class="text-wrapper-3"><input type="text" name="memberBirthDate" placeholder="생년월일" value="011201">
                        </div>
                    </div>
                </div>
                <img class="union" src="${pageContext.request.contextPath}/resources/img/union.svg" />
                <div class="text-wrapper-4">CBY</div>
                <div class="div-wrapper">
                    <div class="overlap-4">
                        <div class="rectangle-3"></div>
                        <div class="text-wrapper-5"><button onclick="save()">Sign up</button></div>
                    </div>
                </div>

            </div>
        </form>
    </div>
</div>
</body>

</html>