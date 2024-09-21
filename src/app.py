import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(page_title='Dashboard Py', layout='wide')

st.title('Educação')

df = pd.read_csv('src/data/part-00000-4a76159e-72db-4184-b120-53352321e01e.c000.csv')
