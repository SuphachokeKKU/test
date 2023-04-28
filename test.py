import requests
import streamlit as st

st.title("Test Streamlit deploy!!!")

r = requests.get("https://wunchana.mdsolutions.in.th")
print(r.text)
