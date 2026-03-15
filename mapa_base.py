# =============================================================================
# MAPA BASE - Distrito Federal (Brasília)
# Projeto: GDS_BR | Geo Data Science Brasil
# Descrição: Script para gerar um mapa cartográfico do Distrito Federal com
#            dados oficiais do IBGE, usando o sistema SIRGAS 2000 (EPSG:4674).
#
# LAYOUT DOS PAINÉIS:
#  ┌──────────────────────┬──────────────────┐
#  │                      │  Localização     │
#  │                      ├──────────────────┤
#  │        MAPA          │  Legenda         │
#  │                      ├──────────────────┤
#  │                      │  Info. Técnicas  │
#  │                      ├──────────────────┤
#  │                      │  Info. Cartogr.  │
#  └──────────────────────┴──────────────────┘
# =============================================================================


# --- SEÇÃO 1: IMPORTAÇÃO DAS BIBLIOTECAS ---
import matplotlib.pyplot as plt                # Ferramenta principal para desenhar gráficos e mapas
from matplotlib.lines import Line2D            # Ferramenta para criar linhas personalizadas (usada na legenda)
from matplotlib.patches import Patch, Rectangle # 'Patch': áreas coloridas na legenda | 'Rectangle': retângulos
import geopandas as gpd                        # Ferramenta para trabalhar com dados geográficos (polígonos, malhas)
import requests                                # Ferramenta para fazer requisições à internet (baixar dados de APIs)
import io                                      # Ferramenta para tratar dados em memória como se fossem um arquivo
from shapely.geometry import Point             # Ferramenta para criar geometrias (Ponto, Linha, Polígono)
from pyproj import Transformer                 # Ferramenta para converter coordenadas entre diferentes projeções


# --- SEÇÃO 2: CONFIGURAÇÃO DO ESTILO VISUAL ---
# O 'try/except' tenta usar um estilo e, se falhar, usa uma alternativa.
try:
    plt.style.use('seaborn-v0_8-whitegrid')  # Estilo seaborn: fundo branco com grade cinza
except Exception:
    plt.style.use('ggplot')                  # Alternativa se o seaborn não estiver disponível


# --- SEÇÃO 3: DADOS GEOGRÁFICOS E PROJEÇÃO ---
# Define o ponto central de Brasília e converte para o sistema oficial: SIRGAS 2000 (EPSG:4674).

# Cria um conversor de coordenadas: de GPS (EPSG:4326) → SIRGAS 2000 Brasil (EPSG:4674)
transformer = Transformer.from_crs("EPSG:4326", "EPSG:4674", always_xy=True)

lon, lat = -47.8825, -15.7942               # Longitude e latitude de Brasília (referência: GPS/Google Maps)
x, y = transformer.transform(lon, lat)       # Converte as coordenadas para o sistema SIRGAS 2000
ponto_brasilia = Point(x, y)                 # Cria o objeto geométrico "Ponto" com as coordenadas convertidas


# --- SEÇÃO 4: BUSCANDO DADOS GEOGRÁFICOS DO IBGE ---

# URL da API do IBGE: malha do Distrito Federal (ID 5300108), qualidade máxima
url_ibge = "https://servicodados.ibge.gov.br/api/v4/malhas/municipios/5300108?formato=application/vnd.geo+json&qualidade=maxima"
print("Buscando malha do Distrito Federal no IBGE...")
response = requests.get(url_ibge)                            # Faz o download dos dados geográficos
gdf_municipio = gpd.read_file(io.BytesIO(response.content)) # Lê os dados e cria um GeoDataFrame
gdf_municipio = gdf_municipio.to_crs("EPSG:4674")           # Converte para SIRGAS 2000

# URL da API do IBGE: contorno do Brasil com divisão por estados (UFs)
url_brasil = "https://servicodados.ibge.gov.br/api/v4/malhas/paises/BR?formato=application/vnd.geo+json&qualidade=intermediaria&intrarregiao=UF"
print("Buscando contorno do Brasil com UFs no IBGE...")
response_brasil = requests.get(url_brasil)                               # Faz o download do contorno do Brasil
gdf_brasil = gpd.read_file(io.BytesIO(response_brasil.content))         # Cria GeoDataFrame com os estados do Brasil
gdf_brasil = gdf_brasil.set_crs("EPSG:4326", allow_override=True)       # Define o CRS como geográfico
gdf_municipio_geo = gdf_municipio.to_crs("EPSG:4326")                   # Versão do DF em graus


