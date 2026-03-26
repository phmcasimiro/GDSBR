import streamlit as st
from shapely.geometry import Point
import os

st.set_page_config(page_title="Criando um Ponto", page_icon="📍")

st.markdown("# 1. Criando um Ponto (Creating a Point)")

st.markdown("""
**Explicação:**

Um ponto geométrico (`Point`) representa uma única localização no espaço, definida por coordenadas numéricas (longitude e latitude). 

Com a biblioteca **Shapely**, pontos podem ser criados passando as coordenadas `(x, y)` ou `(longitude, latitude)`, e são a base para construir outras geometrias.
""")

st.markdown("**Código:**")

code = """
from shapely.geometry import Point
import matplotlib.pyplot as plt

# Criando um ponto (Longitude, Latitude)
# Exemplo: Brasília, DF
# Longitude = x = -47.8825
# Latitude  = y = -15.7942
ponto = Point(-47.8825, -15.7942)

print(f"Ponto criado: {ponto}")
# Saída: POINT (-47.8825 -15.7942)
"""
st.code(code, language="python")

st.markdown("**Resultado:**")

# Caminho da imagem relativo à raiz do projeto onde o comando streamlit é executado
image_path = os.path.join("assets", "img", "point_example.png")

if os.path.exists(image_path):
    st.image(image_path, caption="Exemplo de Ponto")
else:
    st.error(f"Imagem não encontrada em: {image_path}")
