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

st.markdown("# ์ํ์๋น ํธ๋ ๋๋ณ ๋์กฐ์ฑ๐")


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
df_t19 = df_t19.rename(columns={'๊ฐ๊ฒฉ์ด ๋น์ธ๋ ํ๋ฆฌ๋ฏธ์(๊ณ ๊ธ)์ ํ์ ๊ตฌ์ํ๊ฒ ๋ค':'ํ๋ฆฌ๋ฏธ์ ์ ํ'
                            ,'๊ฐ๊ฒฉ์ด ๋น์ธ๋ ๋ค์ํ๊ณ  ์๋ก์ด ๋ง์ ์ฒจ๊ฐํ ์ ํ์ ๊ตฌ์ํ๊ฒ ๋ค':'์๋กญ๊ณ  ๋ค์ํ ๋ง'
                            ,'๊ฐ๊ฒฉ์ด ๋น์ธ๋ ๊ฑด๊ฐ์ ์ข์ ์๋ฃ ์์ ์ฑ์ด ํ๋ณด๋ ์ ํ์ ๊ตฌ์ํ๊ฒ ๋ค':'์๋ฃ ์์ ์ฑ'
                            ,'๊ฐ๊ฒฉ์ด ๋น์ธ๋ ์ํฌ์ฅ ์ฌ์ฉ ๋ฐ ์ทจ์/์กฐ๋ฆฌ๊ฐ ๊ฐํธํ๋ ์ ํ์ ๊ตฌ์ํ๊ฒ ๋ค':'์ํฌ์ฅ, ์กฐ๋ฆฌ ๊ฐํธํ'
                            ,'์ ํ์ ์๊ทธ๋ ์ด๋/์ ์ ํ ๊ฐ๋ฐ๊ณผ ๊ด๊ณ์์ด ๊ฐ๊ฒฉ๋ง ์ ๋ ดํ๋ฉด ๊ตฌ์ํ๊ฒ ๋ค':'์ค๋ก์ง ๊ฐ๊ฒฉ'})

df_t20 = df_20.rename(columns=df_20.iloc[0])
df_t20 = df_t20.drop(df_t20.index[0])
df_t20 = df_t20.astype({i:"float" for i in df_t20.columns[2:]})
df_t20 = df_t20.rename(columns={'๊ฐ๊ฒฉ์ด ๋น์ธ๋ ํ๋ฆฌ๋ฏธ์(๊ณ ๊ธ)์ ํ์ ๊ตฌ์ํ๊ฒ ๋ค':'ํ๋ฆฌ๋ฏธ์ ์ ํ'
                            ,'๊ฐ๊ฒฉ์ด ๋น์ธ๋ ๋ค์ํ๊ณ  ์๋ก์ด ๋ง์ ์ฒจ๊ฐํ ์ ํ์ ๊ตฌ์ํ๊ฒ ๋ค':'์๋กญ๊ณ  ๋ค์ํ ๋ง'
                            ,'๊ฐ๊ฒฉ์ด ๋น์ธ๋ ๊ฑด๊ฐ์ ์ข์ ์๋ฃ ์์ ์ฑ์ด ํ๋ณด๋ ์ ํ์ ๊ตฌ์ํ๊ฒ ๋ค':'์๋ฃ ์์ ์ฑ'
                            ,'๊ฐ๊ฒฉ์ด ๋น์ธ๋ ์ํฌ์ฅ ์ฌ์ฉ ๋ฐ ์ทจ์/์กฐ๋ฆฌ๊ฐ ๊ฐํธํ๋ ์ ํ์ ๊ตฌ์ํ๊ฒ ๋ค':'์ํฌ์ฅ, ์กฐ๋ฆฌ ๊ฐํธํ'
                            ,'์ ํ์ ์๊ทธ๋ ์ด๋/์ ์ ํ ๊ฐ๋ฐ๊ณผ ๊ด๊ณ์์ด ๊ฐ๊ฒฉ๋ง ์ ๋ ดํ๋ฉด ๊ตฌ์ํ๊ฒ ๋ค':'์ค๋ก์ง ๊ฐ๊ฒฉ'})

