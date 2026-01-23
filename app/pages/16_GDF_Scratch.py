import streamlit as st
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

st.header("16. GeoDataFrame from Scratch")

st.markdown("""
**Explicação:**

Você pode criar um GeoDataFrame manualmente passando um dicionário de dados e especificando a coluna de geometria.

Neste item aprenderemos a criar GeoDataFrames manualmente, o que pode ser útil para:
1. Criar dados de teste
2. Processar dados em tempo real
3. Converter dados tabulares em dados geoespaciais
""")

st.markdown("""**Código:**""")

st.code("""
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Criar dados de cidades brasileiras
cidades_dados = {
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília', 'Salvador'],
    'estado': ['SP', 'RJ', 'MG', 'DF', 'BA'],
    'populacao_milhoes': [12.3, 6.7, 2.5, 3.1, 2.9],
    'regiao': ['Sudeste', 'Sudeste', 'Sudeste', 'Centro-Oeste', 'Nordeste'],
    'pib_bilhoes': [699, 329, 125, 254, 103]
}

# Geometrias correspondentes (coordenadas reais)
cidades_geometrias = [
    Point(-46.6333, -23.5505), # São Paulo
    Point(-43.1729, -22.9068), # Rio de Janeiro
    Point(-43.9378, -19.8157), # Belo Horizonte
    Point(-47.8825, -15.7939), # Brasília
    Point(-38.5108, -12.9711)  # Salvador
]

# Criar GeoDataFrame explicitamente
gdf = gpd.GeoDataFrame(
    data=cidades_dados,
    geometry=cidades_geometrias,
    crs="EPSG:4326" # WGS84 - sistema global de coordenadas
)

print(gdf)
""", language="python")

st.markdown("""**Resultado:**""")

st.image("assets/img/gdf_scratch.png", caption="GDF from Scratch")


st.markdown("""
**Explicação:**

Exemplo de como criar um GeoDataFrame manualmente passando um dicionário de dados e especificando a coluna de geometria.
""")

st.markdown("""**Código:**""")

st.code("""
# Criar dados de talhões de uma fazenda
talhoes_dados = {
    'talhao': ['A1', 'A2', 'B1', 'B2', 'C1'],
    'cultura': ['Soja', 'Milho', 'Café', 'Cana', 'Soja'],
    'area_ha': [50, 45, 30, 60, 55],
    'produtividade': [3.5, 4.2, 2.8, 6.0, 3.8],
    'responsavel': ['João', 'Maria', 'José', 'Ana', 'Carlos']
}

# Geometrias - polígonos retangulares simulando talhões
talhoes_geometrias = [
    Polygon([(0, 0), (5, 0), (5, 10), (0, 10), (0, 0)]), # Talhão A1
    Polygon([(5, 0), (10, 0), (10, 10), (5, 10), (5, 0)]), # Talhão A2
    Polygon([(0, 10), (5, 10), (5, 16), (0, 16), (0, 10)]), # Talhão B1
    Polygon([(5, 10), (10, 10), (10, 16), (5, 16), (5, 10)]), # Talhão B2
    Polygon([(2.5, 16), (7.5, 16), (7.5, 20), (2.5, 20), (2.5, 16)]) # Talhão C1
]

gdf_talhoes = gpd.GeoDataFrame(
    data=talhoes_dados,
    geometry=talhoes_geometrias,
    crs="EPSG:4326"
)

# Mapear culturas para cores
cores_culturas = {
    'Soja': 'yellowgreen',
    'Milho': 'gold',
    'Café': 'saddlebrown',
    'Cana': 'darkgreen'
}

# Criar coluna de cores
gdf_talhoes['cor'] = gdf_talhoes['cultura'].map(cores_culturas)

# Plotar com cores por cultura
gdf_talhoes.plot(
    ax=ax,
    color=gdf_talhoes['cor'],
    edgecolor='black',
    linewidth=1.5,
    alpha=0.7
)

# Adicionar labels
for idx, row in gdf_talhoes.iterrows():
    # Calcular centro do polígono
    centro = row.geometry.centroid
    ax.annotate(
        text=f"{row['talhao']}\n{row['area_ha']} ha\n{row['cultura']}",
        xy=(centro.x, centro.y),
        xytext=(0, 0),
        textcoords="offset points",
        fontsize=8,
        ha='center',
        va='center',
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8)
    )

ax.set_title('2. Talhões de Fazenda (Polígonos)', fontweight='bold')
ax.set_xlabel('Coordenada X (km)')
ax.set_ylabel('Coordenada Y (km)')
ax.grid(True, alpha=0.3)

# Legenda de cores
legend_elements = [Patch(facecolor=cor, label=cultura, alpha=0.7)
                   for cultura, cor in cores_culturas.items()]
ax.legend(handles=legend_elements, title='Culturas', loc='upper left')

save_fig('gdf_farm.png')
""", language="python")

st.markdown("""**Resultado:**""")

st.image("assets/img/gdf_farm.png", caption="GDF from Scratch")