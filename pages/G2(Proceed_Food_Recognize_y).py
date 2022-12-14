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

st.markdown("# ๊ฐ๊ณต ์ํ ๊ฐ๊ฒฉ ์์น ์ธ์๋๐")

st.set_option('deprecation.showPyplotGlobalUse', False)

url1="https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/%E1%84%80%E1%85%A1%E1%84%80%E1%85%A9%E1%86%BC%E1%84%89%E1%85%B5%E1%86%A8%E1%84%91%E1%85%AE%E1%86%B7_%E1%84%80%E1%85%A1%E1%84%80%E1%85%A7%E1%86%A8%E1%84%8B%E1%85%A6_%E1%84%83%E1%85%A2%E1%84%92%E1%85%A1%E1%86%AB_%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8_2019.csv"
url2="https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/%EA%B0%80%EA%B3%B5%EC%8B%9D%ED%92%88_%EA%B0%80%EA%B2%A9%EC%97%90_%EB%8C%80%ED%95%9C_%EC%9D%B8%EC%8B%9D_2020.csv"
url3="https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/%EA%B0%80%EA%B3%B5%EC%8B%9D%ED%92%88_%EA%B0%80%EA%B2%A9%EC%97%90_%EB%8C%80%ED%95%9C_%EC%9D%B8%EC%8B%9D_2021.csv"

df_2019 = pd.read_csv(url1, encoding="cp949")
df_2020 = pd.read_csv(url2, encoding="cp949")
df_2021 = pd.read_csv(url3, encoding="cp949")


df_2019=df_2019[~df_2019['ํน์ฑ๋ณ(2)'].str.contains('์๊ณ')]
df_2019=df_2019.drop(columns=['ํน์ฑ๋ณ(1)', '์์ ', '์ ํ ๊ทธ๋ ์ง ์๋ค (%)'], axis=1)
df_2019=df_2019.reset_index(drop=True)

df_2019 = df_2019.rename(columns={"์ธ์๋ณ(1)" : "์ธ์", "๊ทธ๋ ์ง ์์ ํธ์ด๋ค (%)":"๊ทธ๋ ์ง ์์ ํธ์ด๋ค", 
                                  "๋ณดํต์ด๋ค/๊ทธ์  ๊ทธ๋ ๋ค (%)":"๋ณดํต์ด๋ค",
                                  "๊ทธ๋ฐ ํธ์ด๋ค (%)":"๊ทธ๋ฐ ํธ์ด๋ค", "๋งค์ฐ ๊ทธ๋ ๋ค (%)":"๋งค์ฐ ๊ทธ๋ ๋ค"})
df_2019_num = df_2019.iloc[0:20]
df_2019_num = df_2019_num.rename(columns={"ํน์ฑ๋ณ(2)": "๊ฐ๊ตฌ์ ์"})
df_2019_num = df_2019_num.set_index("๊ฐ๊ตฌ์ ์")


df_2020=df_2020[~df_2020['ํน์ฑ๋ณ(2)'].str.contains('์๊ณ')]
df_2020=df_2020.drop(columns=['ํน์ฑ๋ณ(1)', '์์ ', '์ ํ ๊ทธ๋ ์ง ์๋ค (%)'], axis=1)
df_2020=df_2020.reset_index(drop=True)

df_2020 = df_2020.rename(columns={"์ธ์๋ณ(1)" : "์ธ์", "๊ทธ๋ ์ง ์์ ํธ์ด๋ค (%)":"๊ทธ๋ ์ง ์์ ํธ์ด๋ค", 
                                  "๋ณดํต์ด๋ค/๊ทธ์  ๊ทธ๋ ๋ค (%)":"๋ณดํต์ด๋ค",
                                  "๊ทธ๋ฐ ํธ์ด๋ค (%)":"๊ทธ๋ฐ ํธ์ด๋ค", "๋งค์ฐ ๊ทธ๋ ๋ค (%)":"๋งค์ฐ ๊ทธ๋ ๋ค"})
df_2020_num = df_2020.iloc[0:20]
df_2020_num = df_2020_num.rename(columns={"ํน์ฑ๋ณ(2)": "๊ฐ๊ตฌ์ ์"})
df_2020_num = df_2020_num.set_index("๊ฐ๊ตฌ์ ์")


df_2021=df_2021[~df_2021['ํน์ฑ๋ณ(2)'].str.contains('์๊ณ')]
df_2021=df_2021.drop(columns=['ํน์ฑ๋ณ(1)', '์์ ', '์ ํ ๊ทธ๋ ์ง ์๋ค (%)'], axis=1)
df_2021=df_2021.reset_index(drop=True)
df_2021=df_2021.rename(columns={"์ธ์๋ณ(1)" : "์ธ์", "๊ทธ๋ ์ง ์์ ํธ์ด๋ค (%)":"๊ทธ๋ ์ง ์์ ํธ์ด๋ค", 
                                  "๋ณดํต์ด๋ค/๊ทธ์  ๊ทธ๋ ๋ค (%)":"๋ณดํต์ด๋ค",
                                  "๊ทธ๋ฐ ํธ์ด๋ค (%)":"๊ทธ๋ฐ ํธ์ด๋ค", "๋งค์ฐ ๊ทธ๋ ๋ค (%)":"๋งค์ฐ ๊ทธ๋ ๋ค"})