df_t21 = df_21.rename(columns=df_21.iloc[0])
df_t21 = df_t21.drop(df_t21.index[0])
df_t21 = df_t21.astype({i:"float" for i in df_t21.columns[2:]})
df_t21 = df_t21.rename(columns={'๊ฑด๊ฐ(์์)์ ์ข์ ์ ํ์ ๊ตฌ์ํ๊ฒ ๋ค':'๊ฑด๊ฐํ ์ ํ'
                            ,'์๋ฃ์ ํ์ง๊ณผ ์์ ์ฑ์ด ํ๋ณด๋ ์ ํ ๊ตฌ์ํ๊ฒ ๋ค':'์๋ฃ ์์ ์ฑ'
                            ,'๋ค์ํ๊ณ  ์๋ก์ด ๋ง์ ๋ธ ์ ํ ๊ตฌ์ํ๊ฒ ๋ค':'์๋กญ๊ณ  ๋ค์ํ ๋ง'
                            ,'์ํฌ์ฅ ์ฌ์ฉ ๋ฐ ์ทจ์ยท์กฐ๋ฆฌ ๊ฐํธํ๋ ์ ํ ๊ตฌ์ํ๊ฒ ๋ค':'์ํฌ์ฅ, ์กฐ๋ฆฌ ๊ฐํธํ'
                            ,'์ ํ์ ์๊ทธ๋ ์ด๋/์ ์ ํ ๊ฐ๋ฐ๊ณผ ๊ด๊ณ์์ด ๊ฐ๊ฒฉ๋ง ์ ๋ ดํ๋ฉด ๊ตฌ์ํ๊ฒ ๋ค':'์ค๋ก์ง ๊ฐ๊ฒฉ'})



st.set_option('deprecation.showPyplotGlobalUse', False)


with st.expander('๋ฐ์ดํฐํ๋ ์ ๋ณด๊ธฐ๐งพ') :
    st.write("""
    ### 2019๋
    """)
    st.dataframe(df_t19)
    
    st.write("""
    ### 2020๋
    """)
    st.dataframe(df_t20)
    
    st.write("""
    ### 2021๋
    """)
    st.dataframe(df_t21)
    
my_order = ['๊ฐ๊ตฌ์์๋ณ', '์ฑ๋ณ', '์ฐ๋ น๋ณ']
    
status = st.radio('๊ทธ๋ํ ์ ํ', my_order)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


if status == my_order[0] :
    st.markdown("### ์ํ์๋น ๊ฐ๊ตฌ์์๋ณ ๋์กฐ์ฑ ๐")
    
    df19_c = df_t19[df_t19['ํน์ฑ๋ณ(1)'] == '๊ฐ๊ตฌ์์๋ณ']
    df_19_c = df19_c.drop(['ํน์ฑ๋ณ(1)'], axis=1)
    df_19_c = df_19_c.set_index(keys='ํน์ฑ๋ณ(2)')
    df_19_c = df_19_c.rename_axis('๊ฐ๊ตฌ์์๋ณ')


    df20_c = df_t20[df_t20['ํน์ฑ๋ณ(1)'] == '๊ฐ๊ตฌ์์๋ณ']
    df_20_c = df20_c.drop(['ํน์ฑ๋ณ(1)'], axis=1)
    df_20_c = df_20_c.set_index(keys='ํน์ฑ๋ณ(2)')
    df_20_c = df_20_c.rename_axis('๊ฐ๊ตฌ์์๋ณ')


    df21_c = df_t21[df_t21['ํน์ฑ๋ณ(1)'] == '๊ฐ๊ตฌ์์๋ณ']
    df_21_c = df21_c.drop(['ํน์ฑ๋ณ(1)'], axis=1)
    df_21_c = df_21_c.set_index(keys='ํน์ฑ๋ณ(2)')
    df_21_c = df_21_c.rename_axis('๊ฐ๊ตฌ์์๋ณ')
    
    df_19_c.T.plot(kind='bar', figsize=(25,10), rot=0, fontsize=25)
    plt.title("2019๋ ๊ฐ๊ตฌ์์๋ณ", fontsize=30)
    plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
    st.pyplot(plt.show())

    df_20_c.T.plot(kind='bar', figsize=(25,10), rot=0, fontsize=25)
    plt.title("2020๋ ๊ฐ๊ตฌ์์๋ณ", fontsize=30)
    plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
    st.pyplot(plt.show())

    df_21_c.T.plot(kind='bar', figsize=(25,10), rot=0, fontsize=25)
    plt.title("2021๋ ๊ฐ๊ตฌ์์๋ณ", fontsize=30)
    plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
    st.pyplot(plt.show())
    
