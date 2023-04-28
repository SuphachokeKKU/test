import requests

st.title("Test Streamlit deploy!!!")

r = request.get("https://wunchana.mdsolutions.in.th")
print(r.text)
