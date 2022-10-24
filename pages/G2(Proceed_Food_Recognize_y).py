import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import koreanize_matplotlib

st.set_page_config(
    page_title="가공식품 가격에 대한 인식",
    page_icon="🚀",
    layout="wide",
)

st.markdown("# 가공 식품 가격 상승 인식도 📈")

st.set_option('deprecation.showPyplotGlobalUse', False)

url1="https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/%E1%84%80%E1%85%A1%E1%84%80%E1%85%A9%E1%86%BC%E1%84%89%E1%85%B5%E1%86%A8%E1%84%91%E1%85%AE%E1%86%B7_%E1%84%80%E1%85%A1%E1%84%80%E1%85%A7%E1%86%A8%E1%84%8B%E1%85%A6_%E1%84%83%E1%85%A2%E1%84%92%E1%85%A1%E1%86%AB_%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8_2019.csv"
url2="https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/%EA%B0%80%EA%B3%B5%EC%8B%9D%ED%92%88_%EA%B0%80%EA%B2%A9%EC%97%90_%EB%8C%80%ED%95%9C_%EC%9D%B8%EC%8B%9D_2020.csv"
url3="https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/%EA%B0%80%EA%B3%B5%EC%8B%9D%ED%92%88_%EA%B0%80%EA%B2%A9%EC%97%90_%EB%8C%80%ED%95%9C_%EC%9D%B8%EC%8B%9D_2021.csv"

df_2019 = pd.read_csv(url1, encoding="cp949")
df_2020 = pd.read_csv(url2, encoding="cp949")
df_2021 = pd.read_csv(url3, encoding="cp949")


df_2019=df_2019[~df_2019['특성별(2)'].str.contains('소계')]
df_2019=df_2019.drop(columns=['특성별(1)', '시점', '전혀 그렇지 않다 (%)'], axis=1)
df_2019=df_2019.reset_index(drop=True)

df_2019 = df_2019.rename(columns={"인식별(1)" : "인식", "그렇지 않은 편이다 (%)":"그렇지 않은 편이다", 
                                  "보통이다/그저 그렇다 (%)":"보통이다",
                                  "그런 편이다 (%)":"그런 편이다", "매우 그렇다 (%)":"매우 그렇다"})
df_2019_num = df_2019.iloc[0:20]
df_2019_num = df_2019_num.rename(columns={"특성별(2)": "가구원 수"})
df_2019_num = df_2019_num.set_index("가구원 수")


df_2020=df_2020[~df_2020['특성별(2)'].str.contains('소계')]
df_2020=df_2020.drop(columns=['특성별(1)', '시점', '전혀 그렇지 않다 (%)'], axis=1)
df_2020=df_2020.reset_index(drop=True)

df_2020 = df_2020.rename(columns={"인식별(1)" : "인식", "그렇지 않은 편이다 (%)":"그렇지 않은 편이다", 
                                  "보통이다/그저 그렇다 (%)":"보통이다",
                                  "그런 편이다 (%)":"그런 편이다", "매우 그렇다 (%)":"매우 그렇다"})
df_2020_num = df_2020.iloc[0:20]
df_2020_num = df_2020_num.rename(columns={"특성별(2)": "가구원 수"})
df_2020_num = df_2020_num.set_index("가구원 수")


df_2021=df_2021[~df_2021['특성별(2)'].str.contains('소계')]
df_2021=df_2021.drop(columns=['특성별(1)', '시점', '전혀 그렇지 않다 (%)'], axis=1)
df_2021=df_2021.reset_index(drop=True)
df_2021=df_2021.rename(columns={"인식별(1)" : "인식", "그렇지 않은 편이다 (%)":"그렇지 않은 편이다", 
                                  "보통이다/그저 그렇다 (%)":"보통이다",
                                  "그런 편이다 (%)":"그런 편이다", "매우 그렇다 (%)":"매우 그렇다"})
df_2021_num = df_2021.iloc[0:20]
df_2021_num = df_2021_num.rename(columns={"특성별(2)": "가구원 수"})
df_2021_num = df_2021_num.set_index("가구원 수")

with st.expander('데이터프레임 보기') :
    st.dataframe(df_2019)
    st.dataframe(df_2020)
    st.dataframe(df_2021)

my_order = ['가구원수별', '성별', '연령별']
    
status = st.radio('그래프 선택', my_order)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    # 첫번째 방법
if status == my_order[0] :
    st.write("""
    ### 가구원수별
    """)
    df_2019_num_3=df_2019_num[df_2019_num['인식'].str.contains('전년에 비해 올해 가공식품 가격이 많이 상승했다')]
    df_2019_num_3= df_2019_num_3.drop(columns=['인식'], axis=1)

    df_2020_num_3=df_2020_num[df_2020_num['인식'].str.contains('전년에 비해 올해 가공식품 가격이 많이 상승했다')]
    df_2020_num_3= df_2020_num_3.drop(columns=['인식'], axis=1)

    df_2021_num_3=df_2021_num[df_2021_num['인식'].str.contains('전년에 비해 올해 가공식품 가격이 많이 상승했다')]
    df_2021_num_3= df_2021_num_3.drop(columns=['인식'], axis=1)


    df_2019_num_3.T.plot(kind="bar", figsize=(30,10),fontsize=25, rot=0)
    plt.title("2019년 가구원수별 전년 대비 가공 식품 가격 상승 인식", fontsize=25)
    plt.legend(fontsize=20, bbox_to_anchor=(1.1,1))
    st.pyplot(plt.show())

    df_2020_num_3.T.plot(kind="bar", figsize=(30,10),fontsize=25, rot=0)
    plt.title("2020년 가구원수별 전년 대비 가공 식품 가격 상승 인식", fontsize=25)
    plt.legend(fontsize=20, bbox_to_anchor=(1.1,1))
    st.pyplot(plt.show())

    df_2021_num_3.T.plot(kind="bar", figsize=(30,10),fontsize=25, rot=0)
    plt.title("2021년 가구원수별 전년 대비 가공 식품 가격 상승 인식", fontsize=25)
    plt.legend(fontsize=20, bbox_to_anchor=(1.1,1))
    st.pyplot(plt.show())

