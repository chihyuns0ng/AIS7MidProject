import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import koreanize_matplotlib

st.set_page_config(
    page_title="MID_일론머스크",
    page_icon="🚀",
    layout="wide",
)

st.markdown("# 식품소비 성별 동조성 📈")


url19 = 'https://raw.githubusercontent.com/HyenC/AIS7MidProject/main/data/%E1%84%89%E1%85%B5%E1%86%A8%E1%84%91%E1%85%AE%E1%86%B7%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5_%E1%84%90%E1%85%B3%E1%84%85%E1%85%A6%E1%86%AB%E1%84%83%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8C%E1%85%A9%E1%84%89%E1%85%A5%E1%86%BC_19.csv'
url20 = 'https://raw.githubusercontent.com/HyenC/AIS7MidProject/main/data/%E1%84%89%E1%85%B5%E1%86%A8%E1%84%91%E1%85%AE%E1%86%B7%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5_%E1%84%90%E1%85%B3%E1%84%85%E1%85%A6%E1%86%AB%E1%84%83%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8C%E1%85%A9%E1%84%89%E1%85%A5%E1%86%BC_20.csv'
url21 = 'https://raw.githubusercontent.com/HyenC/AIS7MidProject/main/data/%E1%84%89%E1%85%B5%E1%86%A8%E1%84%91%E1%85%AE%E1%86%B7%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5_%E1%84%90%E1%85%B3%E1%84%85%E1%85%A6%E1%86%AB%E1%84%83%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8C%E1%85%A9%E1%84%89%E1%85%A5%E1%86%BC_21.csv'

@st.cache
def load_data(url19):
    df_19 = pd.read_csv(url19, encoding='cp949')
    return df_19

@st.cache
def load_data(url20):
    df_20 = pd.read_csv(url20, encoding='cp949')
    return df_20

@st.cache
def load_data(url21):
    df_21 = pd.read_csv(url21, encoding='cp949')
    return df_21

df_19 = load_data(url19)
df_20 = load_data(url20)
df_21 = load_data(url21)


df_t19 = df_19.rename(columns=df_19.iloc[0])
df_t19 = df_t19.drop(df_t19.index[0])
df_t19 = df_t19.astype({i:"float" for i in df_t19.columns[2:]})

df_t20 = df_20.rename(columns=df_20.iloc[0])
df_t20 = df_t20.drop(df_t20.index[0])
df_t20 = df_t20.astype({i:"float" for i in df_t20.columns[2:]})

df_t21 = df_21.rename(columns=df_21.iloc[0])
df_t21 = df_t21.drop(df_t21.index[0])
df_t21 = df_t21.astype({i:"float" for i in df_t21.columns[2:]})


df19_s = df_t19[df_t19['특성별(1)'] == '가구주성별']
df_19_s = df19_s.drop(['특성별(1)'], axis=1)
# df_19_s = df_19_s.set_index(keys='특성별(2)')
df_19_s = df_19_s.rename(columns={'특성별(1)':'성별'})
df19 = df19_s.drop(['특성별(1)'], axis=1)
df19 = df19.rename(columns={'특성별(2)':'성별'                            
                            ,'가격이 비싸도 프리미엄(고급)제품을 구입하겠다':'프리미엄 제품'
                            ,'가격이 비싸도 다양하고 새로운 맛을 첨가한 제품을 구입하겠다':'새롭고 다양한 맛'
                            ,'가격이 비싸도 건강에 좋은 원료 안전성이 확보된 제품을 구입하겠다':'원료 안전성'
                            ,'가격이 비싸도 소포장 사용 및 취식/조리가 간편화된 제품을 구입하겠다':'소포장, 조리 간편화'
                            ,'제품의 업그레이드/신제품 개발과 관계없이 가격만 저렴하면 구입하겠다':'오로지 가격'})
d19 = df19.T
d19 = d19.rename(columns=d19.iloc[0])
d19 = d19.drop(d19.index[0])


