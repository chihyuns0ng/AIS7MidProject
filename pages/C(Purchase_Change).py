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

st.markdown("# 간편식 구입변화📊")


url_7 = "https://raw.githubusercontent.com/hj2628/AIS7MidProject/main/%E1%84%80%E1%85%A1%E1%86%AB%E1%84%91%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8_%E1%84%91%E1%85%AE%E1%86%B7%E1%84%86%E1%85%A9%E1%86%A8%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%83%E1%85%A9%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%80%E1%85%AE%E1%84%8B%E1%85%B5%E1%86%B8%E1%84%87%E1%85%A7%E1%86%AB%E1%84%92%E1%85%AA"

@st.cache
def load_data(url_7):
    data_7 = pd.read_csv(url_7)
    return data_7

data_7 = load_data(url_7)

with st.expander('데이터프레임 보기🧾'):
    st.dataframe(data_7)

    
my_order = ['매우 감소', '약간 감소', '비슷', '약간 증가', '매우 증가']
    
status = st.radio('그래프 선택', my_order)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    # 첫번째 방법
if status == my_order[0] :
    st.write("""
    ### 매우 감소
    """)

    plt.figure(figsize=(15, 5))
    sns.barplot(data=data_7, x="연도", y="매우감소", hue="품목군").set_title("연도별 간편식 구입변화(%)")
    plt.legend(bbox_to_anchor=(1.12,1))
    st.pyplot()

if status == my_order[1] :
    st.write("""
    ### 약간 감소
    """)

    plt.figure(figsize=(15, 5))
    sns.barplot(data=data_7, x="연도", y="약간감소", hue="품목군").set_title("연도별 간편식 구입변화(%)")
    plt.legend(bbox_to_anchor=(1.12,1))
    st.pyplot()

if status == my_order[2] :
    st.write("""
    ### 비슷
    """)

    plt.figure(figsize=(15, 5))
    sns.barplot(data=data_7, x="연도", y="비슷", hue="품목군").set_title("연도별 간편식 구입변화(%)")
    plt.legend(bbox_to_anchor=(1.12,1))
    st.pyplot()

if status == my_order[3] :
    st.write("""
    ### 약간 증가
    """)

    plt.figure(figsize=(15, 5))
    sns.barplot(data=data_7, x="연도", y="약간증가", hue="품목군").set_title("연도별 간편식 구입변화(%)")
    plt.legend(bbox_to_anchor=(1.12,1))
    st.pyplot()

if status == my_order[4] :
    st.write("""
    ### 매우 증가
    """)

    plt.figure(figsize=(15, 5))
    sns.barplot(data=data_7, x="연도", y="매우증가", hue="품목군").set_title("연도별 간편식 구입변화(%)")
    plt.legend(bbox_to_anchor=(1.12,1))
    st.pyplot()
