import sympy as sp

x,y = sp.symbols("x,y")
z = 4 - x**2 - y**2
dx = sp.diff(z, x)
dy = sp.diff(z, y)
I = sp.integrate(sp.sqrt(dx**2 + dy**2 + 1) , (x,-1,1), (y,-1,1))
print(I.evalf())

import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

numpts = 1000
pts = np.zeros((numpts,3))
pts[:,:2] = np.random.uniform(-1,1,(numpts,2))
pts[0:4, :2] = [[-1.0, -1.0],[-1.0, 1.0],[1.0, -1.0],[1.0, 1.0]]
pts[50:100, 0] = -1.0
pts[100:150, 0] = 1.0
pts[150:200, 1] = -1.0
pts[200:250, 1] = 1.0

pts[:,2] = 4.0 - pts[:,0]**2 - pts[:,1]**2

tri = Delaunay(pts[:,:2])
plt.triplot(pts[:,0], pts[:,1], tri.simplices)
plt.show()

p = pts[tri.simplices[:,0]]
q = pts[tri.simplices[:,1]]
r = pts[tri.simplices[:,2]]

u = q - p
v = r - p

a = np.cross(u, v)
area = np.sum(np.linalg.norm(a, axis=1))/2

print(area)
