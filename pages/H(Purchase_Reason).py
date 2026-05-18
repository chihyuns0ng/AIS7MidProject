import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import koreanize_matplotlib
# import plotly.graph_objects as go

st.set_page_config(
    page_title="🚀일론머스크 MID🚀",
    page_icon="⭐️",
    layout="wide",
)

st.markdown("# 간편식 구입 이유📊")


st.set_option('deprecation.showPyplotGlobalUse', False)

url = ["https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_19.csv"
, "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_20.csv"
, "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_21.csv"
]


kosis3_19=pd.read_csv(url[0])
kosis3_20=pd.read_csv(url[1])
kosis3_21=pd.read_csv(url[2])



kosis3_19_gender = kosis3_19[6:8].drop("특성별(1)", axis=1)
kosis3_20_gender = kosis3_20[6:8].drop("특성별(1)", axis=1)
kosis3_21_gender = kosis3_21[5:7].drop("특성별(1)", axis=1)

kosis3_19_gender = kosis3_19_gender.set_index("특성별(2)")
kosis3_19_gender = kosis3_19_gender.rename_axis("가구원수")
kosis3_20_gender = kosis3_20_gender.set_index("특성별(2)")
kosis3_20_gender = kosis3_20_gender.rename_axis("가구원수")
kosis3_21_gender = kosis3_21_gender.set_index("특성별(2)")
kosis3_21_gender = kosis3_21_gender.rename_axis("가구원수")

kosis3_gender = pd.concat([kosis3_19_gender, kosis3_20_gender, kosis3_21_gender])

kosis3_gender.loc["2019년"] = 0
kosis3_gender.loc["2020년"] = 0
kosis3_gender.loc["2021년"] = 0

for i in kosis3_gender.columns:
    kosis3_gender.loc["2019년"][i] = (kosis3_gender.loc["남성"][i][0] + kosis3_gender.loc["여성"][i][0]) / 2
    kosis3_gender.loc["2020년"][i] = (kosis3_gender.loc["남성"][i][1] + kosis3_gender.loc["여성"][i][1]) / 2
    kosis3_gender.loc["2021년"][i] = (kosis3_gender.loc["남성"][i][2] + kosis3_gender.loc["여성"][i][2]) / 2
    
df = kosis3_gender.drop(["남성", "여성"])

with st.expander('데이터프레임 보기🧾'):
    st.dataframe(df)

fig = plt.pie(df.T["2019년"][:-2], labels=df.T.index[:-2], startangle=180, autopct='%1.1f%%', counterclock=False, wedgeprops=dict(width=0.5)
            , explode=(0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02), colors=["royalblue", "gold", "silver", "tomato", "violet", "darkgray", "gainsboro", "gainsboro"])
plt.legend(bbox_to_anchor=(1.2,1.1))
plt.title("2019년 구입 이유")
st.pyplot()


fig = plt.pie(df.T["2020년"][:-2], labels=df.T.index[:-2], startangle=180, autopct='%1.1f%%', counterclock=False, wedgeprops=dict(width=0.5)
            , explode=(0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02), colors=["royalblue", "gold", "gainsboro", "tomato", "violet", "darkgray", "silver", "gainsboro"])
plt.legend(bbox_to_anchor=(1.2,1.1))
plt.title("2020년 구입 이유")
st.pyplot()



fig = plt.pie(df.T["2021년"][:-2], labels=df.T.index[:-2], startangle=180, autopct='%1.1f%%', counterclock=False, wedgeprops=dict(width=0.5)
            , explode=(0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02), colors=["royalblue", "gold", "darkgray", "tomato", "violet", "darkgray", "silver", "gainsboro"])
plt.legend(bbox_to_anchor=(1.2,1.1))
plt.title("2021년 구입 이유")
st.pyplot()
