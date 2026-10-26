import sympy as sp

x, y = sp.symbols("x y", real=True)

f = 1/sp.sqrt(x**2 + y**2)

print(sp.simplify(sp.diff(f, x)))
print(sp.simplify(sp.diff(f, y)))
