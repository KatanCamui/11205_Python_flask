import streamlit as st

options = st.multiselect(
    '你喜歡什麼顏色',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('你選擇:', options)