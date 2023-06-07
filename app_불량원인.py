import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_year = pd.read_csv('df_total.csv',index_col=0)

# 경고 비활성화
st.set_option('deprecation.showPyplotGlobalUse', False)


def run_app_불량원인():
   
    if  st.header('불량유형 원인별 A/S 접수 데이터') :
        st.markdown("<br>", unsafe_allow_html=True)  # 줄 간격 추가
        st.markdown("<br>", unsafe_allow_html=True)  # 줄 간격 추가

        # 체크박스로 표시할 년도 목록 생성
        불량원인_list = sorted(df_year['원인'].unique(), reverse=False) #sorted()함수로 오름차순 정력
        st.error('전체 불량원인 유형 데이터를 보려면 체크')

        # 체크박스로 선택된 불량원인 목록 가져오기
        all_불량원인_selected = st.checkbox("모든 불량원인 선택")
        st.markdown("<br>", unsafe_allow_html=True)  # 줄 간격 추가

        if not all_불량원인_selected:
            selection_label = "**특정 불량원인 유형 데이터만 보고 싶을 경우 아래에서 선택하세요**"
            selected_불량원인_list = st.multiselect(selection_label + ":", 불량원인_list, default=[])
            if len(selected_불량원인_list) == 0:
                st.stop()  # 데이터프레임과 그래프를 표시하지 않고 종료
        
        else:
            selected_불량원인_list = 불량원인_list

        # 선택된 불량원인에 해당하는 데이터프레임 필터링
        if not all_불량원인_selected and len(selected_불량원인_list) == 0:
            filtered_불량원인_df = pd.DataFrame()  # 빈 데이터프레임 생성
        else:
            filtered_불량원인_df = df_year.loc[df_year['원인'].isin(selected_불량원인_list)]


        # 선택된 불량원인에 해당하는 데이터프레임 필터링
        filtered_불량원인_df = df_year.loc[df_year['원인'].isin(selected_불량원인_list)]

        # 필터링된 데이터프레임 출력
        st.dataframe(filtered_불량원인_df)        

        # 분류된 데이터프레임의 개수 출력
        st.write("데이터프레임 개수:", len(filtered_불량원인_df))

        # 선택된 원인별 개수 데이터프레임 생성
        count_df = pd.DataFrame({'원인': selected_불량원인_list})
        count_df['데이터 개수'] = count_df['원인'].apply(lambda year: filtered_불량원인_df.loc[filtered_불량원인_df['원인'] == year].shape[0])

        # 데이터 개수를 내람차순으로 정렬
        count_df = count_df.sort_values('데이터 개수', ascending=False)

        # 갯수의 합계 계산하여 추가
        count_df.loc['합계'] = ['', count_df['데이터 개수'].sum()]

        st.dataframe(count_df)

        # 불량원인별 Count Plot 그리기
        if not filtered_불량원인_df.empty:
            st.set_option('deprecation.showPyplotGlobalUse', False)
            plt.figure(figsize=(8, 6))

            # 데이터 개수를 내림차순으로 정렬한 순서로 그래프 그리기 (count_df 데이터프레임에서 합계행 제외시킴)
            order = count_df[count_df.index != '합계']['원인'].values.tolist()
            sns.countplot(data=filtered_불량원인_df, x='원인', order=order)

            plt.xlabel('원인')
            plt.xticks(rotation=45)
            plt.ylabel('접수건수')
            plt.title('불량원인별 A/S 접수건수')
            plt.tight_layout()
    
            # 그래프를 이미지로 변환하여 앱 대시보드에 표시
            st.write("불량원인 A/S 접수건수:")
            st.pyplot()


        if not filtered_불량원인_df.empty:
            # 불량원인별 점유율 계산
            plt.figure(figsize=(10,6))
            불량원인_counts = filtered_불량원인_df['원인'].value_counts()
            labels = 불량원인_counts.index.tolist()
            sizes = 불량원인_counts.values.tolist()
            # 파이 그래프 그리기
            plt.pie(sizes, labels=labels, autopct='%1.1f%%')
            # 그래프 제목 설정
            plt.title('불량원인별 불량율 접수 데이터')
            # 그래프 출력
            st.pyplot(plt)

    else:
        st.write('파일을 업로드해주세요.')


