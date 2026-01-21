# Geo Data Science BR - GDSBR

### **DESCRIÇÃO:** _Projetos de Geotecnologia que envolvem Análise de Dados, Machine Learning e Engenharia de Software com uso de agentes de IA para acelerar o aprendizado e o desenvolvimento dos projetos_

### **OBJETIVO:** _Divulgar o uso de Python para Análise de Dados e Machine Learning em projetos de Geotecnologia com auxílio de Agentes de IA e uso de tecnologias modernas._

### **PÚBLICO:** _Estudantes, profissionais e entusiastas de Geoprocessamento e Geografia que não sabem programar e que queiram iniciar em programação com linguagem Python para construir projetos de Geotecnologia com as ferramentas mais modernas e aplicadas no Mercado de Trabalho de TI._

## PROJETO 1: INTRODUÇÃO À GEOMETRIAS

### 1. Criando um Ponto (Creating a Point)

**Explicação:**
Um ponto geométrico (`Point`) representa uma única localização no espaço, definida por coordenadas numéricas (longitude e latitude). Na biblioteca **Shapely**, pontos podem ser criados passando as coordenadas `(x, y)` ou `(longitude, latitude)`, e são a base para construir outras geometrias.

**Código:**
```python
from shapely.geometry import Point
import matplotlib.pyplot as plt

# Criando um ponto (Longitude, Latitude)
# Exemplo: Brasília, DF
# Longitude = x = -47.8825
# Latitude  = y = -15.7942
ponto = Point(-47.8825, -15.7942)

print(f"Ponto criado: {ponto}")
# Saída: POINT (-47.8825 -15.7942)
```

**Resultado:**

![Exemplo de Ponto](assets\img\point_example.png)
---
### 2. Criando Linhas (Creating Line Segments)

**Explicação:**
Uma linha (`LineString`) é uma sequência de pelo menos dois pontos conectados. Representa objetos lineares como ruas, rios ou limites. Em `shapely`, é criada a partir de uma lista de coordenadas `(x, y)` ou pontos.

**Código:**
```python
from shapely.geometry import LineString

# Criando uma linha com 2 pontos (Ponta A -> Ponta B)
line = LineString([(-47.9500, -15.7900), (-47.8200, -15.8000)])

print(f"Linha criada: {line}")
```

**Resultado:**

![Exemplo de Linha](assets\img\line_example.png)
---
### 3. Criando Polígonos e Multipolígonos (Creating Polygons and Multipolygons)

**Explicação:**
- **Polígono (`Polygon`)**: Uma área fechada definida por uma borda externa (shell) e opcionalmente bordas internas (holes). O primeiro e o último ponto da sequência devem ser iguais para fechar o anel (ou o Shapely fecha automaticamente).
- **Multipolígono (`MultiPolygon`)**: Uma coleção de um ou mais polígonos tratados como um único objeto geométrico (ex: um arquipélago, ou um país com ilhas).

**Código:**
```python
from shapely.geometry import Polygon, MultiPolygon

# Criando um Polígono (Triângulo)
poly = Polygon([
    (-47.8500, -15.8200),
    (-47.8000, -15.8200),
    (-47.8250, -15.8500)
])

# Criando um Multipolígono (Dois quadrados desconexos)
mpoly = MultiPolygon([
    Polygon([(0,0), (1,0), (1,1), (0,1)]),
    Polygon([(2,2), (3,2), (3,3), (2,3)])
])

print(f"Polígono: {poly}")
print(f"Multipolígono: {mpoly}")
```

**Resultado:**

![Exemplo de Polígono](assets\img\polygon_example.png)
---
### 4. Buffering a Geometry
### 5. Set Operations on Geometries
### 6. Area and Perimeter Computation
### 7. Computing Centroids
### 8. Enclosing Polygons
### 9. Creating a Bounding Box
### 10. Within-test
### 11. Distance Calculation
### 12. Simplifying Geometries
### 13. 3D Objects in Shapely

## PROJETO 2: VECTOR DATA IN PYTHON
### 14. Querying the Built-in Datasets in GeoPandas
### 15. Parsing a Data File into a GeoDataFrame
### 16. Creating a GeoDataFrame from Scratch
### 17. Creating a GeoDataFrame from a DataFrame
### 18. Writing a GeoDataFrame to a File
### 19. Accessing the Geometry Column as a GeoSeries
### 20. Bounds of a GeoSeries
### 21. Area and Perimeter Computation
### 22. Simple Visualization with GeoPandas
### 23. Buffering a GeoDataFrame
### 24. Spatial Join with GeoPandas
### 25. Overlaying GeoDataFrames
### 26. Dissolving Polygons
### 27. Splitting Geometries in a GeoDataFrame
### 28. Applying Simple Functions on GeoDataFrames
### 29. Generating Random Synthetic Data
### 30. Counting Points in Polygons


