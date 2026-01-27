import streamlit as st
from shapely.geometry import MultiPoint
import os

st.set_page_config(page_title="Polígono Envolvente", page_icon="📦")
st.markdown("# 8. Polígono Envolvente (Enclosing Polygons)")

st.markdown("""
**Explicação:**

Uma operação comum é encontrar o menor polígono convexo que envolve um conjunto de pontos (Convex Hull). Imagine um elástico esticado ao redor dos pinos (pontos).
""")

st.markdown("**Código:**")

st.code("""
# Exemplo de criação de um polígono envolvente
from shapely.geometry import MultiPoint
points = MultiPoint([(0,0), (1,3), (2,2), (4,1), (3,0), (-1,1)])
hull = points.convex_hull
# Retorna um Polígono
print(hull) 

# Exemplo de Representação Gráfica
# Criando o gráfico
fig, ax = plt.subplots(figsize=(6, 6)) 
# Criando os pontos
points = MultiPoint([(0,0), (1,3), (2,2), (4,1), (3,0), (-1,1)]) 
# Criando o polígono envolvente
hull = points.convex_hull 
# Plotando os pontos
for p in points.geoms:
    ax.plot(p.x, p.y, 'ko')
# Coordenadas do polígono envolvente
x, y = hull.exterior.xy 
# Plotando o polígono envolvente
ax.plot(x, y, 'b--', label='Convex Hull') 
# Título do gráfico
ax.set_title('Convex Hull') 
# Legenda do gráfico
ax.legend()
save_fig('convex_hull.png') # Salvar a figura

""", language="python")

st.markdown("**Resultado:**")

st.image(os.path.join("assets", "img", "convex_hull.png"))
