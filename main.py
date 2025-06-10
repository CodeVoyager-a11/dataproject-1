import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 제목
st.title("최근 10년간 시·구별 고등학교 대입률")

# 데이터 로드
uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # 연도는 인덱스로 설정
    df.set_index("연도", inplace=True)
    
    # 시·구 선택
    options = st.multiselect(
        "확인할 시·구를 선택하세요:",
        options=df.columns,
        default=list(df.columns)
    )

    if options:
        # 선택한 시·구의 데이터만 추출
        selected_data = df[options]

        # 선그래프 출력
        st.line_chart(selected_data)
    else:
        st.warning("하나 이상의 시·구를 선택해주세요.")
else:
    st.info("CSV 파일을 업로드해주세요. 첫 열은 '연도', 이후는 시·구명이 되어야 합니다.")

