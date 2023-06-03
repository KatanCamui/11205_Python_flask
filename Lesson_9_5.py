import streamlit as st

agree = st.checkbox('我同意')

if agree:
    st.write('Great!')