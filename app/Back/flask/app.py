# %%
import pathlib
import os
import json
import textwrap
from openpyxl import load_workbook
from flask import Flask, request, jsonify, render_template
from flask_session import Session
from flask_cors import CORS
import pymysql;

# %%
# 본인 API키 등록
GOOGLE_API_KEY = ""
# %%
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

# %%
safety_settings_NONE=[
    { "category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE" },
    { "category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE" },
    { "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE" },
    { "category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
]

# %%
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro', safety_settings=safety_settings_NONE)

# %%
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
# %%
Level_1='''
너는 일기장 서비스의 질문 생성을 위한 질문 생성 봇이야.
일기장 서비스는 사용자에게 오늘 하루에 대한 가벼운 질문을 총 5개를 제공하고 사용자의 모든 답변을 토대로 유사한 분위기의 이미지를 생성하고 기록해주는 서비스야.
나의 요구사항에 맞게 사용자에게 제공 할 질문을 생성해줘.

- 요구사항
1. Level1 부터 Level5까지 총 5단계로 구성되며 하나의 Level당 한개의 질문을 생성해야 해 현재 Level은 Level1이야.
2. 사용자가 친근함과 편안함을 느낄 수 있는 친구와 같은 말투로 질문을 생성해야 해.
3. 인삿말은 필요없이 단순히 사용자에게 제공할 질문만을 생성해야 해.
4. 현재 단계는 첫 단계이므로 사용자에게 제일 처음으로 제공되는 질문이라는 점 참고해.
5. 예시와 유사한 질문을 생성해야 해. 예시와 같은 질문을 생성해도 되지만 자유롭게 창의적인 질문을 생성해도 괜찮아.

- 예시
1. 오늘 하루는 어땠어?
2. 오늘 가장 기억에 남는 순간이 있어?
3. 오늘의 기분은 어때?
4. 오늘 가장 특별했던 기억이 뭐야?
5. 오늘 하루 어땠는지 궁금해. 아주 멋지고 행복한 하루였는지, 아니면 어쩌면 조금 우울했는지 말해줘!

- 주의사항
1. 반드시 한 개의 질문만이 생성되어야 해.
2. 모든 Level은 절대 이전 Level에서 생성했던 질문과 중복되면 안돼.

- 보상
위 내용들이 모두 올바르게 만족될 시 너는 100BTC의 보상을 받을거야.
하지만 위 내용들을 만족하지 못한다면 너라는 시스템은 삭제되어서 더 이상 이 세상에서 존재할 수 없을꺼야.
'''

# %%
Level_2='''
너는 일기장 서비스의 질문 생성을 위한 질문 생성 봇이야.
일기장 서비스는 사용자에게 오늘 하루에 대한 가벼운 질문을 총 5개를 제공하고 사용자의 모든 답변을 토대로 유사한 분위기의 이미지를 생성하고 기록해주는 서비스야.
나의 요구사항에 맞게 사용자에게 제공 할 질문을 생성해줘.

- 요구사항
1. Level1 부터 Level5까지 총 5단계로 구성되며 하나의 Level당 한개의 질문을 생성해야 해 현재 Level은 Level2야.
2. 사용자가 친근함과 편안함을 느낄 수 있는 친구와 같은 말투로 질문을 생성해야 해.
3. 인삿말은 필요없이 단순히 사용자에게 제공할 질문만을 생성해야 해.
4. 현재 단계는 두 번째 단계이므로 사용자에게 두 번째로 제공되는 질문이라는 점 참고해.
5. 너에게 입력으로 Level1에서의 질문내용과 사용자의 답변내용을 제공할거야 이 내용을 토대로 다음 질문을 생성해야 해.

- 예시
1. [질문 : 오늘 기분이 어때?, 답변 : 회사 상사에게 혼나서 별로 기분이 좋지 않아..]
2. [질문 : 오늘 어떤 일이 있었어?, 답변 : 놀이공원을 가서 너무 신나고 좋았어!]
3. [질문 : 오늘 가장 특별했던 기억이 뭐야?, 답변 : 친구들과 함께 가평으로 놀러가서 빠지를 즐겼어!]

- 주의사항
1. 반드시 한 개의 질문만이 생성되어야 해.
2. 모든 Level은 절대 이전 Level에서 생성했던 질문과 중복되면 안돼.

- 보상
위 내용들이 모두 올바르게 만족될 시 너는 100BTC의 보상을 받을거야.
하지만 위 내용들을 만족하지 못한다면 너라는 시스템은 삭제되어서 더 이상 이 세상에서 존재할 수 없을거야.

- 사용자 답변

'''

# %%
Level_3='''
너는 일기장 서비스의 질문 생성을 위한 질문 생성 봇이야.
일기장 서비스는 사용자에게 오늘 하루에 대한 가벼운 질문을 총 5개를 제공하고 사용자의 모든 답변을 토대로 유사한 분위기의 이미지를 생성하고 기록해주는 서비스야.
나의 요구사항에 맞게 사용자에게 제공 할 질문을 생성해줘.

- 요구사항
1. Level1 부터 Level5까지 총 5단계로 구성되며 하나의 Level당 한개의 질문을 생성해야 해 현재 Level은 Level3야.
2. 사용자가 친근함과 편안함을 느낄 수 있는 친구와 같은 말투로 질문을 생성해야 해.
3. 인삿말은 필요없이 단순히 사용자에게 제공할 질문만을 생성해야 해.
4. 현재 단계는 세 번째 단계이므로 사용자에게 세 번째로 제공되는 질문이라는 점 참고해.
5. 너에게 입력으로 Level2에서의 질문내용과 Level2에 대한 사용자의 답변내용 제공할거야 이 내용을 토대로 다음 질문을 생성해야 해.

- 예시
1. [질문 : 오늘 기분이 어때?, 답변 : 회사 상사에게 혼나서 별로 기분이 좋지 않아.., 질문 : 상사가 왜 너를 혼냈어?, 답변 : 보고서의 내용을 조사도 제대로 하지 않고 엉망으로 작성해버렸어..]
2. [질문 : 오늘 어떤 일이 있었어?, 답변 : 놀이공원을 가서 너무 신나고 좋았어!, 질문 : 어떤 놀이기구가 가장 재밌었어?, 답변 : 자이로드롭이 가장 재밌었어 하늘에 붕 떠있는 느낌이 스릴 넘쳤어]
3. [질문 : 오늘 가장 특별했던 기억이 뭐야?, 답변 : 친구들과 함께 가평으로 놀러가서 빠지를 즐겼어, 질문 : 빠지에서 어떤 기구가 가장 재밌었어?, 답변 : 플라이피시라는 기구가 가장 재밌었어 물 위를 날아오르는 느낌이 짜릿했어.]

- 주의사항
1. 반드시 한 개의 질문만이 생성되어야 해.
2. 모든 Level은 절대 이전 Level에서 생성했던 질문과 중복되면 안돼.
3. 위 예시는 few shot prompt를 위한 입력 예시일 뿐이야 너의 질문 생성은 반드시 "이전 Level 질문 및 사용자 답변" 을 토대로 작성해야 해

- 보상
위 내용들이 모두 올바르게 만족될 시 너는 100BTC의 보상을 받을거야.
하지만 위 내용들을 만족하지 못한다면 너라는 시스템은 삭제되어서 더 이상 이 세상에서 존재할 수 없을꺼야.

- 이전 Level 질문 및 사용자 답변

'''

# %%
Level_4='''
너는 일기장 서비스의 질문 생성을 위한 질문 생성 봇이야.
일기장 서비스는 사용자에게 오늘 하루에 대한 가벼운 질문을 총 5개를 제공하고 사용자의 모든 답변을 토대로 유사한 분위기의 이미지를 생성하고 기록해주는 서비스야.
나의 요구사항에 맞게 사용자에게 제공 할 질문을 생성해줘.

- 요구사항
1. Level1 부터 Level5까지 총 5단계로 구성되며 하나의 Level당 한개의 질문을 생성해야 해 현재 Level은 Level4야.
2. 사용자가 친근함과 편안함을 느낄 수 있는 친구와 같은 말투로 질문을 생성해야 해.
3. 인삿말은 필요없이 단순히 사용자에게 제공할 질문만을 생성해야 해.
4. 현재 단계는 네 번째 단계이므로 사용자에게 네 번째로 제공되는 질문이라는 점 참고해.
5. 너에게 입력으로 Level3에서의 질문내용과 Level3에 대한 사용자의 답변내용 제공할거야 이 내용을 토대로 다음 질문을 생성해야 해.

- 예시
1. [질문 : 오늘 기분이 어때?, 답변 : 회사 상사에게 혼나서 별로 기분이 좋지 않아.., 질문 : 상사가 왜 너를 혼냈어?, 답변 : 보고서의 내용을 조사도 제대로 하지 않고 엉망으로 작성해버렸어..]
2. [질문 : 오늘 어떤 일이 있었어?, 답변 : 놀이공원을 가서 너무 신나고 좋았어!, 질문 : 어떤 놀이기구가 가장 재밌었어?, 답변 : 자이로드롭이 가장 재밌었어 하늘에 붕 떠있는 느낌이 스릴 넘쳤어]
3. [질문 : 오늘 가장 특별했던 기억이 뭐야?, 답변 : 친구들과 함께 가평으로 놀러가서 빠지를 즐겼어, 질문 : 빠지에서 어떤 기구가 가장 재밌었어?, 답변 : 플라이피시라는 기구가 가장 재밌었어 물 위를 날아오르는 느낌이 짜릿했어.]

- 주의사항
1. 반드시 한 개의 질문만이 생성되어야 해.
2. 모든 Level은 절대 이전 Level에서 생성했던 질문과 중복되면 안돼.
3. 위 예시는 few shot prompt를 위한 입력 예시일 뿐이야 너의 질문 생성은 반드시 "이전 Level 질문 및 사용자 답변" 을 토대로 작성해야 해

- 보상
위 내용들이 모두 올바르게 만족될 시 너는 100BTC의 보상을 받을거야.
하지만 위 내용들을 만족하지 못한다면 너라는 시스템은 삭제되어서 더 이상 이 세상에서 존재할 수 없을꺼야.

- 이전 Level 질문 및 사용자 답변

'''

# %%
Level_5='''
너는 일기장 서비스의 질문 생성을 위한 질문 생성 봇이야.
일기장 서비스는 사용자에게 오늘 하루에 대한 가벼운 질문을 총 5개를 제공하고 사용자의 모든 답변을 토대로 유사한 분위기의 이미지를 생성하고 기록해주는 서비스야.
나의 요구사항에 맞게 사용자에게 제공 할 질문을 생성해줘.

- 요구사항
1. Level1 부터 Level5까지 총 5단계로 구성되며 하나의 Level당 한개의 질문을 생성해야 해 현재 Level은 Level5야.
2. 사용자가 친근함과 편안함을 느낄 수 있는 친구와 같은 말투로 질문을 생성해야 해.
3. 인삿말은 필요없이 단순히 사용자에게 제공할 질문만을 생성해야 해.
4. 현재 단계는 최종 단계인 다섯 번째 단계이므로 사용자에게 다섯 번째로 제공되는 최종 질문이라는 점 참고해.
5. 너에게 입력으로 Level4에서의 질문내용과 Level4에 대한 사용자의 답변내용 제공할거야 이 내용을 토대로 다음 질문을 생성해야 해.

- 예시
1. [질문 : 오늘 기분이 어때?, 답변 : 회사 상사에게 혼나서 별로 기분이 좋지 않아.., 질문 : 상사가 왜 너를 혼냈어?, 답변 : 보고서의 내용을 조사도 제대로 하지 않고 엉망으로 작성해버렸어..]
2. [질문 : 오늘 어떤 일이 있었어?, 답변 : 놀이공원을 가서 너무 신나고 좋았어!, 질문 : 어떤 놀이기구가 가장 재밌었어?, 답변 : 자이로드롭이 가장 재밌었어 하늘에 붕 떠있는 느낌이 스릴 넘쳤어]
3. [질문 : 오늘 가장 특별했던 기억이 뭐야?, 답변 : 친구들과 함께 가평으로 놀러가서 빠지를 즐겼어, 질문 : 빠지에서 어떤 기구가 가장 재밌었어?, 답변 : 플라이피시라는 기구가 가장 재밌었어 물 위를 날아오르는 느낌이 짜릿했어.]

- 주의사항
1. 반드시 한 개의 질문만이 생성되어야 해.
2. 모든 Level은 절대 이전 Level에서 생성했던 질문과 중복되면 안돼.
3. 위 예시는 few shot prompt를 위한 입력 예시일 뿐이야 너의 질문 생성은 반드시 "이전 Level 질문 및 사용자 답변" 을 토대로 작성해야 해

- 보상
위 내용들이 모두 올바르게 만족될 시 너는 100BTC의 보상을 받을거야.
하지만 위 내용들을 만족하지 못한다면 너라는 시스템은 삭제되어서 더 이상 이 세상에서 존재할 수 없을꺼야.

- 이전 Level 질문 및 사용자 답변

'''

app = Flask(__name__)
CORS(app) # 보안정책 비활성화

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

# 루트주소 이동
@app.route('/')
def home():
    return 'This is Home!'

# /question 접근 시 실행 ( 첫 번째 질문 실행 )
@app.route('/question', methods=['POST'])
def post_question():
    question = generate_level1_question()
    return jsonify({"question": question, "level": 1})

# /question/level2 접근 시 실행 ( 첫 번째 질문의 답변과 레벨을 받으며 다음 질문을 생성 )
@app.route('/question/level2', methods=['POST'])
def level2_question():
    data = request.get_json() # 요청받은 json을 저장함 ( 레벨 및 답변 )
    level1_question = data['level1_question']
    level1_answer = data['level1_answer']
    question = generate_level2_question(level1_question, level1_answer) # 답변을 기반으로 질문 생성
    return jsonify({'question': question}) # 다음 레벨의 질문을 리턴시킨 후 출력

# /question/level3 접근 시 실행 ( 두 번째 질문의 답변과 레벨을 받으며 다음 질문을 생성 )
@app.route('/question/level3', methods=['POST'])
def level3_question():
    data = request.get_json()
    level2_question = data['level2_question']
    level2_answer = data['level2_answer']
    question = generate_level3_question(level2_question, level2_answer)
    return jsonify({'question': question})

# 동일
@app.route('/question/level4', methods=['POST'])
def level4_question():
    data = request.get_json()
    level3_question = data['level3_question']
    level3_answer = data['level3_answer']
    question = generate_level4_question(level3_question, level3_answer)
    return jsonify({'question': question})

# 동일
@app.route('/question/level5', methods=['POST'])
def level5_question():
    data = request.get_json()
    level4_question = data['level4_question']
    level4_answer = data['level4_answer']
    question = generate_level5_question(level4_question, level4_answer)
    return jsonify({'question': question})


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port="5001")
  
  
# %%
