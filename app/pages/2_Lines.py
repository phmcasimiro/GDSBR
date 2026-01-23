import streamlit as st
from shapely.geometry import LineString
import os

st.set_page_config(page_title="Criando Linhas", page_icon="📏")

st.markdown("# 2. Criando Linhas (Creating Line Segments)")

st.markdown("""
**Explicação:**

Uma linha (`LineString`) é uma sequência de pelo menos dois pontos conectados. Representa objetos lineares como ruas, rios ou limites. Em `shapely`, é criada a partir de uma lista de coordenadas `(x, y)` ou pontos.
""")

st.markdown("**Código:**")

code = """
from shapely.geometry import LineString

# Criando uma linha com 2 pontos (Ponta A -> Ponta B)
# Exemplo: Eixo Monumental Simplificado
line = LineString([(-47.9500, -15.7900), (-47.8200, -15.8000)])

print(f"Linha criada: {line}")
"""
st.code(code, language="python")

st.markdown("**Resultado:**")

image_path = os.path.join("assets", "img", "line_example.png")
if os.path.exists(image_path):
    st.image(image_path, caption="Exemplo de Linha (LineString)")
else:
    st.error(f"Imagem não encontrada em: {image_path}")
