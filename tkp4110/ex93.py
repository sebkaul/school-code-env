import numpy as np
from scipy.optimize import brentq
import matplotlib.pyplot as plt

R, CA0 = 8.3144, 5000        # J/mol K, mol/m3
E1, E2 = 48534, 123846

k1 = lambda T: np.exp(17.3 - E1 / (R * T))
k2 = lambda T: np.exp(41.7 - E2 / (R * T))
left = lambda T: (1 - 0.7) * k1(T) * E1
right = lambda T: 0.7 * k2(T) * E2

T = brentq(lambda T: left(T) - right(T), 280, 400)
print(f"T = {T:.2f} K")

rA = lambda T: CA0 * (0.3 * k1(T) - 0.7 * k2(T))
rA_max = rA(T)
print(f"T_opt = {T:.2f} K, -r_A,max = {rA_max:.1f} mol/(m3·min)")

Ts = np.linspace(300, 370, 500)
plt.plot(Ts, rA(Ts))
plt.axvline(T, ls="--", label=f"T_opt = {T:.1f} K")
plt.plot(T, rA_max, "o", label=f"max: {rA_max:.0f} mol/(m³·min) at {T:.1f} K")
plt.xlabel("T [K]")
plt.ylabel(r"$-r_A$ [mol/(m$^3$·min)]")
plt.title(r"Reaction rate vs temperature at $X = 0.7$")
plt.legend()
plt.show()
