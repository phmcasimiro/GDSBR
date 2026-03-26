# =============================================================================
# MAPA BASE - Maracanã e Rio de Janeiro
# Projeto: GDS_BR | Geo Data Science Brasil
# Descrição: Script para gerar um mapa cartográfico do Maracanã e Rio de Janeiro
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

# ============================================
# --- SEÇÃO 1: IMPORTAÇÃO DAS BIBLIOTECAS ---
# ============================================

import matplotlib.pyplot as plt                # Importa a ferramenta principal para criar desenhos, gráficos e mapas
from matplotlib.gridspec import GridSpec       # Importa a ferramenta de controle absoluto de grade (Layout avançado)
from matplotlib.lines import Line2D            # Importa uma classe para criar linhas personalizadas nas legendas
from matplotlib.patches import Patch, Rectangle # Importa ferramentas para desenhar áreas coloridas (Patch) e retângulos (Rectangle)
import geopandas as gpd                        # Importa a biblioteca especializada em Mapas e Dados Geográficos (GeoDataFrames)
import requests                                # Importa a biblioteca para fazer "pedidos" de dados para sites e APIs na internet
import io                                      # Importa uma ferramenta para tratar dados baixados da internet como se fossem arquivos no PC
from shapely.geometry import Point             # Importa a ferramenta para criar representações matemáticas de "Pontos" geográficos
from pyproj import Transformer                 # Importa a ferramenta que converte coordenadas (ex: de graus para metros ou vice-versa)

# ===============================================
# --- SEÇÃO 2: CONFIGURAÇÃO DO ESTILO VISUAL ---
# ===============================================

# O bloco 'try/except' é uma rede de segurança: se o primeiro comando falhar, o código não para e tenta o segundo.
try:
    plt.style.use('seaborn-v0_8-whitegrid')  # Tenta aplicar um visual limpo com fundo branco e linhas de grade cinza
except Exception:
    plt.style.use('ggplot')                  # Se o estilo acima não existir no seu PC, usa este estilo padrão alternativo

# ======================================================================================================
# --- SEÇÃO 3: DADOS GEOGRÁFICOS E PROJEÇÃO ---
# Aqui definimos onde o Estádio do Maracanã está no mundo e preparamos a conversão para o formato oficial do Brasil.
# ======================================================================================================

# Cria uma regra de conversão: transforma de "WGS84" (EPSG:4326) para "SIRGAS 2000" (EPSG:4674 - padrão oficial brasileiro)
transformer = Transformer.from_crs("EPSG:4326", "EPSG:4674", always_xy=True)

lon, lat = -43.22995, -22.91181              # Define um ponto com a Longitude e Latitude reais do Estádio do Maracanã
x, y = transformer.transform(lon, lat)       # Usa a regra de conversão para transformar os números acima para o formato SIRGAS 2000
ponto_maracana = Point(x, y)                 # Cria um objeto que o computador entende como um "Ponto Geográfico" no mapa

# ======================================================================================================
# --- SEÇÃO 4: BUSCANDO DADOS GEOGRÁFICOS DO IBGE ---
# Nesta parte, o código vai "telefonar" para o servidor do IBGE e baixar os desenhos dos mapas.
# ======================================================================================================

# Endereço (URL) onde o IBGE guarda o desenho (malha) do Município do Rio de Janeiro
url_ibge = "https://servicodados.ibge.gov.br/api/v4/malhas/municipios/3304557?formato=application/vnd.geo+json&qualidade=maxima"
print("Buscando malha do Município do Rio de Janeiro no IBGE...")       # Mostra uma mensagem no terminal para sabermos o que está acontecendo
response = requests.get(url_ibge)                            # Vai até o site e baixa os dados (como baixar um arquivo)
gdf_municipio = gpd.read_file(io.BytesIO(response.content)) # Abre esses dados baixados e os organiza em uma tabela inteligente (DataFrame)
gdf_municipio = gdf_municipio.to_crs("EPSG:4674")           # Garante que o desenho do mapa esteja no sistema SIRGAS 2000