df_2021_num = df_2021.iloc[0:20]
df_2021_num = df_2021_num.rename(columns={"ํน์ฑ๋ณ(2)": "๊ฐ๊ตฌ์ ์"})
df_2021_num = df_2021_num.set_index("๊ฐ๊ตฌ์ ์")

with st.expander('๋ฐ์ดํฐํ๋ ์ ๋ณด๊ธฐ๐งพ') :
    st.dataframe(df_2019)
    st.dataframe(df_2020)
    st.dataframe(df_2021)

my_order = ['๊ฐ๊ตฌ์์๋ณ', '์ฑ๋ณ', '์ฐ๋ น๋ณ']
    
status = st.radio('๊ทธ๋ํ ์ ํ', my_order)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    # ์ฒซ๋ฒ์งธ ๋ฐฉ๋ฒ
if status == my_order[0] :
    st.write("""
    ### ๊ฐ๊ตฌ์์๋ณ
    """)
    df_2019_num_3=df_2019_num[df_2019_num['์ธ์'].str.contains('์ ๋์ ๋นํด ์ฌํด ๊ฐ๊ณต์ํ ๊ฐ๊ฒฉ์ด ๋ง์ด ์์นํ๋ค')]
    df_2019_num_3= df_2019_num_3.drop(columns=['์ธ์'], axis=1)

    df_2020_num_3=df_2020_num[df_2020_num['์ธ์'].str.contains('์ ๋์ ๋นํด ์ฌํด ๊ฐ๊ณต์ํ ๊ฐ๊ฒฉ์ด ๋ง์ด ์์นํ๋ค')]
    df_2020_num_3= df_2020_num_3.drop(columns=['์ธ์'], axis=1)

    df_2021_num_3=df_2021_num[df_2021_num['์ธ์'].str.contains('์ ๋์ ๋นํด ์ฌํด ๊ฐ๊ณต์ํ ๊ฐ๊ฒฉ์ด ๋ง์ด ์์นํ๋ค')]
    df_2021_num_3= df_2021_num_3.drop(columns=['์ธ์'], axis=1)


    df_2019_num_3.T.plot(kind="bar", figsize=(30,10),fontsize=25, rot=0)
    plt.title("2019๋ ๊ฐ๊ตฌ์์๋ณ ์ ๋ ๋๋น ๊ฐ๊ณต ์ํ ๊ฐ๊ฒฉ ์์น ์ธ์", fontsize=25)
    plt.legend(fontsize=20, bbox_to_anchor=(1.1,1))
    st.pyplot(plt.show())

    df_2020_num_3.T.plot(kind="bar", figsize=(30,10),fontsize=25, rot=0)
    plt.title("2020๋ ๊ฐ๊ตฌ์์๋ณ ์ ๋ ๋๋น ๊ฐ๊ณต ์ํ ๊ฐ๊ฒฉ ์์น ์ธ์", fontsize=25)
    plt.legend(fontsize=20, bbox_to_anchor=(1.1,1))
    st.pyplot(plt.show())

    df_2021_num_3.T.plot(kind="bar", figsize=(30,10),fontsize=25, rot=0)
    plt.title("2021๋ ๊ฐ๊ตฌ์์๋ณ ์ ๋ ๋๋น ๊ฐ๊ณต ์ํ ๊ฐ๊ฒฉ ์์น ์ธ์", fontsize=25)
    plt.legend(fontsize=20, bbox_to_anchor=(1.1,1))
    st.pyplot(plt.show())

