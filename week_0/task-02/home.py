import streamlit as st
import plotly.graph_objects as go
import pandas as pd

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


if not hasattr(st.session_state, "loaded_df"):
    st.session_state.loaded_df = df
st.write(st.session_state.loaded_df.df.head())
