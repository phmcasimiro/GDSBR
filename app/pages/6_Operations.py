import streamlit as st
from shapely.geometry import Polygon
import os

st.set_page_config(page_title="Operações de Conjuntos", page_icon="🔄")
st.markdown("# 5. Operações de Conjuntos em Geometrias")

st.markdown("""
**Explicação:**

O Shapely permite realizar operações da teoria dos conjuntos entre geometrias, como:
- **União**: A união de duas geometrias.
- **Interseção**: A parte comum entre elas.
- **Diferença**: O que resta de uma geometria ao subtrair a outra.
""")

st.markdown("**Código:**")

st.code("""
from shapely.geometry import Polygon

p1 = Polygon([(0,0), (2,0), (2,2), (0,2)])
p2 = Polygon([(1,1), (3,1), (3,3), (1,3)])

uniao = p1.union(p2)
interseccao = p1.intersection(p2)
diferenca = p1.difference(p2)
""", language="python")

st.markdown("**Resultado:**")

st.image(os.path.join("assets", "img", "sets.png"))