elif status == my_order[1] :
    st.markdown("### ์ํ์๋น ์ฑ๋ณ ๋์กฐ์ฑ ๐")
    
    my_order1 = ['2019๋', '2020๋', '2021๋']
    
    status1 = st.radio('๋๋ ์ ํ', my_order1)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    st.set_option('deprecation.showPyplotGlobalUse', False)
   
    if status1 == my_order1[0]:
        st.write("""
        ### 2019๋
        """)
        
        df19_s = df_t19[df_t19['ํน์ฑ๋ณ(1)'] == '๊ฐ๊ตฌ์ฃผ์ฑ๋ณ']
        df_19_s = df19_s.drop(['ํน์ฑ๋ณ(1)'], axis=1)
        # df_19_s = df_19_s.set_index(keys='ํน์ฑ๋ณ(2)')
        df_19_s = df_19_s.rename(columns={'ํน์ฑ๋ณ(1)':'์ฑ๋ณ'})
        df19 = df19_s.drop(['ํน์ฑ๋ณ(1)'], axis=1)
        df19 = df19.rename(columns={'ํน์ฑ๋ณ(2)':'์ฑ๋ณ'                            
                                    ,'๊ฐ๊ฒฉ์ด ๋น์ธ๋ ํ๋ฆฌ๋ฏธ์(๊ณ ๊ธ)์ ํ์ ๊ตฌ์ํ๊ฒ ๋ค':'ํ๋ฆฌ๋ฏธ์ ์ ํ'
                                    ,'๊ฐ๊ฒฉ์ด ๋น์ธ๋ ๋ค์ํ๊ณ  ์๋ก์ด ๋ง์ ์ฒจ๊ฐํ ์ ํ์ ๊ตฌ์ํ๊ฒ ๋ค':'์๋กญ๊ณ  ๋ค์ํ ๋ง'
                                    ,'๊ฐ๊ฒฉ์ด ๋น์ธ๋ ๊ฑด๊ฐ์ ์ข์ ์๋ฃ ์์ ์ฑ์ด ํ๋ณด๋ ์ ํ์ ๊ตฌ์ํ๊ฒ ๋ค':'์๋ฃ ์์ ์ฑ'
                                    ,'๊ฐ๊ฒฉ์ด ๋น์ธ๋ ์ํฌ์ฅ ์ฌ์ฉ ๋ฐ ์ทจ์/์กฐ๋ฆฌ๊ฐ ๊ฐํธํ๋ ์ ํ์ ๊ตฌ์ํ๊ฒ ๋ค':'์ํฌ์ฅ, ์กฐ๋ฆฌ ๊ฐํธํ'
                                    ,'์ ํ์ ์๊ทธ๋ ์ด๋/์ ์ ํ ๊ฐ๋ฐ๊ณผ ๊ด๊ณ์์ด ๊ฐ๊ฒฉ๋ง ์ ๋ ดํ๋ฉด ๊ตฌ์ํ๊ฒ ๋ค':'์ค๋ก์ง ๊ฐ๊ฒฉ'})
        d19 = df19.T
        d19 = d19.rename(columns=d19.iloc[0])
        d19 = d19.drop(d19.index[0])
        
        explode = [0.06, 0.02, 0.01, 0.02, 0.04]
        colors = ['whitesmoke','yellow','cornflowerblue','lightgreen', 'lightgray']
        plt.pie(d19['๋จ์ฑ'], labels=d19.index, autopct='%.1f%%', counterclock=False, explode=explode, colors=colors)
        plt.title('2019๋', size = 15)
        st.pyplot(plt.show())

        explode = [0.06, 0.02, 0.01, 0.02, 0.04]
        colors = ['whitesmoke','yellow','lightsalmon','lightgreen', 'lightgray']
        plt.pie(d19['์ฌ์ฑ'], labels=d19.index, autopct='%.1f%%', counterclock=False, explode=explode , colors=colors)
        plt.title('2019๋', size = 15)
        st.pyplot(plt.show())

    elif status1 == my_order1[1]:
        st.write("""
        ### 2020๋
        """)
        
        df20_s = df_t20[df_t20['ํน์ฑ๋ณ(1)'] == '๊ฐ๊ตฌ์ฃผ์ฑ๋ณ']
        df_20_s = df20_s.drop(['ํน์ฑ๋ณ(1)'], axis=1)
        # df_20_s = df_20_s.set_index(keys='ํน์ฑ๋ณ(2)')
        df_20_s = df_20_s.rename(columns={'ํน์ฑ๋ณ(1)':'์ฑ๋ณ'})
        df20 = df20_s.drop(['ํน์ฑ๋ณ(1)'], axis=1)
        df20 = df20.rename(columns={'ํน์ฑ๋ณ(2)':'์ฑ๋ณ'                            
                                    ,'๊ฐ๊ฒฉ์ด ๋น์ธ๋ ํ๋ฆฌ๋ฏธ์(๊ณ ๊ธ)์ ํ์ ๊ตฌ์ํ๊ฒ ๋ค':'ํ๋ฆฌ๋ฏธ์ ์ ํ'
                                    ,'๊ฐ๊ฒฉ์ด ๋น์ธ๋ ๋ค์ํ๊ณ  ์๋ก์ด ๋ง์ ์ฒจ๊ฐํ ์ ํ์ ๊ตฌ์ํ๊ฒ ๋ค':'์๋กญ๊ณ  ๋ค์ํ ๋ง'
                                    ,'๊ฐ๊ฒฉ์ด ๋น์ธ๋ ๊ฑด๊ฐ์ ์ข์ ์๋ฃ ์์ ์ฑ์ด ํ๋ณด๋ ์ ํ์ ๊ตฌ์ํ๊ฒ ๋ค':'์๋ฃ ์์ ์ฑ'
                                    ,'๊ฐ๊ฒฉ์ด ๋น์ธ๋ ์ํฌ์ฅ ์ฌ์ฉ ๋ฐ ์ทจ์/์กฐ๋ฆฌ๊ฐ ๊ฐํธํ๋ ์ ํ์ ๊ตฌ์ํ๊ฒ ๋ค':'์ํฌ์ฅ, ์กฐ๋ฆฌ ๊ฐํธํ'
                                    ,'์ ํ์ ์๊ทธ๋ ์ด๋/์ ์ ํ ๊ฐ๋ฐ๊ณผ ๊ด๊ณ์์ด ๊ฐ๊ฒฉ๋ง ์ ๋ ดํ๋ฉด ๊ตฌ์ํ๊ฒ ๋ค':'์ค๋ก์ง ๊ฐ๊ฒฉ'})
        d20 = df20.T
        d20 = d20.rename(columns=d20.iloc[0])
        d20 = d20.drop(d20.index[0])
        
        explode = [0.06, 0.02, 0.01, 0.02, 0.04]
        colors = ['whitesmoke','yellow','cornflowerblue','lightgreen', 'lightgray']
        plt.pie(d20['๋จ์ฑ'], labels=d20.index, autopct='%.1f%%', counterclock=False, explode=explode, colors=colors)
        plt.title('2020๋', size = 15)
        st.pyplot(plt.show())

        explode = [0.06, 0.02, 0.01, 0.02, 0.04]
        colors = ['whitesmoke','yellow','lightsalmon','lightgreen', 'lightgray']
        plt.pie(d20['์ฌ์ฑ'], labels=d20.index, autopct='%.1f%%', counterclock=False, explode=explode , colors=colors)
        plt.title('2020๋', size = 15)
        st.pyplot(plt.show())

    elif status1 == my_order1[2]:
        st.write("""
        ### 2021๋
        """)
        
        df21_s = df_t21[df_t21['ํน์ฑ๋ณ(1)'] == '๊ฐ๊ตฌ์ฃผ์ฑ๋ณ']
        df_21_s = df21_s.drop(['ํน์ฑ๋ณ(1)'], axis=1)
        # df_21_s = df_21_s.set_index(keys='ํน์ฑ๋ณ(2)')
        df_21_s = df_21_s.rename(columns={'ํน์ฑ๋ณ(1)':'์ฑ๋ณ'})
        df21 = df21_s.drop(['ํน์ฑ๋ณ(1)'], axis=1)
        df21 = df21.rename(columns={'ํน์ฑ๋ณ(2)':'์ฑ๋ณ'
                                    ,'๊ฑด๊ฐ(์์)์ ์ข์ ์ ํ์ ๊ตฌ์ํ๊ฒ ๋ค':'๊ฑด๊ฐํ ์ ํ'
                                    ,'์๋ฃ์ ํ์ง๊ณผ ์์ ์ฑ์ด ํ๋ณด๋ ์ ํ ๊ตฌ์ํ๊ฒ ๋ค':'์๋ฃ ์์ ์ฑ'
                                    ,'๋ค์ํ๊ณ  ์๋ก์ด ๋ง์ ๋ธ ์ ํ ๊ตฌ์ํ๊ฒ ๋ค':'์๋กญ๊ณ  ๋ค์ํ ๋ง'
                                    ,'์ํฌ์ฅ ์ฌ์ฉ ๋ฐ ์ทจ์ยท์กฐ๋ฆฌ ๊ฐํธํ๋ ์ ํ ๊ตฌ์ํ๊ฒ ๋ค':'์ํฌ์ฅ, ์กฐ๋ฆฌ ๊ฐํธํ'
                                    ,'์ ํ์ ์๊ทธ๋ ์ด๋/์ ์ ํ ๊ฐ๋ฐ๊ณผ ๊ด๊ณ์์ด ๊ฐ๊ฒฉ๋ง ์ ๋ ดํ๋ฉด ๊ตฌ์ํ๊ฒ ๋ค':'์ค๋ก์ง ๊ฐ๊ฒฉ'})
        d21 = df21.T
        d21 = d21.rename(columns=d21.iloc[0])
        d21 = d21.drop(d21.index[0])
        
        explode = [0.06, 0.02, 0.01, 0.02, 0.04]
        colors = ['sandybrown','cornflowerblue','yellow','lightgreen', 'lightgray']
        plt.pie(d21['๋จ์ฑ'], labels=d21.index, autopct='%.1f%%', counterclock=False, explode=explode, colors=colors)
        plt.title('2021๋', size = 15)
        st.pyplot(plt.show())

        explode = [0.06, 0.02, 0.01, 0.02, 0.04]
        colors = ['sandybrown','lightsalmon','yellow','lightgreen', 'lightgray']
        plt.pie(d21['์ฌ์ฑ'], labels=d21.index, autopct='%.1f%%', counterclock=False, explode=explode , colors=colors)
        plt.title('2021๋', size = 15)
        st.pyplot(plt.show())
    
