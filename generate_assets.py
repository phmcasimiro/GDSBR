import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon, MultiPoint, MultiPolygon
import numpy as np
import os

# Configuração Global
try:
    plt.style.use('seaborn-v0_8-whitegrid')
except:
    plt.style.use('ggplot')

output_dir = os.path.join('assets', 'img')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def save_fig(name):
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, name), dpi=100)
    plt.close()
    print(f"Gerado: {name}")

# --- 1. Point (Ponto) ---
fig, ax = plt.subplots(figsize=(8, 6))
ponto = Point(-47.8825, -15.7942)
ax.plot(ponto.x, ponto.y, marker='o', color='red', markersize=15, linestyle='None', label='Ponto P')
ax.annotate(f'P({ponto.x}, {ponto.y})', (ponto.x, ponto.y), xytext=(10, 10), textcoords='offset points', fontsize=12)
ax.set_xlim(ponto.x - 0.1, ponto.x + 0.1)
ax.set_ylim(ponto.y - 0.1, ponto.y + 0.1)
ax.set_title('Representação de um Ponto (Shapely)', fontsize=16)
ax.set_xlabel('Longitude', fontsize=12)
ax.set_ylabel('Latitude', fontsize=12)
ax.grid(True)
ax.legend()
save_fig('point_example.png')

# --- 2. Line (Linha) ---
fig, ax = plt.subplots(figsize=(6, 4))
line_coords = [(-47.9500, -15.7900), (-47.8200, -15.8000)]
line = LineString(line_coords)
x, y = line.xy
ax.plot(x, y, color='blue', linewidth=3, label='LineString')
ax.scatter(x, y, color='black')
ax.set_title('Exemplo de Linha (LineString)')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
save_fig('line_example.png')

# --- 3. Polygon (Polígono) ---
fig, ax = plt.subplots(figsize=(6, 4))
poly_coords = [(-47.8500, -15.8200), (-47.8000, -15.8200), (-47.8250, -15.8500), (-47.8500, -15.8200)]
poly = Polygon(poly_coords)
x, y = poly.exterior.xy
ax.fill(x, y, color='lightgreen', alpha=0.5, label='Polygon')
ax.plot(x, y, color='green', linewidth=2)
ax.set_title('Exemplo de Polígono (Polygon)')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
save_fig('polygon_example.png')

# --- 4. Buffering ---
fig, ax = plt.subplots(figsize=(6, 6))
p = Point(0, 0)
buffer = p.buffer(1)
x, y = buffer.exterior.xy
ax.fill(x, y, alpha=0.5, color='blue', label='Buffer (r=1)')
ax.plot(0, 0, 'ro', label='Point')
ax.set_title('Buffering a Point')
ax.legend()
ax.set_aspect('equal')
save_fig('buffer.png')

# --- 5. Set Operations ---
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
p1 = Polygon([(0,0), (2,0), (2,2), (0,2)])
p2 = Polygon([(1,1), (3,1), (3,3), (1,3)])
# Union
u = p1.union(p2)
x, y = u.exterior.xy
ax1.fill(x, y, alpha=0.5, color='purple')
ax1.set_title('Union')
# Intersection
i = p1.intersection(p2)
x, y = i.exterior.xy
ax2.fill(x, y, alpha=0.5, color='green')
ax2.set_title('Intersection')
# Difference
d = p1.difference(p2)
x, y = d.exterior.xy
ax3.fill(x, y, alpha=0.5, color='red')
ax3.set_title('Difference (P1 - P2)')
save_fig('sets.png')

# --- 6. Area and Perimeter ---
fig, ax = plt.subplots(figsize=(6, 6))
poly = Polygon([(0,0), (4,0), (4,3), (0,0)])
x, y = poly.exterior.xy
ax.fill(x, y, alpha=0.3, color='orange')
ax.plot(x, y, color='black')
ax.text(1.5, 1, f"Area: {poly.area}\nPerim: {poly.length}", fontsize=12)
ax.set_title('Area and Perimeter')
save_fig('area_perimeter.png')

# --- 7. Centroids ---
fig, ax = plt.subplots(figsize=(6, 6))
poly = Polygon([(0,0), (4,0), (4,4), (0,4)])
centroid = poly.centroid
x, y = poly.exterior.xy
ax.fill(x, y, alpha=0.3, color='cyan')
ax.plot(centroid.x, centroid.y, 'rx', markersize=10, label='Centroid')
ax.set_title('Polygon Centroid')
ax.legend()
save_fig('centroid.png')

