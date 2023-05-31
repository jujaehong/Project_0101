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
    st.title('인천광역시_숙박업소현황_202209')

    df = pd.read_csv('인천광역시_숙박업소현황_202209.csv') # 데이터 불러오기
    
    if st.button('데이터 보기') :
        st.dataframe(df)

    # petal_length 컬럼을 정렬하고 싶다.
    # 오름차순정렬, 내림차순정렬 두가지 옵션 선택토록

    status = st.radio('정렬을 선택하세요', ['오름차순','내림차순']) 
    
    if status == '오름차순' :
        st.dataframe(df.sort_values('객실수'))
    elif status == '내림차순' :
        st.dataframe(df.sort_values('객실수',ascending=False))
    
    # 데이터 프레임의 컬럼이름을 보여주고,
    # 유저가 컬럼을 선택하면
    # 해당컬럼만 가져와서 데이터프레임을 보여주고 싶다.

    # df.columns (컬럼 가져오기)  
    # multiselect 
    column_list = st.multiselect('컬럼을 선택하세요',df.columns)

    print(column_list)

    # 선택한 컬럼으로 데이터프레임 보여주기!
    st.dataframe(df[column_list])











if __name__ == '__main__':
    main()