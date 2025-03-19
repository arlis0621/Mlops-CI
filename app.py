
import streamlit as st
st.title("calci")
st.write("Enter a number")
a = st.number_input("Enter a number")
sq=a**2
cb=a**3
st.write("The square of the number is",sq)
st.write("The cube of the number is",cb)
