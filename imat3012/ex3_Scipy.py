from scipy.integrate import tplquad
import numpy as np

f = lambda z, y, x : 1
a, b = 0, 5
c = lambda x : 0
d = lambda x : x**2
e = lambda x, y : 0
g = lambda x, y : x**2

answer = tplquad(f, a, b, c, d, e, g)

print(answer)

