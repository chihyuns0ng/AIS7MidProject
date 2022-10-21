import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import koreanize_matplotlib
# import plotly.graph_objects as go

st.set_page_config(
    page_title="가구원수별 구입 이유",
    page_icon="🚀",
    layout="wide",
)

st.markdown("# 간편식 구입이유 - 가구원수별👨‍👩‍👧‍👦")
st.sidebar.markdown("# 간편식 구입이유")
st.sidebar.markdown("# 가구원수별👨‍👩‍👧‍👦")

st.set_option('deprecation.showPyplotGlobalUse', False)

url = ["https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_19.csv?token=GHSAT0AAAAAAB2CCWJN72UB6C4D4FBDCYKQY2R6YOA"
, "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_20.csv?token=GHSAT0AAAAAAB2CCWJMGCLC4V4C2TRSQZGOY2R6ZIQ"
, "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_21.csv?token=GHSAT0AAAAAAB2CCWJNRHGMKZE4D66N3TZUY2R6ZKA"
]


kosis3_19=pd.read_csv(url[0])
kosis3_20=pd.read_csv(url[1])
kosis3_21=pd.read_csv(url[2])


kosis3_19_number = kosis3_19[1:6].drop("특성별(1)", axis=1)
kosis3_20_number = kosis3_20[1:6].drop("특성별(1)", axis=1)
kosis3_21_number = kosis3_21[1:5].drop("특성별(1)", axis=1)

kosis3_19_number = kosis3_19_number.set_index("특성별(2)")
kosis3_19_number = kosis3_19_number.rename_axis("가구원수")
kosis3_20_number = kosis3_20_number.set_index("특성별(2)")
kosis3_20_number = kosis3_20_number.rename_axis("가구원수")
kosis3_21_number = kosis3_21_number.set_index("특성별(2)")
kosis3_21_number = kosis3_21_number.rename_axis("가구원수")

st.write("""
### 2019년
""")

fig = kosis3_19_number.T[:-2].plot(kind="bar", figsize=(20,10),fontsize=15, rot=20)
plt.title("2019년 가구원수별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())

st.write("""
### 2020년
""")

fig = kosis3_20_number.T[:-2].plot(kind="bar", figsize=(20,10),fontsize=15, rot=20)
plt.title("2020년 가구원수별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())

st.write("""
### 2021년
""")

fig = kosis3_21_number.T[:-2].plot(kind="bar", figsize=(20,10),fontsize=15, rot=20)
plt.title("2021년 가구원수별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())
