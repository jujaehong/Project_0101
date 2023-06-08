# 가상의 전자제품 제조회사 특정제품 불량분석
## 제품명 : 휴대용 스마트 TV _ 기획상품
### 모델명 : SSAN-TV-4
- A/S 데이터 수집기간 : 2021년 05월 01일부터 ~ 2023년 05월 31일까지
- 총 수집 데이터 : 10,000

### 분석 데이터 개수 : 2EA
- 1. AS_Management_Data_A.csv
- 2. AS_Management_Data_B.csv

### 분석데이터 설명
### AS_Management_Data_A.csv 
#### 컬럼수 : 12
 - 접 수 번 호 : 고객 고객불만처리접수 할때 관리를 하기위한 고유번호
 - 접 수 일 자 : 최초 A/S센터에 접수하는 날자
 - 제 조 일 자 : 제품 제조 일자
 - 불량유형_대 : 불량유형 넓은 범위 분류 카테고리
 - 불량유형_중 : 불량유형 중간 범위 분류 카테고리
 - 불량유형_소 : 불량유형 세부 범위 분류 카테고리
 - 불 량 원 인 : 세부 범위 분류에 따른 불량의 원인
 - 보 증 유 무 : 품질보증기간 1년 ( 접수일자 - 제조일자 <= 365일 "무상 A/S" , 접수일자 - 제조일자 > 365일 "유상 A/S )
 - 처 리 내 역 : 품질보증기간에 따른 처리내역 ( "부품교체" . "제품교환" )
 - 수 리 부 품 : 불량원인에 따른 교체되는 부품
 - 부 품 비 용 : 수리비 청구와 관계없이 교체되는 수리부품에 대한 가격
 - 수리비 청구 : 품질보증기간이 지난 고객에게 청구할 A/S 비용 ( 데이터에는 부품의 가격만 명시되어 있음 )
 ### AS_Management_Data_B.csv
 #### 컬럼수 : 4
 - 접 수 번 호 : 고객 고객불만처리접수 할때 관리를 하기위한 고유번호
 - 수 리 부 품 : 불량원인에 따른 교체되는 부품
 - 부품공급업체 
   - 케이스_납품업체 : 케이스를 공급하는 업체 ( "A케이스", "B사출", "C커버" ) 세개의 공급업체가 있음.
   - 액정_납품업체 : 액정을 공급하는 업체 ("A액정" , "B패널", "C코닝" ) 세개의 공급업체가 있음.
   - 컨넥터_납품업체 : 컨넥터를 공급하는 업체 ( "A케이블", "B통신", "C텍" ) 세개의 공급업체가 있음.
   - M_Pcb_납품업체 : Main Pcb Board 공급업체 ( "A테크", "B테크", "C테크놀러지" ) 세개의 공급업체가 있음.  
   - SW_PCB_납품업체 : Switch Pcb Board 공급업체 ( "A테크", "B테크", "C테크놀러지" ) 세개의 공급업체가 있음.  
   - SMPS_Pcb_납품업체 : Smps Pcb Board 공급업체 ( "A테크", "B테크", "C테크놀러지" ) Q.C담당
   - Fuse_납품업체 : 퓨즈 공급업체 ( "A상사", "B파츠" ) 두개의 공급업체가 있음.
   - Battery_납품업체 : 배터리 공급업체 ( "A리튬", "B전지", "C파워" ) 세개의 공급업체가 있음. 
 - Q.C담당 : 제품 검사원 ( "김민지", "이수현" ) 세명의 검사원이 제품 검사를 한다.


## 데이터 분석 과정
  ### 1. Jupyter Notebook 으로 데이터 확인 및 분석
  #### 사용한 라이브러리
   - import pandas as pd
   - import numpy as np
   - import matplotlib.pyplot as plt
  #### AS_Management_Data_A.csv 불러오기
   - df_a 변수에 저장
   - 데이터프레임 확인하기
   - 결측치 확인하기
   - 제조일자, 접수일자 년도별 컬럼 추가하기
   - 제조년도별 접수수량 파악하기 ( 기간별 분석 )
   - 접수년도별 접수수량 파악하기 ( 기간별 분석 )
   - 불량유형 대분류,중분류,소분류 수량 파악하기 ( 불량 유형별 분석 )
   - 불량원인별 수량 파악하기 ( 불량원인별 분석 )
   - 수리부품별 불량율 파악하기 ( 수리부품별 불량율 분석 )
   - 품질보증 유상/무상 접수수량 파악하기  
  #### AS_Management_Data_B.csv 불러오기
   - df_b 변수에 저장
   - merge() 함수를 사용하여 df_a 와 df_b의 공통된 접수번호를 기준으로 데이터 합치기
   - "원인" 컬럼에서 "검수미비"에 따른 Q.C담당 수량 파악하기
   - "수리부품_X" 컬럼에서 공통된 부품공급업체를 그룹화 하고 해당 부품부품을 공급하는 공급업체의 불량실적 파악하기
     - (그룹화된 부품공급업체의 불량수량을 Bar그래프로 표시, 서브 Pie차트로 해당부품공급업체별 차지하는 불량비율 표시하기 )
  ### 2. VS Code로 앱대시보드 작업하기
   #### 사용한 라이브러리
  - import streamlit as st
  - import pandas as pd
  - import numpy as np
  - import matplotlib.pyplot as plt
  - from streamlit_option_menu import option_menu
  - import seaborn as sns
  #### app.py 파일 만들고 streamlit 기본환경 만들기
  #### 앱대시보드에 표시할 항목별 함수정의 하고 app.py로 import 하기
  - from app_홈 import run_app_홈
  - from app_제조년도별 import run_app_제조년도별
  - from app_접수년도별 import run_app_접수년도별
  - from app_1대분류 import run_app_1대분류
  - from app_2중분류 import run_app_2중분류
  - from app_3소분류 import run_app_3소분류
  - from app_불량원인 import run_app_불량원인
  - from app_부품공급업체 import run_app_부품공급업체
  - from app_수리부품 import run_app_수리부품
  - from app_품질보증 import run_app_품질보증
  #### streamlit run app.py 를 터미널에서 실행시켜 앱대시보드 출력 확인하기
  - st.sidebar 실행 확인
  - st.checkbox 실행 확인
  - st.multiselect 실행 확인
  - 데이터프레임 출력 확인
  - Bar 그래프 출력 확인
  - Pie 차트 출력 확인
  - 이미지 출력 확인
  ### 3. github Commit 및 Push 하기
   #### Github Desktop를 사용하여 Commit 및 Push
   #### PuTTY 실행
    - ec2-user 입력
    - 가상환경 진입
    - cd Github 폴더진입
    - git clone 하기
   #### github Settings -> Secres and vaiables -> Actions 진입 후 Repository secrets 만들기
    - HOST
    - SSH_PRIVATE)KEY ( app_dashboard.pem 메모장으로 열어 내용 복사 후 삽입 )
    - USER
   #### Actions -> set up a workflow yourself 진입
    - main.yml 작성 ( 경로는 PuTTY에서 clone한 위치경로를 넣어준다. )
    
    
  
  
  






















