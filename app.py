import pandas as pd
import streamlit as st
import plotly.express as px
from test import ratio_charting
from test import ratio_charting_annotate
from config import ticker_dictionary

st.set_page_config(page_title='Investing Dashboard')
st.title('CHEEMS Investing')
st.sidebar.write('Tool Selection')

tool = st.sidebar.selectbox('', ['Ratio Charting'])

st.header(tool)

# Ratio Charting Page
if tool == 'Ratio Charting':
    # dropboxes for asset selection
    asset1 = st.selectbox('Asset 1', list(ticker_dictionary))
    asset2 = st.selectbox('Asset 2', list(ticker_dictionary))
    st.subheader("chart options")
    # put all checkbox chart options here
    log_value = st.checkbox('log', value=True, key='log')
    mean_value = st.checkbox('show mean', value=False, key='mean')
    # generate the graph
    st.plotly_chart(ratio_charting(
        asset1, asset2, log=log_value, avg=mean_value))
    # annotate graph in external window
    annotate = st.button("annotate graph", key="annotate graph")
    st.write("Please select prefered chart options before annotating.")
    st.write("**Note:** annotation chart will open a new tab")
    if annotate == True:
        ratio_charting_annotate(asset1, asset2, log=log_value, avg=mean_value)
