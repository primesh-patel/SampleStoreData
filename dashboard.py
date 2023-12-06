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

col1, col2 = st.columns((2))
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Gettting the min and max date
startDate = pd.to_datetime(df["Order Date"]).min()
endDate = pd.to_datetime(df["Order Date"]).max()

with col1:
    date1 = pd.to_datetime(st.date_input("Start Date", startDate))

with col2:
    date2 = pd.to_datetime(st.date_input("End Date", endDate))

df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)].copy()

st.sidebar.header("Choose your filter: ")
# Create for Region
region = st.sidebar.multiselect("Pick your Region", df["Region"].unique())
if not region:
    df2 = df.copy()
else:
    df2 = df[df["Region"].isin(region)]

    # Create for State
state = st.sidebar.multiselect("Pick the State", df2["State"].unique())
if not state:
    df3 = df2.copy()
else:
    df3 = df2[df2["State"].isin(state)]