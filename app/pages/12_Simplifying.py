import streamlit as st
from shapely.geometry import LineString
import os

st.set_page_config(page_title="Simplifying Geometries", page_icon="✂️")
st.markdown("# 12. Simplifying Geometries")

st.markdown("""
**Explicação:**

Reduz o número de vértices de uma geometria mantendo sua forma geral. Útil para reduzir tamanho de arquivos e acelerar renderização. Geralmente usa o algoritmo Douglas-Peucker.
""")

st.markdown("**Código:**")

st.code("""
from shapely.geometry import LineString

line = LineString([(0,0), (1,0.1), (2,-0.1), (3,0), (4,0)])
# tolerance: distância máxima permitida entre a linha original e a simplificada
simplified = line.simplify(tolerance=0.2, preserve_topology=False)

print(line)
print(simplified)
""", language="python")

st.markdown("**Resultado:**")

st.image(os.path.join("assets", "img", "simplify.png"))
