<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="${pageContext.request.contextPath}/resources/css/global.css" />
    <link rel="stylesheet" href="${pageContext.request.contextPath}/resources/css/main.css" />
    <link rel="stylesheet" href="${pageContext.request.contextPath}/resources/css/days.css" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reset-css@4.0.1/reset.min.css" />
    <link href="https: //fonts.googleapis.com/css2?family=Caveat:wght@400..700&display=swap" rel="stylesheet">

    <script>
        function toggleSidebar() {
            var sidebar = document.getElementById("sidebar");
            sidebar.classList.toggle("active");
        }
        const update = () => {
            location.href = "/member/update";
        }
        const logout = () => {
            location.href = "/member/logout";
        }
        function goToMyInfo() {
            location.href = "${pageContext.request.contextPath}/member/my-info";
        }
    </script>

</head>
<body>
<div class="box">
    <div class="group">
        <div class="overlap-group">
            <div class="main"></div>
            <div class="rectangle"></div>
            <div class="headbar"></div>
            <div class="ellipse"></div>
            <div class="div"></div>
            <div class="ellipse-2"></div>
            <div class="ellipse-3"></div>
            <div class="ellipse-4"></div>
            <div class="ellipse-5"></div>
            <div class="ellipse-6"></div>
            <div class="ellipse-7"></div>
            <div class="ellipse-8"></div>
            <div class="ellipse-9"></div>
            <div class="ellipse-10"></div>
            <div class="ellipse-11"></div>
            <div class="ellipse-12"></div>
            <div class="ellipse-13"></div>
            <div class="ellipse-14"></div>
            <div class="ellipse-15"></div>
            <div class="ellipse-16"></div>
            <div class="ellipse-17"></div>
            <div class="ellipse-18"></div>
            <div class="ellipse-19"></div>
            <div class="ellipse-20"></div>
            <div class="ellipse-21"></div>
            <div class="ellipse-22"></div>
            <div class="ellipse-23"></div>
            <div class="ellipse-24"></div>
            <div class="ellipse-25"></div>
            <div class="ellipse-26"></div>
            <div class="ellipse-27"></div>
            <div class="ellipse-28"></div>
            <div class="ellipse-29"></div>
            <div class="ellipse-30"></div>
            <div class="text-wrapper">sun</div>
            <div class="text-wrapper-2">mon</div>
            <div class="text-wrapper-3">tue</div>
            <div class="text-wrapper-4">wed</div>
            <div class="text-wrapper-5">thu</div>
            <div class="text-wrapper-6">fri</div>
            <div class="text-wrapper-7">sat</div>
            <div class="navbar">
                <div class="dec">dec</div>
                <div class="nov">nov</div>
                <div class="oct">oct</div>
                <div class="sep">sep</div>
                <div class="aug">aug</div>
                <div class="jul">jul</div>
                <div class="jun">jun</div>
                <div class="may">may</div>
                <div class="apr">apr</div>
                <div class="mar">mar</div>
                <div class="feb">feb</div>
                <div class="jan">jan</div>
            </div>
            <div class="text-wrapper-17">1</div>
            <img class="line" src="${pageContext.request.contextPath}/resources/img/line-17.png" />
            <div class="text-wrapper-18">2024</div>
            <div class="text-wrapper-19">january</div>
            <div class="icon" onclick="toggleSidebar()"><img class="img" src="${pageContext.request.contextPath}/resources/img/person_FILL0_wght400_GRAD0_opsz24.png" /></div>
            <div id="sidebar" class="sidebar">
                <!-- 메뉴 항목들 -->
                <form action="${pageContext.request.contextPath}/member/update">
                    <div class="menu-item"><button onclick="update()">userUpdate</button></div>
                </form>
                <form action="${pageContext.request.contextPath}/member/login">
                    <div class="menu-item"><button onclick="logout()">userLogout</button></div>
                </form>
                <form action="${pageContext.request.contextPath}/member/my-info">
                    <div class="menu-item"><button onclick="goToMyInfo()">내정보</button></div>
                </form>
            </div>
            <div class="text-wrapper-20">CBY.com</div>
        </div>
    </div>
</div>
</body>
</html>
