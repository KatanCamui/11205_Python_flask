import streamlit as st

option = st.selectbox(
    '你想要如何聯絡?',
    ('Email', '電話', '手機'))

st.write('你選擇:', option)