import sympy as sp

x = sp.symbols("x")
y = sp.sin(x)

area = sp.integrate(y, (x,0,sp.pi))
print(area)