# Endereço para baixar o contorno de todos os estados do Brasil (UFs) usado no Mapa de Localização
url_brasil = "https://servicodados.ibge.gov.br/api/v4/malhas/paises/BR?formato=application/vnd.geo+json&qualidade=intermediaria&intrarregiao=UF"
print("Buscando contorno do Brasil com UFs no IBGE...")      # Mensagem de progresso
response_brasil = requests.get(url_brasil)                               # Baixa os dados do contorno do Brasil
gdf_brasil = gpd.read_file(io.BytesIO(response_brasil.content))         # Transforma os dados do Brasil em uma tabela geográfica
gdf_brasil = gdf_brasil.set_crs("EPSG:4326", allow_override=True)       # Define que os dados originais estão em formato de graus (GPS)
gdf_municipio_geo = gdf_municipio.to_crs("EPSG:4326")                   # Cria uma cópia do mapa do DF em formato de graus para o mapa de localização

# --- SEÇÃO 5: DEFINIÇÃO DO LAYOUT DO MAPA (GRIDSPEC) ---
# Aqui usamos a grade absoluta para ter controle total de cada pixel e espaço.

# Cria uma figura (o papel em branco) no tamanho A4 Paisagem (11.69 x 8.27 polegadas)
fig = plt.figure(figsize=(11.69, 8.27))

# Define uma grade de 4 linhas e 4 colunas
# hspace: espaço vertical entre linhas | wspace: espaço horizontal entre colunas
# Aumentamos as margens (left, bottom) para os números das coordenadas não sumirem
gs = GridSpec(4, 4, figure=fig, 
              hspace=0.02, wspace=0.1, 
              left=0.07, right=0.98, top=0.95, bottom=0.07,
              height_ratios=[1.2, 0.8, 1.0, 1.0], # Altura de cada linha
              width_ratios=[1, 1, 1, 1])          # Largura de cada coluna

# Atribui cada painel a uma área da grade:
# ax_mapa: ocupa da linha 0 até a 4 (todas) e das colunas 0 até a 3 (quase tudo)
ax_mapa = fig.add_subplot(gs[0:4, 0:3])

# Painéis da Direita (todos na última coluna, index 3):
ax_localizacao = fig.add_subplot(gs[0, 3]) # Linha 0, Coluna 3
ax_legenda     = fig.add_subplot(gs[1, 3]) # Linha 1, Coluna 3
ax_info_tec    = fig.add_subplot(gs[2, 3]) # Linha 2, Coluna 3
ax_info_carto  = fig.add_subplot(gs[3, 3]) # Linha 3, Coluna 3

# =========================================================================
# --- SEÇÃO 6: PAINEL PRINCIPAL — MAPA ---
# =========================================================================

# Desenha o formato do Município do Rio de Janeiro no quadradinho principal (ax_mapa)
gdf_municipio.plot(ax=ax_mapa, color='lightgrey', edgecolor='black', alpha=0.5, label='Município do Rio de Janeiro')

# Desenha o pontinho vermelho representando o Maracanã
ax_mapa.plot(
    ponto_maracana.x, ponto_maracana.y,            # Posição X e Y do ponto
    marker='o', color='red', markersize=12,        # Formato de bola, cor vermelha e tamanho 12
    linestyle='None', label='Maracanã (SIRGAS 2000)' # Sem linha conectando, apenas o ponto
)

# Escreve o texto com os números das coordenadas logo acima do ponto do Maracanã
ax_mapa.annotate(
    f'Lon: {ponto_maracana.x:.4f}\nLat: {ponto_maracana.y:.4f}', # O texto (Longitude e Latitude com 4 casas decimais)
    (ponto_maracana.x, ponto_maracana.y),                        # Onde o texto deve apontar
    xytext=(10, 10), textcoords='offset points',               # Desloca o texto 10 pontos para o lado e para cima
    fontsize=9, fontweight='bold'                                # Tamanho da letra 9 e em negrito
)

