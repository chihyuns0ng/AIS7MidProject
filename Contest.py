import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import koreanize_matplotlib
from PIL import Image

st.set_page_config(
    page_title="유통데이터 활용 경진대회",
    page_icon="🚀",
    layout="wide",
)

def load_image(image_file):
    img = Image.open(image_file)
    return img

load_image("main_1.jpg")
load_image("main_2.jpg")
load_image("main_3.jpg")

st.markdown("# 🚚유통데이터 활용 경진대회📊")
st.markdown("# ")
st.markdown("# ")
st.write("""
#### 유통데이터 분석을 통한 지속가능한 간편식 사업 활성화 프로젝트 
#
######  최초의 데이터의 상품 목록은 대분류> 중분류> 소분류로 분류됩니다.
######  소분류를 기준으로 삼게 되면 상품 유형이 너무 많아지기 때문에 대분류를 기준으로 데이터 프레임을 관찰하였고
######  그 결과는 다음과 같습니다.
""")



st.image("main_1.jpg")

st.write("""
#
######  상위 8개의 항목 중에서 주방 · 청소 · 욕실용품을 제외하고는 모두 식품과 관련된 소비였기에 주제의 큰 카테고리를 식품으로 잡게 되었으며
######  대표적으로 두드러진 생수 · 과자 · 라면 · 커피를 매주마다 사람들이 소비하는 생필품으로 규정해 제외한 다음
######  나머지 카테고리 중 식품 데이터라고 판단한 항목들에 대해 분석한 결과 우유 · 냉장냉동 · 간편식이 두드러진다는 결과를 도출해냈습니다.
""")

st.image("main_2.jpg")

st.markdown("# ")
st.markdown("# ")

st.image("main_3.jpg")

st.write("""
#
######  이와 같은 자료를 바탕으로 어떤 데이터를 조사했으며 그 결과가 어떠했을지는 부디 다른 페이지들을 통해 직접 관찰해주시기 바랍니다.
######  A : 코로나19 감염현황
######  B : 식품 구매데이터
######  C : 간편식 구입변화의 추이
######  D : 식품소비 트렌드별 동조성 (가구원수별, 성별, 연령별)
######  E : 월평균 간편식 지출액
######  F : 간편식 품목별 구입경험
######  G : 가공 식품 가격 등락 민감도 / 상승 인식도
######  H : 간편식을 구입하는 이유
######  I : 간편식을 구입하지 않는 이유
""")
