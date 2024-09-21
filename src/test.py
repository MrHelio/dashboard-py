import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(page_title='Dashboard Py', layout='wide')

st.title('Test')


# Carregar o arquivo Excel
uploaded_file = pd.read_excel('dashboard-py/src/divulgacao_brasil_ideb_2023.xlsx')

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    # Selecionar as colunas para os gráficos
    all_columns = df.columns.tolist()
    selected_columns = st.multiselect('Selecione as colunas para os gráficos:', all_columns)

    # Criar um container para os gráficos
    graph_container = st.container()

    with graph_container:
        for column in selected_columns:
            fig, ax = plt.subplots()
            plt.hist(df[column], bins=20)
            plt.title(f'Histograma de {column}')
            st.pyplot(fig)

    # Opção para escolher o tipo de gráfico
    chart_type = st.selectbox("Escolha o tipo de gráfico", ["Histograma", "Gráfico de Linhas", "Gráfico de Barras"])

    if chart_type == "Gráfico de Linhas":
        plt.plot(df.index, df[column])
    elif chart_type == "Gráfico de Barras":
        plt.bar(df.index, df[column])