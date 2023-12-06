import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Data Analytics", page_icon="chart_with_upwards_trend", layout="wide")

st.title(" :chart_with_upwards_trend: Sample SuperStore EDA")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a file", type=(["csv","txt","xlsx","xls"]))
if fl is not None:
    filename =  fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding="ISO-8859-1")
else:
    os.chdir(r"D:\campusX\ds_1")
    df = pd.read_csv("SampleSuperstore.csv", encoding = "ISO-8859-1")