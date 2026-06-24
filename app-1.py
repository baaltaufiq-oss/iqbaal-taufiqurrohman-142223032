
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Retail Store Sales Dashboard", layout="wide")

st.title("📊 Retail Store Product Sales Dashboard")

uploaded_file = st.file_uploader("Upload CSV Dataset", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Preview Data")
    st.dataframe(df.head())

    st.subheader("Informasi Dataset")
    col1, col2 = st.columns(2)
    col1.metric("Jumlah Baris", df.shape[0])
    col2.metric("Jumlah Kolom", df.shape[1])

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    st.subheader("Statistik Deskriptif")
    st.dataframe(df[numeric_cols].describe())

    st.subheader("Korelasi Antar Variabel")
    corr = df[numeric_cols].corr()
    fig_corr = px.imshow(corr, text_auto=True, aspect="auto")
    st.plotly_chart(fig_corr, use_container_width=True)

    st.subheader("Visualisasi Kolom")
    selected_col = st.selectbox("Pilih Kolom Numerik", numeric_cols)

    fig_hist = px.histogram(df, x=selected_col, nbins=30)
    st.plotly_chart(fig_hist, use_container_width=True)

    fig_box = px.box(df, y=selected_col)
    st.plotly_chart(fig_box, use_container_width=True)

else:
    st.info("Upload file RetailStoreProductSalesDataset.csv untuk memulai analisis.")
