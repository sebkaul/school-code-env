import sympy as sp
x,y,a = sp.symbols("x,y,a")

f = x*x*y

svar = sp.integrate(f, (y, -sp.sqrt(a**2 - x**2), 0), (x,-a,a))
print(svar)

