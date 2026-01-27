import streamlit as st
from shapely.geometry import Point
import os

st.set_page_config(page_title="3D Objects", page_icon="🧊")
st.markdown("# 13. 3D Objects in Shapely")

st.markdown("""
**Explicação:**

O Shapely suporta coordenadas Z (x, y, z). 
No entanto, a maioria das operações geométricas (interseção, buffer, etc.) são calculadas apenas no plano 2D (x, y), ignorando o Z, embora o valor Z seja preservado nos resultados.
""")

st.markdown("**Código:**")

st.code("""
# Exemplo Simples de Ponto 3D
from shapely.geometry import Point
# Cria um Ponto 3D (x, y, z)
p3d = Point(1, 2, 3)
# O atributo ".has_z" é um booleano que retorna True se a geometria possuir a coordenada "z".
# Em pipelines de dados essa verificação é útil para validar se o esquema de dados de entrada contém informações de altitude antes de processá-los.
print(p3d.has_z)
print(p3d.z)

# Exemplo de Representação 3D de um Ponto
from shapely.plotting import save_fig
import matplotlib.pyplot as plt
# Criar um objeto de figura (fig) no qual será projetado o gráfico.
# O parâmetro figsize=(6, 6) define o tamanho da imagem em 6x6 polegadas
fig = plt.figure(figsize=(6, 6))
# Adiciona um conjunto de eixos à figura. O argumento projection='3d' é o que habilita o suporte ao espaço tridimensional (eixos X, Y e Z)
ax = fig.add_subplot(111, projection='3d')
# Adiciona um ponto nas coordenadas (0, 0, 0) no gráfico de dispersão (scatter plot)
# (c='r') Define a cor como vermelho (red)
# (marker='o') Define o formato do marcador como um círculo
ax.scatter([0], [0], [0], c='r', marker='o')
# Adiciona uma etiqueta de texto ao gráfico para facilitar a interpretação.
# Texto colocado em (z=0.1). Esse pequeno "offset" (deslocamento) é uma boa prática para que o texto não fique exatamente em cima do ponto
ax.text(0, 0, 0.1, "Point(0,0,0)")
# Define o título do gráfico
ax.set_title('3D Point Support')
# Salva a figura em um arquivo PNG
save_fig('3d_point.png')
""", language="python")

st.markdown("**Resultado:**")

st.image(os.path.join("assets", "img", "3d_point.png"))
