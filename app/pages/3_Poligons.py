import streamlit as st
from shapely.geometry import Polygon, MultiPolygon
import os

st.set_page_config(page_title="Polígonos e Multipolígonos", page_icon="📐")

st.markdown("# 3. Criando Polígonos e Multipolígonos (Creating Polygons and Multipolygons)")

st.markdown("""
**Explicação:**

- **Polígono (`Polygon`)**: Uma área fechada definida por uma borda externa (shell) e opcionalmente bordas internas (holes). O primeiro e o último ponto da sequência devem ser iguais para fechar o anel (ou o Shapely fecha automaticamente).
- **Multipolígono (`MultiPolygon`)**: Uma coleção de um ou mais polígonos tratados como um único objeto geométrico (ex: um arquipélago, ou um país com ilhas).
""")

st.markdown("**Código:**")

code = """
from shapely.geometry import Polygon, MultiPolygon

# Criando um Polígono (Triângulo)
poly = Polygon([
    (-47.8500, -15.8200),
    (-47.8000, -15.8200),
    (-47.8250, -15.8500)
])

# Criando um Multipolígono (Dois quadrados desconexos para exemplo)
mpoly = MultiPolygon([
    Polygon([(0,0), (1,0), (1,1), (0,1)]),
    Polygon([(2,2), (3,2), (3,3), (2,3)])
])

print(f"Polígono: {poly}")
print(f"Multipolígono: {mpoly}")
"""
st.code(code, language="python")

st.markdown("**Resultado:**")

image_path = os.path.join("assets", "img", "polygon_example.png")
if os.path.exists(image_path):
    st.image(image_path, caption="Exemplo de Polígono (Polygon)")
else:
    st.error(f"Imagem não encontrada em: {image_path}")
