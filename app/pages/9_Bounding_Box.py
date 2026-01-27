import streamlit as st
from shapely.geometry import Polygon
import os

st.set_page_config(page_title="Bounding Box", page_icon="📦")
st.markdown("# 9. Criando uma Bounding Box")

st.markdown("""
**Explicação:**

O *Bounding Box* (Envelope) é o menor retângulo alinhado aos eixos x e y que contém a geometria inteira. É muito útil para filtros espaciais rápidos (indexação).
""")

st.markdown("**Código:**")

st.code("""
# Exemplo de criação de uma Bounding Box
from shapely.geometry import Polygon
# Criando o polígono
poly = Polygon([(1,1), (2,3), (3,2)]) 
# Coordenadas do polígono
minx, miny, maxx, maxy = poly.bounds 
# Retorna (minx, miny, maxx, maxy)
print(f"Bounds: {poly.bounds}")
# Criando geometria retângulo a partir dos bounds
bbox = Polygon([(minx, miny), (maxx, miny), (maxx, maxy), (minx, maxy)])

# Exemplo de Representação Gráfica
# Tamanho da figura
fig, ax = plt.subplots(figsize=(6, 6))
# Polígono
poly = Polygon([(1,1), (2,3), (3,2)]) 
# Coordenadas do polígono
minx, miny, maxx, maxy = poly.bounds 
# Bounding Box
bbox = Polygon([(minx, miny), (maxx, miny), (maxx, maxy), (minx, maxy)]) 
# Coordenadas do polígono
x, y = poly.exterior.xy 
# Preenchendo o polígono com transparência e cor amarela
ax.fill(x, y, color='yellow', alpha=0.5)
# Coordenadas do Bounding Box
x, y = bbox.exterior.xy
# Plotando o Bounding Box com cor vermelha e tracejado
ax.plot(x, y, 'r--', label='Bounding Box')
# Adicionando título e legenda
ax.set_title('Bounding Box')
ax.legend()
# Salvar a figura
save_fig('bbox.png')    
""", language="python")

st.markdown("**Resultado:**")

st.image(os.path.join("assets", "img", "bbox.png"))
