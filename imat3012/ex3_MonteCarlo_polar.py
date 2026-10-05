import numpy as np

rng = np.random.default_rng()

N = 10**7

x0, x1 = 0, 3
y0, y1 = 0, 2
z0, z1 = 0, 4

x = rng.uniform(x0, x1, N)
y = rng.uniform(y0, y1, N)
z = rng.uniform(z0, z1, N)

V_box = (x1 - x0) * (y1 - y0) * (z1 - z0)

inside = np.ones(N, dtype=bool)

f = 1
vals = inside * f
I_est = np.mean(vals) * V_box
err = np.std(vals) * V_box / np.sqrt(N)
print("Monte Carlo estimat:", I_est, "+/-", err)
