import streamlit as st
from shapely.geometry import LineString
import os

st.set_page_config(page_title="Simplifying Geometries", page_icon="✂️")
st.markdown("# 12. Simplifying Geometries")

st.markdown("""
**Explicação:**

Reduz o número de vértices de uma geometria mantendo sua forma geral. Útil para reduzir tamanho de arquivos e acelerar renderização. Geralmente usa o algoritmo Douglas-Peucker.
""")

st.markdown("**Código:**")

st.code("""
from shapely.geometry import LineString

# Exemplo simples de uma linha
# Cria uma linha com 5 vértices
line = LineString([(0,0), (1,0.1), (2,-0.1), (3,0), (4,0)]) 
# Simplifica a linha
# tolerance: distância máxima permitida entre a linha original e a simplificada
# preserve_topology: se True, a simplificação não pode criar autointerseções
simplified = line.simplify(tolerance=0.2, preserve_topology=False) 
# Imprime a linha original e a simplificada
print(line)
print(simplified)

# Exemplo mais complexo de Simplificação
# Inicializa uma figura e um eixo usando Matplotlib. 
# O formato retangular (8, 4) é ideal para visualizar séries temporais ou linhas extensas
fig, ax = plt.subplots(figsize=(8, 4))
# Simulação de dados reais capturados por GPS, que raramente são linhas perfeitas.
# Cria uma lista de 50 coordenadas baseadas em uma curva senoide, mas adiciona um "ruído" aleatório (0.1*np.random.normal())
# A LineString converte essa lista em um objeto geométrico do Shapely.
coords = [(x, np.sin(x) + 0.1*np.random.normal()) for x in np.linspace(0, 10, 50)]
line = LineString(coords)
# Aplica o algoritmo de Douglas-Peucker para reduzir o número de vértices da linha
# Tolerância (0.5): Quanto maior o valor, mais agressiva é a remoção de pontos
# (preserve_topology=False) Permite uma simplificação mais rápida, sem checar se a linha se autointersecciona após a redução.
simplified = line.simplify(0.5, preserve_topology=False)
# Extrai as coordenadas da linha original. 
# (alpha=0.3) (transparência) e (b-) (cor azul) deixam o "ruído" em segundo plano, facilitando a comparação visual.
x, y = line.xy
ax.plot(x, y, 'b-', alpha=0.3, label='Original')
# Plota a linha resultante em vermelho (r-) com uma espessura maior (linewidth=2). 
# Essa configuração destaca como o algoritmo conseguiu manter a forma geral da curva senoide removendo os pequenos desvios aleatórios. 
x, y = simplified.xy
ax.plot(x, y, 'r-', linewidth=2, label='Simplified (tol=0.5)')
# Define o título do gráfico e exibe a legenda.
ax.set_title('Simplifying Geometries')
ax.legend()
# Salva a figura
save_fig('simplify.png')

""", language="python")

st.markdown("**Resultado:**")

st.image(os.path.join("assets", "img", "simplify.png"))
