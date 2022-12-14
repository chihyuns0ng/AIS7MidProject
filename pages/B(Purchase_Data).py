import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import koreanize_matplotlib

st.set_page_config(
    page_title="๐์ผ๋ก ๋จธ์คํฌ MID๐",
    page_icon="โญ๏ธ",
    layout="wide",
)

url = "https://raw.githubusercontent.com/hj2628/AIS7MidProject/main/2019_%E1%84%80%E1%85%AE%E1%84%86%E1%85%A2%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5_%E1%84%8B%E1%85%AF%E1%86%AF%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%91%E1%85%AE%E1%86%B7%E1%84%86%E1%85%A9%E1%86%A8%E1%84%80%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%80%E1%85%AE%E1%84%86%E1%85%A2%E1%84%8E%E1%85%AE%E1%84%8B%E1%85%B5"

url_2 = "https://raw.githubusercontent.com/hj2628/AIS7MidProject/main/2020_%E1%84%80%E1%85%AE%E1%84%86%E1%85%A2%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5_%E1%84%8B%E1%85%AF%E1%86%AF%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%91%E1%85%AE%E1%86%B7%E1%84%86%E1%85%A9%E1%86%A8%E1%84%80%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%80%E1%85%AE%E1%84%86%E1%85%A2%E1%84%8E%E1%85%AE%E1%84%8B%E1%85%B5"

url_3 = "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/purchase_data.csv"


@st.cache
def load_data(url):
    data = pd.read_csv(url)
    return data

@st.cache
def load_data(url_2):
    data_2 = pd.read_csv(url_2)
    return data_2

@st.cache(allow_output_mutation=True)
def load_data(url_3):
    data_3 = pd.read_csv(url_3)
    return data_3


data = load_data(url)
data_2 = load_data(url_2)
data_3 = load_data(url_3)

st.markdown("# 19~20๋๋ ๊ตฌ๋งค๋ฐ์ดํฐ๐")

with st.expander('๋ฐ์ดํฐํ๋ ์ ๋ณด๊ธฐ๐งพ'):
    st.dataframe(data)
    st.dataframe(data_2)
    st.dataframe(data_3)

pxh = px.histogram(data, x="์", y="Sales_Unit", color="MasterCategoryFullName", histfunc="sum", barmode="group", title="19๋ ํ๋ชฉ๋ณ ๊ตฌ๋งค์ถ์ด")
st.plotly_chart(pxh)


pxh = px.histogram(data_2, x="์", y="Sales_Unit", color="MasterCategoryFullName", histfunc="sum", barmode="group", title="20๋ ํ๋ชฉ๋ณ ๊ตฌ๋งค์ถ์ด")
st.plotly_chart(pxh)


if st.button('SUMMARY'):
    data_3.index = data_3["MasterCategoryFullName"]
    data_3 = data_3.drop("MasterCategoryFullName", axis=1)

    data_3.loc["Others"] = 0
    data_3.loc["Others"]["Sales_Unit"] = data_3["Sales_Unit"][5:].sum()
    data_3.loc["Others"]["count"] = data_3["count"][5:].sum()


    data_3 = data_3.drop(["์์ ยท ๊ณผ์ ยท ๋ผ๋ฉด ยท ์ปคํผ", "์์  ยท ๊ฑดํด์ฐ๋ฌผ", "์ฃผ๋ฅ", "์นํจ ยท ์ด๋ฐฅ ยท ๋ฒ ์ด์ปค๋ฆฌ"
                          , "๊ฒฌ๊ณผ ยท ์ ์ ยท ์ฐจ๋ฅ", "์ ยท ์ก๊ณก", "์ฅ ๊ฑด๊ฐ", "ํ์ผ ยท ๋ฉด์ญ", "๋นํ๋ฏผ ยท ๋ฏธ๋ค๋", "๊ฑด๊ฐ์์ฌ ยท ๊ฟ"])


    fig = plt.pie(data_3["count"], labels=data_3.index, startangle=180, autopct='%1.1f%%', counterclock=False, wedgeprops=dict(width=0.5)
                  , explode=(0.1, 0, 0, 0, 0), colors = ['lightskyblue', 'lightgreen', 'bisque', 'salmon', 'lightgray'])
    plt.legend(bbox_to_anchor=(2,1))
    st.pyplot()
