import streamlit as st

def run_app_홈():

    st.markdown("<h1 style='text-align: center; font-size: 50px;'>A/접수 건수 불량 데이터 분석</h1>", unsafe_allow_html=True)
    
    img_url = 'https://littledeep.com/wp-content/uploads/2020/09/tv-illustration-free-download.png'
    st.markdown(f"<div style='width:100%; text-align:center;'><img src='{img_url}' width='40%'/></div>", unsafe_allow_html=True)
    # st.image(img_url)


    st.markdown("<h1 style='text-align: center; font-size: 20px;'>제품명 : 휴대용 스마트 TV _ 기획상품</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 20px;'>모델명 : SSAN-TV-4</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 15px;'>(A/S 데이터 수집기간 : 2021년 05월 01일부터 ~ 2023년 05월 31일까지)</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 15px;'>(총 수집 데이터 : 10,000개)</h1>", unsafe_allow_html=True)




# 참고 자료

    # st.warning('경고하고 싶을때 문장')
    # st.info('알림을 주고 싶을때')
    # st.error('문제가 발생했음을 알려주고 싶을때')

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns