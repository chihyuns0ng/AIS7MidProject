import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import koreanize_matplotlib
# import plotly.graph_objects as go

st.set_page_config(
    page_title="연령별 구입이유",
    page_icon="🚀",
    layout="wide",
)

st.markdown("# 간편식 구입이유 - 연령별👶🧑👴")
st.sidebar.markdown("# 간편식 구입이유")
st.sidebar.markdown("# 연령별👶🧑👴")

st.set_option('deprecation.showPyplotGlobalUse', False)

url = ["https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_19.csv"
, "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_20.csv"
, "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_21.csv"
]


kosis3_19=pd.read_csv(url[0])
kosis3_20=pd.read_csv(url[1])
kosis3_21=pd.read_csv(url[2])

kosis3_19_age = kosis3_19[8:].drop("특성별(1)", axis=1)
kosis3_20_age = kosis3_20[8:].drop("특성별(1)", axis=1)
kosis3_21_age = kosis3_21[7:].drop("특성별(1)", axis=1)

kosis3_19_age = kosis3_19_age.set_index("특성별(2)")
kosis3_19_age = kosis3_19_age.rename_axis("가구원수")
kosis3_20_age = kosis3_20_age.set_index("특성별(2)")
kosis3_20_age = kosis3_20_age.rename_axis("가구원수")
kosis3_21_age = kosis3_21_age.set_index("특성별(2)")
kosis3_21_age = kosis3_21_age.rename_axis("가구원수")

st.write("""
### 2019년
""")

fig = kosis3_19_age.T[:-2].plot(kind="bar", figsize=(20,10),fontsize=15, rot=20)
plt.title("2019년 연령별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())

st.write("""
### 2020년
""")

fig = kosis3_20_age.T[:-2].plot(kind="bar", figsize=(20,10),fontsize=15, rot=20)
plt.title("2020년 연령별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())

st.write("""
### 2021년
""")

fig = kosis3_21_age.T[:-2].plot(kind="bar", figsize=(20,10),fontsize=15, rot=20)
plt.title("2021년 연령별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())