# Define os limites de visão do mapa (o "zoom") baseado no tamanho do DF, deixando um espacinho em volta
minx, miny, maxx, maxy = gdf_municipio.total_bounds # Pega as coordenadas mais extremas (norte, sul, leste, oeste)
ax_mapa.set_xlim(minx - 0.05, maxx + 0.05)           # Define o limite horizontal da câmera
ax_mapa.set_ylim(miny - 0.05, maxy + 0.05)           # Define o limite vertical da câmera

ax_mapa.set_xlabel('Longitude (Graus)')      # Nomeia a linha de baixo do gráfico
ax_mapa.set_ylabel('Latitude (Graus)')       # Nomeia a linha lateral do gráfico
ax_mapa.grid(True, linestyle='--', alpha=0.6) # Coloca linhas de grade pontilhadas e meio transparentes

# --- AJUSTE DE ALINHAMENTO E ESTILO (BOUNDBOX) ---
# Usamos datalim para o quadro preencher a grade e mantemos o mapa interno proporcional
ax_mapa.set_adjustable('datalim') 

# =========================================================================
# --- SEÇÃO 7: PAINEL — LOCALIZAÇÃO ---
# =========================================================================

# h_rect = altura do retângulo, y_text = posição do texto
def _estilizar_painel(ax, titulo, h_rect=0.12, y_text=0.94, esconder_eixos=True, font_size=9):
    """Função para aplicar o visual didático: bordas e cabeçalho cinza."""
    for spine in ax.spines.values(): # Percorre as 4 bordas do painel
        spine.set_visible(True)      # Garante que a borda apareça
        spine.set_linewidth(1)       # Define a grossura da linha da borda como 1
        spine.set_edgecolor('grey')  # Define a cor da borda como cinza (didático)
    
    if esconder_eixos:
        ax.set_xticks([])            # Limpa os números da parte de baixo do painel
        ax.set_yticks([])            # Limpa os números da parte lateral do painel
    
    # Desenha o retângulo cinza no topo do painel lateral para ser o "título"
    ax.add_patch(Rectangle(
        (0, 1 - h_rect), 1, h_rect, transform=ax.transAxes, 
        facecolor='lightgrey', edgecolor='lightgrey', clip_on=False
    ))
    
    # Escreve o nome do painel centralizado em cima do retângulo cinza
    ax.text(0.5, y_text, titulo, transform=ax.transAxes, 
            fontsize=font_size, fontweight='bold', ha='center', va='center')

# Estilização do MAPA PRINCIPAL (agora com cabeçalho cinza e eixos visíveis)
_estilizar_painel(ax_mapa, 'Município do Rio de Janeiro e Estádio do Maracanã — SIRGAS 2000', h_rect=0.045, y_text=0.978, esconder_eixos=False, font_size=12)

# Aplica a função de estilo no painel de "Localização"
_estilizar_painel(ax_localizacao, "Localização", h_rect=0.1, y_text=0.95)

# Força o painel a preencher todo o espaço da grade
ax_localizacao.set_adjustable('datalim')

# Desenha o mapa do Brasil completo em cinza no painel de localização
gdf_brasil.plot(ax=ax_localizacao, color='lightgrey', edgecolor='darkgrey', linewidth=0.5)
# Desenha apenas o Distrito Federal em vermelho para mostrar onde ele fica dentro do Brasil
gdf_municipio_geo.plot(ax=ax_localizacao, color='red', edgecolor='red')

# Ajusta a "câmera" para mostrar o Brasil centralizado no painel de localização
ax_localizacao.set_xlim(-85, -25)   # Define o limite leste-oeste (longitude)
ax_localizacao.set_ylim(-42, 15)    # Define o limite norte-sul (latitude)

# =========================================================================
# --- SEÇÃO 8: PAINEL — LEGENDA ---
# =========================================================================

