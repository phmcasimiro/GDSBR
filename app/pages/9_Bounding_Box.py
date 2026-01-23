import streamlit as st
from shapely.geometry import Polygon
import os

st.set_page_config(page_title="Bounding Box", page_icon="📦")
st.markdown("# 9. Criando uma Bounding Box")

st.markdown("""
**Explicação:**

O *Bounding Box* (Envelope) é o menor retângulo alinhado aos eixos x e y que contém a geometria inteira. É muito útil para filtros espaciais rápidos (indexação).
""")

st.markdown("**Código:**")

st.code("""
from shapely.geometry import Polygon

poly = Polygon([(1,1), (2,3), (3,2)])
minx, miny, maxx, maxy = poly.bounds

print(f"Bounds: {poly.bounds}")
# Criando geometria retângulo a partir dos bounds
bbox = Polygon([(minx, miny), (maxx, miny), (maxx, maxy), (minx, maxy)])
""", language="python")

st.markdown("**Resultado:**")

st.image(os.path.join("assets", "img", "bbox.png"))
