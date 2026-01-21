import streamlit as st
from shapely.geometry import Point
import os

st.set_page_config(page_title="Distance Calculation", page_icon="📏")
st.markdown("# 11. Distance Calculation")

st.markdown("""
**Explicação:**

Calcula a menor distância Euclidiana (em linha reta) entre duas geometrias.
""")

st.markdown("**Código:**")

st.code("""
from shapely.geometry import Point

p1 = Point(0, 0)
p2 = Point(3, 4)

dist = p1.distance(p2)

print(f"Distância: {dist}") # 5.0 (Hipotenusa de 3-4-5)
""", language="python")

st.markdown("**Resultado:**")

st.image(os.path.join("assets", "img", "distance.png"))
