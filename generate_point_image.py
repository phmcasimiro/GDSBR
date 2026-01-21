import matplotlib.pyplot as plt
from shapely.geometry import Point

# Tentar usar um estilo disponível, fallback para default se não existir
try:
    plt.style.use('seaborn-v0_8-whitegrid')
except:
    plt.style.use('ggplot')

# Criar um Ponto (Ex: Brasília)
# Longitude (x), Latitude (y)
ponto = Point(-47.8825, -15.7942)

# Configurar a figura
fig, ax = plt.subplots(figsize=(8, 6))

# Plotar o ponto
# ax.plot(x, y, 'marker', ...)
ax.plot(ponto.x, ponto.y, marker='o', color='red', markersize=15, linestyle='None', label='Ponto P')

# Adicionar anotação
ax.annotate(f'P({ponto.x}, {ponto.y})', (ponto.x, ponto.y), 
            xytext=(10, 10), textcoords='offset points', fontsize=12)

# Ajustar limites para ver melhor o ponto no contexto (simulado)
ax.set_xlim(ponto.x - 0.1, ponto.x + 0.1)
ax.set_ylim(ponto.y - 0.1, ponto.y + 0.1)

# Labels e Título
ax.set_title('Representação de um Ponto (Shapely)', fontsize=16)
ax.set_xlabel('Longitude', fontsize=12)
ax.set_ylabel('Latitude', fontsize=12)
ax.grid(True)
ax.legend()

# Salvar a imagem
plt.tight_layout()
plt.savefig('point_example.png', dpi=100)
print("Imagem 'point_example.png' gerada com sucesso.")
