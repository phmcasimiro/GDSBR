import streamlit as st
from shapely.geometry import Polygon
import os

st.set_page_config(page_title="Área e Perímetro", page_icon="📏")
st.markdown("# 6. Área e Perímetro")

st.markdown("""
**Explicação:**

Geometrias como Polígonos possuem propriedades diretas para calcular área (`.area`) e perímetro (`.length`).
""")

st.markdown("**Código:**")

st.code("""
from shapely.geometry import Polygon

# Triângulo retângulo 3-4-5
poly = Polygon([(0,0), (4,0), (4,3)])

print(f"Área: {poly.area}") # 6.0
print(f"Perímetro: {poly.length}") # 12.0
""", language="python")

st.markdown("**Resultado:**")

st.image(os.path.join("assets", "img", "area_perimeter.png"))
