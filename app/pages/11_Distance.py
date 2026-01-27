import streamlit as st
from shapely.geometry import Point
import os

st.set_page_config(page_title="Distance Calculation", page_icon="📏")
st.markdown("# 11. Distance Calculation")

st.markdown("""
**Explicação:**

Calcula a menor distância Euclidiana (em linha reta) entre duas geometrias.
""")

st.markdown("**Código:**")

st.code("""
# Exemplo de cálculo de distância entre dois pontos
from shapely.geometry import Point
# Ponto 1
p1 = Point(0, 0)
# Ponto 2
p2 = Point(3, 4) 
# Calcula a distância entre os dois pontos
dist = p1.distance(p2) 
# 5.0 (Hipotenusa de 3-4-5)
print(f"Distância: {dist}")

# Exemplo de representação gráfica de distância entre dois pontos
# Cria um gráfico com tamanho 6x6
fig, ax = plt.subplots(figsize=(6, 6))
# Ponto 1
p1 = Point(0, 0) 
# Ponto 2
p2 = Point(3, 4)
# Calcula a distância entre os dois pontos
dist = p1.distance(p2)
# Plota a linha reta entre os dois pontos
# ('b--') define a cor azul e o estilo de linha tracejada
ax.plot([p1.x, p2.x], [p1.y, p2.y], 'b--')
# Plota o ponto 1
# ('go') define a cor verde e o estilo de marcador de pontos
ax.plot(p1.x, p1.y, 'go') 
# Plota o ponto 2
# ('go') define a cor verde e o estilo de marcador de pontos
ax.plot(p2.x, p2.y, 'go') 
# Adiciona o texto com a distância
# (1.5, 2) define a posição do texto
ax.text(1.5, 2, f"Dist: {dist}", fontsize=12) 
# Define o título do gráfico
ax.set_title('Euclidean Distance')
# Salva a figura
save_fig('distance.png')
""", language="python")

st.markdown("**Resultado:**")

st.image(os.path.join("assets", "img", "distance.png"))
