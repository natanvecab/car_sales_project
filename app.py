import pandas as pd
import plotly.express as px
import streamlit as st

# Cabeçalho
st.header('Análise de Vendas de Carros: Visualizando Dados de Anúncios')

# Ler o arquivo CSV
car_data = pd.read_csv('C:\\Users\\navec\\Desktop\\Estudo\\vehicles_us.csv')

# Preencher os valores nulos na coluna 'model_year' com 'N/A'
car_data['model_year'].fillna(value="N/A", inplace=True)

# Preencher os valores nulos na coluna 'odometer' com 'N/A'
car_data['odometer'].fillna(value="N/A", inplace=True)

# Arredondar valores de ponto flutuante na coluna 'odometer' apenas se forem numéricos
car_data['odometer'] = pd.to_numeric(car_data['odometer'], errors='coerce').round().astype('Int64')

# Converter a coluna 'model_year' para string
car_data['model_year'] = car_data['model_year'].astype(str)

# Extrair a marca do carro da coluna 'model'
car_data['car_brand'] = car_data['model'].apply(lambda x: x.split()[0])

# Criar um botão para o histograma
hist_button = st.button('Histograma de hodômetro')

# Se o botão for clicado, criar o histograma
if hist_button:
    st.write('Criando um histograma para identificar as quantidades de veículos através do hodômetro')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Criar um botão para o gráfico de dispersão
scatter_button = st.button('Gráfico de dispersão para ano dos veículos')

# Se o botão for clicado, criar o gráfico de dispersão
if scatter_button:
    st.write('Criando um gráfico de dispersão para identificar o preço por ano dos veículos')
    fig_scatter = px.scatter(car_data, x="model_year", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Criar um botão para o gráfico de barras (marcas de veículos)
bar_button = st.button('Gráfico de barras para marcas de veículos')

# Se o botão for clicado, criar o gráfico de barras (marcas de carros)
if bar_button:
    st.write('Criando um gráfico de barras para identificar as quantidades de marcas de veículos')
    fig_bar = px.histogram(car_data, x='car_brand')
    st.plotly_chart(fig_bar, use_container_width=True)

# Criar um botão para o gráfico de dispersão (cores por ano dos veículos)
scatter_button_color = st.button('Gráfico de dispersão para cores por ano dos veículos')

# Se o botão for clicado, criar o gráfico de dispersão (cores por ano dos veículos)
if scatter_button_color:
    st.write('Criando um gráfico de dispersão para identificar as cores por ano dos veículos')
    fig_scatter_color = px.scatter(car_data, x='model_year', y='paint_color')
    st.plotly_chart(fig_scatter_color, use_container_width=True)