# --- 8. Enclosing (Convex Hull) ---
fig, ax = plt.subplots(figsize=(6, 6))
points = MultiPoint([(0,0), (1,3), (2,2), (4,1), (3,0), (-1,1)])
hull = points.convex_hull
for p in points.geoms:
    ax.plot(p.x, p.y, 'ko')
x, y = hull.exterior.xy
ax.plot(x, y, 'b--', label='Convex Hull')
ax.set_title('Convex Hull')
ax.legend()
save_fig('convex_hull.png')

# --- 9. Bounding Box ---
fig, ax = plt.subplots(figsize=(6, 6))
poly = Polygon([(1,1), (2,3), (3,2)])
minx, miny, maxx, maxy = poly.bounds
bbox = Polygon([(minx, miny), (maxx, miny), (maxx, maxy), (minx, maxy)])
x, y = poly.exterior.xy
ax.fill(x, y, color='yellow', alpha=0.5)
x, y = bbox.exterior.xy
ax.plot(x, y, 'r--', label='Bounding Box')
ax.set_title('Bounding Box')
ax.legend()
save_fig('bbox.png')

# --- 10. Within Test ---
fig, ax = plt.subplots(figsize=(6, 6))
poly = Polygon([(0,0), (4,0), (4,4), (0,4)])
p_in = Point(2, 2)
p_out = Point(5, 5)
x, y = poly.exterior.xy
ax.plot(x, y, 'k-')
ax.plot(p_in.x, p_in.y, 'go', label='Within (True)')
ax.plot(p_out.x, p_out.y, 'ro', label='Within (False)')
ax.set_title('Within Test')
ax.legend()
save_fig('within.png')

# --- 11. Distance ---
fig, ax = plt.subplots(figsize=(6, 6))
p1 = Point(0, 0)
p2 = Point(3, 4)
dist = p1.distance(p2)
ax.plot([p1.x, p2.x], [p1.y, p2.y], 'b--')
ax.plot(p1.x, p1.y, 'go')
ax.plot(p2.x, p2.y, 'go')
ax.text(1.5, 2, f"Dist: {dist}", fontsize=12)
ax.set_title('Euclidean Distance')
save_fig('distance.png')

# --- 12. Simplifying ---
fig, ax = plt.subplots(figsize=(8, 4))
coords = [(x, np.sin(x) + 0.1*np.random.normal()) for x in np.linspace(0, 10, 50)]
line = LineString(coords)
simplified = line.simplify(0.5, preserve_topology=False)
x, y = line.xy
ax.plot(x, y, 'b-', alpha=0.3, label='Original')
x, y = simplified.xy
ax.plot(x, y, 'r-', linewidth=2, label='Simplified (tol=0.5)')
ax.set_title('Simplifying Geometries')
ax.legend()
save_fig('simplify.png')

# --- 14. Built-in Datasets Alternative (Continente Fictício) ---
import geopandas as gpd
from shapely.geometry import box, Point

fig, ax = plt.subplots(figsize=(10, 6))

# Dataset de exemplo: Regiões de um continente fictício
def criar_continente_ficticio():
    # Criar polígonos representando países/regiões
    # Coordenadas para um continente fictício
    coordenadas = [
        box(0, 0, 5, 5),      # Região Noroeste
        box(5, 0, 10, 5),     # Região Nordeste
        box(0, 5, 5, 10),     # Região Sudoeste
        box(5, 5, 10, 10),    # Região Sudeste
        box(2.5, 2.5, 7.5, 7.5)  # Região Central
    ]
    
    nomes_regioes = ['Noroeste', 'Nordeste', 'Sudoeste', 'Sudeste', 'Central']
    populacoes = [1500000, 2300000, 1800000, 2700000, 1200000]
    
    continente_data = {
        'regiao': nomes_regioes,
        'populacao': populacoes,
        'geometry': coordenadas
    }
    
    gdf = gpd.GeoDataFrame(continente_data, crs="EPSG:4326")
    
    # Adicionar algumas cidades (pontos)
    cidades = {
        'cidade': ['Capital', 'Porto', 'Montanha', 'Vale', 'Lago'],
        'geometry': [
            Point(5, 5),
            Point(8, 2),
            Point(3, 7),
            Point(6, 6),
            Point(2, 3)
        ]
    }
    
    gdf_cidades = gpd.GeoDataFrame(cidades, crs="EPSG:4326")
    
    return gdf, gdf_cidades

# Usar o dataset fictício
gdf_regioes, gdf_cidades = criar_continente_ficticio()

