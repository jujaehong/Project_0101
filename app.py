import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler
# sklean.preprocessing은 데이터 전처리 관련
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

def main():
    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴', menu)

    st.title('A/S접수에 의한 품질 데이터 분석')

    file_uploader1 = st.file_uploader('접수데이터', key='file_uploader1')
    
    st.header('A/S 접수 데이터')
    
    if  file_uploader1 is not None:
        df_a = pd.read_csv(file_uploader1)
        st.dataframe(df_a)

    
    # 제조년별 a/s접수 수량 보기
    st.subheader('최대 / 최소 데이터 확인하기')
    df_a['제조년'].value_counts().sort_index()
    column = st.selectbox('컬럼을 선택하세요.', df_a.columns[3:])
    st.text('최대 데이터')
    st.dataframe(df_a[df[column] == df_a[column].max()])

    # petal_length 컬럼을 정렬하고 싶다.
    # 오름차순정렬, 내림차순정렬 두가지 옵션 선택토록


    st.subheader('이 영역은 서브헤더 영역')
    st.success('성공했을때 나타내고 싶은 문장')
    st.warning('경고하고 싶을때 문장')
    st.info('알림을 주고 싶을때')
    st.error('문제가 발생했음을 알려주고 싶을때')   










if __name__ == '__main__':
    main()