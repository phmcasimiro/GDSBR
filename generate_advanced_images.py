import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon, MultiPoint, GeometryCollection
from shapely.ops import unary_union
import numpy as np
import os

# Configuração
try:
    plt.style.use('seaborn-v0_8-whitegrid')
except:
    plt.style.use('ggplot')

output_dir = os.path.join('assets', 'img')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def save_fig(name):
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, name), dpi=100)
    plt.close()
    print(f"Gerado: {name}")

# 4. Buffering
fig, ax = plt.subplots(figsize=(6, 6))
p = Point(0, 0)
buffer = p.buffer(1) # cria um buffer de raio 1 ao redor do ponto
x, y = buffer.exterior.xy
ax.fill(x, y, alpha=0.5, color='blue', label='Buffer (r=1)')
ax.plot(0, 0, 'ro', label='Point')
ax.set_title('Buffering a Point')
ax.legend()
ax.set_aspect('equal')
save_fig('buffer.png')

# 5. Set Operations
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
p1 = Polygon([(0,0), (2,0), (2,2), (0,2)])
p2 = Polygon([(1,1), (3,1), (3,3), (1,3)])

# Union
u = p1.union(p2)
x, y = u.exterior.xy
ax1.fill(x, y, alpha=0.5, color='purple')
ax1.set_title('Union')
# Intersection
i = p1.intersection(p2)
x, y = i.exterior.xy
ax2.fill(x, y, alpha=0.5, color='green')
ax2.set_title('Intersection')
# Difference
d = p1.difference(p2)
x, y = d.exterior.xy
ax3.fill(x, y, alpha=0.5, color='red')
ax3.set_title('Difference (P1 - P2)')
save_fig('sets.png')

# 6. Area and Perimeter
fig, ax = plt.subplots(figsize=(6, 6))
poly = Polygon([(0,0), (4,0), (4,3), (0,0)]) # Triangulo retangulo 3-4-5
x, y = poly.exterior.xy
ax.fill(x, y, alpha=0.3, color='orange')
ax.plot(x, y, color='black')
ax.text(1.5, 1, f"Area: {poly.area}\nPerim: {poly.length}", fontsize=12)
ax.set_title('Area and Perimeter')
save_fig('area_perimeter.png')

# 7. Centroids
fig, ax = plt.subplots(figsize=(6, 6))
poly = Polygon([(0,0), (4,0), (4,4), (0,4)])
centroid = poly.centroid
x, y = poly.exterior.xy
ax.fill(x, y, alpha=0.3, color='cyan')
ax.plot(centroid.x, centroid.y, 'rx', markersize=10, label='Centroid')
ax.set_title('Polygon Centroid')
ax.legend()
save_fig('centroid.png')

# 8. Enclosing (Convex Hull)
fig, ax = plt.subplots(figsize=(6, 6))
points = MultiPoint([(0,0), (1,3), (2,2), (4,1), (3,0), (-1,1)])
hull = points.convex_hull
for p in points.geoms:
    ax.plot(p.x, p.y, 'ko')
x, y = hull.exterior.xy
ax.plot(x, y, 'b--', label='Convex Hull')
ax.set_title('Convex Hull')
ax.legend()
save_fig('convex_hull.png')

# 9. Bounding Box
fig, ax = plt.subplots(figsize=(6, 6))
poly = Polygon([(1,1), (2,3), (3,2)])
minx, miny, maxx, maxy = poly.bounds
bbox = Polygon([(minx, miny), (maxx, miny), (maxx, maxy), (minx, maxy)])
x, y = poly.exterior.xy
ax.fill(x, y, color='yellow', alpha=0.5)
x, y = bbox.exterior.xy
ax.plot(x, y, 'r--', label='Bounding Box')
ax.set_title('Bounding Box')
ax.legend()
save_fig('bbox.png')

# 10. Within Test
fig, ax = plt.subplots(figsize=(6, 6))
poly = Polygon([(0,0), (4,0), (4,4), (0,4)])
p_in = Point(2, 2)
p_out = Point(5, 5)
x, y = poly.exterior.xy
ax.plot(x, y, 'k-')
ax.plot(p_in.x, p_in.y, 'go', label='Within (True)')
ax.plot(p_out.x, p_out.y, 'ro', label='Within (False)')
ax.set_title('Within Test')
ax.legend()
save_fig('within.png')

# 11. Distance
fig, ax = plt.subplots(figsize=(6, 6))
p1 = Point(0, 0)
p2 = Point(3, 4)
dist = p1.distance(p2)
ax.plot([p1.x, p2.x], [p1.y, p2.y], 'b--')
ax.plot(p1.x, p1.y, 'go')
ax.plot(p2.x, p2.y, 'go')
ax.text(1.5, 2, f"Dist: {dist}", fontsize=12)
ax.set_title('Euclidean Distance')
save_fig('distance.png')

# 12. Simplifying
fig, ax = plt.subplots(figsize=(8, 4))
coords = [(x, np.sin(x) + 0.1*np.random.normal()) for x in np.linspace(0, 10, 50)]
line = LineString(coords)
simplified = line.simplify(0.5, preserve_topology=False)
x, y = line.xy
ax.plot(x, y, 'b-', alpha=0.3, label='Original')
x, y = simplified.xy
ax.plot(x, y, 'r-', linewidth=2, label='Simplified (tol=0.5)')
ax.set_title('Simplifying Geometries')
ax.legend()
save_fig('simplify.png')

# 13. 3D Objects (Pseudo visualization)
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter([0], [0], [0], c='r', marker='o')
ax.text(0, 0, 0.1, "Point(0,0,0)")
ax.set_title('3D Point Support')
save_fig('3d_point.png')
