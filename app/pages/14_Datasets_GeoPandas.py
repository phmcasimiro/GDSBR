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

st.markdown("### **Explicando o Código:**")

st.markdown("#### Parte 1: Importando as Bibliotecas")

st.code("""
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import box, Point
""", language="python")

st.markdown("""
`geopandas (gpd)`: É a "biblioteca principal" para trabalhar com dados geográficos

`matplotlib.pyplot (plt)`: É a biblioteca usada para projetar mapas

`box` e `Point`: São métodos usados para projetar formas geométricas:

`box(x1, y1, x2, y2)`: Cria um retângulo

`Point(x, y)`: Cria um ponto
""")

st.markdown("#### Parte 2: Criando as Regiões (Polígonos)")

st.code("""
coordenadas = [
    box(0, 0, 5, 5),      # Noroeste
    box(5, 0, 10, 5),     # Nordeste
    box(0, 5, 5, 10),     # Sudoeste
    box(5, 5, 10, 10),    # Sudeste
    box(2.5, 2.5, 7.5, 7.5) # Central
]
""", language="python")

st.markdown("""
- Cada `box(x1, y1, x2, y2)` define um retângulo:
- `x1, y1`: Canto inferior esquerdo
- `x2, y2`: Canto superior direito
- Exemplo: `box(0, 0, 5, 5)` cria um quadrado de 5x5 unidades
""")

st.markdown("####  Parte 3: Criando o GeoDataFrame das Regiões")

st.code("""
gdf_regioes = gpd.GeoDataFrame({
    'regiao': nomes,
    'populacao': populacao,
    'geometry': coordenadas
}, crs="EPSG:4326")
""", language="python")

st.markdown("""

- GeoDataFrame: É como uma "tabela Excel especial" que tem:
    - Colunas normais (regiao, populacao)
    - Coluna especial geometry (as formas dos polígonos)

- Estrutura da tabela:

| regiao    | populacao | geometry          |
|-----------|-----------|-------------------|
| Noroeste  | 1.5       | POLYGON((0 0,...))|
| Nordeste  | 2.3       | POLYGON((5 0,...))|
| ...       | ...       | ...               |
""")

st.markdown("#### Parte 4: Criando as Cidades (Pontos)")

st.code("""
cidades = {'nome': ['Capital', 'Porto', 'Montanha'],
    'geometry': [
        Point(5, 5),    # Centro do mapa
        Point(8, 2),    # Leste, baixo
        Point(3, 7)     # Oeste, alto
        ]
}
gdf_cidades = gpd.GeoDataFrame(cidades, crs="EPSG:4326")
""", language="python")

st.markdown("""
- Cada Point(x, y) é uma cidade
- Coordenadas são como "endereços matemáticos" no mapa
- Também criamos um GeoDataFrame, mas agora com pontos
""")

st.markdown("#### Parte 5: Projetando o Mapa")

st.code("""
fig, ax = plt.subplots(figsize=(8, 6))
""", language="python")

st.markdown("""
- Projetamos a área total do mapa (figura) de 8x6 polegadas
- `ax` : É a área onde projetamos o mapa
""")

st.markdown("#### Parte 5: Projetando o Mapa")

st.code("""
fig, ax = plt.subplots(figsize=(8, 6))
""", language="python")

st.markdown("""
- Projetamos a área total do mapa (figura) de 8x6 polegadas
- `ax` : É a área onde projetamos o mapa
""")

st.markdown("#### Parte 5.1: Projetando as regiões")

st.code("""
gdf_regioes.plot(ax=ax, column='populacao', cmap='Blues', legend=True, edgecolor='black')
""", language="python")

st.markdown("""
- `ax=ax`: "Projete nesta tela específica"

- `column='populacao'`: "Utilize a coluna 'populacao' para construir o mapa temático das regiões"

- `cmap='Blues'`: "Use tons de azul (quanto mais escuro, maior a população)"

- `legend=True`: "Mostre uma legenda explicando as cores"

- `edgecolor='black'`: "Contornos pretos entre as regiões"
""")

st.markdown("#### Parte 5.2: Projetando as Cidades")

st.code("""
gdf_cidades.plot(ax=ax, color='red', markersize=50)
""", language="python")

st.markdown("""
- No mesmo mapa projetado `ax=ax`, adicione os pontos

- `color='red'`: Todas as cidades são vermelhas

- `markersize=50`: Tamanho dos pontos (50 é bem visível)
""")

st.markdown("#### Parte 5.3: Nomeando as cidades")

st.code("""
for idx, row in gdf_cidades.iterrows():
    ax.annotate(row['nome'], (row.geometry.x, row.geometry.y), 
                xytext=(5,5), textcoords='offset points')
""", language="python")

st.markdown("""
- "Para cada cidade no mapa, escreva seu nome 5 pixels acima e à direita do ponto"

- `iterrows()`: "Percorra linha por linha da tabela de cidades"

- `row.geometry.x` e `row.geometry.y`: Pegue as coordenadas X e Y do ponto

- `xytext=(5,5)`: Desloque o texto 5 pixels em X e Y

- `textcoords='offset points'`: "As coordenadas estão em pixels"
""")

st.markdown("#### Conceitos Chave")

st.markdown("""

1. GeoDataFrame ≠ DataFrame normal
    - Tem coluna geometry especial
    - Entende coordenadas e formas

2. Duas formas básicas:
    - Polígonos (box): Áreas (regiões, países, bairros)
    - Pontos (Point): Localizações específicas (cidades, lojas)

3. CRS é essencial,sem CRS, o computador não sabe como projetar o mapa
    - EPSG:4326 = Coordenadas de GPS (lat/long)


- **CRS:** ***SIRGAS 2000***
    - **TIPO:** _Geográfico_
    - **CÓDIGO:** _`4674`_
    - **DESCRIÇÃO:** _Padrão oficial do IBGE. Coordenadas em Latitude/Longitude_
- **CRS:** ***SIRGAS 2000/UTM zone 23S***
    - **TIPO:** _Projetado_
    - **CÓDIGO:** _`31983`_
    - **DESCRIÇÃO:** _Mais usado (Sul/Sudeste/Centro-Oeste). Coordenadas em metros (E, N)_
- **CRS:** ***SIRGAS 2000/UTM zone 22S***
    - **TIPO:** _Projetado_
    - **CÓDIGO:** _`31982`_
    - **DESCRIÇÃO:** _Usado no Sul e parte do Sudeste._
- **CRS:** ***SIRGAS 2000/UTM zone 24S***
    - **TIPO:** _Projetado_
    - **CÓDIGO:** _`31984`_
    - **DESCRIÇÃO:** _Usado no Sudeste e Nordeste._
- **CRS:** ***WGS 84***
    - **TIPO:** _Geográfico_
    - **CÓDIGO:** _`4326`_
    - **DESCRIÇÃO:** _Padrão Global (GPS/Webmapping). Latitude/Longitude._
- **CRS:** ***SAD 1969/UTM zone 23S***
    - **TIPO:** _Projetado_
    - **CÓDIGO:** _`29193`_
    - **DESCRIÇÃO:** _Antigo padrão (ainda em uso em muitos projetos)._

4. Ordem de projeção das camadas:
    - Primeiro projeta as regiões (fundo)
    - Depois projeta as cidades (sobreposto)
    - Finalmente adiciona texto (última camada)
""")
