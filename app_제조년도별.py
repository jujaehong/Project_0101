import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'  # 폰트 이름을 적절하게 변경하세요
import seaborn as sns



def run_app_제조년도별():

    df_year = pd.read_csv('df_year',index_col=0)

        
    if  st.header('제조년도별 A/S 접수 데이터') :

        # 체크박스로 표시할 년도 목록 생성
        제조_years_list = sorted(df_year['제조년'].unique(), reverse=False) #sorted()함수로 오름차순 정력

        # 체크박스로 선택된 년도 목록 가져오기
        selected_제조_years = st.multiselect('제조년도 선택', 제조_years_list)

        # 선택된 년도에 해당하는 데이터프레임 필터링
        filtered_df = df_year.loc[df_year['제조년'].isin(selected_제조_years)]

        # 필터링된 데이터프레임 출력
        st.dataframe(filtered_df)        

        # 선택된 연도별 개수 데이터프레임 생성
        count_df = pd.DataFrame({'제조년': selected_제조_years})
        count_df['데이터 개수'] = count_df['제조년'].apply(lambda year: filtered_df.loc[filtered_df['제조년'] == year].shape[0])

        # 갯수의 합계 계산하여 추가
        count_df.loc['합계'] = ['', count_df['데이터 개수'].sum()]


        # 제조년도별 Count Plot 그리기
        if not filtered_df.empty:
            st.set_option('deprecation.showPyplotGlobalUse', False)
            plt.figure(figsize=(8, 6))
            sns.countplot(data=filtered_df, x='제조년')
            plt.xlabel('제조년도')
            plt.ylabel('접수건수')
            plt.title('제조년도별 A/S 접수건수')
            plt.tight_layout()

            # 그래프를 이미지로 변환하여 앱 대시보드에 표시
            st.write("제조년도별 개수 그래프:")
            st.pyplot()


        if not filtered_df.empty :
            # 제조년도별 점유율 계산
            plt.figure(figsize=(10,6))
            제조년_counts = filtered_df['제조년'].value_counts()
            labels = 제조년_counts.index.tolist()
            sizes = 제조년_counts.values.tolist()
            # 파이 그래프 그리기
            plt.pie(sizes, labels=labels, autopct='%1.1f%%')
            # 그래프 제목 설정
            plt.title('제조년별 불량율 접수 데이터')
            # 그래프 출력
            st.pyplot(plt)



