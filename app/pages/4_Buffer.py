import streamlit as st
from shapely.geometry import Point
import os

st.set_page_config(page_title="Buffering", page_icon="🔘")
st.markdown("# 4. Buffer (Buffering a Geometry)")

st.markdown("""
**Explicação:**

O buffer cria uma nova geometria que representa todos os pontos dentro de uma determinada distância da geometria original. É muito usado para zonas de influência.
""")

st.markdown("**Código:**")

st.code("""
from shapely.geometry import Point

p = Point(0, 0)
buffer_geom = p.buffer(1.0) # Buffer circular de raio 1

print(buffer_geom.area) # Aprox pi * r^2
""", language="python")

st.markdown("**Resultado:**")

st.image(os.path.join("assets", "img", "buffer.png"))
