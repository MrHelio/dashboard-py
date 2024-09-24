import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Dashboard', layout='wide')
st.title('Análise de Taxas de Aprovação')
st.write("Temos um dashboard interativo que vai mostrar as taxas de aprovações do IDEB (Índice de Desenvolvimento da Educação Básica) no Brasil.")

df = pd.read_excel('/home/helio/Projects/dashboard-py/src/divulgacao_brasil_ideb_2023-1.xlsx')
df = df.drop('Rede', axis=1)


# Selecionar as colunas a serem plotadas
columns = df.columns.tolist()
selected_columns = st.multiselect('Selecione as colunas para os gráficos:', columns)

# Escolher o tipo de gráfico
chart_type = st.radio("Escolha o tipo de gráfico", ('Linha', 'Coluna'))

sns.set_style("darkgrid")
sns.set_palette("pastel")

# Criar os gráficos
if chart_type == 'Linha':
    for column in selected_columns:
        fig = plt.figure(figsize=(12, 7))
        sns.lineplot(x=df.index, y=column, data=df)
        plt.title(f'{column}')
        plt.xlabel('Rede Pública')
        plt.ylabel('Taxa de Aprovação (%)')
        st.pyplot(fig)
        
elif chart_type == 'Coluna':
    for column in selected_columns:
        fig = plt.figure(figsize=(12, 7))
        sns.barplot(x=df.index, y=column, data=df)
        plt.title(f'{column}')
        plt.xlabel('Rede Pública')
        plt.ylabel('Taxa de Aprovação (%)')
        st.pyplot(fig)

