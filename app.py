
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Delivery Time Dataset Explorer", layout="wide")

st.title("🚚 Delivery Time Dataset Explorer")

uploaded = st.file_uploader("Upload CSV (optional)", type=["csv"])

if uploaded is not None:
    df = pd.read_csv(uploaded)
else:
    df = pd.read_csv("train.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.write("Shape:", df.shape)

st.subheader("Columns")
st.write(list(df.columns))

numeric_cols = df.select_dtypes(include="number").columns.tolist()

if numeric_cols:
    col = st.selectbox("Select numeric column", numeric_cols)
    st.bar_chart(df[col].value_counts().head(20))

st.subheader("Summary Statistics")
st.dataframe(df.describe(include="all"))
