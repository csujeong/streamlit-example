from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Streamlit! 첫번째 테스트

`/streamlit_app.py` 소스를 편집해서 이 앱을 원하는 대로 맞춤설정하세요 :heart:

궁금한 점이 있으면 [설명서](https://docs.streamlit.io) 와 [community
forums](https://discuss.streamlit.io) 을 확인해보세요~~^^

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
