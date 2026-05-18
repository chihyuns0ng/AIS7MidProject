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

st.markdown("# 식품소비 트렌드별 동조성📊")

url19 = 'https://raw.githubusercontent.com/HyenC/AIS7MidProject/main/data/%E1%84%89%E1%85%B5%E1%86%A8%E1%84%91%E1%85%AE%E1%86%B7%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5_%E1%84%90%E1%85%B3%E1%84%85%E1%85%A6%E1%86%AB%E1%84%83%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8C%E1%85%A9%E1%84%89%E1%85%A5%E1%86%BC_19.csv'
url20 = 'https://raw.githubusercontent.com/HyenC/AIS7MidProject/main/data/%E1%84%89%E1%85%B5%E1%86%A8%E1%84%91%E1%85%AE%E1%86%B7%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5_%E1%84%90%E1%85%B3%E1%84%85%E1%85%A6%E1%86%AB%E1%84%83%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8C%E1%85%A9%E1%84%89%E1%85%A5%E1%86%BC_20.csv'
url21 = 'https://raw.githubusercontent.com/HyenC/AIS7MidProject/main/data/%E1%84%89%E1%85%B5%E1%86%A8%E1%84%91%E1%85%AE%E1%86%B7%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5_%E1%84%90%E1%85%B3%E1%84%85%E1%85%A6%E1%86%AB%E1%84%83%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8C%E1%85%A9%E1%84%89%E1%85%A5%E1%86%BC_21.csv'


@st.cache_data
def load_data_19(url):
    return pd.read_csv(url, encoding='cp949')

@st.cache_data
def load_data_20(url):
    return pd.read_csv(url, encoding='cp949')

@st.cache_data
def load_data_21(url):
    return pd.read_csv(url, encoding='cp949')


df_19 = load_data_19(url19)
df_20 = load_data_20(url20)
df_21 = load_data_21(url21)


df_t19 = df_19.rename(columns=df_19.iloc[0])
df_t19 = df_t19.drop(df_t19.index[0])
df_t19 = df_t19.astype({i: "float" for i in df_t19.columns[2:]})
df_t19 = df_t19.rename(columns={
    '가격이 비싸도 프리미엄(고급)제품을 구입하겠다': '프리미엄 제품',
    '가격이 비싸도 다양하고 새로운 맛을 첨가한 제품을 구입하겠다': '새롭고 다양한 맛',
    '가격이 비싸도 건강에 좋은 원료 안전성이 확보된 제품을 구입하겠다': '원료 안전성',
    '가격이 비싸도 소포장 사용 및 취식/조리가 간편화된 제품을 구입하겠다': '소포장, 조리 간편화',
    '제품의 업그레이드/신제품 개발과 관계없이 가격만 저렴하면 구입하겠다': '오로지 가격'
})

df_t20 = df_20.rename(columns=df_20.iloc[0])
df_t20 = df_t20.drop(df_t20.index[0])
df_t20 = df_t20.astype({i: "float" for i in df_t20.columns[2:]})
df_t20 = df_t20.rename(columns={
    '가격이 비싸도 프리미엄(고급)제품을 구입하겠다': '프리미엄 제품',
    '가격이 비싸도 다양하고 새로운 맛을 첨가한 제품을 구입하겠다': '새롭고 다양한 맛',
    '가격이 비싸도 건강에 좋은 원료 안전성이 확보된 제품을 구입하겠다': '원료 안전성',
    '가격이 비싸도 소포장 사용 및 취식/조리가 간편화된 제품을 구입하겠다': '소포장, 조리 간편화',
    '제품의 업그레이드/신제품 개발과 관계없이 가격만 저렴하면 구입하겠다': '오로지 가격'
})

