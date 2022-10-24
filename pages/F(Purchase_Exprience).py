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

url_6 = "https://raw.githubusercontent.com/hj2628/AIS7MidProject/main/%E1%84%80%E1%85%A1%E1%86%AB%E1%84%91%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8_%E1%84%91%E1%85%AE%E1%86%B7%E1%84%86%E1%85%A9%E1%86%A8%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%83%E1%85%A9%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%80%E1%85%AE%E1%84%8B%E1%85%B5%E1%86%B8%E1%84%80%E1%85%A7%E1%86%BC%E1%84%92%E1%85%A5%E1%86%B7"


@st.cache
def load_data(url_6):
    data_6 = pd.read_csv(url_6)
    return data_6

data_6 = load_data(url_6)

if st.checkbox('Dataframe'):
    st.dataframe(data_6)

st.write("""
### 경험 없음
""")

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(15, 5))
sns.barplot(data=data_6, x="연도", y="없음", hue="품목군").set_title("연도별 간편식 구입경험")
plt.legend(bbox_to_anchor=(1,1))
st.pyplot()

st.write("""
### 경험 있음
""")

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(15, 5))
sns.barplot(data=data_6, x="연도", y="있음", hue="품목군").set_title("연도별 간편식 구입경험")
plt.legend(bbox_to_anchor=(1,1))
st.pyplot()
