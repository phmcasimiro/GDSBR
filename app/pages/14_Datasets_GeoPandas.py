import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import box, Point

st.header("14. Built-in Datasets Alternative (Continente Fictício)")

st.markdown("""
**Explicação:**

A Biblioteca GeoPandas facilita a manipulação de dados vetoriais (pontos, linhas, polígonos) e criação de GeoDataFrames.

Abaixo, foi criado um exemplo completo de um **"Continente Fictício"** com regiões (polígonos) e cidades (pontos) para ilustrar como criar e visualizar GeoDataFrames compostos.
""")

st.markdown("**Código:**")

st.code("""
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import box, Point

# 1. Criando dados das Regiões (Polígonos)
coordenadas = [
    box(0, 0, 5, 5),      # Noroeste
    box(5, 0, 10, 5),     # Nordeste
    box(0, 5, 5, 10),     # Sudoeste
    box(5, 5, 10, 10),    # Sudeste
    box(2.5, 2.5, 7.5, 7.5) # Central
]
nomes = ['Noroeste', 'Nordeste', 'Sudoeste', 'Sudeste', 'Central']
populacao = [1.5, 2.3, 1.8, 2.7, 1.2] # Milhões

gdf_regioes = gpd.GeoDataFrame({
    'regiao': nomes,
    'populacao': populacao,
    'geometry': coordenadas
}, crs="EPSG:4326")

# 2. Criando dados das Cidades (Pontos)
cidades = {
    'nome': ['Capital', 'Porto', 'Montanha'],
    'geometry': [
        Point(5, 5),
        Point(8, 2),
        Point(3, 7)
    ]
}
gdf_cidades = gpd.GeoDataFrame(cidades, crs="EPSG:4326")

# 3. Visualizando
fig, ax = plt.subplots(figsize=(8, 6))

# Plot Regiões (colorido por população)
gdf_regioes.plot(ax=ax, column='populacao', cmap='Blues', legend=True, edgecolor='black')

# Plot Cidades
gdf_cidades.plot(ax=ax, color='red', markersize=50)

# Labels
for idx, row in gdf_cidades.iterrows():
    ax.annotate(row['nome'], (row.geometry.x, row.geometry.y), xytext=(5,5), textcoords='offset points')

plt.title("Continente Fictício")
plt.show()
""", language="python")

st.markdown("**Resultado:**")

st.image("assets/img/gdf_builtin.png", caption="Exemplo Didático: Continente Fictício")
