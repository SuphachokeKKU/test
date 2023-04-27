import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector

st.title("Test Streamlit deploy!!!")

conn = mysql.connector.connect(host=st.secrets['db_host'], port=st.secrets['db_port'], user=st.secrets['db_user'],password=st.secrets['db_pass'])

cur = None
if(conn.is_connected()):
    st.text("Connect to DBMS succesful!")
    cur = conn.cursor()
    cur.execute("show databases;")
    st.text(cur.fetchall())
else:
    st.text("Connect to DBMS error!")
