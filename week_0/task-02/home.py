import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Car Sales Board")
@st.cache_data
def load_data(path:str):
    data = pd.read_csv(path)
    return data


with st.sidebar:
    uploadfile = st.file_uploader("Browse data", type=["csv", "xlsx"])

    if uploadfile is None:
        st.info("Upload file through drag and drop")
        st.stop()

    df = load_data(uploadfile)

col1, col2 = st.columns(2)

with col1.expander("Basic Statistic"):
    st.write(df.describe())





