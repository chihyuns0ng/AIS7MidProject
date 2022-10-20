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

st.markdown("# 식품소비 성별 동조성 📈")
st.sidebar.markdown("# 간편식 관련 분석 데이터 📈")


url19 = 'https://raw.githubusercontent.com/HyenC/AIS7MidProject/main/data/%E1%84%89%E1%85%B5%E1%86%A8%E1%84%91%E1%85%AE%E1%86%B7%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5_%E1%84%90%E1%85%B3%E1%84%85%E1%85%A6%E1%86%AB%E1%84%83%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8C%E1%85%A9%E1%84%89%E1%85%A5%E1%86%BC_19.csv'
url20 = 'https://raw.githubusercontent.com/HyenC/AIS7MidProject/main/data/%E1%84%89%E1%85%B5%E1%86%A8%E1%84%91%E1%85%AE%E1%86%B7%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5_%E1%84%90%E1%85%B3%E1%84%85%E1%85%A6%E1%86%AB%E1%84%83%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8C%E1%85%A9%E1%84%89%E1%85%A5%E1%86%BC_20.csv'
url21 = 'https://raw.githubusercontent.com/HyenC/AIS7MidProject/main/data/%E1%84%89%E1%85%B5%E1%86%A8%E1%84%91%E1%85%AE%E1%86%B7%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5_%E1%84%90%E1%85%B3%E1%84%85%E1%85%A6%E1%86%AB%E1%84%83%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8C%E1%85%A9%E1%84%89%E1%85%A5%E1%86%BC_21.csv'

@st.cache
def load_data(url19):
    df_19 = pd.read_csv(url19, encoding='cp949')
    return df_19

@st.cache
def load_data(url20):
    df_20 = pd.read_csv(url20, encoding='cp949')
    return df_20

@st.cache
def load_data(url21):
    df_21 = pd.read_csv(url21, encoding='cp949')
    return df_21

df_19 = load_data(url19)
df_20 = load_data(url20)
df_21 = load_data(url21)


df_t19 = df_19.rename(columns=df_19.iloc[0])
df_t19 = df_t19.drop(df_t19.index[0])
df_t19 = df_t19.astype({i:"float" for i in df_t19.columns[2:]})

df_t20 = df_20.rename(columns=df_20.iloc[0])
df_t20 = df_t20.drop(df_t20.index[0])
df_t20 = df_t20.astype({i:"float" for i in df_t20.columns[2:]})

df_t21 = df_21.rename(columns=df_21.iloc[0])
df_t21 = df_t21.drop(df_t21.index[0])
df_t21 = df_t21.astype({i:"float" for i in df_t21.columns[2:]})


df19_s = df_t19[df_t19['특성별(1)'] == '가구주성별']
df_19_s = df19_s.drop(['특성별(1)'], axis=1)
df_19_s = df_19_s.set_index(keys='특성별(2)')
df_19_s = df_19_s.rename_axis('성별')

df20_s = df_t20[df_t20['특성별(1)'] == '가구주성별']
df_20_s = df20_s.drop(['특성별(1)'], axis=1)
df_20_s = df_20_s.set_index(keys='특성별(2)')
df_20_s = df_20_s.rename_axis('성별')

df21_s = df_t21[df_t21['특성별(1)'] == '가구주성별']
df_21_s = df21_s.drop(['특성별(1)'], axis=1)
df_21_s = df_21_s.set_index(keys='특성별(2)')
df_21_s = df_21_s.rename_axis('성별')


st.set_option('deprecation.showPyplotGlobalUse', False)


fig = df_19_s.T.plot(kind='bar', figsize=(25,10), rot=5, fontsize=15)
plt.title("2019년 성별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())

fig = df_20_s.T.plot(kind='bar', figsize=(25,10), rot=5, fontsize=15)
plt.title("2020년 성별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())

fig = df_21_s.T.plot(kind='bar', figsize=(25,10), rot=5, fontsize=15)
plt.title("2021년 성별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())