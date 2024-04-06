from email.mime import image
from enum import unique
from tkinter import Image
import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

st.set_page_config(layout ="wide")
@st.cache_data
def create_df():
    df = pd.read_excel(
        io = "fuel.xlsx",
        engine = "openpyxl",
        sheet_name = "brasil",
        usecols = "A:Q",
        nrows= 21583
    )
    return df

df = create_df()
usefulColumns = ["mes", "produto", "regiao", "estado", "preco_medio_revenda"]
df = df[usefulColumns]

with st.sidebar:
    st.subheader("Preço dos Combustíveis no Brasil a partir de 2013")
    logo = Image.open("logo.jpg")
    st.image(logo)
    st.subheader("Seleção de Filtros")
    fProduto = st.selectbox(
        "Selecione o combustível:",
        options = df["produto"].unique()
    )

    fEstado = st.selectbox(
        "Selecione o Estado:",
        options = df["estado"].unique()
    )

dfUser = df.loc[
    (df["produto"] == fProduto) & (df["estado"] == fEstado)
]

updateData = dfUser["mes"].dt.strftime("%Y/%b")

dfUser["mes"] = updateData[0:]

st.header("Preços dos Combustíveis no Brasil desde 2013")
st.markdown("**Combustível Selecionado:** " + fProduto)
st.markdown("**Estado:** " + fEstado)

grafCombEstado = alt.Chart(dfUser).mark_line(
    point = alt.OverlayMarkDef(color="red", size=20)
).encode(
    x = "mes:T",
    y = "preco_medio_revenda",
    strokeWidth = alt.value(3)
).properties(
    height = 400,
    width = 900
)

st.altair_chart(grafCombEstado)