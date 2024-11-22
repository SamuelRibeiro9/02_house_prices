import geopandas as gpd
import streamlit as st
import pandas as pd
import numpy as np

from joblib import load

from notebooks.src.config import DADOS_LIMPOS, DADOS_GEO_MEDIAN, MODELO_FINAL

@st.cache_data
def carregar_dados_limpos():
    return pd.read_parquet(DADOS_LIMPOS)

@st.cache_data
def carregar_dados_geo():
    return gpd.read_parquet(DADOS_GEO_MEDIAN)

@st.cache_resource
def carregar_modelo():
    return load(MODELO_FINAL)

df = carregar_dados_limpos()
gdf_geo = carregar_dados_geo()
modelo = carregar_modelo()

st.title('Previsão de preços de imóveis')

longitude = st.number_input('Longitude', value=-122.33)
latitude = st.number_input('Latitude', value=37.88)
housing_median_age = st.number_input('Idade do Imóvel', value=10)
total_rooms = st.number_input('Total de Cômodos', value=800)
total_bedrooms = st.number_input('Total de Quartos', value=300)
population = st.number_input('População', value=800)
households = st.number_input('Domicílios', value=100)
median_income = st.slider('Renda média (múltiplos de 10k dólares)', 0.5, 15.0, value=10.0, step=0.5)
ocean_proximity = st.selectbox('Proximidade do oceano', df['ocean_proximity'].unique())
median_income_cat = st.number_input('Categoria de renda', value=4)
rooms_per_households = st.number_input('Quartos por domicílo', value=7)
bedrooms_per_room = st.number_input('Quartos por domicílo', value=0.2)
population_per_households = st.number_input('Quartos por domicílo', value=4)

entrada_modelo = {
    'longitude': longitude,
    'latitude': latitude,
    'housing_median_age': housing_median_age,
    'total_rooms': total_rooms,
    'total_bedrooms': total_bedrooms,
    'population': population,
    'households': households,
    'median_income': median_income,
    'ocean_proximity': ocean_proximity,
    'median_income_cat': median_income_cat,
    'rooms_per_households': rooms_per_households,
    'bedrooms_per_room': bedrooms_per_room,
    'population_per_households': population_per_households,
}

df_entrada_modelo = pd.DataFrame(entrada_modelo, index=[0])

botao_previsao = st.button('Executar previsão')

if botao_previsao:
    preco = modelo.predict(df_entrada_modelo)
    st.write(f'Preço previsto: U$ {preco[0][0]:.2f}')
