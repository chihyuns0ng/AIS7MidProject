import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import koreanize_matplotlib

st.set_page_config(
    page_title="๐์ผ๋ก ๋จธ์คํฌ MID๐",
    page_icon="โญ๏ธ",
    layout="wide",
)

st.markdown("# ๊ฐํธ์ ๊ตฌ์๋ณํ๐")


url_7 = "https://raw.githubusercontent.com/hj2628/AIS7MidProject/main/%E1%84%80%E1%85%A1%E1%86%AB%E1%84%91%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8_%E1%84%91%E1%85%AE%E1%86%B7%E1%84%86%E1%85%A9%E1%86%A8%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%83%E1%85%A9%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%80%E1%85%AE%E1%84%8B%E1%85%B5%E1%86%B8%E1%84%87%E1%85%A7%E1%86%AB%E1%84%92%E1%85%AA"

@st.cache
def load_data(url_7):
    data_7 = pd.read_csv(url_7)
    return data_7

data_7 = load_data(url_7)

with st.expander('๋ฐ์ดํฐํ๋ ์ ๋ณด๊ธฐ๐งพ'):
    st.dataframe(data_7)

    
my_order = ['๋งค์ฐ ๊ฐ์', '์ฝ๊ฐ ๊ฐ์', '๋น์ท', '์ฝ๊ฐ ์ฆ๊ฐ', '๋งค์ฐ ์ฆ๊ฐ']
    
status = st.radio('๊ทธ๋ํ ์ ํ', my_order)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    # ์ฒซ๋ฒ์งธ ๋ฐฉ๋ฒ
if status == my_order[0] :
    st.write("""
    ### ๋งค์ฐ ๊ฐ์
    """)

    plt.figure(figsize=(15, 5))
    sns.barplot(data=data_7, x="์ฐ๋", y="๋งค์ฐ๊ฐ์", hue="ํ๋ชฉ๊ตฐ").set_title("์ฐ๋๋ณ ๊ฐํธ์ ๊ตฌ์๋ณํ(%)")
    plt.legend(bbox_to_anchor=(1.12,1))
    st.pyplot()

if status == my_order[1] :
    st.write("""
    ### ์ฝ๊ฐ ๊ฐ์
    """)

    plt.figure(figsize=(15, 5))
    sns.barplot(data=data_7, x="์ฐ๋", y="์ฝ๊ฐ๊ฐ์", hue="ํ๋ชฉ๊ตฐ").set_title("์ฐ๋๋ณ ๊ฐํธ์ ๊ตฌ์๋ณํ(%)")
    plt.legend(bbox_to_anchor=(1.12,1))
    st.pyplot()

if status == my_order[2] :
    st.write("""
    ### ๋น์ท
    """)

    plt.figure(figsize=(15, 5))
    sns.barplot(data=data_7, x="์ฐ๋", y="๋น์ท", hue="ํ๋ชฉ๊ตฐ").set_title("์ฐ๋๋ณ ๊ฐํธ์ ๊ตฌ์๋ณํ(%)")
    plt.legend(bbox_to_anchor=(1.12,1))
    st.pyplot()

if status == my_order[3] :
    st.write("""
    ### ์ฝ๊ฐ ์ฆ๊ฐ
    """)

    plt.figure(figsize=(15, 5))
    sns.barplot(data=data_7, x="์ฐ๋", y="์ฝ๊ฐ์ฆ๊ฐ", hue="ํ๋ชฉ๊ตฐ").set_title("์ฐ๋๋ณ ๊ฐํธ์ ๊ตฌ์๋ณํ(%)")
    plt.legend(bbox_to_anchor=(1.12,1))
    st.pyplot()

if status == my_order[4] :
    st.write("""
    ### ๋งค์ฐ ์ฆ๊ฐ
    """)

    plt.figure(figsize=(15, 5))
    sns.barplot(data=data_7, x="์ฐ๋", y="๋งค์ฐ์ฆ๊ฐ", hue="ํ๋ชฉ๊ตฐ").set_title("์ฐ๋๋ณ ๊ฐํธ์ ๊ตฌ์๋ณํ(%)")
    plt.legend(bbox_to_anchor=(1.12,1))
    st.pyplot()
