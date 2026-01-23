import streamlit as st
import geopandas as gpd

st.header("28. Applying Simple Functions on GeoDataFrames")

st.markdown("""
**Explicação:**
Métodos como `.translate`, `.rotate`, e `.scale` permitem modificar geometrias facilmente.
""")

st.code("""
translated = gdf.translate(xoff=1.0)
""", language="python")

st.image("assets/img/gdf_functions.png", caption="Translation")
