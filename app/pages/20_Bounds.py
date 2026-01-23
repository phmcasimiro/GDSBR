import streamlit as st

st.header("20. Bounds of a GeoSeries")

st.markdown("""
**Explicação:**
Você pode obter os limites (bounds) de cada geometria ou da série inteira (`total_bounds`), retornando (minx, miny, maxx, maxy).
""")

st.code("""
# Limites totais (minx, miny, maxx, maxy)
bounds = gdf.total_bounds
print(bounds)
""", language="python")

st.image("assets/img/gdf_bounds.png", caption="Bounds")
