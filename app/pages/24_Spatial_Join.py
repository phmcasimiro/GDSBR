import streamlit as st
import geopandas as gpd

st.header("24. Spatial Join with GeoPandas")

st.markdown("""
**Explicação:**
`sjoin` permite unir dois GeoDataFrames com base em sua relação espacial (ex: quais pontos estão dentro de quais polígonos).
""")

st.code("""
joined = gpd.sjoin(pontos, poligonos, op='within')
""", language="python")

st.image("assets/img/gdf_sjoin.png", caption="Spatial Join Params")
