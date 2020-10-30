import streamlit as st
import pandas as pd
import numpy as np

st.title('German Credit Modeling with Streamlit')

DATA_URL = ('input/german_credit_easy.xls')

@st.cache
def load_data(nrows):
    data = pd.read_excel(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done Reading data German Credit! (using st.cache)")