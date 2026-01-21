import streamlit as st
from shapely.geometry import Point
import os

st.set_page_config(page_title="3D Objects", page_icon="🧊")
st.markdown("# 13. 3D Objects in Shapely")

st.markdown("""
**Explicação:**

O Shapely suporta coordenadas Z (x, y, z). No entanto, a maioria das operações geométricas (interseção, buffer, etc.) são calculadas apenas no plano 2D (x, y), ignorando o Z, embora o valor Z seja preservado nos resultados.
""")

st.markdown("**Código:**")

st.code("""
from shapely.geometry import Point

# Ponto 3D (x, y, z)
p3d = Point(1, 2, 3)

print({p3d.has_z}) # True
print(p3d.z) # 3.0
""", language="python")

st.markdown("**Resultado:**")

st.image(os.path.join("assets", "img", "3d_point.png"))
