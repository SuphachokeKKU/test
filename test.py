import requests
import streamlit as st

st.title("Test Streamlit deploy!!!")

r = request.get("https://wunchana.mdsolutions.in.th")
print(r.text)
