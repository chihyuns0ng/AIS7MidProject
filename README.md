# 🚀 일론머스크 팀 - 코로나19와 간편식 소비 트렌드 분석

[Streamlit 바로가기](https://chihyuns0ng-ais7midproject-contest-x6zxez.streamlit.app/)

## 📌 프로젝트 개요

코로나19 팬데믹 전후(2019~2022년)의 식품 소비 트렌드 변화를 분석한 데이터 시각화 대시보드입니다.  
코로나19 확진자 추이와 간편식 구매 데이터를 연결하여, 팬데믹이 소비 패턴에 미친 영향을 다각도로 탐색합니다.

---

## 🗂️ 탭 구성

| 탭 | 제목 | 내용 |
|---|---|---|
| A | 코로나19 감염현황 | 2020~2022년 월별 코로나 확진자 수 시각화 |
| B | 구매 데이터 | 2019~2020년 품목별 월별 구매 추이 |
| D | 식품소비 트렌드별 동조성 | 가구원수별·성별·연령별 식품 소비 트렌드 동조성 (2019~2021) |
| E | 월평균 간편식 지출액 | 가구원수별·성별·연령별 간편식 지출 금액 변화 (2019~2021) |
| F | 간편식 품목별 구입경험 | 연도별 간편식 품목군별 구입 경험 유무 비교 |
| G1 | 가공식품 가격 등락 민감도 | 가구원수별·성별·연령별 가격 민감도 인식 (2019~2021) |
| G2 | 가공식품 가격 상승 인식도 | 가구원수별·성별·연령별 전년 대비 가격 상승 인식 (2019~2021) |
| H | 간편식 구입 이유 | 연도별 간편식 구입 이유 비율 (파이차트) |

---

## 🛠️ 기술 스택

- **Python 3.10**
- **Streamlit** - 웹 대시보드
- **Pandas** - 데이터 처리
- **Matplotlib / Seaborn** - 정적 시각화
- **Plotly Express** - 인터랙티브 시각화
- **koreanize-matplotlib** - matplotlib 한글 폰트

---

## 📦 설치 및 실행

```bash
# 레포지토리 클론
git clone https://github.com/chihyuns0ng/AIS7MidProject.git
cd AIS7MidProject

# 패키지 설치
pip install -r requirements.txt

# 앱 실행
streamlit run Contest.py
```

---

## 📁 프로젝트 구조

```
AIS7MidProject/
├── Contest.py                          # 메인 페이지
├── requirements.txt
├── data/                               # CSV 데이터 파일
└── pages/                              # 멀티페이지 탭
    ├── A(COVID).py                     # 코로나19 감염현황
    ├── B(Purchase_Data).py             # 구매 데이터
    ├── D(Trend).py                     # 식품소비 트렌드별 동조성
    ├── E(Expenditure).py               # 월평균 간편식 지출액
    ├── F(Purchase_Exprience).py        # 간편식 품목별 구입경험
    ├── G1(Proceed_Food_Recognize_s).py # 가공식품 가격 등락 민감도
    ├── G2(Proceed_Food_Recognize_y).py # 가공식품 가격 상승 인식도
    └── H(Purchase_Reason).py           # 간편식 구입 이유
```

---

## 📊 데이터 출처

- 코로나19 확진자 현황 (질병관리청)
- 식품소비 트렌드별 동조성 조사 (한국농촌경제연구원 KREI)
- 가공식품 가격에 대한 인식 조사 (KOSIS 국가통계포털)
- 간편식 구입경험 및 구입이유 조사 (KOSIS 국가통계포털)
- 구매 데이터 (내부 데이터)

---

## 👥 팀원

| GitHub |
|---|
| [@sunyoung-cho](https://github.com/sunyoung-cho) |
| [@chihyuns0ng](https://github.com/chihyuns0ng) |
| [@HyenC](https://github.com/HyenC) |
| [@hj2628](https://github.com/hj2628) |

---

## 📄 License

[MIT](./LICENSE)
