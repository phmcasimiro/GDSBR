import streamlit as st
from shapely.geometry import Point, Polygon
import os

st.set_page_config(page_title="Within Test", page_icon="🎯")
st.markdown("# 10. Within-test")

st.markdown("""
**Explicação:**

Verifica se uma geometria está totalmente dentro de outra. Retorna `True` ou `False`. É fundamental para análises do tipo "Ponto em Polígono".
""")

st.markdown("**Código:**")

st.code("""
from shapely.geometry import Point, Polygon

poly = Polygon([(0,0), (4,0), (4,4), (0,4)])
p_in = Point(2, 2)
p_out = Point(5, 5)

print(p_in.within(poly))  # True
print(poly.contains(p_in)) # True
print(p_out.within(poly)) # False
""", language="python")

st.markdown("**Resultado:**")

st.image(os.path.join("assets", "img", "within.png"))
