import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector

st.title("Test Streamlit deploy!!!")

st.text(st.secrets['db_host'])
