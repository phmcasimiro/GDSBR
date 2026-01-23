import streamlit as st
import geopandas as gpd
from shapely.geometry import Polygon

st.header("21. Area and Perimeter Computation")

st.markdown("""
**Explicação:**
GeoDataFrames calculam área e perímetro da mesma forma que o Shapely, mas para toda a série de geometrias de uma vez.
""")

st.code("""
s = gpd.GeoSeries([Polygon([(0,0), (0,2), (2,2), (2,0)])])
area = s.area
perimetro = s.length
""", language="python")

st.image("assets/img/gdf_area_perimeter.png", caption="Area and Perimeter")
