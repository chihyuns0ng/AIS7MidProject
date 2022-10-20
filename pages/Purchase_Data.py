import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import koreanize_matplotlib

st.set_page_config(
    page_title="구매데이터 19,20년",
    page_icon="🚀",
    layout="wide",
)

url = "https://raw.githubusercontent.com/hj2628/AIS7MidProject/main/2019_%E1%84%80%E1%85%AE%E1%84%86%E1%85%A2%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5_%E1%84%8B%E1%85%AF%E1%86%AF%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%91%E1%85%AE%E1%86%B7%E1%84%86%E1%85%A9%E1%86%A8%E1%84%80%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%80%E1%85%AE%E1%84%86%E1%85%A2%E1%84%8E%E1%85%AE%E1%84%8B%E1%85%B5"

url_2 = "https://raw.githubusercontent.com/hj2628/AIS7MidProject/main/2020_%E1%84%80%E1%85%AE%E1%84%86%E1%85%A2%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5_%E1%84%8B%E1%85%AF%E1%86%AF%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%91%E1%85%AE%E1%86%B7%E1%84%86%E1%85%A9%E1%86%A8%E1%84%80%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%80%E1%85%AE%E1%84%86%E1%85%A2%E1%84%8E%E1%85%AE%E1%84%8B%E1%85%B5"


@st.cache
def load_data(url):
    data = pd.read_csv(url)
    return data

@st.cache
def load_data(url_2):
    data_2 = pd.read_csv(url_2)
    return data_2


data = load_data(url)
data_2 = load_data(url_2)

st.markdown("## 🚀19~20년도 구매데이터🚀")
st.sidebar.markdown("# 🚀19~20년도 구매데이터🚀")

st.dataframe(data)
st.dataframe(data_2)


pxh = px.histogram(data, x="월", y="Sales_Unit", color="MasterCategoryFullName", histfunc="sum", barmode="group", title="19년 품목별 구매추이")
st.plotly_chart(pxh)


pxh = px.histogram(data_2, x="월", y="Sales_Unit", color="MasterCategoryFullName", histfunc="sum", barmode="group", title="20년 품목별 구매추이")
st.plotly_chart(pxh)