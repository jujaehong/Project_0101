import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_year = pd.read_csv('df_total', index_col=0)

def run_app_수리부품():
    if  st.header('수리부품별 부품공급업체 불량집계 데이터'):
        st.markdown("<br><br>", unsafe_allow_html=True)  # 줄 간격 추가


        # 체크박스로 표시할 년도 목록 생성
        부품공급업체_list = sorted(df_year['부품공급업체'].unique(), reverse=False)
        st.error('전체 소분류 유형 데이터를 보려면 체크')

        # 체크박스로 선택된 옵션 가져오기
        전체선택 = st.checkbox("수리부품 전체선택")

        st.markdown("<br>", unsafe_allow_html=True)  # 줄 간격 추가
        if 전체선택:
            selected_수리부품 = df_year['수리부품'].unique()
        else:
            selected_수리부품 = st.multiselect('**특정 불량부품 공급업체 데이터만 보고 싶을 경우 아래에서 선택하세요**', 
                                           df_year['수리부품'].unique())


        # 선택된 수리부품에 해당하는 데이터프레임 필터링
        if len(selected_수리부품) == 0:
            filtered_df = pd.DataFrame()  # 빈 데이터프레임 생성
        else:
            filtered_df = df_year[df_year['수리부품'].isin(selected_수리부품)]

        # df_year 데이터프레임의 수리부품과 부품공급업체 컬럼 가져오기
        if '수리부품' in df_year.columns and '부품공급업체' in df_year.columns:
            # 선택한 수리부품에 해당하는 부품공급업체 그룹화 및 결과 저장
            result_df = pd.DataFrame(columns=['부품공급업체'])

            # 선택한 수리부품에 해당하는 부품공급업체 그룹화 및 결과 저장
            for 수리부품 in selected_수리부품:
                grouped_selected = df_year[df_year['수리부품'] == 수리부품].groupby('부품공급업체').size().reset_index(name=수리부품)
                result_df = pd.merge(result_df, grouped_selected, on='부품공급업체', how='outer')

            # 마지막 행에 부품공급업체별 개수의 합계 추가
            result_df.loc[len(result_df)] = ['합계'] + result_df.iloc[:, 1:].sum().tolist()

            if len(selected_수리부품) > 0:
                # 결과 출력
                st.write(result_df)
            st.markdown("<br><br>", unsafe_allow_html=True)  # 줄 간격 추가

            # 선택한 수리부품별로 그래프 그리기
            for 수리부품 in selected_수리부품:
                # 해당 수리부품에 대한 데이터프레임 필터링
                part_df = filtered_df[filtered_df['수리부품'] == 수리부품]

                if not part_df.empty:
                    # 해당 수리부품에 대한 부품공급업체 목록 가져오기
                    부품공급업체_list = sorted(part_df['부품공급업체'].unique(), reverse=True)

                    plt.figure(figsize=(12, 6),dpi=80)

                    # 첫 번째 서브플롯: Count Plot
                    plt.subplot(1, 2, 1)
                    colors = sns.color_palette('Set2', len(부품공급업체_list))  # Set the colors to match the palette
                    color_mapping = {}  # 부품공급업체와 색상 매핑 딕셔너리 생성
                    for idx, supplier in enumerate(부품공급업체_list):
                        color_mapping[supplier] = colors[idx]
                    sns.countplot(data=part_df, x='부품공급업체', palette=color_mapping.values(), order=부품공급업체_list)  # 내림차순으로 표시


                    # 각 막대(bar)에 접수건수 표시
                    for p in plt.gca().patches:
                        height = p.get_height()
                        plt.gca().text(p.get_x() + p.get_width() / 2, height / 2, '{:d} EA'.format(int(height)), ha='center', va='center', fontsize=15)

                    plt.xlabel('부품공급업체')
                    plt.ylabel('접수건수')
                    plt.title(f'{수리부품}별 부품공급업체별 A/S 접수건수')

                    # 두 번째 서브플롯: 파이 차트
                    plt.subplot(1, 2, 2)
                    불량원인_counts = part_df['부품공급업체'].value_counts()
                    labels = 불량원인_counts.index.tolist()
                    sizes = 불량원인_counts.values.tolist()

                    plt.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 15}, colors=[color_mapping[supplier] for supplier in labels])
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
                plt.figure(figsize=(10, 6),dpi=80)
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

        else:
            st.write("데이터프레임에 '수리부품' 또는 '부품공급업체' 컬럼이 존재하지 않습니다.")

    else:
        st.write('파일을 업로드해주세요.')






