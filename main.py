import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium


# 고등학교 대입률 데이터
data = {
    '연도': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    '고등학교_대입률': [70.8, 69.8, 68.9, 69.7, 70.4, 72.5, 73.7, 73.3, 72.8, 73.6]
}
df = pd.DataFrame(data)

# 앱 제목
st.title("최근 10년간 고등학교 대입률")

# 선그래프 출력
st.line_chart(df.set_index('연도'))

# 데이터 테이블 보기
st.write("### 원본 데이터", df)

