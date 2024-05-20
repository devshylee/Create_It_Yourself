<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="${pageContext.request.contextPath}/resources/css/globals.css" />
    <link rel="stylesheet" href="${pageContext.request.contextPath}/resources/css/sign-up.css" />
    <!-- <link rel="stylesheet" href="sigh-up.js" /> -->
    <script src="https://code.jquery.com/jquery-3.6.3.min.js" integrity="sha256-pvPw+upLPUjgMXY0G+8O0xUf+/Im1MZjXxxgOcBQBXU=" crossorigin="anonymous"></script>

    <script>
        document.addEventListener("DOMContentLoaded", function () {
            // "Sign up" 버튼을 찾습니다.
            const signUpButton = document.querySelector('input[type="submit"][value="Sign-up"]');

            // "Sign up" 버튼에 클릭 이벤트 리스너를 추가합니다.
            signUpButton.addEventListener('click', function (event) {
                event.preventDefault(); // 기본 이벤트(폼 전송) 방지

                // 입력값을 가져옵니다.
                const memberEmail = document.joinform.memberEmail.value;
                const memberName = document.joinform.memberName.value;
                const memberPassword = document.joinform.memberPassword.value;
                const memberBirthDate = document.joinform.memberBirthDate.value;

                // 입력값이 비어 있는지 확인합니다.
                if (memberEmail === "") {
                    alert("이메일을 입력해주세요.");
                    document.joinform.memberEmail.focus();
                    return false; // 제출을 막습니다.
                } else if (memberName === "") {
                    alert("이름을 입력해주세요.");
                    document.joinform.memberName.focus();
                    return false; // 제출을 막습니다.
                } else if (memberPassword === "") {
                    alert("비밀번호를 입력해주세요.");
                    document.joinform.memberPassword.focus();
                    return false; // 제출을 막습니다.
                } else if (memberBirthDate === "") {
                    alert("생년월일을 입력해주세요.");
                    document.joinform.memberBirthDate.focus();
                    return false; // 제출을 막습니다.
                } else {
                    // 모든 필드가 비어 있지 않으면 제출을 허용합니다.
                    save();
                }
            });

            // save 함수는 여전히 필요하므로 그대로 둡니다.
        });


        // signUpButton.addEventListener('click', function (event) {
        //         event.preventDefault(); // 기본 이벤트(폼 전송) 방지
        //         save();
        //     });
        //
        //
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
        // });
        const emailCheck = () => {
            const email = document.getElementById("memberEmail").value;
            const checkResult = document.getElementById("check-result");
            console.log("입력한 이메일", email);
            $.ajax({
                // 요청방식: post, url: "email-check", 데이터: 이메일
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
        <form action="${pageContext.request.contextPath}/member/save" method="post" id="register_form" name="joinform">
            <div class="overlap">
                <div class="rectangle"></div>
                <img class="vector" src="${pageContext.request.contextPath}/resources/img/vector.svg" />
                <div class="div">
                    <div class="overlap-group">
                        <div class="rectangle-2"></div>
                        <div class="text-wrapper"><input type="text" name="memberPassword" placeholder="비밀번호를 입력하세요"
                                                         ></div>
                        <img class="free-icon-password" src="${pageContext.request.contextPath}/resources/img/free-icon-password-4520142-1.png" />
                    </div>
                    <div class="overlap-3">
                        <div class="rectangle-2"></div>
                        <div class="text-wrapper-3">
                            <input type="text" name="memberEmail" placeholder="이메일" id="memberEmail" onblur="emailCheck()">
                        </div>
                        <div class="check-result-wrapper">
                            <p id="check-result"></p>
                        </div>
                    </div>
                </div>

                <div class="overlap-wrapper">
                    <div class="overlap-3">
                        <div class="rectangle-2"></div>
                        <div class="text-wrapper-3"><input type="text" name="memberName" placeholder="이름"></div>
                    </div>
                </div>

                <div class="overlap-group-wrapper">
                    <div class="overlap-3">
                        <div class="rectangle-2"></div>
                        <div class="text-wrapper-3"><input type="text" name="memberBirthDate" placeholder="생년월일">
                        </div>
                    </div>
                </div>

                <img class="union" src="${pageContext.request.contextPath}/resources/img/union.svg" />
                <div class="text-wrapper-4">CBY</div>
                <div class="div-wrapper">
                    <div class="overlap-4">
                        <div class="rectangle-3"></div>
                        <div class="text-wrapper-5"><button class="sign-up-button" onclick="save()">Sign up</button>
                        </div>
                    </div>
                </div>

            </div>
        </form>
    </div>
</div>
</body>

</html>