# --- SEÇÃO 5: DEFINIÇÃO DO LAYOUT DO MAPA (MOSAICO) ---
# O 'mapa' ocupa toda a coluna esquerda (4 linhas).
# A coluna direita tem 4 painéis com alturas variadas.
layout = [
    ['mapa', 'localizacao'],   # Linha 1: localização à direita
    ['mapa', 'legenda'],       # Linha 2: legenda à direita
    ['mapa', 'info_tecnica'],  # Linha 3: informações técnicas à direita
    ['mapa', 'info_carto'],    # Linha 4: informações cartográficas à direita
]

# Cria a figura e os eixos
# height_ratios=[1.875, 0.5, 1.0, 1.0]: Localização 25% mais alta que antes (1.5 -> 1.875)
fig, axs = plt.subplot_mosaic(
    layout,
    figsize=(14, 15),           # Ajustamos a altura para compensar o novo painel mais alto
    width_ratios=[3, 1],
    height_ratios=[1.875, 0.5, 1.0, 1.0]
)

ax_mapa        = axs['mapa']
ax_localizacao = axs['localizacao']
ax_legenda     = axs['legenda']
ax_info_tec    = axs['info_tecnica']
ax_info_carto  = axs['info_carto']


# =========================================================================
# --- SEÇÃO 6: PAINEL PRINCIPAL — MAPA ---
# =========================================================================

# Desenha a malha municipal do DF
gdf_municipio.plot(ax=ax_mapa, color='lightgrey', edgecolor='black', alpha=0.5, label='Distrito Federal')

# Desenha o ponto de Brasília
ax_mapa.plot(
    ponto_brasilia.x, ponto_brasilia.y, 
    marker='o', color='red', markersize=12, linestyle='None', 
    label='Brasília (SIRGAS 2000)'
)

# Anotação de coordenadas
ax_mapa.annotate(
    f'Lon: {ponto_brasilia.x:.4f}\nLat: {ponto_brasilia.y:.4f}',
    (ponto_brasilia.x, ponto_brasilia.y),
    xytext=(10, 10), textcoords='offset points', 
    fontsize=9, fontweight='bold'
)

# Ajuste de zoom
minx, miny, maxx, maxy = gdf_municipio.total_bounds
ax_mapa.set_xlim(minx - 0.05, maxx + 0.05)
ax_mapa.set_ylim(miny - 0.05, maxy + 0.05)

# Título principal do mapa agora colocado internamente para alinhar com os painéis laterais
ax_mapa.text(0.5, 0.98, 'Limite do Distrito Federal — SIRGAS 2000', 
            transform=ax_mapa.transAxes, fontsize=16, fontweight='bold', ha='center', va='top')
# ax_mapa.set_title('Limite do Distrito Federal — SIRGAS 2000', fontsize=16, fontweight='bold')  # Antigo título externo
ax_mapa.set_xlabel('Longitude (Graus)')
ax_mapa.set_ylabel('Latitude (Graus)')
ax_mapa.grid(True, linestyle='--', alpha=0.6)


# =========================================================================
# --- SEÇÃO 7: PAINEL — LOCALIZAÇÃO ---
# =========================================================================

def _estilizar_painel(ax, titulo, h_rect=0.12, y_text=0.94):
    """Função auxiliar: aplica bordas e cabeçalho cinza."""
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1)
    ax.set_xticks([])
    ax.set_yticks([])
    # Cabeçalho
    ax.add_patch(Rectangle(
        (0, 1 - h_rect), 1, h_rect, transform=ax.transAxes, 
        facecolor='lightgrey', edgecolor='lightgrey', clip_on=False
    ))
    # Título
    ax.text(0.5, y_text, titulo, transform=ax.transAxes, 
            fontsize=9, fontweight='bold', ha='center', va='center')

# Estilização com ajuste de altura para o cabeçalho (devido ao height_ratio diferenciado)
_estilizar_painel(ax_localizacao, "Localização", h_rect=0.1, y_text=0.95)

# Desenha contorno do Brasil e destaca DF
gdf_brasil.plot(ax=ax_localizacao, color='lightgrey', edgecolor='darkgrey', linewidth=0.5)
gdf_municipio_geo.plot(ax=ax_localizacao, color='red', edgecolor='red')

# Ajusta os limites do eixo para dar "respiro" ao mapa do Brasil (evita tocar no header/bordas)
ax_localizacao.set_xlim(-85, -25)   # De -75/-34 para -85/-25 (maior margem horizontal)
ax_localizacao.set_ylim(-42, 15)    # De -35/6 para -42/15 (maior margem vertical)


