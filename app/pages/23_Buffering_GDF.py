import streamlit as st
import geopandas as gpd

st.header("23. Buffering a GeoDataFrame")

st.markdown("""
**Explicação:**
Aplicar `.buffer()` em um GeoDataFrame retorna uma nova GeoSeries com as geometrias expandidas.
""")

st.code("""
buffered_gdf = gdf.buffer(0.5)
buffered_gdf.plot()
""", language="python")

st.image("assets/img/gdf_buffer.png", caption="Buffering")