df_t21 = df_21.rename(columns=df_21.iloc[0])
df_t21 = df_t21.drop(df_t21.index[0])
df_t21 = df_t21.astype({i: "float" for i in df_t21.columns[2:]})
df_t21 = df_t21.rename(columns={
    '건강(영양)에 좋은 제품을 구입하겠다': '건강한 제품',
    '원료의 품질과 안전성이 확보된 제품 구입하겠다': '원료 안전성',
    '다양하고 새로운 맛을 낸 제품 구입하겠다': '새롭고 다양한 맛',
    '소포장 사용 및 취식·조리 간편화된 제품 구입하겠다': '소포장, 조리 간편화',
    '제품의 업그레이드/신제품 개발과 관계없이 가격만 저렴하면 구입하겠다': '오로지 가격'
})


with st.expander('데이터프레임 보기🧾'):
    st.write("### 2019년")
    st.dataframe(df_t19)
    st.write("### 2020년")
    st.dataframe(df_t20)
    st.write("### 2021년")
    st.dataframe(df_t21)

my_order = ['가구원수별', '성별', '연령별']
status = st.radio('그래프 선택', my_order)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


if status == my_order[0]:
    st.markdown("### 식품소비 가구원수별 동조성 📈")

    df_19_c = df_t19[df_t19['특성별(1)'] == '가구원수별'].drop(['특성별(1)'], axis=1).set_index('특성별(2)').rename_axis('가구원수별')
    df_20_c = df_t20[df_t20['특성별(1)'] == '가구원수별'].drop(['특성별(1)'], axis=1).set_index('특성별(2)').rename_axis('가구원수별')
    df_21_c = df_t21[df_t21['특성별(1)'] == '가구원수별'].drop(['특성별(1)'], axis=1).set_index('특성별(2)').rename_axis('가구원수별')

    fig1, ax1 = plt.subplots(figsize=(25, 10))
    df_19_c.T.plot(kind='bar', ax=ax1, rot=0, fontsize=25)
    ax1.set_title("2019년 가구원수별", fontsize=30)
    ax1.legend(fontsize=20, bbox_to_anchor=(1.2, 1))
    st.pyplot(fig1)
    plt.close(fig1)

    fig2, ax2 = plt.subplots(figsize=(25, 10))
    df_20_c.T.plot(kind='bar', ax=ax2, rot=0, fontsize=25)
    ax2.set_title("2020년 가구원수별", fontsize=30)
    ax2.legend(fontsize=20, bbox_to_anchor=(1.2, 1))
    st.pyplot(fig2)
    plt.close(fig2)

    fig3, ax3 = plt.subplots(figsize=(25, 10))
    df_21_c.T.plot(kind='bar', ax=ax3, rot=0, fontsize=25)
    ax3.set_title("2021년 가구원수별", fontsize=30)
    ax3.legend(fontsize=20, bbox_to_anchor=(1.2, 1))
    st.pyplot(fig3)
    plt.close(fig3)

