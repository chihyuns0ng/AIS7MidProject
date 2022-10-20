import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import koreanize_matplotlib
# import plotly.graph_objects as go

st.set_page_config(
    page_title="1론머스크 MidProject",
    page_icon="🚀",
    layout="wide",
)

st.markdown("# 🚀1론머스크🚀")
st.sidebar.markdown("# 공공데이터")

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

fig = kosis3_19_gender.T[:-2].plot(kind="bar", figsize=(20,10),fontsize=15, rot=20)
plt.title("2019년 가구원수별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())

fig = kosis3_20_gender.T[:-2].plot(kind="bar", figsize=(20,10),fontsize=15, rot=20)
plt.title("2020년 가구원수별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())

fig = kosis3_21_gender.T[:-2].plot(kind="bar", figsize=(20,10),fontsize=15, rot=20)
plt.title("2021년 가구원수별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())