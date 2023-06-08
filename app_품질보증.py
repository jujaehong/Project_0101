import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# 경고 비활성화
st.set_option('deprecation.showPyplotGlobalUse', False)

df_year = pd.read_csv('df_total.csv', index_col=0)

def run_app_품질보증():

    if st.header('품질 보증 내/외 데이터'):
        st.info('품질보증기간 : 1년 무상 서비스')
        st.markdown("<br><br>", unsafe_allow_html=True)  # 줄 간격 추가

        # 전체 수리부품별 불량율 계산
        품질보증_counts = df_year['유상/무상'].value_counts()
        품질보증_df = pd.DataFrame({'유상/무상': 품질보증_counts.index, '개수': 품질보증_counts.values})

        # 데이터프레임 출력
        st.write(품질보증_df)

        # 차트 그리기
        sizes = 품질보증_counts.values.tolist()
        labels = 품질보증_counts.index.tolist()

        # 색상 설정
        colors = ['steelblue', 'lightsteelblue']

        # 막대 그래프
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

        ax1.bar(labels, sizes, color=colors)
        ax1.set_xlabel('유상/무상')
        ax1.set_ylabel('개수')
        ax1.set_title('유상/무상 개수')

        # 파이 차트
        ax2.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
        ax2.set_title('유상/무상 비율')

        # 그래프 출력
        st.pyplot(fig)






