import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import koreanize_matplotlib

st.set_page_config(
    page_title="구입경험",
    page_icon="🚀",
    layout="wide",
)

st.markdown("# 🍚🍖🍜간편식 품목별 구입경험🍗🍕🍔")
st.sidebar.markdown("# 간편식 품목별 구입경험🍖")

url="https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/%E1%84%80%E1%85%A1%E1%86%AB%E1%84%91%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8_%E1%84%91%E1%85%AE%E1%86%B7%E1%84%86%E1%85%A9%E1%86%A8%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%83%E1%85%A9%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%80%E1%85%AE%E1%84%8B%E1%85%B5%E1%86%B8%E1%84%80%E1%85%A7%E1%86%BC%E1%84%92%E1%85%A5%E1%86%B7.csv"

df_exp = pd.read_csv(url)


df_exp.columns = ["품목군", "연도", "없음", "있음"]
df_exp = df_exp.drop(df_exp.index[0])

df_exp = df_exp.astype({'연도' : 'int'})

df_exp = df_exp.astype({'없음' : 'float'})

df_exp = df_exp.astype({'있음' : 'float'})

fig, ax = plt.subplots()
sns.barplot(data=df_exp, x="연도", y="없음", hue="품목군").set_title("간편식 구입경험")
plt.legend(bbox_to_anchor=(1,1))
st.pyplot(fig)

fig, ax = plt.subplots()
sns.barplot(data=df_exp, x="연도", y="있음", hue="품목군").set_title("간편식 구입경험")
plt.legend(bbox_to_anchor=(1,1))
st.pyplot(fig)
