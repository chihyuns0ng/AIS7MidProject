import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import koreanize_matplotlib

st.set_page_config(
    page_title="가공식품 가격에 대한 인식",
    page_icon="🚀",
    layout="wide",
)

st.markdown("# 가공 식품 가격 등락 민감도 📈")

st.set_option('deprecation.showPyplotGlobalUse', False)

url1="https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/%E1%84%80%E1%85%A1%E1%84%80%E1%85%A9%E1%86%BC%E1%84%89%E1%85%B5%E1%86%A8%E1%84%91%E1%85%AE%E1%86%B7_%E1%84%80%E1%85%A1%E1%84%80%E1%85%A7%E1%86%A8%E1%84%8B%E1%85%A6_%E1%84%83%E1%85%A2%E1%84%92%E1%85%A1%E1%86%AB_%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8_2019.csv"
url2="https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/%EA%B0%80%EA%B3%B5%EC%8B%9D%ED%92%88_%EA%B0%80%EA%B2%A9%EC%97%90_%EB%8C%80%ED%95%9C_%EC%9D%B8%EC%8B%9D_2020.csv"
url3="https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/%EA%B0%80%EA%B3%B5%EC%8B%9D%ED%92%88_%EA%B0%80%EA%B2%A9%EC%97%90_%EB%8C%80%ED%95%9C_%EC%9D%B8%EC%8B%9D_2021.csv"

@st.cache
def load_data(url1):
    df_2019 = pd.read_csv(url1, encoding='cp949')
    return df_2019
df_2019 = load_data(url1)

@st.cache
def load_data(url2):
    df_2020 = pd.read_csv(url2, encoding='cp949')
    return df_2020
df_2020 = load_data(url2)

@st.cache
def load_data(url3):
    df_2021 = pd.read_csv(url3, encoding='cp949')
    return df_2021
df_2021 = load_data(url3)


df_2019=df_2019[~df_2019['특성별(2)'].str.contains('소계')]
df_2019=df_2019.drop(columns=['특성별(1)', '시점', '전혀 그렇지 않다 (%)'], axis=1)
df_2019=df_2019.reset_index(drop=True)
df_2019 = df_2019.rename(columns={"인식별(1)" : "인식", "그렇지 않은 편이다 (%)":"그렇지 않은 편이다", 
                                  "보통이다/그저 그렇다 (%)":"보통이다",
                                  "그런 편이다 (%)":"그런 편이다", "매우 그렇다 (%)":"매우 그렇다"})
df_2019

df_2020=df_2020[~df_2020['특성별(2)'].str.contains('소계')]
df_2020=df_2020.drop(columns=['특성별(1)', '시점', '전혀 그렇지 않다 (%)'], axis=1)
df_2020=df_2020.reset_index(drop=True)
df_2020 = df_2020.rename(columns={"인식별(1)" : "인식", "그렇지 않은 편이다 (%)":"그렇지 않은 편이다", 
                                  "보통이다/그저 그렇다 (%)":"보통이다",
                                  "그런 편이다 (%)":"그런 편이다", "매우 그렇다 (%)":"매우 그렇다"})
df_2020


df_2021=df_2021[~df_2021['특성별(2)'].str.contains('소계')]
df_2021=df_2021.drop(columns=['특성별(1)', '시점', '전혀 그렇지 않다 (%)'], axis=1)
df_2021=df_2021.reset_index(drop=True)
df_2021=df_2021.rename(columns={"인식별(1)" : "인식", "그렇지 않은 편이다 (%)":"그렇지 않은 편이다", 
                                  "보통이다/그저 그렇다 (%)":"보통이다",
                                  "그런 편이다 (%)":"그런 편이다", "매우 그렇다 (%)":"매우 그렇다"})
df_2021
