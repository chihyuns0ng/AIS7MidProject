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

st.markdown("# ๊ฐํธ์ ๊ตฌ์ํ์ง ์๋ ์ด์ ๐")


url21 = 'https://raw.githubusercontent.com/HyenC/AIS7MidProject/main/data/%E1%84%80%E1%85%A1%E1%86%AB%E1%84%91%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8_%E1%84%80%E1%85%AE%E1%84%8B%E1%85%B5%E1%86%B8%E1%84%92%E1%85%A1%E1%84%8C%E1%85%B5_%E1%84%8B%E1%85%A1%E1%86%AD%E1%84%82%E1%85%B3%E1%86%AB_%E1%84%8B%E1%85%B5%E1%84%8B%E1%85%B2_21.csv'

@st.cache
def load_data(url21):
    df_21 = pd.read_csv(url21, encoding='cp949')
    return df_21

df_21 = load_data(url21)


@st.cache
def load_data(url21):
    df_21 = pd.read_csv(url21, encoding='cp949')
    return df_21

df_21 = load_data(url21)

df_t21 = df_21.rename(columns=df_21.iloc[0])
df_t21 = df_t21.drop(df_t21.index[0])
with st.expander('๋ฐ์ดํฐํ๋ ์ ๋ณด๊ธฐ๐งพ'):
    st.dataframe(df_t21)
df_t21 = df_t21.drop(columns=['์ ํ์ด ๋ค์ํ์ง ์์์','๊ธฐํ'])
df_t21 = df_t21.astype({i:"float" for i in df_t21.columns[2:]})


df21_a = df_t21[df_t21['ํน์ฑ๋ณ(1)'] == '๊ฐ๊ตฌ์ฃผ์ฐ๋ น๋ณ']
df_21_a = df21_a.drop(['ํน์ฑ๋ณ(1)'], axis=1)
df_21_a = df_21_a.set_index(keys='ํน์ฑ๋ณ(2)')
df_21_a = df_21_a.rename_axis('์ฐ๋ น๋ณ')

df21_c = df_t21[df_t21['ํน์ฑ๋ณ(1)'] == '๊ฐ๊ตฌ์์๋ณ']
df_21_c = df21_c.drop(['ํน์ฑ๋ณ(1)'], axis=1)
df_21_c = df_21_c.set_index(keys='ํน์ฑ๋ณ(2)')
df_21_c = df_21_c.rename_axis('๊ฐ๊ตฌ์์๋ณ')

df21_s = df_t21[df_t21['ํน์ฑ๋ณ(1)'] == '๊ฐ๊ตฌ์ฃผ์ฑ๋ณ']
df_21_s = df21_s.drop(['ํน์ฑ๋ณ(1)'], axis=1)
df_21_s = df_21_s.set_index(keys='ํน์ฑ๋ณ(2)')
df_21_s = df_21_s.rename_axis('์ฑ๋ณ')


df_21_c.T.plot(kind='barh', figsize=(25,12), rot=0, fontsize=20)
plt.title("๊ฐ๊ตฌ์์๋ณ ๊ฐํธ์์ ๊ตฌ์ํ์ง ์๋ ์ด์ ", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())

df_21_s.T.plot(kind='barh', figsize=(25,12), rot=0, fontsize=20)
plt.title("์ฑ๋ณ ๊ฐํธ์์ ๊ตฌ์ํ์ง ์๋ ์ด์ ", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())

df_21_a.T.plot(kind='barh', figsize=(25,12), rot=0, fontsize=20)
plt.title("์ฐ๋ น๋ณ ๊ฐํธ์์ ๊ตฌ์ํ์ง ์๋ ์ด์ ", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())