# Aplica a função de estilo no painel de "Legenda"
_estilizar_painel(ax_legenda, "Legenda", h_rect=0.12, y_text=0.94)

# Define quais elementos vão aparecer na caixa de legenda (o que cada cor/símbolo significa)
legend_elements = [
    Patch(facecolor='lightgrey', edgecolor='black', alpha=0.5, label='DF'), # Representa a área do DF
    Line2D([0], [0], marker='o', color='w', label='Maracanã',               # Representa o ponto do Maracanã
           markerfacecolor='red', markersize=8, linestyle='None')           # Define a cor vermelha e tamanho do ponto na legenda
]



ax_legenda.legend(
    handles=legend_elements,
    # Para definir a posição da legenda, use as opções: 'best', 'upper right', 'upper left', 'lower left', 
    # 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'
    loc='upper left',
    # (0, 0.82) -> 0 na horizontal (esquerda) e 0.82 na vertical (abaixo da caixa cinza)
    bbox_to_anchor=(0.0, 0.82), 
    fontsize=8, 
    frameon=False, 
    ncol=1    
)

# =========================================================================
# --- SEÇÃO 9: PAINEL — INFORMAÇÕES TÉCNICAS (BRANDING) ---
# =========================================================================

# Aplica a função de estilo no painel de "Informação Técnica"
_estilizar_painel(ax_info_tec, "Informação Técnica", h_rect=0.12, y_text=0.94)

# Escreve o texto principal do projeto dentro desse painel
ax_info_tec.text(0.5, 0.75, "Mapa do Maracanã e Rio de Janeiro", transform=ax_info_tec.transAxes,
                 fontsize=10, fontweight='bold', ha='center', va='center')
# Escreve o nome da marca/projeto abaixo do título
ax_info_tec.text(0.5, 0.65, "GeoDataScience - BR", transform=ax_info_tec.transAxes,
                 fontsize=9, ha='center', va='center')

# Tenta carregar e mostrar uma imagem de logo
try:
    # Tenta ler o arquivo de imagem
    logo = plt.imread("assets/img/world-map.png")
    # Parâmetros: [Esquerda, Base, Largura, Altura]. Valores de 0 a 1 (ex: 0.4 = 40% da largura do painel)
    ax_logo = ax_info_tec.inset_axes([0.4, 0.3, 0.2, 0.2]) 
    # Mostra a imagem
    ax_logo.imshow(logo)                               
    # Esconde os números das bordas da imagem
    ax_logo.axis('off')                                
except Exception:
    # Se a imagem não for encontrada, escreve um texto de aviso no lugar
    ax_info_tec.text(0.5, 0.3, "[Logo World Map]", transform=ax_info_tec.transAxes,
                     ha='center', va='center', color='grey')

# =========================================================================
# --- SEÇÃO 10: PAINEL — INFORMAÇÕES CARTOGRÁFICAS ---
# =========================================================================

# Aplica a função de estilo no painel de informações cartográficas
_estilizar_painel(ax_info_carto, "Informações Cartográficas", h_rect=0.12, y_text=0.94)

# Cria o bloco de texto com os dados técnicos do mapa
texto_tecnico = (
    "Sistema: SIRGAS 2000 | EPSG: 4674\n" # Qual o sistema de medidas usado
    "Projeção: Geográfica\n"               # Diz que o mapa é "plano" baseado em graus
    "Escala: 1:250.000\n"                   # Define a proporção de redução do mapa
    "Fonte: IBGE, 2024"                    # De onde vieram os dados
)
# Escreve esse texto no painel, centralizado
ax_info_carto.text(0.5, 0.82,
                   texto_tecnico,
                   transform=ax_info_carto.transAxes,
                   fontsize=8, ha='center', va='top')

# -----------------------
# --- ROSA DOS VENTOS ---
# -----------------------

