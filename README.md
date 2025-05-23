# ✍️ Create It Yourself - AI 기반 질문형 일기 작성 서비스

> 하루 5개의 질문과 이미지 생성으로 완성하는  
> **질문 기반 간편 일기 작성 서비스**

---

## 📌 프로젝트 소개

바쁜 현대인들이 복잡한 형식 없이 간편하게 일기를 작성할 수 있도록,  
**AI 기반의 질문-답변 시스템과 이미지 생성을 결합한 새로운 일기 서비스**를 기획했습니다.

### ✔️ 필요성
- 바쁜 일상 속에서 일기를 쓰기 어려운 사람들을 위해 간단한 형식의 기록 방식을 제공
- 글을 쓰는 대신 질문에 답하는 방식으로 심리적 부담을 줄임

### ✔️ 서비스 개요
- 사용자는 매일 5개의 질문에 답변만 하면 일기 작성이 완료됨
- 답변 내용을 바탕으로 **AI가 맞춤형 이미지를 생성**
- 사용자의 감정, 분위기, 기록을 시각적으로 함께 저장할 수 있음

---

## 💡 핵심 기능

### 🔐 회원 기능 (Spring)
- **회원가입**
  - 사용자 정보 검증 후 DB에 저장
- **로그인**
  - 인증 성공 시 세션 생성
- **로그아웃**
  - 세션 삭제 및 로그아웃 처리

### ❓ 질문 생성 (Flask + Gemini Pro API)
- 질문은 1~5단계로 구성되며, 이전 답변을 바탕으로 다음 질문이 생성됨
- 자연스럽고 연관성 있는 질문 생성을 위해 **Google Gemini Pro** API 활용
- 모든 질문/답변은 DB에 저장

### 🖼️ 이미지 생성 (Flask + DALL·E 3)
- 마지막 질문까지 완료 시, 전체 답변을 기반으로 이미지 생성 프롬프트 작성
- 프롬프트는 영어로 번역되어 **OpenAI DALL·E 3 API**를 통해 이미지 생성
- 생성된 이미지는 URL로 반환 → 이미지 저장 후 바이너리 인코딩하여 DB에 저장

### 📅 일기 조회 기능 (Flask)
- 특정 날짜의 질문 및 답변 조회 (JSON 반환)
- 해당 날짜의 이미지도 JSON 형태로 조회 가능

---

## 🧰 기술 스택

| 분야 | 기술 |
|------|------|
| **Frontend** | Figma + Anima Plugin, HTML5, CSS3, JavaScript |
| **Backend** | Flask, Spring (MyBatis, Gradle) |
| **Database** | MySQL, AWS RDS |
| **Deployment** | AWS EC2 |
| **AI 모델** | Google Gemini Pro, OpenAI DALL·E 3 |
