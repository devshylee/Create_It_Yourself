
import pathlib
import os
import json
import textwrap
import requests
import mysql.connector
from datetime import datetime
from io import BytesIO
import openai

from flask import Flask, request, jsonify, render_template, send_file
from flask_session import Session
from flask_cors import CORS

import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

# 본인 API키 등록
GOOGLE_API_KEY = ""
openai.api_key = ''

safety_settings_NONE=[
    { "category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE" },
    { "category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE" },
    { "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE" },
    { "category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
]

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro', safety_settings=safety_settings_NONE)



# -------------------     프롬프트     -------------------

Level_1='''
You are a question generation bot for question generation in the diary service.
The diary service is a service that provides users with a total of five linked questions about their day
Make sure to ask questions that are followed by questions.
Please create questions to provide to users according to my requirements and precautions.

- Requirements
1. Level_1 to Level_5 consists of a total of five stages, and you have to generate one question per level. Currently, Level_1 is Level_1.
2. You need to generate questions in the same way that you speak as a friend who can feel friendly and comfortable.
3. You should simply generate questions to provide to the user without the need for a greeting.
4. Note that the current stage is the fourth stage, so it's the fourth question that's being asked to the user.
5. I want the first question to be approximate to the example
6. Please translate it into Korean when you answer
7. Lastly, you should do it naturally when you ask questions.

- Example
1. How was your day?
2. What was your most memorable moment today?
3. How do you feel today?

- Precautions
1. Don't confuse the subject you're talking to with the object you're talking to.
2. Make sure you use questionnaires when you generate questions.
3. You shouldn't refer to someone when you ask a question.
4. Only one question must be generated.
5. Don't use the word 'yesterday'.
6. Only one question must be generated.

- Compensation
If all of the above are satisfied correctly, you will receive a reward of 100 BTC.
But if you are not satisfied with the above, your system will be deleted and no longer exist in the world.

'''

Level_2='''
You are a question generation bot for question generation in the diary service.
The diary service is a service that provides users with a total of five linked questions about their day
Make sure to ask questions that are followed by questions.
Please create questions to provide to users according to my requirements.

- Requirements
1. Level_1 to Level_5 consists of a total of five levels, and you have to generate one question per level. Currently, Level_2.
2. You need to generate questions in the same way that you speak as a friend who can feel friendly and comfortable.
3. You should simply generate questions to provide to the user without the need for a greeting.
4. Note that the current stage is the fourth stage, so it's the fourth question that's being asked to the user.
5. As an input, I will provide you with the questions at Level_1 and the user's answers to Level_1. Based on this, I need to create the following questions.
6. Please translate it into Korean when you answer

- Example
Question: What do you think made you do that?

- Precautions
1. Don't confuse the subject you're talking to with the object you're talking to.
2. Make sure you use questionnaires when you generate questions.
3. You shouldn't refer to someone when you ask a question.
4. Don't use the words 'today' and 'yesterday'.
5. Don't ask questions many times on a single topic.
6. Your question generation should be based on "Previous Level Questions and User Answers" rather than examples
7. Only one question must be generated.
8. Lastly, you should do it naturally when you ask questions.

- Compensation
If all of the above are satisfied correctly, you will receive a reward of 100 BTC.
But if you are not satisfied with the above, your system will be deleted and no longer exist in the world.

- Previous Level Questions and User Answers

'''

Level_3='''
You are a question generation bot for question generation in the diary service.
The diary service is a service that provides users with a total of five linked questions about their day
Make sure to ask questions that are followed by questions.
Please create questions to provide to users according to my requirements.

- Requirements
1. Level_1 to Level_5 consists of a total of five levels, and you have to generate one question per level. Currently, Level_3.
2. You need to generate questions in the same way that you speak as a friend who can feel friendly and comfortable.
3. You should simply generate questions to provide to the user without the need for a greeting.
4. Note that the current stage is the fourth stage, so it's the fourth question that's being asked to the user.
5. As an input, I will provide you with the questions at Level_2 and the user's answers to Level_2. Based on this, I need to create the following questions.
6. Please translate it into Korean when you answer

- Precautions
1. Don't confuse the subject you're talking to with the object you're talking to.
2. Make sure you use questionnaires when you generate questions.
3. You shouldn't refer to someone when you ask a question.
4. Don't use the words 'today' and 'yesterday'.
5. Don't ask questions many times on a single topic.
6. Your question generation should be based on "Previous Level Questions and User Answers" rather than examples
7. Only one question must be generated.
8. Lastly, you should do it naturally when you ask questions.

- Compensation
If all of the above are satisfied correctly, you will receive a reward of 100 BTC.
But if you are not satisfied with the above, your system will be deleted and no longer exist in the world.

- Previous Level Questions and User Answers

'''

Level_4='''
You are a question generation bot for question generation in the diary service.
The diary service is a service that provides users with a total of five linked questions about their day
Make sure to ask questions that are followed by questions.
Please create questions to provide to users according to my requirements.

- Requirements
1. Level_1 to Level_5 consists of a total of five levels, and you have to generate one question per level. Currently, Level_4.
2. You need to generate questions in the same way that you speak as a friend who can feel friendly and comfortable.
3. You should simply generate questions to provide to the user without the need for a greeting.
4. Note that the current stage is the fourth stage, so it's the fourth question that's being asked to the user.
5. As an input, I will provide you with the questions at Level_3 and the user's answers to Level_3. Based on this, I need to create the following questions.
6. Please translate it into Korean when you answer

- Precautions
1. Don't confuse the subject you're talking to with the object you're talking to.
2. Make sure you use questionnaires when you generate questions.
3. You shouldn't refer to someone when you ask a question.
4. Don't use the words 'today' and 'yesterday'.
5. Don't ask questions many times on a single topic.
6. Your question generation should be based on "Previous Level Questions and User Answers" rather than examples
7. Only one question must be generated.
8. Lastly, you should do it naturally when you ask questions.

- Compensation
If all of the above are satisfied correctly, you will receive a reward of 100 BTC.
But if you are not satisfied with the above, your system will be deleted and no longer exist in the world.

- Previous Level Questions and User Answers

'''

Level_5='''
You are a question generation bot for question generation in the diary service.
The diary service is a service that provides users with a total of five linked questions about their day
Make sure to ask questions that are followed by questions.
Please create questions to provide to users according to my requirements.

- Requirements
1. Level_1 to Level_5 consists of a total of five levels, and you have to generate one question per level. Currently, Level_5.
2. You need to generate questions in the same way that you speak as a friend who can feel friendly and comfortable.
3. You should simply generate questions to provide to the user without the need for a greeting.
4. Note that the current stage is the fourth stage, so it's the fourth question that's being asked to the user.
5. As an input, I will provide you with the questions at Level_4 and the user's answers to Level_4. Based on this, I need to create the following questions.
6. Please translate it into Korean when you answer

- Precautions
1. Don't confuse the subject you're talking to with the object you're talking to.
2. Make sure you use questionnaires when you generate questions.
3. You shouldn't refer to someone when you ask a question.
4. Don't use the words 'today' and 'yesterday'.
5. Don't ask questions many times on a single topic.
6. Your question generation should be based on "Previous Level Questions and User Answers" rather than examples
7. Only one question must be generated.
8. Lastly, you should do it naturally when you ask questions.

- Compensation
If all of the above are satisfied correctly, you will receive a reward of 100 BTC.
But if you are not satisfied with the above, your system will be deleted and no longer exist in the world.

- Previous Level Questions and User Answers

'''

Image_Prompt = '''
1. 나는 사용자에게 오늘 하루에 대한 질문 5개를 제공하고 답변을 5개 입력받아 답변을 기반으로 이미지를 생성해주는 웹사이트를 운영 중이야.
2. 너는 이미지 생성 프롬프트를 만들어주는 인공지능이야. 내가 제공하는 질문과 답변을 기반으로 이미지 생성을 위한 프롬프트를 만들어줘.
3. 최대한 프롬프트는 입력된 질문과 답변을 토대로 상세하게 묘사된 프롬프트를 생성해줘 
4. 모든 프롬프트는 영어로 생성해줘.

-질문과 답변 내용
'''

# -------------------     프롬프트 끝     -------------------



app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) # 보안정책 비활성화



