import streamlit as st
import geopandas as gpd

st.header("27. Splitting Geometries in a GeoDataFrame")

st.markdown("""
**Explicação:**
`explode` separa MultiPolígonos ou MultiLinhas em linhas individuais de geometrias simples.
""")

st.code("""
exploded = gdf.explode(index_parts=True)
""", language="python")

st.image("assets/img/gdf_splitting.png", caption="Exploding")
