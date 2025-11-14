"""Minimal Streamlit demo."""
import pandas as pd
import streamlit as st

st.title("sales-prediction-analytics-project")
df = pd.read_csv("data/warehouse_throughput.csv")
st.dataframe(df.head(20))