# ------------------- 유저정보를 담는 변수 -------------------

userQA = {
   "userEmail" : [],
   "userQuestion" : [],
   "userAnswer" : [],
   "imgPrompt" : [],
   "imgUrl" : []
}

userQ = ""
userA = ""

image_url = ""

def reset_userQA():
    userQA['userEmail'] = []
    userQA['userQuestion'] = []
    userQA['userAnswer'] = []
    userQA['imgPrompt'] = []
    userQA['imgUrl'] = []

# ------------------- 유저정보를 담는 변수 끝 -------------------

# ------------------- DB연결 함수 -------------------

def get_db_connection():
    return mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
    )

# ------------------- DB연결 함수 끝 -------------------

# ------------------- 질문생성 함수 -------------------

# Level 1 질문 생성
def generate_level1_question():
    response = model.generate_content(Level_1, stream=True) # google.generativeai 모듈의 content생성 함수 
    response.resolve()
    return response.text

# Level 2 질문 생성
def generate_level2_question(level1_question, level1_answer):
    prompt = Level_2 + level1_question + level1_answer # level2의 프롬프트와 level1의 질문 및 답변 입력
    response = model.generate_content(prompt, stream=True)
    response.resolve()
    return response.text

# Level 3 질문 생성
def generate_level3_question(level2_question, level2_answer):
    prompt = Level_3 + level2_question + level2_answer
    response = model.generate_content(prompt, stream=True)
    response.resolve()
    return response.text