elif status == my_order[1]:
    st.markdown("### 식품소비 성별 동조성 📈")

    my_order1 = ['2019년', '2020년', '2021년']
    status1 = st.radio('년도 선택', my_order1)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    if status1 == my_order1[0]:
        st.write("### 2019년")
        df19_s = df_t19[df_t19['특성별(1)'] == '가구주성별'].drop(['특성별(1)'], axis=1)
        df19_s = df19_s.rename(columns={'특성별(2)': '성별'})
        d19 = df19_s.set_index('성별').T

        fig1, ax1 = plt.subplots()
        explode = [0.06, 0.02, 0.01, 0.02, 0.04]
        colors = ['whitesmoke', 'yellow', 'cornflowerblue', 'lightgreen', 'lightgray']
        ax1.pie(d19['남성'], labels=d19.index, autopct='%.1f%%', counterclock=False, explode=explode, colors=colors)
        ax1.set_title('2019년 남성')
        st.pyplot(fig1)
        plt.close(fig1)

        fig2, ax2 = plt.subplots()
        colors = ['whitesmoke', 'yellow', 'lightsalmon', 'lightgreen', 'lightgray']
        ax2.pie(d19['여성'], labels=d19.index, autopct='%.1f%%', counterclock=False, explode=explode, colors=colors)
        ax2.set_title('2019년 여성')
        st.pyplot(fig2)
        plt.close(fig2)

    elif status1 == my_order1[1]:
        st.write("### 2020년")
        df20_s = df_t20[df_t20['특성별(1)'] == '가구주성별'].drop(['특성별(1)'], axis=1)
        df20_s = df20_s.rename(columns={'특성별(2)': '성별'})
        d20 = df20_s.set_index('성별').T

        fig1, ax1 = plt.subplots()
        explode = [0.06, 0.02, 0.01, 0.02, 0.04]
        colors = ['whitesmoke', 'yellow', 'cornflowerblue', 'lightgreen', 'lightgray']
        ax1.pie(d20['남성'], labels=d20.index, autopct='%.1f%%', counterclock=False, explode=explode, colors=colors)
        ax1.set_title('2020년 남성')
        st.pyplot(fig1)
        plt.close(fig1)

        fig2, ax2 = plt.subplots()
        colors = ['whitesmoke', 'yellow', 'lightsalmon', 'lightgreen', 'lightgray']
        ax2.pie(d20['여성'], labels=d20.index, autopct='%.1f%%', counterclock=False, explode=explode, colors=colors)
        ax2.set_title('2020년 여성')
        st.pyplot(fig2)
        plt.close(fig2)

    elif status1 == my_order1[2]:
        st.write("### 2021년")
        df21_s = df_t21[df_t21['특성별(1)'] == '가구주성별'].drop(['특성별(1)'], axis=1)
        df21_s = df21_s.rename(columns={'특성별(2)': '성별'})
        d21 = df21_s.set_index('성별').T

        fig1, ax1 = plt.subplots()
        explode = [0.06, 0.02, 0.01, 0.02, 0.04]
        colors = ['sandybrown', 'cornflowerblue', 'yellow', 'lightgreen', 'lightgray']
        ax1.pie(d21['남성'], labels=d21.index, autopct='%.1f%%', counterclock=False, explode=explode, colors=colors)
        ax1.set_title('2021년 남성')
        st.pyplot(fig1)
        plt.close(fig1)

        fig2, ax2 = plt.subplots()
        colors = ['sandybrown', 'lightsalmon', 'yellow', 'lightgreen', 'lightgray']
        ax2.pie(d21['여성'], labels=d21.index, autopct='%.1f%%', counterclock=False, explode=explode, colors=colors)
        ax2.set_title('2021년 여성')
        st.pyplot(fig2)
        plt.close(fig2)

elif status == my_order[2]:
    st.markdown("### 식품소비 연령별 동조성 📈")

    df_19_a = df_t19[df_t19['특성별(1)'] == '가구주연령별'].drop(['특성별(1)'], axis=1).set_index('특성별(2)').rename_axis('연령별')
    df_20_a = df_t20[df_t20['특성별(1)'] == '가구주연령별'].drop(['특성별(1)'], axis=1).set_index('특성별(2)').rename_axis('연령별')
    df_21_a = df_t21[df_t21['특성별(1)'] == '가구주연령별'].drop(['특성별(1)'], axis=1).set_index('특성별(2)').rename_axis('연령별')

    fig1, ax1 = plt.subplots(figsize=(25, 10))
    df_19_a.T.plot(kind='bar', ax=ax1, rot=0, fontsize=25)
    ax1.set_title("2019년 연령별", fontsize=30)
    ax1.legend(fontsize=20, bbox_to_anchor=(1.2, 1))
    st.pyplot(fig1)
    plt.close(fig1)

    fig2, ax2 = plt.subplots(figsize=(25, 10))
    df_20_a.T.plot(kind='bar', ax=ax2, rot=0, fontsize=25)
    ax2.set_title("2020년 연령별", fontsize=30)
    ax2.legend(fontsize=20, bbox_to_anchor=(1.2, 1))
    st.pyplot(fig2)
    plt.close(fig2)

    fig3, ax3 = plt.subplots(figsize=(25, 10))
    df_21_a.T.plot(kind='bar', ax=ax3, rot=0, fontsize=25)
    ax3.set_title("2021년 연령별", fontsize=30)
    ax3.legend(fontsize=20, bbox_to_anchor=(1.2, 1))
    st.pyplot(fig3)
    plt.close(fig3)
