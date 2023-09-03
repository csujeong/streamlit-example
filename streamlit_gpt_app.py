from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Streamlit! 첫번째 테스트

다음은 단 몇 줄의 코드로 수행할 수 있는 작업의 예입니다.:
"""


with st.echo(code_location='below'):
    total_points = st.slider("나선형의 포인트 수", 1, 5000, 2000)
    num_turns = st.slider("나선형의 회전수", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

# =========================================================
# env 파일을 사용하기 위한 라이브러리 import
#from dotenv import load_dotenv
#load_dotenv()

# langchain, chat 모드 사용
from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()

# Llama 사용
# from langchain.llms import CTransformers
# lim = CTransformers(
#     model ="llama-2-7b-chat.ggmlv3.q6_K.bin",
#     model_type = "llama"
# )

# streamlit으로 Frontend 만들기
import streamlit as st
from PIL import Image

# 화면 상단 여백 제거
st.write("<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)

# 웹페이지 제목
st.title("AI & Poem")
st.markdown("### Your Topics, Our AI Poems")

# 그림 삽입
col1, col2, col3 = st.columns([0.25, 0.5, 0.25])
with col2:
#    img = Image.open("AI-Poet.png")
    img = Image.open("britychat.png")
    to st.image(img)

# 시 주제 입력 받음
content = st.text_input("시의 주제를 제시해 주세요")

# 시 작성
if st.button('시 작성 요청'):
    with st.spinner('시 작성 중... 잠시만 기다려 주세요'):
        result  = chat_model.predict(content + "에 대한 시를 써주세요")
        st.write(result)

# 수익화
from streamlit_extras.buy_me_a_coffee import button
button(username="jakukyr", floating=True, width=221)