'''# Desenha a "Seta do Norte" (um desenho que aponta para onde fica o Norte)
ax_info_carto.annotate(
    'N', xy=(0.5, 0.55), xytext=(0.5, 0.35),                     # xy = ponta da seta (0.55), xytext = base/texto (0.35)
    arrowprops=dict(facecolor='black', width=2, headwidth=8),    # Estilo da seta (preta e grossa)
    ha='center', va='center', fontsize=16, fontweight='bold',    # Estilo da letra 'N'
    xycoords=ax_info_carto.transAxes                             # Usa coordenadas do painel (0 a 1)
)'''

# Desenha a Rosa dos Ventos
ax_rosa = ax_info_carto.inset_axes([0.4, 0.35, 0.2, 0.2])
ax_rosa.imshow(plt.imread("assets/img/RosaVentos.png"))
ax_rosa.axis('off')

# ---------------------------------------------------------
# --- ESCALA GRÁFICA PROFISSIONAL (Modelo Cartográfico) ---
# ---------------------------------------------------------

# Desenha uma barra com segmentos alternados (preto/branco)
for i, x in enumerate([0.2, 0.4, 0.6]):
    cor = 'black' if i % 2 == 0 else 'white'
    ax_info_carto.add_patch(Rectangle((x, 0.2), 0.2, 0.03, 
                                      transform=ax_info_carto.transAxes, facecolor=cor, edgecolor='black', lw=1))

# Tiques e Textos da Escala (0 a 45 km para facilitar divisões de 15km)
ax_info_carto.text(0.2, 0.12, "0", transform=ax_info_carto.transAxes, ha='center', fontsize=7)
ax_info_carto.text(0.4, 0.12, "15", transform=ax_info_carto.transAxes, ha='center', fontsize=7)
ax_info_carto.text(0.6, 0.12, "30", transform=ax_info_carto.transAxes, ha='center', fontsize=7)
ax_info_carto.text(0.8, 0.12, "45 km", transform=ax_info_carto.transAxes, ha='center', fontsize=7, fontweight='bold')

# --- OUTROS MODELOS DE ESCALA (Exemplos Adicionais) ---
# OPÇÃO B (Linha Simples):
# ax_info_carto.plot([0.2, 0.8], [0.22, 0.22], transform=ax_info_carto.transAxes, color='black', lw=2)
# for x in [0.2, 0.4, 0.6, 0.8]: ax_info_carto.plot([x, x], [0.18, 0.26], transform=ax_info_carto.transAxes, color='black', lw=1)

# OPÇÃO C (Barra com Subdivisão Inicial):
# ax_info_carto.add_patch(Rectangle((0.2, 0.2), 0.1, 0.03, transform=ax_info_carto.transAxes, facecolor='black'))
# ax_info_carto.add_patch(Rectangle((0.3, 0.2), 0.5, 0.03, transform=ax_info_carto.transAxes, facecolor='white', edgecolor='black'))

# =========================================================================
# --- SEÇÃO 11: FINALIZAÇÃO E EXPORTAÇÃO ---
# =========================================================================

# Ajusta automaticamente os espaços entre todos os painéis para nada ficar sobreposto
#plt.tight_layout(pad=1.0, rect=[0.01, 0.01, 0.99, 0.99])

# Cria uma moldura (quadro) preta em volta de toda a imagem final para ficar elegante
fig.patches.extend([
    Rectangle(
        (0.005, 0.005), 0.99, 0.99,  # Posiciona o quadro quase na borda total (0.5% de margem)
        fill=False, color='black', lw=2, transform=fig.transFigure, figure=fig # Linha preta grossa (lw=2)
    )
])

plt.savefig('assets/maps/mapa_ibge_sirgas.png', dpi=300)      # Salva na pasta assets/maps como PNG
plt.savefig('assets/maps/mapa_ibge_sirgas.pdf')               # Salva na pasta assets/maps como PDF
print("Arquivos salvos em 'assets/maps/' com sucesso!")
