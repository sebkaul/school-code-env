import numpy as np, matplotlib.pyplot as plt

t  = np.array([0, 6.0, 9.8, 14.5, 20.7, 28.5, 40.5])
Pt = np.array([3.00, 3.30, 3.43, 3.55, 3.70, 3.85, 4.00])

CA0 = 3.0 / (0.082 * 618)
X   = 2 * (Pt - 3) / 3
CA  = CA0 * (1 - X)

plt.plot(t, CA, 'o-')
plt.xlabel("$t$ [min]")
plt.ylabel("$C_A$ [mol/L]")
plt.grid()
plt.show()
