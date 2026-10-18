import numpy as np
import sympy as sp
import scipy

u, v = sp.symbols("u v", positive=True)

r = sp.Matrix([sp.cos(u)*v, sp.sin(u)*v, v**2/2])

drdu = r.diff(u)
drdv = r.diff(v)

print(drdu)
print(drdv)

# b

crossproduct = drdu.cross(drdv)
dS = crossproduct.norm()

print(crossproduct)
print(dS)

n0 = crossproduct.subs({u: 5*sp.pi/6, v: 2})
N = -sp.simplify(n0/n0.norm())

print(N)

# c

L = sp.integrate(sp.simplify(dS), (u, 0, sp.pi), (v, sp.sqrt(3), 2*sp.sqrt(6)))
print(L)

