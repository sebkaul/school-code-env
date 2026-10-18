import sympy as sp

phi, theta = sp.symbols("phi theta")
rho = sp.symbols("rho", positive=True)
deg = sp.pi/180   # multiply degrees by this to get radians

A = sp.integrate(rho**2 * sp.sin(phi),
                 (phi, 49*deg, 53*deg),
                 (theta, 0, 7*deg))

print(sp.N(A.subs(rho, 6365)))    # sp.N = give me a decimal

r = sp.solve(sp.Eq(A, 269837), rho)

print(sp.N(r[0]))
