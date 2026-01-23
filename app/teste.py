import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from matplotlib.patches import Patch

def create_and_plot_farm_plots_gdf(fig, subplot_index):
    ax = fig.add_subplot(subplot_index)

    print("\n" + "="*70)
    print("EXEMPLO 2: Criando polígonos - Regiões de uma Fazenda")
    print("="*70)

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

    # Adicionar labels com informações
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
    return ax

# Assuming `fig` is already defined from previous cells or create a new one if this is the only plot
# If `fig` from previous cells is desired, comment out the next two lines and use the existing fig
fig = plt.figure(figsize=(16, 12)) # Create a new figure for this plot if running standalone
fig.suptitle('Criando GeoDataFrames do Zero - Exemplos Práticos', fontsize=16, fontweight='bold', y=1.02)

# Call the function to create and plot the farm plots
ax2 = create_and_plot_farm_plots_gdf(fig, 232)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()