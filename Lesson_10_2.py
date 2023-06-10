import streamlit as st
import pandas as pd

codeFrame = pd.read_csv('codeSearch.csv',usecols=['code','name'])
codeSeries = codeFrame['code'].astype(str) + codeFrame['name']

with st.sidebar:
    select_code = st.multiselect("請選擇股票號碼:",codeSeries,
                                 max_selections=4)

#st.write(select_code)

for code in select_code:
    code = code[:4] + ".TW"
    st.write(code)
