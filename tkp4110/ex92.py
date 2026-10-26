import numpy as np
from scipy.optimize import brentq
import matplotlib.pyplot as plt

R, FA0, CA0 = 8.3144, 8000, 5000        # J/mol K, mol/min, mol/m3
dH, Cp0 = 75312, 8e6 / 5000             # J/mol, J/mol K
UA, V, T0, Ta = 80000 * 150, 6.8627, 293, 283

k1 = lambda T: np.exp(17.3 - 48534 / (R * T))
X_MB = lambda T: 1 / (FA0 / (V * k1(T) * CA0) + 1)
X_EB = lambda T: (Cp0 * (T - T0) + UA / FA0 * (T - Ta)) / dH

T = brentq(lambda T: X_MB(T) - X_EB(T), 280, 400)
print(f"T = {T:.2f} K, X = {X_MB(T):.3f}")

Ts = np.linspace(280, 400, 500)
plt.plot(Ts, X_MB(Ts), label="X_MB"); plt.plot(Ts, X_EB(Ts), label="X_EB")
plt.legend(); plt.xlabel("T [K]"); plt.ylabel("X"); plt.show()
