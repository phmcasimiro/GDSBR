import streamlit as st
import geopandas as gpd

st.header("30. Counting Points in Polygons")

st.markdown("""
**Explicação:**
Combinando Spatial Join (`sjoin`) com operações de agregação, podemos contar quantos pontos caem em cada polígono.
""")

st.code("""
joined = gpd.sjoin(pts, polys, predicate='within')
counts = joined.index_right.value_counts()
""", language="python")

st.image("assets/img/gdf_counting.png", caption="Point Counts")