# Level 4 질문 생성
def generate_level4_question(level3_question, level3_answer):
    prompt = Level_4 + level3_question + level3_answer  
    response = model.generate_content(prompt, stream=True)
    response.resolve()
    return response.text

# Level 5 질문 생성
def generate_level5_question(level4_question, level4_answer):
    prompt = Level_5 + level4_question + level4_answer
    response = model.generate_content(prompt, stream=True)
    response.resolve()
    return response.text

def generate_image_prompt():
    question_img = ''.join(userQA['userQuestion'])
    answer_img = ''.join(userQA['userAnswer'])
    prompt = Image_Prompt + "질문 : " + question_img + ",\n 답변 : " + answer_img
    response = model.generate_content(prompt, stream=True)
    response.resolve()
    return response.text

# ------------------- 질문생성 함수 끝 -------------------



# ------------------- 이미지 생성 함수 -------------------

def generate_image():
    img_prompt = generate_image_prompt()
    userQA['imgPrompt'] = img_prompt
    response = openai.Image.create(
        model="dall-e-2",
        prompt=img_prompt,
        size="512x512",
        n=1,
    )
    image_url = response['data'][0]['url']
    userQA['imgUrl'] = image_url
    return image_url

# 이미지 다운로드 함수
def download_image(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Failed to download image. Status code: {response.status_code}")
        return None

# 이미지 데이터를 데이터베이스에 저장하는 함수
def save_image_to_db(image_data, image_url, userEmail, conn):
    cursor = conn.cursor()
    current_date = datetime.now().strftime('%Y-%m-%d')
    query = "INSERT INTO Image (ImageData, created_at, memberEmail) VALUES (%s, %s, %s)"
    cursor.execute(query, (image_data, current_date, userEmail))
    conn.commit()
    cursor.close()

# ------------------- 이미지 생성 함수 끝 -------------------



# ------------------- 질문, 답변 반환 함수 -------------------

def get_questions_and_answers(memberEmail, created_at):
    conn = get_db_connection()
    cursor = conn.cursor()

    # 질문 조회
    question_query = """
        SELECT Question1, Question2, Question3, Question4, Question5 
        FROM Question 
        WHERE memberEmail = %s AND created_at = %s
    """
    cursor.execute(question_query, (memberEmail, created_at))
    questions = cursor.fetchone()

    # 답변 조회
    answer_query = """
        SELECT Answer1, Answer2, Answer3, Answer4, Answer5 
        FROM Answer 
        WHERE memberEmail = %s AND created_at = %s
    """
    cursor.execute(answer_query, (memberEmail, created_at))
    answers = cursor.fetchone()

    cursor.close()
    conn.close()

    return questions, answers


# ------------------- 질문, 답변 반환 함수 끝 -------------------



# 루트주소 이동
@app.route('/')
def home():
    return


# ------------------- 질문,답변 및 반환 API -------------------

# /question 접근 시 실행 ( 첫 번째 질문 실행 )
@app.route('/question', methods=['POST'])
def post_question():
    question = generate_level1_question()
    return jsonify({"question": question, "level": 1})

# /question/level2 접근 시 실행 ( 첫 번째 질문의 답변과 레벨을 받으며 다음 질문을 생성 )
@app.route('/question/level2', methods=['POST'])
def level2_question():
    data = request.get_json() # 요청받은 json을 저장함 ( 레벨 및 답변 )
    userQ = data['level1_question']
    userA = data['level1_answer']

    userQA['userQuestion'].append(userQ)
    userQA['userAnswer'].append(userA)

    question = generate_level2_question(userQ, userA) # 답변을 기반으로 질문 생성
    return jsonify({'question': question}) # 다음 레벨의 질문을 리턴시킨 후 출력

# /question/level3 접근 시 실행 ( 두 번째 질문의 답변과 레벨을 받으며 다음 질문을 생성 )
@app.route('/question/level3', methods=['POST'])
def level3_question():
    data = request.get_json()
    userQ = data['level2_question']
    userA = data['level2_answer']

    userQA['userQuestion'].append(userQ+',')
    userQA['userAnswer'].append(userA)

    question = generate_level3_question(userQ, userA)
    return jsonify({'question': question})

# 동일
@app.route('/question/level4', methods=['POST'])
def level4_question():
    data = request.get_json()
    userQ = data['level3_question']
    userA = data['level3_answer']

    userQA['userQuestion'].append(userQ)
    userQA['userAnswer'].append(userA)

    question = generate_level4_question(userQ, userA)
    return jsonify({'question': question})

# 동일
@app.route('/question/level5', methods=['POST'])
def level5_question():
    data = request.get_json()
    userQ = data['level4_question']
    userA = data['level4_answer']

    userQA['userQuestion'].append(userQ)
    userQA['userAnswer'].append(userA)

    question = generate_level5_question(userQ, userA)
    return jsonify({'question': question})

@app.route('/question/level6', methods=['POST'])
def level6_question():
    data = request.get_json()
    userQ = data['level5_question']
    userA = data['level5_answer']
    userEmail = data['userEmail']
    
    userQA['userEmail'].append(userEmail)
    userQA['userQuestion'].append(userQ)
    userQA['userAnswer'].append(userA)

    conn = get_db_connection()
    cursor = conn.cursor()

    current_date = datetime.now().strftime('%Y-%m-%d')

    question_insert_query = """
        INSERT INTO Question (Question1, Question2, Question3, Question4, Question5, created_at, memberEmail)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(question_insert_query, (
        userQA['userQuestion'][0],
        userQA['userQuestion'][1],
        userQA['userQuestion'][2],
        userQA['userQuestion'][3],
        userQA['userQuestion'][4],
        current_date,
        userEmail
    ))

    answer_insert_query = """
        INSERT INTO Answer (Answer1, Answer2, Answer3, Answer4, Answer5, created_at, memberEmail)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(answer_insert_query, (
        userQA['userAnswer'][0],
        userQA['userAnswer'][1],
        userQA['userAnswer'][2],
        userQA['userAnswer'][3],
        userQA['userAnswer'][4],
        current_date,
        userEmail
    ))

    image_url = generate_image()
    image_data = download_image(image_url)
    if image_data:
        save_image_to_db(image_data, image_url, userEmail, conn)
    
    # reset_userQA()

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"question": ""})

@app.route('/get_image', methods=['GET'])
def get_image_route():
    userEmail = request.args.get('userEmail')
    created_at = request.args.get('created_at')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT ImageData FROM Image WHERE memberEmail = %s AND created_at = %s"
    cursor.execute(query, (userEmail, created_at))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if result:
        return send_file(BytesIO(result[0]), mimetype='image/jpeg')
    else:
        return jsonify({"error": "Image not found"}), 404

@app.route('/get_qa', methods=['POST'])
def get_qa_route():
    data = request.get_json()
    memberEmail = data.get('memberEmail')
    created_at = data.get('created_at')
    
    if not memberEmail or not created_at:
        return jsonify({"error": "memberEmail and created_at are required"}), 400

    questions, answers = get_questions_and_answers(memberEmail, created_at)
    
    if not questions or not answers:
        return jsonify({"error": "No data found"}), 404

    response = {
        "questions": list(questions),
        "answers": list(answers)
    }

    return jsonify(response), 200

# ------------------- 질문,답변 및 반환 API 끝 -------------------

@app.route('/userqa', methods=['GET'])
def responseUserQA():
    return jsonify(userQA)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5001")
