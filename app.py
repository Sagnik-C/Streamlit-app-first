import streamlit as st

st.title("Multiply Numbers")
st.write("---")
num1 = st.number_input(label="Enter first number")
num2 = st.number_input(label="Enter second number")

if st.button("Calculate result"):
    st.success(f"Answer = {num1*num2}")