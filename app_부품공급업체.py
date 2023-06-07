import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_year = pd.read_csv('df_total',index_col=0)

def run_app_부품공급업체():
    if st.header('수리부품별 부품공급업체 불량집계 데이터'):
        # 체크박스로 표시할 년도 목록 생성
        부품공급업체_list = sorted(df_year['부품공급업체'].unique(), reverse=False) #sorted()함수로 오름차순 정렬

        # 체크박스로 선택된 옵션 가져오기
        전체선택 = st.checkbox("수리부품 전체선택")

        if 전체선택:
            selected_수리부품 = df_year['수리부품'].unique()
        else:
            selected_수리부품 = st.multiselect('수리부품 선택', df_year['수리부품'].unique())

        # 선택된 수리부품에 해당하는 데이터프레임 필터링
        if len(selected_수리부품) == 0:
            filtered_df = pd.DataFrame()  # 빈 데이터프레임 생성
        else:
            filtered_df = df_year[df_year['수리부품'].isin(selected_수리부품)]

        # df_year 데이터프레임의 수리부품과 부품공급업체 컬럼 가져오기
        if '수리부품' in df_year.columns and '부품공급업체' in df_year.columns:
            수리부품 = df_year['수리부품']
            부품공급업체 = df_year['부품공급업체']

            # 선택한 수리부품에 해당하는 부품공급업체 그룹화 및 출력
            selected_options = 부품공급업체_list

            # 선택한 수리부품에 해당하는 부품공급업체 그룹화 결과를 저장할 데이터프레임 생성
            result_df = pd.DataFrame(columns=['부품공급업체'])

            # 선택한 수리부품에 해당하는 부품공급업체 그룹화 및 결과 저장
            for 수리부품 in selected_수리부품:
                grouped_selected = df_year[df_year['수리부품'] == 수리부품].groupby('부품공급업체').size().reset_index(name=수리부품)
                result_df = pd.merge(result_df, grouped_selected, on='부품공급업체', how='outer')

            # 마지막 행에 부품공급업체별 개수의 합계 추가
            result_df.loc[len(result_df)] = ['합계'] + result_df.iloc[:, 1:].sum().tolist()

            # 결과 출력
            st.write(result_df)


            # 선택한 수리부품별로 그래프 그리기
            for 수리부품 in selected_수리부품:
                # 해당 수리부품에 대한 데이터프레임 필터링
                part_df = filtered_df[filtered_df['수리부품'] == 수리부품]

                if not part_df.empty:
                    st.set_option('deprecation.showPyplotGlobalUse', False)
                    plt.figure(figsize=(12, 6))

                    # 첫 번째 서브플롯: Count Plot
                    plt.subplot(1, 2, 1)
                    sns.countplot(data=part_df, x='부품공급업체')
                    plt.xlabel('부품공급업체')
                    plt.ylabel('접수건수')
                    plt.title(f'{수리부품}별 부품공급업체별 A/S 접수건수')

                    # 두 번째 서브플롯: 파이 차트
                    plt.subplot(1, 2, 2)
                    불량원인_counts = part_df['부품공급업체'].value_counts()
                    labels = 불량원인_counts.index.tolist()
                    sizes = 불량원인_counts.values.tolist()
                    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
                    plt.title(f'{수리부품}별 부품공급업체별 불량율 접수 데이터')

                    plt.tight_layout()

                    # 그래프를 이미지로 변환하여 앱 대시보드에 표시
                    st.write(f"{수리부품}별 부품공급업체별 A/S 접수건수 및 불량율:")
                    st.pyplot()

            if len(selected_수리부품) == 0:
                filtered_df = df_year  # 전체 데이터프레임 사용
            else:
                filtered_df = df_year[df_year['수리부품'].isin(selected_수리부품)]

            if not filtered_df.empty:
                # 불량원인별 점유율 계산
                plt.figure(figsize=(10, 6))
                불량원인_counts = filtered_df['수리부품'].value_counts()
                labels = 불량원인_counts.index.tolist()
                sizes = 불량원인_counts.values.tolist()
                # 파이 그래프 그리기
                plt.pie(sizes, labels=labels, autopct='%1.1f%%')
                # 그래프 제목 설정
                plt.title('전체 수리부품별 불량율 접수 데이터')
                # 그래프 출력
                st.pyplot(plt)
            else:
                st.write("선택된 수리부품에 해당하는 데이터가 없습니다.")

  
        else:
            st.write("데이터프레임에 '수리부품' 또는 '부품공급업체' 컬럼이 존재하지 않습니다.")

    else:
        st.write('파일을 업로드해주세요.')






