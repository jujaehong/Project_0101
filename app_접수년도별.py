import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'  # 폰트 이름을 적절하게 변경하세요
import seaborn as sns



def run_app_접수년도별():

    file_uploader1 = st.file_uploader('접수데이터', key='file_uploader1')

    if file_uploader1 is not None:
        df_a = pd.read_csv(file_uploader1)
        st.dataframe(df_a)
        
        st.header('접수년도별 A/S 접수 데이터')
        # 년도 추출하여 새로운 컬럼 추가
        df_a["접수년"] = pd.to_datetime(df_a['접수일자']).dt.year
        # 체크박스로 표시할 년도 목록 생성
        접수_years_list = df_a['접수년'].unique()
        접수_years_list = sorted(접수_years_list, reverse=False)
        # 체크박스로 선택된 년도 목록 가져오기
        selected_접수_years = st.multiselect('접수년도 선택', 접수_years_list)
        # 선택된 년도에 해당하는 데이터프레임 필터링
        filtered_접수_df = df_a.loc[df_a['접수년'].isin(selected_접수_years)]
        # 필터링된 데이터프레임 출력
        st.dataframe(filtered_접수_df)        
        # 선택된 연도별 개수 데이터프레임 생성
        count_df = pd.DataFrame({'접수년': selected_접수_years})
        count_df['데이터 개수'] = count_df['접수년'].apply(lambda year: filtered_접수_df.loc[filtered_접수_df['접수년'] == year].shape[0])
        # 갯수의 합계 계산하여 추가
        count_df.loc['합계'] = ['', count_df['데이터 개수'].sum()]
        # 데이터프레임 가로 넓이 설정
        count_df_style = count_df.style.set_table_attributes("style='width:100%;'")
        st.dataframe(count_df_style)

        # 접수년도별 Count Plot 그리기
        if not filtered_접수_df.empty:
            st.set_option('deprecation.showPyplotGlobalUse', False)
            plt.figure(figsize=(8, 6))
            sns.countplot(data=filtered_접수_df, x='접수년')
            plt.xlabel('접수년도')
            plt.ylabel('접수건수')
            plt.title('접수년도별 A/S 접수건수')
            plt.tight_layout()

            # 그래프를 이미지로 변환하여 앱 대시보드에 표시
            st.write("접수년도별 개수 그래프:")
            st.pyplot()


        if not filtered_접수_df.empty:
            # 접수년도별 점유율 계산
            plt.figure(figsize=(10,6))
            접수년_counts = filtered_접수_df['접수년'].value_counts()
            labels = 접수년_counts.index.tolist()
            sizes = 접수년_counts.values.tolist()
            # 파이 그래프 그리기
            plt.pie(sizes, labels=labels, autopct='%1.1f%%')
            # 그래프 제목 설정
            plt.title('접수년별 불량율 접수 데이터')
            # 그래프 출력
            st.pyplot(plt)

    else:
        st.write('파일을 업로드해주세요.')

