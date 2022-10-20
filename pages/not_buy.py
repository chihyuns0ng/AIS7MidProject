import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import koreanize_matplotlib

st.set_page_config(
    page_title="MID_일론머스크",
    page_icon="🚀",
    layout="wide",
)

st.markdown("# 간편식 구입하지 않는 이유 📈")
st.sidebar.markdown("# 간편식 관련 분석 데이터 📈")

st.write("""
### 2021년
""")


url21 = 'https://raw.githubusercontent.com/HyenC/AIS7MidProject/main/data/%E1%84%80%E1%85%A1%E1%86%AB%E1%84%91%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8_%E1%84%80%E1%85%AE%E1%84%8B%E1%85%B5%E1%86%B8%E1%84%92%E1%85%A1%E1%84%8C%E1%85%B5_%E1%84%8B%E1%85%A1%E1%86%AD%E1%84%82%E1%85%B3%E1%86%AB_%E1%84%8B%E1%85%B5%E1%84%8B%E1%85%B2_21.csv'


@st.cache
def load_data(url21):
    df_21 = pd.read_csv(url21, encoding='cp949')
    return df_21

df_21 = load_data(url21)

df_t21 = df_21.rename(columns=df_21.iloc[0])
df_t21 = df_t21.drop(df_t21.index[0])
df_t21
df_t21 = df_t21.astype({i:"float" for i in df_t21.columns[2:]})
