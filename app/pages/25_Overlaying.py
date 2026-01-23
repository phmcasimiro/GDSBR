import streamlit as st
import geopandas as gpd

st.header("25. Overlaying GeoDataFrames")

st.markdown("""
**Explicação:**
`overlay` realiza operações de conjunto (união, interseção, diferença) entre dois GeoDataFrames completos.
""")

st.code("""
interseccao = gpd.overlay(df1, df2, how='intersection')
uniao = gpd.overlay(df1, df2, how='union')
""", language="python")

st.image("assets/img/gdf_overlay.png", caption="Overlay Operations")
