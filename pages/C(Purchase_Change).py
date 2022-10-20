import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import koreanize_matplotlib

st.set_page_config(
    page_title="구입변화",
    page_icon="🚀",
    layout="wide",
)

st.markdown("# 간편식 구입변화📈")
st.sidebar.markdown("# 간편식 구입변화📈")


ur1="https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/%E1%84%80%E1%85%A1%E1%86%AB%E1%84%91%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8_%E1%84%91%E1%85%AE%E1%86%B7%E1%84%86%E1%85%A9%E1%86%A8%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%83%E1%85%A9%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%80%E1%85%AE%E1%84%8B%E1%85%B5%E1%86%B8%E1%84%87%E1%85%A7%E1%86%AB%E1%84%92%E1%85%AA.csv"
df_ch = pd.read_csv(ur1)

df_ch = df_ch.astype({'연도' : 'int'})
df_ch = df_ch.astype({'매우감소' : 'float'})
df_ch = df_ch.astype({'약간감소' : 'float'})
df_ch = df_ch.astype({'비슷' : 'float'})
df_ch = df_ch.astype({'약간증가' : 'float'})
df_ch = df_ch.astype({'매우증가' : 'float'})
df_ch = df_ch.astype({'평균' : 'float'})

st.write("""
### 매우 감소
""")

fig, ax = plt.subplots()
sns.barplot(data=df_ch, x="연도", y="매우감소", hue="품목군").set_title("간편식 구입변화(%)")
plt.legend(bbox_to_anchor=(1,1))
st.pyplot(fig)

st.write("""
### 약간 감소
""")

fig, ax = plt.subplots()
sns.barplot(data=df_ch, x="연도", y="약간감소", hue="품목군").set_title("간편식 구입변화(%)")
plt.legend(bbox_to_anchor=(1,1))
st.pyplot(fig)

st.write("""
### 비슷
""")

fig, ax = plt.subplots()
sns.barplot(data=df_ch, x="연도", y="비슷", hue="품목군").set_title("간편식 구입변화")
plt.legend(bbox_to_anchor=(1,1))
st.pyplot(fig)

st.write("""
### 약간 증가
""")

fig, ax = plt.subplots()
sns.barplot(data=df_ch, x="연도", y="약간증가", hue="품목군").set_title("간편식 구입변화(%)")
plt.legend(bbox_to_anchor=(1,1))
st.pyplot(fig)

st.write("""
### 매우 증가
""")

fig, ax = plt.subplots()
sns.barplot(data=df_ch, x="연도", y="매우증가", hue="품목군").set_title("간편식 구입변화(%)")
plt.legend(bbox_to_anchor=(1,1))
st.pyplot(fig)

st.write("""
### 평균
""")

fig, ax = plt.subplots()
sns.barplot(data=df_ch, x="연도", y="평균", hue="품목군").set_title("간편식 구입변화 평균(점)")
plt.legend(bbox_to_anchor=(1,1))
st.pyplot(fig)
