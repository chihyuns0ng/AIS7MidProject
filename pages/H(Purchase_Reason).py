import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import koreanize_matplotlib
# import plotly.graph_objects as go

st.set_page_config(
    page_title="πμΌλ‘ λ¨Έμ€ν¬ MIDπ",
    page_icon="β­οΈ",
    layout="wide",
)

st.markdown("# κ°νΈμ κ΅¬μ μ΄μ π")


st.set_option('deprecation.showPyplotGlobalUse', False)

url = ["https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_19.csv"
, "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_20.csv"
, "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_21.csv"
]


kosis3_19=pd.read_csv(url[0])
kosis3_20=pd.read_csv(url[1])
kosis3_21=pd.read_csv(url[2])



kosis3_19_gender = kosis3_19[6:8].drop("νΉμ±λ³(1)", axis=1)
kosis3_20_gender = kosis3_20[6:8].drop("νΉμ±λ³(1)", axis=1)
kosis3_21_gender = kosis3_21[5:7].drop("νΉμ±λ³(1)", axis=1)

kosis3_19_gender = kosis3_19_gender.set_index("νΉμ±λ³(2)")
kosis3_19_gender = kosis3_19_gender.rename_axis("κ°κ΅¬μμ")
kosis3_20_gender = kosis3_20_gender.set_index("νΉμ±λ³(2)")
kosis3_20_gender = kosis3_20_gender.rename_axis("κ°κ΅¬μμ")
kosis3_21_gender = kosis3_21_gender.set_index("νΉμ±λ³(2)")
kosis3_21_gender = kosis3_21_gender.rename_axis("κ°κ΅¬μμ")

kosis3_gender = pd.concat([kosis3_19_gender, kosis3_20_gender, kosis3_21_gender])

kosis3_gender.loc["2019λ"] = 0
kosis3_gender.loc["2020λ"] = 0
kosis3_gender.loc["2021λ"] = 0

for i in kosis3_gender.columns:
    kosis3_gender.loc["2019λ"][i] = (kosis3_gender.loc["λ¨μ±"][i][0] + kosis3_gender.loc["μ¬μ±"][i][0]) / 2
    kosis3_gender.loc["2020λ"][i] = (kosis3_gender.loc["λ¨μ±"][i][1] + kosis3_gender.loc["μ¬μ±"][i][1]) / 2
    kosis3_gender.loc["2021λ"][i] = (kosis3_gender.loc["λ¨μ±"][i][2] + kosis3_gender.loc["μ¬μ±"][i][2]) / 2
    
df = kosis3_gender.drop(["λ¨μ±", "μ¬μ±"])

with st.expander('λ°μ΄ν°νλ μ λ³΄κΈ°π§Ύ'):
    st.dataframe(df)

fig = plt.pie(df.T["2019λ"][:-2], labels=df.T.index[:-2], startangle=180, autopct='%1.1f%%', counterclock=False, wedgeprops=dict(width=0.5)
            , explode=(0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02), colors=["royalblue", "gold", "silver", "tomato", "violet", "darkgray", "gainsboro", "gainsboro"])
plt.legend(bbox_to_anchor=(1.2,1.1))
plt.title("2019λ κ΅¬μ μ΄μ ")
st.pyplot()


fig = plt.pie(df.T["2020λ"][:-2], labels=df.T.index[:-2], startangle=180, autopct='%1.1f%%', counterclock=False, wedgeprops=dict(width=0.5)
            , explode=(0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02), colors=["royalblue", "gold", "gainsboro", "tomato", "violet", "darkgray", "silver", "gainsboro"])
plt.legend(bbox_to_anchor=(1.2,1.1))
plt.title("2020λ κ΅¬μ μ΄μ ")
st.pyplot()



fig = plt.pie(df.T["2021λ"][:-2], labels=df.T.index[:-2], startangle=180, autopct='%1.1f%%', counterclock=False, wedgeprops=dict(width=0.5)
            , explode=(0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02), colors=["royalblue", "gold", "darkgray", "tomato", "violet", "darkgray", "silver", "gainsboro"])
plt.legend(bbox_to_anchor=(1.2,1.1))
plt.title("2021λ κ΅¬μ μ΄μ ")
st.pyplot()
