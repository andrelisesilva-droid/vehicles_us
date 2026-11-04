
import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Análise de anúncios de veículos nos EUA")


df = pd.read_csv(
    "https://raw.githubusercontent.com/andrelisesilva-droide/vehicles_us/main/vehicles_us.csv"
)

st.write("Visualização dos dados")
st.dataframe(df.head())

st.header("Distribuição da quilometragem")
fig = px.histogram(df, x="odometer")
st.plotly_chart(fig)

st.header("Relação entre preço e quilometragem")
fig2 = px.scatter(df, x="odometer", y="price")
st.plotly_chart(fig2)