df20_s = df_t20[df_t20['특성별(1)'] == '가구주성별']
df_20_s = df20_s.drop(['특성별(1)'], axis=1)
# df_20_s = df_20_s.set_index(keys='특성별(2)')
df_20_s = df_20_s.rename(columns={'특성별(1)':'성별'})
df20 = df20_s.drop(['특성별(1)'], axis=1)
df20 = df20.rename(columns={'특성별(2)':'성별'                            
                            ,'가격이 비싸도 프리미엄(고급)제품을 구입하겠다':'프리미엄 제품'
                            ,'가격이 비싸도 다양하고 새로운 맛을 첨가한 제품을 구입하겠다':'새롭고 다양한 맛'
                            ,'가격이 비싸도 건강에 좋은 원료 안전성이 확보된 제품을 구입하겠다':'원료 안전성'
                            ,'가격이 비싸도 소포장 사용 및 취식/조리가 간편화된 제품을 구입하겠다':'소포장, 조리 간편화'
                            ,'제품의 업그레이드/신제품 개발과 관계없이 가격만 저렴하면 구입하겠다':'오로지 가격'})
d20 = df20.T
d20 = d20.rename(columns=d20.iloc[0])
d20 = d20.drop(d20.index[0])


df21_s = df_t21[df_t21['특성별(1)'] == '가구주성별']
df_21_s = df21_s.drop(['특성별(1)'], axis=1)
# df_21_s = df_21_s.set_index(keys='특성별(2)')
df_21_s = df_21_s.rename(columns={'특성별(1)':'성별'})
df21 = df21_s.drop(['특성별(1)'], axis=1)
df21 = df21.rename(columns={'특성별(2)':'성별'
                            ,'건강(영양)에 좋은 제품을 구입하겠다':'건강한 제품'
                            ,'원료의 품질과 안전성이 확보된 제품 구입하겠다':'원료 안전성'
                            ,'다양하고 새로운 맛을 낸 제품 구입하겠다':'새롭고 다양한 맛'
                            ,'소포장 사용 및 취식·조리 간편화된 제품 구입하겠다':'소포장, 조리 간편화'
                            ,'제품의 업그레이드/신제품 개발과 관계없이 가격만 저렴하면 구입하겠다':'오로지 가격'})
d21 = df21.T
d21 = d21.rename(columns=d21.iloc[0])
d21 = d21.drop(d21.index[0])


st.set_option('deprecation.showPyplotGlobalUse', False)

st.write("""
### 2019년
""")
explode = [0.06, 0.02, 0.01, 0.02, 0.04]
colors = ['whitesmoke','yellow','cornflowerblue','lightgreen', 'lightgray']
fig = plt.pie(d19['남성'], labels=d19.index, autopct='%.1f%%', counterclock=False, explode=explode, colors=colors)
plt.title('2019년', size = 15)
st.pyplot(plt.show())

explode = [0.06, 0.02, 0.01, 0.02, 0.04]
colors = ['whitesmoke','yellow','lightsalmon','lightgreen', 'lightgray']
fig = plt.pie(d19['여성'], labels=d19.index, autopct='%.1f%%', counterclock=False, explode=explode , colors=colors)
plt.title('2019년', size = 15)
st.pyplot(plt.show())

st.write("""
### 2020년
""")
explode = [0.06, 0.02, 0.01, 0.02, 0.04]
colors = ['whitesmoke','yellow','cornflowerblue','lightgreen', 'lightgray']
fig = plt.pie(d20['남성'], labels=d20.index, autopct='%.1f%%', counterclock=False, explode=explode, colors=colors)
plt.title('2020년', size = 15)
st.pyplot(plt.show())

explode = [0.06, 0.02, 0.01, 0.02, 0.04]
colors = ['whitesmoke','yellow','lightsalmon','lightgreen', 'lightgray']
fig = plt.pie(d20['여성'], labels=d20.index, autopct='%.1f%%', counterclock=False, explode=explode , colors=colors)
plt.title('2020년', size = 15)
st.pyplot(plt.show())

st.write("""
### 2021년
""")
explode = [0.06, 0.02, 0.01, 0.02, 0.04]
colors = ['sandybrown','cornflowerblue','yellow','lightgreen', 'lightgray']
fig = plt.pie(d21['남성'], labels=d21.index, autopct='%.1f%%', counterclock=False, explode=explode, colors=colors)
plt.title('2021년', size = 15)
st.pyplot(plt.show())

explode = [0.06, 0.02, 0.01, 0.02, 0.04]
colors = ['sandybrown','lightsalmon','yellow','lightgreen', 'lightgray']
fig = plt.pie(d21['여성'], labels=d21.index, autopct='%.1f%%', counterclock=False, explode=explode , colors=colors)
plt.title('2021년', size = 15)
st.pyplot(plt.show())
