import streamlit as st
from shapely.geometry import Point, Polygon
import os

st.set_page_config(page_title="Within Test", page_icon="🎯")
st.markdown("# 10. Within-test")

st.markdown("""
**Explicação:**

Verifica se uma geometria está totalmente dentro de outra. Retorna `True` ou `False`. É fundamental para análises do tipo "Ponto em Polígono".
""")

st.markdown("**Código:**")

st.code("""
#Exemplo simples de within-test 
from shapely.geometry import Point, Polygon
# Criando o polígono
poly = Polygon([(0,0), (4,0), (4,4), (0,4)])
# Ponto dentro do polígono
p_in = Point(2, 2)
# Ponto fora do polígono
p_out = Point(5, 5) 
print(p_in.within(poly))  # True
print(poly.contains(p_in)) # True
print(p_out.within(poly)) # False

# Exemplo de representação gráfica
import matplotlib.pyplot as plt
# Tamanho da figura (6,6)
fig, ax = plt.subplots(figsize=(6, 6))
# Polígono (4 vértices)
poly = Polygon([(0,0), (4,0), (4,4), (0,4)]) 
# Ponto dentro do polígono
p_in = Point(2, 2) 
# Ponto fora do polígono
p_out = Point(5, 5) 
# Coordenadas do polígono
x, y = poly.exterior.xy 
# Projeta o polígono
ax.plot(x, y, 'k-') 
# Ponto dentro do polígono
# 'go' = green circle
# label = legenda (Within (True))
ax.plot(p_in.x, p_in.y, 'go', label='Within (True)') 
# Ponto fora do polígono
# 'ro' = red circle
# label = legenda (Within (False))
ax.plot(p_out.x, p_out.y, 'ro', label='Within (False)') 
# Título da figura
ax.set_title('Within Test') 
# Legenda
ax.legend() 
# Salva a figura
save_fig('within.png')
""", language="python")

st.markdown("**Resultado:**")

st.image(os.path.join("assets", "img", "within.png"))
