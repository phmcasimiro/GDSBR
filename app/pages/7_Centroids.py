import streamlit as st
from shapely.geometry import Polygon
import os

st.set_page_config(page_title="Centroids", page_icon="🎯")
st.markdown("# 7. Calculando Centróides")

st.markdown("""
**Explicação:**

O centróide é o centro geométrico de uma figura plana. É um ponto que representa a média aritmética de todos os pontos da forma.
""")

st.markdown("**Código:**")

st.code("""
from shapely.geometry import Polygon

poly = Polygon([(0,0), (4,0), (4,4), (0,4)])
centroid = poly.centroid

print(f"Centróide: {centroid}") # POINT (2 2)
""", language="python")

st.markdown("**Resultado:**")

st.image(os.path.join("assets", "img", "centroid.png"))
