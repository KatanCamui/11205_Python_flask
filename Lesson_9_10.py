import streamlit as st
import datetime

title = st.text_input('輸入:', '預設值')
st.write('現在輸入的值是:', title)

st.divider()

number = st.number_input('請輸入數值')
st.write('The current number is ', number)

st.divider()

d = st.date_input(
    "When\'s your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

st.divider()

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)