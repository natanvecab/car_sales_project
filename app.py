import pandas as pd
import plotly.express as px
import streamlit as st

# Ler o arquivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Criar um botão para o histograma
hist_button = st.button('Criar histograma')

# Se o botão for clicado, criar o histograma
if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Criar um botão para o gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

# Se o botão for clicado, criar o gráfico de dispersão
if scatter_button:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig_scatter = px.scatter(car_data, x="model_year", y="price")  # Modifiquei aqui
    st.plotly_chart(fig_scatter, use_container_width=True)

