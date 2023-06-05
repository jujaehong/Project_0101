import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def run_app_3소분류():
    file_uploader1 = st.file_uploader('접수데이터', key='file_uploader1')

    if file_uploader1 is not None:
        df_a = pd.read_csv(file_uploader1)
        st.dataframe(df_a)
        
        st.header('A/S유형 소분류 접수 데이터')
        # 체크박스로 표시할 년도 목록 생성
        소분류_list = df_a['불량유형_소'].unique()
        소분류_list = sorted(소분류_list, reverse=False)
        # 체크박스로 선택된 년도 목록 가져오기
        selected_소분류_list = st.multiselect('소분류 목록 선택', 소분류_list)
        # 선택된 년도에 해당하는 데이터프레임 필터링
        filtered_소분류_df = df_a.loc[df_a['불량유형_소'].isin(selected_소분류_list)]
        # 필터링된 데이터프레임 출력
        st.dataframe(filtered_소분류_df)        
        # 선택된 연도별 개수 데이터프레임 생성
        count_df = pd.DataFrame({'불량유형_소': selected_소분류_list})
        count_df['데이터 개수'] = count_df['불량유형_소'].apply(lambda year: filtered_소분류_df.loc[filtered_소분류_df['불량유형_소'] == year].shape[0])
        # 갯수의 합계 계산하여 추가
        count_df.loc['합계'] = ['', count_df['데이터 개수'].sum()]
        # 데이터프레임 가로 넓이 설정
        count_df_style = count_df.style.set_table_attributes("style='width:100%;'")
        st.dataframe(count_df_style)

        # 소분류별 Count Plot 그리기
        if not filtered_소분류_df.empty:
            st.set_option('deprecation.showPyplotGlobalUse', False)
            plt.figure(figsize=(8, 6))
            sns.countplot(data=filtered_소분류_df, x='불량유형_소')
            plt.xlabel('소분류')
            plt.ylabel('접수건수')
            plt.title('불량유형 소분류별 A/S 접수건수')
            plt.tight_layout()

            # 그래프를 이미지로 변환하여 앱 대시보드에 표시
            st.write("불량유형 소분류별 A/S 접수건수:")
            st.pyplot()


        if not filtered_소분류_df.empty:
            # 소분류도별 점유율 계산
            plt.figure(figsize=(10,6))
            소분류_counts = filtered_소분류_df['불량유형_소'].value_counts()
            labels = 소분류_counts.index.tolist()
            sizes = 소분류_counts.values.tolist()
            # 파이 그래프 그리기
            plt.pie(sizes, labels=labels, autopct='%1.1f%%')
            # 그래프 제목 설정
            plt.title('소분류별 불량율 접수 데이터')
            # 그래프 출력
            st.pyplot(plt)

    else:
        st.write('파일을 업로드해주세요.')
    