if status == my_order[1] :
    st.write("""
    ### 성별
    """)
    df_2019_gen = df_2019.iloc[20:28]
    df_2019_gen = df_2019_gen.rename(columns={"특성별(2)": "성별"})
    df_2019_gen = df_2019_gen.set_index("성별")

    df_2019_gen_3=df_2019_gen[df_2019_gen['인식'].str.contains('전년에 비해 올해 가공식품 가격이 많이 상승했다')]
    df_2019_gen_3= df_2019_gen_3.drop(columns=['인식'], axis=1)


    df_2020_gen = df_2020.iloc[20:28]
    df_2020_gen = df_2020_gen.rename(columns={"특성별(2)": "성별"})
    df_2020_gen = df_2020_gen.set_index("성별")

    df_2020_gen_3=df_2020_gen[df_2020_gen['인식'].str.contains('전년에 비해 올해 가공식품 가격이 많이 상승했다')]
    df_2020_gen_3= df_2020_gen_3.drop(columns=['인식'], axis=1)


    df_2021_gen = df_2021.iloc[20:28]
    df_2021_gen = df_2021_gen.rename(columns={"특성별(2)": "성별"})
    df_2021_gen = df_2021_gen.set_index("성별")

    df_2021_gen_3=df_2021_gen[df_2021_gen['인식'].str.contains('전년에 비해 올해 가공식품 가격이 많이 상승했다')]
    df_2021_gen_3= df_2021_gen_3.drop(columns=['인식'], axis=1)


    df_2019_gen_3.T.plot(kind="bar", figsize=(30,10),fontsize=25, rot=0)
    plt.title("2019년 성별 전년 대비 가공 식품 가격 상승 인식", fontsize=25)
    plt.legend(fontsize=20, bbox_to_anchor=(1.1,1))
    st.pyplot(plt.show())

    df_2020_gen_3.T.plot(kind="bar", figsize=(30,10),fontsize=25, rot=0)
    plt.title("2020년 성별 전년 대비 가공 식품 가격 상승 인식", fontsize=25)
    plt.legend(fontsize=20, bbox_to_anchor=(1.1,1))
    st.pyplot(plt.show())

    df_2021_gen_3.T.plot(kind="bar", figsize=(30,10),fontsize=25, rot=0)
    plt.title("2021년 성별 전년 대비 가공 식품 가격 상승 인식", fontsize=25)
    plt.legend(fontsize=20, bbox_to_anchor=(1.1,1))
    st.pyplot(plt.show())

if status == my_order[2] :
    st.write("""
    ### 연령별
    """)
    df_2019_age = df_2019.iloc[28:]
    df_2019_age = df_2019_age.rename(columns={"특성별(2)": "연령별"})
    df_2019_age = df_2019_age.set_index("연령별")

    df_2019_age_3=df_2019_age[df_2019_age['인식'].str.contains('전년에 비해 올해 가공식품 가격이 많이 상승했다')]
    df_2019_age_3= df_2019_age_3.drop(columns=['인식'], axis=1)


    df_2020_age = df_2020.iloc[28:]
    df_2020_age = df_2020_age.rename(columns={"특성별(2)": "성별"})
    df_2020_age = df_2020_age.set_index("성별")

    df_2020_age_3=df_2020_age[df_2020_age['인식'].str.contains('전년에 비해 올해 가공식품 가격이 많이 상승했다')]
    df_2020_age_3= df_2020_age_3.drop(columns=['인식'], axis=1)


    df_2021_age = df_2021.iloc[28:]
    df_2021_age = df_2021_age.rename(columns={"특성별(2)": "연령별"})
    df_2021_age = df_2021_age.set_index("연령별")

    df_2021_age_3=df_2021_age[df_2021_age['인식'].str.contains('전년에 비해 올해 가공식품 가격이 많이 상승했다')]
    df_2021_age_3= df_2021_age_3.drop(columns=['인식'], axis=1)


    df_2019_age_3.T.plot(kind="bar", figsize=(30,10),fontsize=25, rot=0)
    plt.title("2019년 연령별 전년 대비 가공 식품 가격 상승 인식", fontsize=25)
    plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
    st.pyplot(plt.show())

    df_2020_age_3.T.plot(kind="bar", figsize=(30,10),fontsize=25, rot=0)
    plt.title("2020년 연령별 전년 대비 가공 식품 가격 상승 인식", fontsize=25)
    plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
    st.pyplot(plt.show())

    df_2021_age_3.T.plot(kind="bar", figsize=(30,10),fontsize=25, rot=0)
    plt.title("2021년 연령별 전년 대비 가공 식품 가격 상승 인식", fontsize=25)
    plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
    st.pyplot(plt.show())
