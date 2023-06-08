import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# 경고 비활성화
st.set_option('deprecation.showPyplotGlobalUse', False)

df_year = pd.read_csv('df_total.csv', index_col=0)

def run_app_수리부품():

    if st.header('수리부품별 부품공급업체 불량집계 데이터'):
        st.markdown("<br><br>", unsafe_allow_html=True)  # 줄 간격 추가

        # 전체 수리부품별 불량율 계산
        불량원인_counts = df_year['수리부품_x'].value_counts()
        labels = 불량원인_counts.index.tolist()
        sizes = 불량원인_counts.values.tolist()

        # 파이차트 그리기
        fig, ax = plt.subplots(figsize=(10, 6), dpi=80)
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax.set_title('전체 수리부품별 불량율 데이터')

        # 그래프 출력
        st.pyplot(fig)
