import streamlit as st

if st.button("say Hello!",key="myButton") :
    st.write("Why hello there")
else:
    st.write("Goodbye")
