import streamlit as st
import geopandas as gpd
import numpy as np

st.header("29. Generating Random Synthetic Data")

st.markdown("""
**Explicação:**
Para testes, podemos gerar dados aleatórios usando numpy e converter para GeoDataFrame.
""")

st.code("""
x = np.random.rand(10)
y = np.random.rand(10)
gdf = gpd.GeoDataFrame(geometry=gpd.points_from_xy(x, y))
""", language="python")

st.image("assets/img/gdf_synthetic.png", caption="Synthetic Data")
