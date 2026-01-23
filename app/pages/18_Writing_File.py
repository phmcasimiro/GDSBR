import streamlit as st

st.header("18. Writing a GeoDataFrame to a File")

st.markdown("""
**Explicação:**
Salvar um GeoDataFrame em arquivo (Shapefile, GeoJSON, etc) é simples com o método `.to_file()`.
""")

st.code("""
# Salvar como GeoJSON
# gdf.to_file("meu_arquivo.geojson", driver='GeoJSON')

# Salvar como Shapefile
# gdf.to_file("meu_arquivo.shp")
""", language="python")

st.image("assets/img/gdf_writing.png", caption="Writing to File")
