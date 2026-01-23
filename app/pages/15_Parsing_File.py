import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt

st.header("15. Parsing a Data File into a GeoDataFrame")

st.markdown("""
**Explicação:**

A Biblioteca GeoPandas facilita a leitura de arquivos geoespaciais (Shapefile, GeoJSON, KML, etc) diretamente para um GeoDataFrame usando `gpd.read_file()`.

Abaixo um exemplo de uso de arquivo .shp e GeoPandas para plotar um mapa mundial.
""")

st.markdown("**Código:**")

st.code(r"""
import geopandas as gpd
import matplotlib.pyplot as plt
import os

# Caminho do arquivo definido pelo usuário
file_path = r"data\NaturalEarth_Geom\ne_10m_admin_0_countries\ne_10m_admin_0_countries.shp"

# Verificar se o arquivo existe antes de tentar abrir
if os.path.exists(file_path):
    try:
        # Carregar o GeoDataFrame
        gdf = gpd.read_file(file_path)
        
        # Configurar a figura
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plotar o mapa
        gdf.plot(ax=ax, color='lightgrey', edgecolor='black')
        
        # Adicionar título e labels
        ax.set_title("Mapa Mundi - Natural Earth", fontsize=15)
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        
        # Salvar a imagem
        output_image = "teste_mapa.png"
        plt.tight_layout()
        plt.savefig(output_image, dpi=150)
        
        print(f"Sucesso! Imagem salva como '{output_image}'")
        plt.close()
        
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
else:
    print(f"Erro: Arquivo não encontrado no caminho: {file_path}")
    print("Verifique se a pasta 'data' está na raiz do projeto 'GeoDataScience'.")
""", language="python")

st.markdown("**Resultado:**")

st.image("assets/img/gdf_parsing2.png", caption="Mapa Mundial")