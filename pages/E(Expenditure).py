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

st.markdown("# 월평균 간편식 지출액📊")

url1 = "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis4_19.csv"
url2 = "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis4_20.csv"
url3 = "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis4_21.csv"

@st.cache_data
def load_data(url):
    return pd.read_csv(url)

kosis4_19 = load_data(url1)
kosis4_20 = load_data(url2)
kosis4_21 = load_data(url3)

# 가구원수별
kosis4_19_number = kosis4_19[1:6].drop("특성별(1)", axis=1)
kosis4_20_number = kosis4_20[1:6].drop("특성별(1)", axis=1)
kosis4_21_number = kosis4_21[1:5].drop("특성별(1)", axis=1)
kosis4_number = pd.concat([kosis4_19_number, kosis4_20_number, kosis4_21_number], axis=0)

# 성별
kosis4_19_gender = kosis4_19[6:8].drop("특성별(1)", axis=1)
kosis4_20_gender = kosis4_20[6:8].drop("특성별(1)", axis=1)
kosis4_21_gender = kosis4_21[5:7].drop("특성별(1)", axis=1)
kosis4_gender = pd.concat([kosis4_19_gender, kosis4_20_gender, kosis4_21_gender])

# 연령별
kosis4_19_age = kosis4_19[8:].drop("특성별(1)", axis=1)
kosis4_20_age = kosis4_20[8:].drop("특성별(1)", axis=1)
kosis4_21_age = kosis4_21[7:].drop("특성별(1)", axis=1)
kosis4_age = pd.concat([kosis4_19_age, kosis4_20_age, kosis4_21_age])


my_order = ['가구원수별', '성별', '연령별']
status = st.radio('그래프 선택', my_order)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


def draw_charts(df, title):
    st.markdown(f"## {title}")
    with st.expander('데이터프레임 보기🧾'):
        st.dataframe(df)
    for col in df.columns[1:-1]:
        fig, ax = plt.subplots()
        sns.barplot(data=df, x="연도", y=col, hue="특성별(2)", ax=ax)
        ax.legend(bbox_to_anchor=(1, 1))
        ax.set_title(col, fontsize=15)
        ax.set_ylabel(" ")
        st.pyplot(fig)
        plt.close(fig)


if status == my_order[0]:
    draw_charts(kosis4_number, "가구원수별")
elif status == my_order[1]:
    draw_charts(kosis4_gender, "성별")
elif status == my_order[2]:
    draw_charts(kosis4_age, "연령별")
