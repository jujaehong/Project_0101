import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_year = pd.read_csv('df_total',index_col=0)

def run_app_3소분류():
    
    
    if  st.header('불량유형 소분류별 A/S 접수 데이터') :

        # 체크박스로 표시할 년도 목록 생성
        소분류_list = sorted(df_year['불량유형_소'].unique(), reverse=False) #sorted()함수로 오름차순 정력

        # 체크박스로 선택된 소분류 목록 가져오기
        all_소분류_selected = st.checkbox("모든 소분류 유형 선택")

        if all_소분류_selected:
            selected_소분류_list = 소분류_list
        else:
            selected_소분류_list = st.multiselect('소분류 선택', 소분류_list)

        # 선택된 소분류에 해당하는 데이터프레임 필터링
        if not all_소분류_selected and len(selected_소분류_list) == 0:
            filtered_소분류_df = pd.DataFrame()  # 빈 데이터프레임 생성
        else:
            filtered_소분류_df = df_year.loc[df_year['불량유형_대'].isin(selected_소분류_list)]

        # 선택된 년도에 해당하는 데이터프레임 필터링
        filtered_소분류_df = df_year.loc[df_year['불량유형_소'].isin(selected_소분류_list)]

        # 필터링된 데이터프레임 출력
        st.dataframe(filtered_소분류_df)        

        # 분류된 데이터프레임의 개수 출력
        st.write("데이터프레임 개수:", len(filtered_소분류_df))

        # 선택된 소분류별 개수 데이터프레임 생성
        count_df = pd.DataFrame({'불량유형_소': selected_소분류_list})
        count_df['데이터 개수'] = count_df['불량유형_소'].apply(lambda year: filtered_소분류_df.loc[filtered_소분류_df['불량유형_소'] == year].shape[0])


        # 데이터 개수를 내람차순으로 정렬
        count_df = count_df.sort_values('데이터 개수', ascending=False)

        # 갯수의 합계 계산하여 추가
        count_df.loc['합계'] = ['', count_df['데이터 개수'].sum()]

        st.dataframe(count_df)

        # 소분류별 Count Plot 그리기
        if not filtered_소분류_df.empty:
            st.set_option('deprecation.showPyplotGlobalUse', False)
            plt.figure(figsize=(8, 6))


            # 데이터 개수를 내림차순으로 정렬한 순서로 그래프 그리기 (count_df 데이터프레임에서 합계행 제외시킴)
            order = count_df[count_df.index != '합계']['불량유형_소'].values.tolist()
            sns.countplot(data=filtered_소분류_df, x='불량유형_소', order=order)


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
    