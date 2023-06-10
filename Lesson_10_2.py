import streamlit as st
import pandas as pd
import yfinance as yf

codeFrame = pd.read_csv('codeSearch.csv',usecols=['code','name'])
codeSeries = codeFrame['code'].astype(str) + codeFrame['name']

with st.sidebar:
    select_code = st.multiselect("請選擇股票號碼:",codeSeries,
                                 max_selections=4)

#st.write(select_code)

@st.cache_data
def fetch_stock_dataFrame(id):
    stock_dataFrame = yf.download(id,start='2022-01-01')
    return stock_dataFrame

charDataFrame = None

#版本一
for code in select_code:
    code1 = code[:4] + ".TW"
    code_stock_dataFrame = fetch_stock_dataFrame(code1)
    code_stock_dataFrame_sorted = code_stock_dataFrame.sort_index(ascending=False)
    st.subheader(code)
    st.dataframe(code_stock_dataFrame_sorted,width=1024)
    st.line_chart(code_stock_dataFrame_sorted,y='Adj Close')
    st.divider()

#版本二
#for code in select_code:
#    code1 = code[:4] + ".TW"
#    code_stock_dataFrame = fetch_stock_dataFrame(code1)
#    code_stock_dataFrame_sorted = code_stock_dataFrame.sort_index(ascending=False)
#    st.subheader(code)
#    if charDataFrame is None:
#        code_stock_dataFrame_sorted['Adj Close']
#        # charDataFrame = code_stock_dataFrame_sorted['Adj Close']
#        #charDataFrame.rename({'Adj Close':code})
#    else:
#        #charDataFrame[code] = 
#    st.dataframe(code_stock_dataFrame_sorted,width=1024)
#    st.line_chart(code_stock_dataFrame_sorted,y='Adj Close')
#    st.divider()
