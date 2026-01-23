import streamlit as st
import geopandas as gpd
from shapely.geometry import Point

st.header("19. Accessing the Geometry Column as a GeoSeries")

st.markdown("""
**Explicação:**
A coluna de geometria de um GeoDataFrame é uma `GeoSeries`. Você pode acessá-la diretamente para realizar operações em massa.
""")

st.code("""
# Acessando a coluna de geometria
geometrias = gdf.geometry

# Plotando apenas a série geométrica
geometrias.plot()
""", language="python")

st.image("assets/img/gdf_geoseries.png", caption="Accessing Geometry")
