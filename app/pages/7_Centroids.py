import streamlit as st
from shapely.geometry import Polygon
import os

st.set_page_config(page_title="Centroids", page_icon="🎯")
st.markdown("# 7. Calculando Centróides")

st.markdown("""
**Explicação:**

O centróide é o centro geométrico de uma figura plana. É um ponto que representa a média aritmética de todos os pontos da forma.
""")

st.markdown("**Código:**")

st.code("""
# Exemplo de cálculo de centróide
from shapely.geometry import Polygon
# Criando o polígono
poly = Polygon([(0,0), (4,0), (4,4), (0,4)])
# Calculando o centróide
centroid = poly.centroid
# Retorna POINT (2 2)
print(f"Centróide: {centroid}")

# Exemplo de representação gráfica
# Criando o gráfico
fig, ax = plt.subplots(figsize=(6, 6))
# Criando o polígono
poly = Polygon([(0,0), (4,0), (4,4), (0,4)]) 
# Calculando o centróide
centroid = poly.centroid 
# Coordenadas do polígono
x, y = poly.exterior.xy 
# Preenchendo o polígono
ax.fill(x, y, alpha=0.3, color='cyan') 
# Plotando o centróide
# 'rx' define o marcador como um triângulo reto vermelho
# markersize define o tamanho do marcador
# label define o texto da legenda
ax.plot(centroid.x, centroid.y, 'rx', markersize=10, label='Centroid')
# Definindo o título e a legenda
ax.set_title('Polygon Centroid')
ax.legend()
# Salvando a figura
save_fig('centroid.png')
""", language="python")

st.markdown("**Resultado:**")

st.image(os.path.join("assets", "img", "centroid.png"))
