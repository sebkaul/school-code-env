import sympy as sp

x, y = sp.symbols("x y", real=True)

P = 4*x / sp.sqrt(x**2 + y**2)
Q = -4*y / sp.sqrt(x**2 + y**2)   # second component, careful with the sign

dPdx = sp.diff(P, x)
dPdy = sp.diff(P, y)
dQdx = sp.diff(Q, x)
dQdy = sp.diff(Q, y)

div  = sp.simplify(dPdx + dQdy)    # div formula from the table
curl = sp.simplify(dQdx - dPdy)    # curl formula from the table

print(div)
print(curl)
