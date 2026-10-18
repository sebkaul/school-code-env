import numpy as np
from matplotlib import pyplot as plt

pts = np.array([[0,0],[0,1],[1,0],[1,1],[2,0],[2,1],[3,0],[3,1]])
triangles = np.array([[0,1,2], [1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7]])

p = pts[triangles[:,0]]
q = pts[triangles[:,1]]
r = pts[triangles[:,2]]
n = len(p)

avg = 1/3 * (p + q + r)
x = avg[:,0]
y = avg[:,1]
f = x**2*y

u = q - p
v = r - p

Muv = np.column_stack((u,v)).reshape(n,2,2)
dA = np.abs(1/2*np.linalg.det(Muv))

svar = np.sum(dA*f)
print(svar)

