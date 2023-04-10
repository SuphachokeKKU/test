import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector
import requests

st.title("Test Streamlit deploy!!!")

r = requests.get("https://wunchana.mdsolutions.in.th")
print(r)
