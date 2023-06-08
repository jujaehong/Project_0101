import streamlit as st
import pandas as pd
# from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import MinMaxScaler
# sklean.preprocessing은 데이터 전처리 관련
# from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
# import io
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
from app_홈 import run_app_홈
from app_제조년도별 import run_app_제조년도별
from app_접수년도별 import run_app_접수년도별
from app_1대분류 import run_app_1대분류
from app_2중분류 import run_app_2중분류
from app_3소분류 import run_app_3소분류
from app_불량원인 import run_app_불량원인
from app_부품공급업체 import run_app_부품공급업체
from app_수리부품 import run_app_수리부품



def main():
    
    # st.sidebar.image('https://littledeep.com/wp-content/uploads/2020/09/tv-illustration-free-download.png', use_column_width=True)
    
    menu = ['Home', '기간별분석', '유형별분석', '불량원인', '수리부품별 부품공급업체']
    
    
    with st.sidebar:
        choice = option_menu("메뉴", ['Home', '기간별분석', '유형별분석', '불량원인', '수리부품별 부품공급업체'],
                            icons=['bi bi-arrow-down-circle-fill', 'bi bi-calendar2-date', 'kanban', 'kanban', 'kanban'],
                            menu_icon="app-indicator", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},})


    if choice == menu[0]:
        run_app_홈()

    
    elif choice == menu[1]:
        menu1 = ['제조년도별 데이터분석', '접수년도별 데이터분석']
     
        with st.sidebar:
            choice1 = option_menu("세부", ['제조년도별 데이터분석', '접수년도별 데이터분석'],
                                icons=['bi bi-calendar2-date', 'bi bi-calendar2-date'],
                                menu_icon="app-indicator", default_index=0,
                                styles={
                "container": {"padding": "5!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "15px"}, 
                "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#02ab21"},})
 
        if choice1 == menu1[0]:
            run_app_제조년도별()
        elif choice1 == menu1[1]:
            run_app_접수년도별()
    
    
    elif choice == menu[2]:
        menu2 = ['대분류 유형 데이터분석', '중분류 유형 데이터분석', '소분류 유형 데이터분석']
        
        # choice2 = st.sidebar.selectbox('세부', menu2)
        
        with st.sidebar:
            choice2 = option_menu("세부", ['대분류 유형 데이터분석', '중분류 유형 데이터분석', '소분류 유형 데이터분석'],
                                icons=['bi bi-arrow-down-circle-fill', 'kanban', 'kanban'],
                                menu_icon="app-indicator", default_index=0,
                                styles={
                "container": {"padding": "5!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "15px"}, 
                "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#02ab21"},})
        if choice2 == menu2[0]:
            run_app_1대분류()
            # pass
        elif choice2 == menu2[1]:
            run_app_2중분류()
            # pass
        elif choice2 == menu2[2]:
            run_app_3소분류()
            # pass
        
    elif choice == menu[3]:
        run_app_불량원인()

    elif choice == menu[4]:
        menu3 = ['수리부품별 데이터', '부품공급업체별 데잍터']
        with st.sidebar:
            choice3 = option_menu("세부", ['수리부품별 데이터', '부품공급업체별 데잍터'],
                                icons=['bi bi-arrow-down-circle-fill', 'kanban'],
                                menu_icon="app-indicator", default_index=0,
                                styles={
                "container": {"padding": "5!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "15px"}, 
                "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#02ab21"},})
 
        if choice3 == menu3[0]:
            run_app_수리부품()
        elif choice3 == menu3[1]:
            run_app_부품공급업체()
        


if __name__ == '__main__':
    main()


