import streamlit as st
import pandas as pd
df=pd.read_csv('mymoviedb.csv')
st.title('Movie Dataset Explorer')
st.dataframe(df.head())
col=st.selectbox('Kolom',df.columns)
try:
    st.bar_chart(df[col].value_counts().head(10))
except:
    st.write(df[col].describe())
