import sympy as sp

t = sp.symbols("t")

x = sp.cos(t)*3
y = sp.sin(t)*2

velx = sp.diff(x, t)
vely = sp.diff(y, t)

print(velx, vely)
