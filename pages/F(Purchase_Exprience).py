import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import koreanize_matplotlib

st.set_page_config(
    page_title="πμΌλ‘ λ¨Έμ€ν¬ MIDπ",
    page_icon="β­οΈ",
    layout="wide",
)

st.markdown("# κ°νΈμ νλͺ©λ³ κ΅¬μκ²½νπ")

url_6 = "https://raw.githubusercontent.com/hj2628/AIS7MidProject/main/%E1%84%80%E1%85%A1%E1%86%AB%E1%84%91%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8_%E1%84%91%E1%85%AE%E1%86%B7%E1%84%86%E1%85%A9%E1%86%A8%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%83%E1%85%A9%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%80%E1%85%AE%E1%84%8B%E1%85%B5%E1%86%B8%E1%84%80%E1%85%A7%E1%86%BC%E1%84%92%E1%85%A5%E1%86%B7"


@st.cache
def load_data(url_6):
    data_6 = pd.read_csv(url_6)
    return data_6

data_6 = load_data(url_6)

with st.expander('λ°μ΄ν°νλ μ λ³΄κΈ°π§Ύ'):
    st.dataframe(data_6)

st.write("""
### κ²½ν μμ
""")

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(15, 5))
sns.barplot(data=data_6, x="μ°λ", y="μμ", hue="νλͺ©κ΅°").set_title("μ°λλ³ κ°νΈμ κ΅¬μκ²½ν")
plt.legend(bbox_to_anchor=(1,1))
st.pyplot()

st.write("""
### κ²½ν μμ
""")

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(15, 5))
sns.barplot(data=data_6, x="μ°λ", y="μμ", hue="νλͺ©κ΅°").set_title("μ°λλ³ κ°νΈμ κ΅¬μκ²½ν")
plt.legend(bbox_to_anchor=(1,1))
st.pyplot()