## PROJETO 3: VISUALIZING GEOSPATIAL DATA
### 31. Using Matplotlib for Categorical Coloring in Geospatial Data
### 32. Using Matplotlib for Continuous Value Coloring with Linear Scale
### 33. Using Matplotlib for Continuous Value Coloring with Logarithmic Scale
### 34. Visualizing Multiple GeoDataFrames
### 35. Creating a Heatmap from Point Data
### 36. Adding Basemap with Contextily
### 37. Creating a Simple Interactive Map with Folium
### 38. Creating a Simple Interactive Map with Plotly
### 39. Visualizing 3D Geometries with Matplotlib
### 40. Visualizing 3D Geometries with Pydeck


## PROJETO 4: MAP PROJECTIONS
### 41. Querying Coordinate Reference Systems
### 42. Setting the Default CRS
### 43. Reprojecting a GeoDataFrame
### 44. Understanding Global vs. Local CRS
### 45. Additional Projection Systems
### 46. Transforming Coordinates Directly
### 47. Obtaining EPSG Codes


## PROJETO 5: SPATIAL INDEXING
### 48. Creating a Simple Spatial Index in GeoPandas
### 49. Using Simple Spatial Indexes for Efficient Queries
### 50. Efficient Spatial Indexing with RTree
### 51. Creating a Square Grid from Scratch
### 52. Visualizing RTree Indexing
### 53. Enclosing Grid Cell Identification Using RTree
### 54. Introduction to H3 Indexing
### 55. Visualizing H3 Grids


## PROJETO 6: GEOCODING
### 56. Geocoding a Single Address Using GeoPy
### 57. Reverse Geocoding Coordinates
### 58. Batch Geocoding Multiple Addresses
### 59. Handling Missing Geocodes
### 60. From Geocoding to GeoDataFrame
### 61. Geocoding within a DataFrame


## PROJETO 7: RASTER DATA IN PYTHON
### 62. Reading Raster Data
### 63. Clip the raster data file using GeoPandas
### 64. Writing Raster Data
### 65. Visualizing Raster Data
### 66. Histogram Equalization on Raster Data
### 67. Applying Simple Functions on Raster Data
### 68. Reprojecting Raster Data
### 69. Compute Zonal Statistics
### 70. Convert a Raster Grid into Vector Data
### 71. Reading Large Raster Files Efficiently
### 72. Clipping Large Raster Files
### 73. Visualizing Large Raster Files
### 74. Downsampling a Large Raster File


## PROJETO 8: INTRODUCTION TO OPENSTREETMAP DATA
### 75. Downloading Administrative Areas from OpenStreetMap (OSM)
### 76. Using OSMnx to Download Points of Interest (POIs)
### 77. Using OSMnx to Download Parks as Polygons
### 78. Using OSMnx to Download Building Footprints
### 79. Using OSMnx to Download Road Networks
### 80. Visualizing Complex Urban Areas


## PROJETO 9: SPATIAL NETWORKS
### 81. Road Networks in GeoPandas
### 82. From GeoDataFrames to Spatial Networks
### 83. Visualizing Spatial Networks
### 84. Calculating the Shortest Path
### 85. Visualizing the Shortest Path
### 86. Generating Walking Distance Isochrones
### 87. Obtaining spatial network statistics
### 88. Network Centrality Measures
### 89. Community Detection in Spatial Networks

## PROJETO 10: GEOSPATIAL STATISCS AND MACHINE LEARNING
### 90. Descriptive Statistics with GeoPandas
### 91. Global Spatial Autocorrelation
### 92. Local Spatial Autocorrelation
### 93. Spatial Feature Generation
### 94. OLS Regression on Spatial Data
### 95. Spatial Regression Models
### 96. Spatial Random Forest
### 97. Comparing Spatial Regression Models
### 98. Hotspot Analysis
### 99. Kernel Density Estimation
### 100. Inverse Distance Weighting for Spatial Interpolation
### 101. Spatial Clustering