# =========================================================================
# --- SEÇÃO 8: PAINEL — LEGENDA ---
# =========================================================================

# Cabeçalho adaptado para a altura reduzida do painel
_estilizar_painel(ax_legenda, "Legenda", h_rect=0.25, y_text=0.88)

legend_elements = [
    Patch(facecolor='lightgrey', edgecolor='black', alpha=0.5, label='DF'),
    Line2D([0], [0], marker='o', color='w', label='Brasília',
           markerfacecolor='red', markersize=8, linestyle='None')
]

# Legenda centralizada e compacta
ax_legenda.legend(
    handles=legend_elements, loc='center', 
    fontsize=8, frameon=False, ncol=1
)


# =========================================================================
# --- SEÇÃO 9: PAINEL — INFORMAÇÕES TÉCNICAS (BRANDING) ---
# =========================================================================

_estilizar_painel(ax_info_tec, "Informação Técnica", h_rect=0.12, y_text=0.94)

# Título e Subtítulo
ax_info_tec.text(0.5, 0.75, "Mapa do Distrito Federal", transform=ax_info_tec.transAxes,
                 fontsize=10, fontweight='bold', ha='center', va='center')
ax_info_tec.text(0.5, 0.65, "GeoDataScience - BR", transform=ax_info_tec.transAxes,
                 fontsize=9, ha='center', va='center')

# Inserindo a Logo
try:
    logo = plt.imread("assets/img/world-map.png")
    # Criamos um novo eixo miniatura dentro do painel para a logo
    ax_logo = ax_info_tec.inset_axes([0.25, 0.1, 0.5, 0.45])
    ax_logo.imshow(logo)
    ax_logo.axis('off')
except Exception:
    ax_info_tec.text(0.5, 0.3, "[Logo World Map]", transform=ax_info_tec.transAxes,
                     ha='center', va='center', color='grey')


# =========================================================================
# --- SEÇÃO 10: PAINEL — INFORMAÇÕES CARTOGRÁFICAS ---
# =========================================================================

_estilizar_painel(ax_info_carto, "Informações Cartográficas", h_rect=0.12, y_text=0.94)

# Texto Técnico transferido para cá
texto_tecnico = (
    "Sistema: SIRGAS 2000 | EPSG: 4674\n"
    "Projeção: Geográfica\n"
    "Escala: 1:250.000\n"
    "Fonte: IBGE, 2024"
)
ax_info_carto.text(0.5, 0.82, texto_tecnico, transform=ax_info_carto.transAxes,
                   fontsize=8, ha='center', va='top')

# Seta do Norte (ajustada para baixo)
ax_info_carto.annotate(
    'N', xy=(0.5, 0.50), xytext=(0.5, 0.38),
    arrowprops=dict(facecolor='black', width=2, headwidth=8),
    ha='center', va='center', fontsize=16, fontweight='bold',
    xycoords=ax_info_carto.transAxes
)

# Escala Gráfica
ax_info_carto.plot([0.2, 0.8], [0.22, 0.22], transform=ax_info_carto.transAxes, color='black', lw=2)
ax_info_carto.plot([0.2, 0.2], [0.18, 0.26], transform=ax_info_carto.transAxes, color='black', lw=1)
ax_info_carto.plot([0.8, 0.8], [0.18, 0.26], transform=ax_info_carto.transAxes, color='black', lw=1)
ax_info_carto.text(0.2, 0.12, "0", transform=ax_info_carto.transAxes, ha='center', fontsize=7)
ax_info_carto.text(0.8, 0.12, "~50 km", transform=ax_info_carto.transAxes, ha='center', fontsize=7, fontweight='bold')


# =========================================================================
# --- SEÇÃO 11: FINALIZAÇÃO E EXPORTAÇÃO ---
# =========================================================================

# Ajusta o layout para ser mais apertado e ocupar melhor o espaço superior
plt.tight_layout(pad=1.0, rect=[0.01, 0.01, 0.99, 0.99])

# Adiciona moldura negra bem rente às bordas da figura
fig.patches.extend([
    Rectangle(
        (0.005, 0.005), 0.99, 0.99,  # Margem de 0.5% apenas
        fill=False, color='black', lw=2, transform=fig.transFigure, figure=fig
    )
])

plt.savefig('mapa_ibge_sirgas.png', dpi=150)          # Salva o mapa como PNG com 150 DPI de resolução
print("Mapa 'mapa_ibge_sirgas.png' gerado com sucesso!")  # Confirmação de sucesso no terminal
