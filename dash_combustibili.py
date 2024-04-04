import streamlit as st
import pandas as pd
import altair as alt

@st.cache_data
def create_df():
    df = pd.read_excel(
        io = "fuel.xlsx",
        engine = "openpyxl",
        sheet_name = "brasil",
        usecols = "A:O",
        nrows=863
    )
    return df

df = create_df()

df