# Plotar as regiões
gdf_regioes.plot(
    ax=ax,
    column='populacao',
    cmap='Blues',
    edgecolor='black',
    legend=True,
    legend_kwds={'label': "População por região"}
)

# Plotar as cidades
gdf_cidades.plot(ax=ax, color='red', markersize=50, alpha=0.7)

# Adicionar labels para as cidades
for idx, row in gdf_cidades.iterrows():
    ax.annotate(
        text=row['cidade'],
        xy=(row.geometry.x, row.geometry.y),
        xytext=(3, 3),
        textcoords="offset points",
        fontsize=9,
        color='darkred'
    )

ax.set_title("Continente Fictício - Regiões e Cidades")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

save_fig('gdf_builtin.png')


# --- 15. Parsing Data File ---
file_path = r"data\NaturalEarth_Geom\ne_10m_admin_0_countries\ne_10m_admin_0_countries.shp"
if os.path.exists(file_path):
    try:
        gdf = gpd.read_file(file_path)
        fig, ax = plt.subplots(figsize=(10, 6))
        gdf.plot(ax=ax, color='lightgrey', edgecolor='black')
        ax.set_title("Mapa Mundi - Natural Earth", fontsize=15)
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        save_fig('gdf_parsing2.png')
    except Exception as e:
        print(f"Error reading file: {e}")
else:
    print(f"File not found: {file_path}")


# --- 16. GDF from Scratch ---
fig, ax = plt.subplots(figsize=(8, 6))

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
gdf_cidades = gpd.GeoDataFrame(
    data=cidades_dados,
    geometry=cidades_geometrias,
    crs="EPSG:4326" # WGS84 - sistema global de coordenadas
)

# Visualizar
gdf_cidades.plot(
    ax=ax,
    markersize=gdf_cidades['populacao_milhoes'] * 20, # Tamanho proporcional
    color='red',
    edgecolor='black',
    alpha=0.7
)

# Adicionar labels
for idx, row in gdf_cidades.iterrows():
    ax.annotate(
        text=row['cidade'],
        xy=(row.geometry.x, row.geometry.y),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=9,
        fontweight='bold'
    )

ax.set_title('1. Cidades Brasileiras (Pontos)', fontweight='bold')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.grid(True, alpha=0.3)
save_fig('gdf_scratch.png')

# Maintain compatibility with later steps
gdf_scratch = gdf_cidades

# --- 16b. GDF from Scratch (Polygons - Fazenda) ---
from matplotlib.patches import Patch

fig, ax = plt.subplots(figsize=(8, 6))

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


# --- 17. GDF from DataFrame ---
import pandas as pd
fig, ax = plt.subplots(figsize=(6, 6))
df = pd.DataFrame({'city': ['A', 'B'], 'lat': [0, 1], 'lon': [1, 0]})
gdf_from_df = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat))
gdf_from_df.plot(ax=ax, color='purple', marker='^', markersize=50)
ax.set_title("GDF from DataFrame")
save_fig('gdf_from_df.png')

# --- 18. Writing to File (Visual check avoided, just plot) ---
save_fig('gdf_writing.png') # Placeholder reusing previous plot context generally works or just skip visual

# --- 19. Geometry Column (GeoSeries) ---
fig, ax = plt.subplots(figsize=(6, 6))
gdf_scratch.geometry.plot(ax=ax, color='orange')
ax.set_title("Accessing Geometry Column")
save_fig('gdf_geoseries.png')

# --- 20. Bounds ---
fig, ax = plt.subplots(figsize=(6, 6))
poly_bound = Polygon([(0,0), (1,3), (2,1)])
s = gpd.GeoSeries([poly_bound])
s.plot(ax=ax, alpha=0.5)
minx, miny, maxx, maxy = s.total_bounds
rect = box(minx, miny, maxx, maxy)
x, y = rect.exterior.xy
ax.plot(x, y, 'r--', label='Total Bounds')
ax.legend()
ax.set_title("Bounds of GeoSeries")
save_fig('gdf_bounds.png')

# --- 21. Area and Perimeter (GDF) ---
fig, ax = plt.subplots(figsize=(6, 6))
s = gpd.GeoSeries([Polygon([(0,0), (0,2), (2,2), (2,0)])])
s.plot(ax=ax, color='cyan', alpha=0.5)
area = s.area[0]
perim = s.length[0]
ax.text(0.5, 1, f"Area: {area}\nPerim: {perim}",ha='center')
ax.set_title("Area and Perimeter (GDF)")
save_fig('gdf_area_perimeter.png')

