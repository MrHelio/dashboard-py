import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.write("""
	## DATASUS ##
	Análise de dados dos anos de 2020 a 2022
""")


# Título do aplicativo
st.title('Visualizador de Dados CSV')

df = pd.read_csv('src/data/part-00000-4a76159e-72db-4184-b120-53352321e01e.c000.csv')

