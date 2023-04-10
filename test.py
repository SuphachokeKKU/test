import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector

st.title("Test Streamlit deploy!!!")

conn = mysql.connector.connect(**st.secrets['mysql'])

cur = None
if(conn.is_connected()):
    st.text("Connect to DBMS succesful!")
    cur = conn.cursor()
    cur.execute("show databases;")
    st.text(cur.fetchall())
else:
    st.text("Connect to DBMS error!")