# --- 22. Simple Visualization ---
fig, ax = plt.subplots(figsize=(6, 6))
gdf_regioes.plot(ax=ax, color='white', edgecolor='black')
ax.set_title("Simple Visualization")
save_fig('gdf_visualization.png')


# --- 23. Buffering GDF ---
fig, ax = plt.subplots(figsize=(6, 6))
gdf_scratch.buffer(0.5).plot(ax=ax, alpha=0.5, color='red')
gdf_scratch.plot(ax=ax, color='black')
ax.set_title("Buffering GeoDataFrame")
save_fig('gdf_buffer.png')

# --- 24. Spatial Join ---
fig, ax = plt.subplots(figsize=(6, 6))
polys = gpd.GeoDataFrame({'id': [1], 'geometry': [box(0, 0, 3, 3)]})
points = gpd.GeoDataFrame({'id': [2, 3], 'geometry': [Point(1, 1), Point(4, 4)]})
polys.plot(ax=ax, alpha=0.3, color='blue')
points.plot(ax=ax, color='red', label='Points')
ax.set_title("Spatial Join Setup")
save_fig('gdf_sjoin.png')


# --- 25. Overlaying ---
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
df1 = gpd.GeoDataFrame({'geometry': [box(0, 0, 2, 2)]})
df2 = gpd.GeoDataFrame({'geometry': [box(1, 1, 3, 3)]})
# Union
gpd.overlay(df1, df2, how='union').plot(ax=ax1, cmap='tab10', alpha=0.5)
ax1.set_title('Union')
# Intersection
gpd.overlay(df1, df2, how='intersection').plot(ax=ax2, color='green', alpha=0.5)
ax2.set_title('Intersection')
# Difference
gpd.overlay(df1, df2, how='difference').plot(ax=ax3, color='red', alpha=0.5)
ax3.set_title('Difference')
save_fig('gdf_overlay.png')

# --- 26. Dissolving ---
fig, ax = plt.subplots(figsize=(6, 6))
d = {'col': [1, 1], 'geometry': [box(0,0,1,1), box(1,0,2,1)]}
gdf = gpd.GeoDataFrame(d)
dissolved = gdf.dissolve(by='col')
dissolved.plot(ax=ax, color='yellow', edgecolor='black')
ax.set_title("Dissolving Polygons")
save_fig('gdf_dissolve.png')

# --- 27. Splitting (Explode) ---
fig, ax = plt.subplots(figsize=(6, 6))
mp = MultiPolygon([Polygon([(0,0),(1,0),(1,1)]), Polygon([(2,2),(3,2),(3,3)])])
gdf_mp = gpd.GeoDataFrame({'id': [1], 'geometry': [mp]})
exploded = gdf_mp.explode(index_parts=True)
exploded.plot(ax=ax, column=exploded.index, cmap='Set1')
ax.set_title("Splitting/Exploding Geometries")
save_fig('gdf_splitting.png')

# --- 28. Simple Functions (Translate) ---
fig, ax = plt.subplots(figsize=(6, 6))
gdf_scratch.plot(ax=ax, color='red', label='Original')
gdf_scratch.translate(xoff=1.0).plot(ax=ax, color='blue', label='Translated')
ax.legend()
ax.set_title("Applying Functions (Translate)")
save_fig('gdf_functions.png')

# --- 29. Random Synthetic Data ---
fig, ax = plt.subplots(figsize=(6, 6))
# Create 10 random points
x = np.random.rand(10) * 10
y = np.random.rand(10) * 10
gdf_random = gpd.GeoDataFrame(geometry=gpd.points_from_xy(x, y))
gdf_random.plot(ax=ax, color='purple')
ax.set_title("Random Synthetic Data")
save_fig('gdf_synthetic.png')

# --- 30. Counting Points in Polygons ---
fig, ax = plt.subplots(figsize=(6, 6))
polys = gpd.GeoDataFrame({'geometry': [box(0,0,5,5), box(5,0,10,5)]})
pts = gpd.GeoDataFrame({'geometry': gpd.points_from_xy(np.random.rand(20)*10, np.random.rand(20)*5)})
polys.plot(ax=ax, alpha=0.3, edgecolor='k')
pts.plot(ax=ax, color='red', markersize=5)
# Sjoin to count
joined = gpd.sjoin(pts, polys, predicate='within')
counts = joined.index_right.value_counts()
for idx, row in polys.iterrows():
    c = counts.get(idx, 0)
    ax.text(row.geometry.centroid.x, row.geometry.centroid.y, str(c), fontsize=20, ha='center')
ax.set_title("Counting Points in Polygons")
save_fig('gdf_counting.png')
