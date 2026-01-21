import streamlit as st
from shapely.geometry import MultiPoint
import os

st.set_page_config(page_title="Polígono Envolvente", page_icon="📦")
st.markdown("# 8. Polígono Envolvente (Enclosing Polygons)")

st.markdown("""
**Explicação:**

Uma operação comum é encontrar o menor polígono convexo que envolve um conjunto de pontos (Convex Hull). Imagine um elástico esticado ao redor dos pinos (pontos).
""")

st.markdown("**Código:**")

st.code("""
from shapely.geometry import MultiPoint

points = MultiPoint([(0,0), (1,3), (2,2), (4,1), (3,0), (-1,1)])
hull = points.convex_hull

print(hull) # Retorna um Polígono
""", language="python")

st.markdown("**Resultado:**")

st.image(os.path.join("assets", "img", "convex_hull.png"))
