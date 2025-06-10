import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 제목
st.title("최근 10년간 취업률 선그래프")

# 가상의 데이터 생성 (실제 데이터를 사용할 경우 여기만 수정하면 됨)
years = list(range(2015, 2025))
employment_rates = [65.2, 66.1, 67.0, 67.8, 68.3, 66.5, 65.9, 67.2, 68.0, 68.5]

# 데이터프레임 생성
df = pd.DataFrame({
    '연도': years,
    '취업률 (%)': employment_rates
})

# 선그래프 그리기
st.line_chart(df.set_index('연도'))

# 참고: 실제 데이터를 사용하려면 아래처럼 불러오세요.
# df = pd.read_csv("employment_data.csv")

