import streamlit as st
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

st.header("17. Creating a GeoDataFrame from a DataFrame")

st.markdown("""
**Explicação:**
É comum converter um DataFrame pandas com colunas de latitude/longitude em um GeoDataFrame usando `gpd.points_from_xy()`.
""")

st.code("""
import pandas as pd
import geopandas as gpd

df = pd.DataFrame({'city': ['A', 'B'], 'lat': [0, 1], 'lon': [1, 0]})
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat))

print(gdf)
""", language="python")

st.image("assets/img/gdf_from_df.png", caption="GDF from DataFrame")
