# import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




df_year = pd.read_csv('df_total.csv',index_col=0)

def run_app_접수년도별():


        
    if  st.header('접수년도별 A/S 접수 데이터') :
        st.markdown("<br>", unsafe_allow_html=True)  # 줄 간격 추가
        st.markdown("<br>", unsafe_allow_html=True)  # 줄 간격 추가

        # 체크박스로 표시할 년도 목록 생성
        접수_years_list = sorted(df_year['접수년'].unique(), reverse=False) #sorted()함수로 오름차순 정력

        st.error('전체 데이터를 보려면 아래 체크박스를 체크하세요!')

        # 체크박스로 선택된 접수년도 목록 가져오기
        all_접수_selected = st.checkbox("ALL 데이터 보기")
        st.markdown("<br>", unsafe_allow_html=True)  # 줄 간격 추가
        
        if not all_접수_selected:
            selection_label = "**특정 접수년도 데이터만 보고 싶을 경우 아래에서 선택하세요**"
            selected_접수_list = st.multiselect(selection_label + ":", 접수_years_list, default=[])
            if len(selected_접수_list) == 0:
                st.stop()  # 데이터프레임과 그래프를 표시하지 않고 종료

        else:
            selected_접수_list = 접수_years_list

        # 선택된 접수년도에 해당하는 데이터프레임 필터링
        if not all_접수_selected and len(selected_접수_list) == 0:
            filtered_접수_df = pd.DataFrame()  # 빈 데이터프레임 생성
        else:
            filtered_접수_df = df_year.loc[df_year['접수년'].isin(selected_접수_list)]

        # 필터링된 데이터프레임 출력
        st.dataframe(filtered_접수_df)        

        # 선택된 연도별 개수 데이터프레임 생성
        count_df = pd.DataFrame({'접수년': selected_접수_list})
        count_df['데이터 개수'] = count_df['접수년'].apply(lambda year: filtered_접수_df.loc[filtered_접수_df['접수년'] == year].shape[0])

        # 갯수의 합계 계산하여 추가
        count_df.loc['합계'] = ['', count_df['데이터 개수'].sum()]

        st.dataframe(count_df) 

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

