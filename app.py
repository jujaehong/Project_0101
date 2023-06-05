import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler
# sklean.preprocessing은 데이터 전처리 관련
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from app_홈 import run_app_홈
from app_제조년도별 import run_app_제조년도별
from app_접수년도별 import run_app_접수년도별
from app_1대분류 import run_app_1대분류
from app_2중분류 import run_app_2중분류
from app_3소분류 import run_app_3소분류
from app_불량원인 import run_app_불량원인



def main():

    menu = ['Home', '기간별분석', '유형별분석', '불량원인']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0]:
        run_app_홈()

    
    elif choice == menu[1]:
        menu1 = ['제조년도별 데이터분석', '접수년도별 데이터분석']
        choice1 = st.sidebar.selectbox('세부', menu1)
        if choice1 == menu1[0]:
            run_app_제조년도별()
        elif choice1 == menu1[1]:
            run_app_접수년도별()
    
    
    elif choice == menu[2]:
        menu2 = ['대분류 유형 데이터분석', '중분류 유형 데이터분석', '소분류 유형 데이터분석']
        choice2 = st.sidebar.selectbox('세부', menu2)
        if choice2 == menu2[0]:
            run_app_1대분류()
            pass
        elif choice2 == menu2[1]:
            run_app_2중분류()
            pass
        elif choice2 == menu2[2]:
            run_app_3소분류()
            pass
        
    elif choice == menu[3]:
        run_app_불량원인()



if __name__ == '__main__':
    main()


