import numpy as np
from scipy.spatial import Delaunay

np.random.seed(42)  # reproducible

N = 5000  # total points — bump if you don't hit tolerance

pts = np.random.rand(N, 2)
pts[:, 0] *= 3.0  # x ∈ [0, 3], y ∈ [0, 1]

# Pin corners
pts[0] = [0, 0]
pts[1] = [3, 0]
pts[2] = [0, 1]
pts[3] = [3, 1]

# Sprinkle points along the 4 edges so Delaunay covers the full rectangle
n_edge = 100  # points per edge
i = 4
pts[i:i+n_edge, 0] = np.linspace(0, 3, n_edge); pts[i:i+n_edge, 1] = 0.0; i += n_edge  # bottom
pts[i:i+n_edge, 0] = np.linspace(0, 3, n_edge); pts[i:i+n_edge, 1] = 1.0; i += n_edge  # top
pts[i:i+n_edge, 0] = 0.0; pts[i:i+n_edge, 1] = np.linspace(0, 1, n_edge); i += n_edge  # left
pts[i:i+n_edge, 0] = 3.0; pts[i:i+n_edge, 1] = np.linspace(0, 1, n_edge); i += n_edge  # right

tri = Delaunay(pts)

p = pts[tri.simplices[:, 0]]
q = pts[tri.simplices[:, 1]]
r = pts[tri.simplices[:, 2]]
n = len(p)

# Midpoints
avg = (p + q + r) / 3
x, y = avg[:, 0], avg[:, 1]
f = x * x * y

# Areas via |det([u v])| / 2
u = q - p
v = r - p
Muv = np.column_stack((u, v)).reshape(n, 2, 2)
dA = np.abs(0.5 * np.linalg.det(Muv))

svar = np.sum(dA * f)
print(f"Estimate: {svar:.6f}")
print(f"Exact:    4.500000")
print(f"Error:    {abs(svar - 4.5):.6f}")