elif status == my_order[1] :
    st.write("""
    ### ์ฑ๋ณ
    """)
    df_2019_gen = df_2019.iloc[20:28]
    df_2019_gen = df_2019_gen.rename(columns={"ํน์ฑ๋ณ(2)": "์ฑ๋ณ"})
    df_2019_gen = df_2019_gen.set_index("์ฑ๋ณ")

    df_2019_gen_3=df_2019_gen[df_2019_gen['์ธ์'].str.contains('์ ๋์ ๋นํด ์ฌํด ๊ฐ๊ณต์ํ ๊ฐ๊ฒฉ์ด ๋ง์ด ์์นํ๋ค')]
    df_2019_gen_3= df_2019_gen_3.drop(columns=['์ธ์'], axis=1)


    df_2020_gen = df_2020.iloc[20:28]
    df_2020_gen = df_2020_gen.rename(columns={"ํน์ฑ๋ณ(2)": "์ฑ๋ณ"})
    df_2020_gen = df_2020_gen.set_index("์ฑ๋ณ")

    df_2020_gen_3=df_2020_gen[df_2020_gen['์ธ์'].str.contains('์ ๋์ ๋นํด ์ฌํด ๊ฐ๊ณต์ํ ๊ฐ๊ฒฉ์ด ๋ง์ด ์์นํ๋ค')]
    df_2020_gen_3= df_2020_gen_3.drop(columns=['์ธ์'], axis=1)


    df_2021_gen = df_2021.iloc[20:28]
    df_2021_gen = df_2021_gen.rename(columns={"ํน์ฑ๋ณ(2)": "์ฑ๋ณ"})
    df_2021_gen = df_2021_gen.set_index("์ฑ๋ณ")

    df_2021_gen_3=df_2021_gen[df_2021_gen['์ธ์'].str.contains('์ ๋์ ๋นํด ์ฌํด ๊ฐ๊ณต์ํ ๊ฐ๊ฒฉ์ด ๋ง์ด ์์นํ๋ค')]
    df_2021_gen_3= df_2021_gen_3.drop(columns=['์ธ์'], axis=1)


    df_2019_gen_3.T.plot(kind="bar", figsize=(30,10),fontsize=25, rot=0)
    plt.title("2019๋ ์ฑ๋ณ ์ ๋ ๋๋น ๊ฐ๊ณต ์ํ ๊ฐ๊ฒฉ ์์น ์ธ์", fontsize=25)
    plt.legend(fontsize=20, bbox_to_anchor=(1.1,1))
    st.pyplot(plt.show())

    df_2020_gen_3.T.plot(kind="bar", figsize=(30,10),fontsize=25, rot=0)
    plt.title("2020๋ ์ฑ๋ณ ์ ๋ ๋๋น ๊ฐ๊ณต ์ํ ๊ฐ๊ฒฉ ์์น ์ธ์", fontsize=25)
    plt.legend(fontsize=20, bbox_to_anchor=(1.1,1))
    st.pyplot(plt.show())

    df_2021_gen_3.T.plot(kind="bar", figsize=(30,10),fontsize=25, rot=0)
    plt.title("2021๋ ์ฑ๋ณ ์ ๋ ๋๋น ๊ฐ๊ณต ์ํ ๊ฐ๊ฒฉ ์์น ์ธ์", fontsize=25)
    plt.legend(fontsize=20, bbox_to_anchor=(1.1,1))
    st.pyplot(plt.show())

elif status == my_order[2] :
    st.write("""
    ### ์ฐ๋ น๋ณ
    """)
    df_2019_age = df_2019.iloc[28:]
    df_2019_age = df_2019_age.rename(columns={"ํน์ฑ๋ณ(2)": "์ฐ๋ น๋ณ"})
    df_2019_age = df_2019_age.set_index("์ฐ๋ น๋ณ")

    df_2019_age_3=df_2019_age[df_2019_age['์ธ์'].str.contains('์ ๋์ ๋นํด ์ฌํด ๊ฐ๊ณต์ํ ๊ฐ๊ฒฉ์ด ๋ง์ด ์์นํ๋ค')]
    df_2019_age_3= df_2019_age_3.drop(columns=['์ธ์'], axis=1)


    df_2020_age = df_2020.iloc[28:]
    df_2020_age = df_2020_age.rename(columns={"ํน์ฑ๋ณ(2)": "์ฑ๋ณ"})
    df_2020_age = df_2020_age.set_index("์ฑ๋ณ")

    df_2020_age_3=df_2020_age[df_2020_age['์ธ์'].str.contains('์ ๋์ ๋นํด ์ฌํด ๊ฐ๊ณต์ํ ๊ฐ๊ฒฉ์ด ๋ง์ด ์์นํ๋ค')]
    df_2020_age_3= df_2020_age_3.drop(columns=['์ธ์'], axis=1)


    df_2021_age = df_2021.iloc[28:]
    df_2021_age = df_2021_age.rename(columns={"ํน์ฑ๋ณ(2)": "์ฐ๋ น๋ณ"})
    df_2021_age = df_2021_age.set_index("์ฐ๋ น๋ณ")

    df_2021_age_3=df_2021_age[df_2021_age['์ธ์'].str.contains('์ ๋์ ๋นํด ์ฌํด ๊ฐ๊ณต์ํ ๊ฐ๊ฒฉ์ด ๋ง์ด ์์นํ๋ค')]
    df_2021_age_3= df_2021_age_3.drop(columns=['์ธ์'], axis=1)


    df_2019_age_3.T.plot(kind="bar", figsize=(30,10),fontsize=25, rot=0)
    plt.title("2019๋ ์ฐ๋ น๋ณ ์ ๋ ๋๋น ๊ฐ๊ณต ์ํ ๊ฐ๊ฒฉ ์์น ์ธ์", fontsize=25)
    plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
    st.pyplot(plt.show())

    df_2020_age_3.T.plot(kind="bar", figsize=(30,10),fontsize=25, rot=0)
    plt.title("2020๋ ์ฐ๋ น๋ณ ์ ๋ ๋๋น ๊ฐ๊ณต ์ํ ๊ฐ๊ฒฉ ์์น ์ธ์", fontsize=25)
    plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
    st.pyplot(plt.show())

    df_2021_age_3.T.plot(kind="bar", figsize=(30,10),fontsize=25, rot=0)
    plt.title("2021๋ ์ฐ๋ น๋ณ ์ ๋ ๋๋น ๊ฐ๊ณต ์ํ ๊ฐ๊ฒฉ ์์น ์ธ์", fontsize=25)
    plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
    st.pyplot(plt.show())
