import streamlit as st
import folium
from streamlit_folium import st_folium
from shapely.geometry import Point, LineString, Polygon, MultiPolygon

st.set_page_config(page_title="WebMap", page_icon="🗺️", layout="wide")

st.title("🗺️ WebMap")
st.markdown("Visualize as geometrias criadas dinamicamente usando **Folium**.")

# Sidebar de controles
st.sidebar.header("Controles")
show_point = st.sidebar.checkbox("Mostrar Ponto (Brasília)", value=True)
show_line = st.sidebar.checkbox("Mostrar Linha (Eixo Monumental - Simplificado)", value=False)
show_poly = st.sidebar.checkbox("Mostrar Polígono (Lago Paranoá - Simplificado)", value=False)
show_multipoly = st.sidebar.checkbox("Mostrar Multipolígono (Parques)", value=False)

# Criando mapa base
m = folium.Map(location=[-15.7942, -47.8825], zoom_start=12)

# 1. Ponto (Brasília)
if show_point:
    ponto = Point(-47.8825, -15.7942)
    folium.Marker(
        location=[ponto.y, ponto.x],
        popup="Brasília (Ponto)",
        tooltip="Ponto Central",
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 2. Linha (Exemplo fictício/simplificado)
if show_line:
    # Coordenadas aproximadas para exemplo
    line_coords = [
        (-47.9500, -15.7900), # Ponta Norte aprox
        (-47.8200, -15.8000)  # Ponta Sul aprox
    ]
    linha = LineString(line_coords)
    # Folium espera [lat, lon], shapely é (x, y) = (lon, lat)
    folium_line_coords = [(y, x) for x, y in line_coords]
    
    folium.PolyLine(
        locations=folium_line_coords,
        color="blue",
        weight=5,
        tooltip="Linha Exemplo"
    ).add_to(m)

# 3. Polígono (Exemplo simplificado triângulo)
if show_poly:
    poly_coords = [
        (-47.8500, -15.8200),
        (-47.8000, -15.8200),
        (-47.8250, -15.8500),
        (-47.8500, -15.8200) # Fechar
    ]
    poligono = Polygon(poly_coords)
    folium_poly_coords = [(y, x) for x, y in poly_coords]
    
    folium.Polygon(
        locations=folium_poly_coords,
        color="green",
        fill=True,
        fill_color="lightgreen",
        fill_opacity=0.4,
        tooltip="Polígono Exemplo"
    ).add_to(m)

# 4. Multipolígono (Exemplo: Dois quadrados distantes)
if show_multipoly:
    # Quadrado 1 (Longe)
    poly1_coords = [(-47.90, -15.75), (-47.88, -15.75), (-47.88, -15.77), (-47.90, -15.77), (-47.90, -15.75)]
    # Quadrado 2 (Perto)
    poly2_coords = [(-47.85, -15.75), (-47.83, -15.75), (-47.83, -15.77), (-47.85, -15.77), (-47.85, -15.75)]
    
    multipoly = MultiPolygon([Polygon(poly1_coords), Polygon(poly2_coords)])
    
    # Adicionar cada parte do multipolígono ao mapa
    for geom in multipoly.geoms:
        # Extrair coordenadas externas
        xx, yy = geom.exterior.coords.xy
        folium_coords = list(zip(yy, xx))
        
        folium.Polygon(
            locations=folium_coords,
            color="orange",
            fill=True,
            fill_color="orange",
            fill_opacity=0.4,
            tooltip="Parte do Multipolígono"
        ).add_to(m)

# Renderizar Mapa
st_folium(m, width=1200, height=600)
