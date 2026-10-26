import scipy
import sympy as sp
import numpy as np

t = sp.symbols("t")

x = sp.cos(t)
y = sp.sin(t)

dx = sp.diff(x)
dy = sp.diff(y)

f = x**3 + y

integrand = f * sp.sqrt(dx**2 + dy**2)

F = sp.lambdify(t, integrand)
L, err = scipy.integrate.quad(F, 0, 2*np.pi)

print(L)
