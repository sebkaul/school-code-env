import numpy as np
from scipy.spatial import Delaunay

# circle
theta = np.linspace(0, 2*np.pi, 100, endpoint=False)

# r = 2 og h = 4
x = 2*np.cos(theta)
y = 2*np.sin(theta)

# bottom
z1 = np.zeros(100) # z = 0
# top
z2 = np.zeros(100) + 4 # z = 4


ring1 = np.column_stack((x,y,z1)).reshape(100, 3)
ring2 = np.column_stack((x,y,z2)).reshape(100, 3)

pts = np.vstack((ring1, ring2))


tri = Delaunay(pts)

p = pts[tri.simplices[:,0]]
q = pts[tri.simplices[:,1]]
r = pts[tri.simplices[:,2]]
s = pts[tri.simplices[:,3]]
n = len(p) 


# avg = 1/3 * (p + q + r + s)
# x = avg[:,0]
# y = avg[:,1]
# z = avg[:,2]
f = 1

u = q - p
v = r - p
w = s - p

Muv = np.column_stack((u,v,w)).reshape(n,3,3)
dA = np.abs(1/6*np.linalg.det(Muv))

# 4. Sum
svar = np.sum(dA*f)
print(svar)

# print(tri.simplices)
# print(p)
