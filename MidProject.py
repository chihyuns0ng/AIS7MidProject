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
st.sidebar.markdown("# 유통데이터 활용")
st.sidebar.markdown("# 경진대회")

st.set_option('deprecation.showPyplotGlobalUse', False)

url = ["https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_19.csv"
, "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_20.csv"
, "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_21.csv"
]

# @st.cache
# url_load_state = st.text('Loading data...')

kosis3_19=pd.read_csv(url[0])
kosis3_20=pd.read_csv(url[1])
kosis3_21=pd.read_csv(url[2])

# url_load_state.text("Done! (using st.cache)")

kosis3_19_number = kosis3_19[1:6].drop("특성별(1)", axis=1)
kosis3_20_number = kosis3_20[1:6].drop("특성별(1)", axis=1)
kosis3_21_number = kosis3_21[1:5].drop("특성별(1)", axis=1)

kosis3_19_number = kosis3_19_number.set_index("특성별(2)")
kosis3_19_number = kosis3_19_number.rename_axis("가구원수")
kosis3_20_number = kosis3_20_number.set_index("특성별(2)")
kosis3_20_number = kosis3_20_number.rename_axis("가구원수")
kosis3_21_number = kosis3_21_number.set_index("특성별(2)")
kosis3_21_number = kosis3_21_number.rename_axis("가구원수")


# a = kosis3_19_number.T[:-2]
# a["index"] = kosis3_19_number.T[:-2].index
# data1 = go.Bar(x=a["index"], y=a["1인"], name="1인")
# data2 = go.Bar(x=a["index"], y=a["2인"], name="2인")
# data3 = go.Bar(x=a["index"], y=a["3인"], name="3인")
# data4 = go.Bar(x=a["index"], y=a["4인"], name="4인")
# data5 = go.Bar(x=a["index"], y=a["5인 이상"], name="5인 이상")
# layout = go.Layout(title="2019년 가구원수별")
# fig = go.Figure(data=[data1, data2, data3, data4, data5], layout=layout)
# fig.show()
# sns.barplot(data=kosis3_19_number.T[:-2])
# st.bar_chart(kosis3_19_number.T[["1인", "2인", "3인", "4인", "5인 이상"]])

# pxh = px.histogram(kosis3_19_number)
# go.Bar()


fig = kosis3_19_number.T[:-2].plot(kind="bar", figsize=(20,10),fontsize=15, rot=20)
plt.title("2019년 가구원수별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())

fig = kosis3_20_number.T[:-2].plot(kind="bar", figsize=(20,10),fontsize=15, rot=20)
plt.title("2019년 가구원수별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())

fig = kosis3_21_number.T[:-2].plot(kind="bar", figsize=(20,10),fontsize=15, rot=20)
plt.title("2019년 가구원수별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())


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
plt.title("2019년 가구원수별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())

fig = kosis3_21_gender.T[:-2].plot(kind="bar", figsize=(20,10),fontsize=15, rot=20)
plt.title("2019년 가구원수별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())


kosis3_19_age = kosis3_19[8:].drop("특성별(1)", axis=1)
kosis3_20_age = kosis3_20[8:].drop("특성별(1)", axis=1)
kosis3_21_age = kosis3_21[7:].drop("특성별(1)", axis=1)

kosis3_19_age = kosis3_19_age.set_index("특성별(2)")
kosis3_19_age = kosis3_19_age.rename_axis("가구원수")
kosis3_20_age = kosis3_20_age.set_index("특성별(2)")
kosis3_20_age = kosis3_20_age.rename_axis("가구원수")
kosis3_21_age = kosis3_21_age.set_index("특성별(2)")
kosis3_21_age = kosis3_21_age.rename_axis("가구원수")

fig = kosis3_19_age.T[:-2].plot(kind="bar", figsize=(20,10),fontsize=15, rot=20)
plt.title("2019년 가구원수별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())

fig = kosis3_20_age.T[:-2].plot(kind="bar", figsize=(20,10),fontsize=15, rot=20)
plt.title("2019년 가구원수별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())

fig = kosis3_21_age.T[:-2].plot(kind="bar", figsize=(20,10),fontsize=15, rot=20)
plt.title("2019년 가구원수별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())
