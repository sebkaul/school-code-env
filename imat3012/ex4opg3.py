import sympy as sp
import scipy

t = sp.symbols("t")

a = 1.00005507808
b = 0.55342925736
c = 0.99873327689

x = 1-(c*(1-t)**3 + 3*b*t*(1-t)**2)
y = 1-(a*t**3 + 3*b*t**2*(1-t))

sp.plot_parametric((x,y), (t,0,1))

dx = sp.diff(x)
dy = sp.diff(y)

integrand = sp.sqrt(dx**2 + dy**2)

f = sp.lambdify(t, integrand)
L, err = scipy.integrate.quad(f, 0, 1)

print(L)
