import numpy as np
from scipy.optimize import brentq
import matplotlib.pyplot as plt

A, E_R = 5.67*10**(13), 25000 
V, F_A = 0.1, 1   # m3, mol/s
dT_ad, T_0, T_STP = 300, 655, 273.15 # K


k = lambda T: A * np.exp(-E_R/T)
v0 = lambda T: (F_A * T * 22.42)/(T_STP * 1000)
tau = lambda T: V/v0(T)
X_MB = lambda T: k(T)*tau(T)/(1 + k(T)*tau(T))
X_EB = lambda T: (T - T_0)/dT_ad

Ts = np.linspace(600, 1100, 1000)
plt.plot(Ts, X_MB(Ts), label="MB")
plt.plot(Ts, X_EB(Ts), label="EB")
plt.ylim(0, 1.05); plt.xlabel("T [K]"); plt.ylabel("X"); plt.legend(); plt.show()

T = brentq(lambda T: X_MB(T) - X_EB(T), 950, 1050)   # bracket around the crossing you see
print(f"T = {T:.1f} K, X = {X_EB(T):.4f}")
