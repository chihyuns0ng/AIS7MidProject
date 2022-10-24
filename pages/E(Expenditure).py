import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import koreanize_matplotlib

st.set_page_config(
    page_title="🚀일론머스크 MID🚀",
    page_icon="⭐️",
    layout="wide",
)

st.markdown("# 💲월평균 간편식 지출액💲")

url1 = "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis4_19.csv"
url2 = "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis4_20.csv"
url3 = "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis4_21.csv"

kosis4_19 = pd.read_csv(url1)
kosis4_20 = pd.read_csv(url2)
kosis4_21 = pd.read_csv(url3)

kosis4_19_number = kosis4_19[1:6].drop("특성별(1)", axis=1)
kosis4_20_number = kosis4_20[1:6].drop("특성별(1)", axis=1)
kosis4_21_number = kosis4_21[1:5].drop("특성별(1)", axis=1)

kosis4_number = pd.concat([kosis4_19_number, kosis4_20_number, kosis4_21_number], axis=0)

st.markdown("## 가구원수별")

with st.expander('데이터프레임 보기🧾'):
    st.dataframe(kosis4_number)

for i in kosis4_number.columns[1:-1]:
    fig = sns.barplot(data=kosis4_number, x="연도", y=i , hue="특성별(2)")
    plt.legend(bbox_to_anchor=(1,1))
    plt.title(i, fontsize=15)
    plt.ylabel(" ")
    st.pyplot(plt.show())


kosis4_19_gender = kosis4_19[6:8].drop("특성별(1)", axis=1)
kosis4_20_gender = kosis4_20[6:8].drop("특성별(1)", axis=1)
kosis4_21_gender = kosis4_21[5:7].drop("특성별(1)", axis=1)

kosis4_gender = pd.concat([kosis4_19_gender, kosis4_20_gender, kosis4_21_gender])

st.markdown("## 성별별")

with st.expander('데이터프레임 보기🧾'):
    st.dataframe(kosis4_gender)

for i in kosis4_gender.columns[1:-1]:
    fig = sns.barplot(data=kosis4_gender, x="연도", y=i , hue="특성별(2)")
    plt.legend(bbox_to_anchor=(1,1))
    plt.title(i, fontsize=15)
    plt.ylabel(" ")
    st.pyplot(plt.show())


kosis4_19_age = kosis4_19[8:].drop("특성별(1)", axis=1)
kosis4_20_age = kosis4_20[8:].drop("특성별(1)", axis=1)
kosis4_21_age = kosis4_21[7:].drop("특성별(1)", axis=1)

kosis4_age = pd.concat([kosis4_19_age, kosis4_20_age, kosis4_21_age])

st.markdown("## 연령별")

with st.expander('데이터프레임 보기🧾'):
    st.dataframe(kosis4_age)

for i in kosis4_age.columns[1:-1]:
    fig = sns.barplot(data=kosis4_age, x="연도", y=i , hue="특성별(2)")
    plt.legend(bbox_to_anchor=(1,1))
    plt.title(i, fontsize=15)
    plt.ylabel(" ")
    st.pyplot(plt.show())
