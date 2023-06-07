import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 경고 비활성화
st.set_option('deprecation.showPyplotGlobalUse', False)

df_year = pd.read_csv('df_total', index_col=0)

def run_app_수리부품(filtered_df):
    if not filtered_df.empty:
        # 불량원인별 점유율 계산
        plt.figure(figsize=(10, 6), dpi=80)
        불량원인_counts = filtered_df['수리부품'].value_counts()
        labels = 불량원인_counts.index.tolist()
        sizes = 불량원인_counts.values.tolist()
        # 파이 그래프 그리기
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        # 그래프 제목 설정
        plt.title('전체 수리부품별 불량율 데이터')
        # 그래프 출력
        st.pyplot()

    else:
        st.write("선택된 수리부품에 해당하는 데이터가 없습니다.")

    # 앱 실행
    run_app_부품공급업체(filtered_df)
    run_app_수리부품(filtered_df)
