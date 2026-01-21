import matplotlib.pyplot as plt
from shapely.geometry import LineString, Polygon
import os

# Configuração de estilo e diretório
try:
    plt.style.use('seaborn-v0_8-whitegrid')
except:
    plt.style.use('ggplot')

# caminho das imagens
output_dir = os.path.join('assets', 'img')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- 1. Gerar Imagem de Linha (LineString) ---
fig, ax = plt.subplots(figsize=(6, 4)) # configuração dotamanho da imagem

# Eixo Monumental Simplificado (aprox)
line_coords = [(-47.9500, -15.7900), (-47.8200, -15.8000)] # coordenadas da linha
line = LineString(line_coords) # criando a linha

x, y = line.xy # extraindo as coordenadas
ax.plot(x, y, color='blue', linewidth=3, label='LineString') # plotando a linha
ax.scatter(x, y, color='black') # plotando os vertices

ax.set_title('Exemplo de Linha (LineString)') # título da imagem
ax.set_xlabel('Longitude') # eixo x
ax.set_ylabel('Latitude') # eixo y
plt.tight_layout() # ajustando o layout
plt.savefig(os.path.join(output_dir, 'line_example.png'), dpi=100) # salvando a imagem
plt.close() # fechando a imagem
print("Imagem 'line_example.png' gerada.")

# --- 2. Gerar Imagem de Polígono (Polygon) ---
fig, ax = plt.subplots(figsize=(6, 4)) # configuração dotamanho da imagem

# Triângulo Simplificado (Lago Paranoá fake)
# As coordenadas devem ser inseridas em ordem sequencial (horária ou anti-horária)
# O último ponto deve ser igual ao primeiro para fechar o polígono
poly_coords = [            # coordenadas do polígono
    (-47.8500, -15.8200),
    (-47.8000, -15.8200),
    (-47.8250, -15.8500),
    (-47.8500, -15.8200) # Fechar
]
poly = Polygon(poly_coords) # criando o polígono

x, y = poly.exterior.xy # extraindo as coordenadas
ax.fill(x, y, color='lightgreen', alpha=0.5, label='Polygon') # preenchendo o polígono
ax.plot(x, y, color='green', linewidth=2) # plotando o polígono

ax.set_title('Exemplo de Polígono (Polygon)') # título da imagem
ax.set_xlabel('Longitude') # eixo x
ax.set_ylabel('Latitude') # eixo y
plt.tight_layout() # ajustando o layout
plt.savefig(os.path.join(output_dir, 'polygon_example.png'), dpi=100) # salvando a imagem
plt.close() # fechando a imagem
print("Imagem 'polygon_example.png' gerada.")
