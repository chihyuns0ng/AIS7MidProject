import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import koreanize_matplotlib

st.set_page_config(
    page_title="COVID19",
    page_icon="😷",
    layout="wide",
)

st.markdown("# 😷코로나19 감염현황😷")

url_3 = "https://raw.githubusercontent.com/hj2628/AIS7MidProject/main/20%E1%84%82%E1%85%A7%E1%86%AB%E1%84%83%E1%85%A9_%E1%84%8B%E1%85%AF%E1%86%AF%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%8F%E1%85%A9%E1%84%85%E1%85%A9%E1%84%82%E1%85%A1_%E1%84%92%E1%85%AA%E1%86%A8%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%A1%E1%84%89%E1%85%AE"

url_4 = "https://raw.githubusercontent.com/hj2628/AIS7MidProject/main/21%E1%84%82%E1%85%A7%E1%86%AB%E1%84%83%E1%85%A9_%E1%84%8B%E1%85%AF%E1%86%AF%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%8F%E1%85%A9%E1%84%85%E1%85%A9%E1%84%82%E1%85%A1_%E1%84%92%E1%85%AA%E1%86%A8%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%A1%E1%84%89%E1%85%AE"

url_5 = "https://raw.githubusercontent.com/hj2628/AIS7MidProject/main/22%E1%84%82%E1%85%A7%E1%86%AB%E1%84%83%E1%85%A9_%E1%84%8B%E1%85%AF%E1%86%AF%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%8F%E1%85%A9%E1%84%85%E1%85%A9%E1%84%82%E1%85%A1_%E1%84%92%E1%85%AA%E1%86%A8%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%A1%E1%84%89%E1%85%AE"


@st.cache
def load_data(url_3):
    data_3 = pd.read_csv(url_3)
    return data_3

@st.cache
def load_data(url_4):
    data_4 = pd.read_csv(url_4)
    return data_4

@st.cache
def load_data(url_5):
    data_5 = pd.read_csv(url_5)
    return data_5

data_3 = load_data(url_3)
data_4 = load_data(url_4)
data_5 = load_data(url_5)

st.markdown("## 코로나19 감염현황 데이터")

with st.expander('데이터프레임 보기') :
    st.dataframe(data_3)
    st.dataframe(data_4)
    st.dataframe(data_5)

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(15, 3))
sns.barplot(data=data_3, x="월", y="확진자수", ci=None).set_title("20년도 월별 코로나 확진자 수")
st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(15, 3))
sns.barplot(data=data_4, x="월", y="확진자수", ci=None).set_title("21년도 월별 코로나 확진자 수")
st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(15, 3))
sns.barplot(data=data_5, x="월", y="확진자수", ci=None).set_title("22년도 월별 코로나 확진자 수")
st.pyplot()