elif status == my_order[2] :
    st.markdown("### ์ํ์๋น ์ฐ๋ น๋ณ ๋์กฐ์ฑ ๐")
    df19_a = df_t19[df_t19['ํน์ฑ๋ณ(1)'] == '๊ฐ๊ตฌ์ฃผ์ฐ๋ น๋ณ']
    df_19_a = df19_a.drop(['ํน์ฑ๋ณ(1)'], axis=1)
    df_19_a = df_19_a.set_index(keys='ํน์ฑ๋ณ(2)')
    df_19_a = df_19_a.rename_axis('์ฐ๋ น๋ณ')


    df20_a = df_t20[df_t20['ํน์ฑ๋ณ(1)'] == '๊ฐ๊ตฌ์ฃผ์ฐ๋ น๋ณ']
    df_20_a = df20_a.drop(['ํน์ฑ๋ณ(1)'], axis=1)
    df_20_a = df_20_a.set_index(keys='ํน์ฑ๋ณ(2)')
    df_20_a = df_20_a.rename_axis('์ฐ๋ น๋ณ')

    df21_a = df_t21[df_t21['ํน์ฑ๋ณ(1)'] == '๊ฐ๊ตฌ์ฃผ์ฐ๋ น๋ณ']
    df_21_a = df21_a.drop(['ํน์ฑ๋ณ(1)'], axis=1)
    df_21_a = df_21_a.set_index(keys='ํน์ฑ๋ณ(2)')
    df_21_a = df_21_a.rename_axis('์ฐ๋ น๋ณ')


    st.set_option('deprecation.showPyplotGlobalUse', False)


    df_19_a.T.plot(kind='bar', figsize=(25,10), rot=0, fontsize=25)
    plt.title("2019๋ ์ฐ๋ น๋ณ", fontsize=30)
    plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
    st.pyplot(plt.show())

    df_20_a.T.plot(kind='bar', figsize=(25,10), rot=0, fontsize=25)
    plt.title("2020๋ ์ฐ๋ น๋ณ", fontsize=30)
    plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
    st.pyplot(plt.show())

    df_21_a.T.plot(kind='bar', figsize=(25,10), rot=0, fontsize=25)
    plt.title("2021๋ ์ฐ๋ น๋ณ", fontsize=30)
    plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
    st.pyplot(plt.show())
