import sympy as sp
x,y,a = sp.symbols("x,y,a", positive=True)

f = x + a

inner = (y, -sp.sqrt(a**2 - x**2), sp.sqrt(a**2 - x**2))
outer = (x,-a,a)
svar = sp.integrate(f, inner, outer)
print(sp.simplify(svar))

