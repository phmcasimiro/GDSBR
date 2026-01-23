import streamlit as st
import geopandas as gpd

st.header("26. Dissolving Polygons")

st.markdown("""
**Explicação:**
`dissolve` agrega geometrias com base em uma coluna de atributo, unindo-as em uma única geometria (similar ao GroupBy do SQL/Pandas).
""")

st.code("""
dissolved = gdf.dissolve(by='coluna_agrupadora')
""", language="python")

st.image("assets/img/gdf_dissolve.png", caption="Dissolving")
