import streamlit as st
import geopandas as gpd

st.header("22. Simple Visualization with GeoPandas")

st.markdown("""
**Explicação:**
O método `.plot()` do GeoPandas é uma maneira rápida e poderosa de visualizar dados espaciais usando Matplotlib.
""")

st.code("""
gdf.plot(color='white', edgecolor='black')
""", language="python")

st.image("assets/img/gdf_visualization.png", caption="Visualization")
