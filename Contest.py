import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import koreanize_matplotlib
from PIL import Image

st.set_page_config(
    page_title="유통데이터 활용 경진대회",
    page_icon="🚀",
    layout="wide",
)

st.markdown("# 🚚유통데이터 활용 경진대회📊")
st.markdown("# ")
st.markdown("# ")

def load_image(image_file):
    img = Image.open(image_file)
    return img

load_image("main_1.jpg")
load_image("main_2.jpg")

st.image("main_1.jpg")

st.markdown("# ")
st.markdown("# ")

st.image("main_2.jpg")
