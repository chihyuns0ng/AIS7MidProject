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

st.markdown("# 간편식 구입 이유📊")

url = [
    "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_19.csv",
    "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_20.csv",
    "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_21.csv",
]

kosis3_19 = pd.read_csv(url[0])
kosis3_20 = pd.read_csv(url[1])
kosis3_21 = pd.read_csv(url[2])

kosis3_19_gender = kosis3_19[6:8].drop("특성별(1)", axis=1).set_index("특성별(2)").rename_axis("가구원수")
kosis3_20_gender = kosis3_20[6:8].drop("특성별(1)", axis=1).set_index("특성별(2)").rename_axis("가구원수")
kosis3_21_gender = kosis3_21[5:7].drop("특성별(1)", axis=1).set_index("특성별(2)").rename_axis("가구원수")

# 수치형으로 변환
kosis3_19_gender = kosis3_19_gender.apply(pd.to_numeric, errors='coerce')
kosis3_20_gender = kosis3_20_gender.apply(pd.to_numeric, errors='coerce')
kosis3_21_gender = kosis3_21_gender.apply(pd.to_numeric, errors='coerce')

# 연도별 남녀 평균을 iloc(위치 기반)으로 안전하게 계산
def calc_avg(df):
    return (df.iloc[0] + df.iloc[1]) / 2

avg_19 = calc_avg(kosis3_19_gender)
avg_20 = calc_avg(kosis3_20_gender)
avg_21 = calc_avg(kosis3_21_gender)

df = pd.DataFrame({"2019년": avg_19, "2020년": avg_20, "2021년": avg_21})

with st.expander('데이터프레임 보기🧾'):
    st.dataframe(df)


def draw_pie(values, labels, title, colors):
    # NaN 또는 0 값은 pie chart 오류를 유발하므로 제거
    mask = values.notna() & (values > 0)
    values = values[mask]
    labels = labels[mask]

    fig, ax = plt.subplots()
    n = len(values)
    explode = (0.02,) * n
    ax.pie(values, labels=labels, startangle=180, autopct='%1.1f%%',
           counterclock=False, wedgeprops=dict(width=0.5),
           explode=explode, colors=colors[:n])
    ax.legend(bbox_to_anchor=(1.2, 1.1))
    ax.set_title(title)
    st.pyplot(fig)
    plt.close(fig)


colors_19 = ["royalblue", "gold", "silver", "tomato", "violet", "darkgray", "gainsboro", "gainsboro"]
colors_20 = ["royalblue", "gold", "gainsboro", "tomato", "violet", "darkgray", "silver", "gainsboro"]
colors_21 = ["royalblue", "gold", "darkgray", "tomato", "violet", "darkgray", "silver", "gainsboro"]

draw_pie(df["2019년"][:-2], df.index[:-2], "2019년 구입 이유", colors_19)
draw_pie(df["2020년"][:-2], df.index[:-2], "2020년 구입 이유", colors_20)
draw_pie(df["2021년"][:-2], df.index[:-2], "2021년 구입 이유", colors_21)
