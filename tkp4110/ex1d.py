# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "matplotlib>=3.11.1",
#     "numpy>=2.5.2",
#     "scipy>=1.18.1",
# ]
# ///
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# input data for Ca0/-rA vs X
Xa = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
Ca0_over_rA = np.array([12, 30, 54, 56, 45, 27, 20, 30, 50])
# Volumetric flow rave (v0)
v_0 = 50 # L/min
v_cstr = 750.0 # L/min

tau = v_cstr/v_0 # 15 min

tau_needed = Xa * Ca0_over_rA

plt.figure(figsize=(10, 6))
plt.plot(Xa, tau_needed, 'b-', label=r'$\tau$ as a function of $X$')
plt.axhline(tau, color='r', ls='--', label=fr'$\tau$ = {tau} min')

plt.xlabel(r'$X_a$')
plt.ylabel(r'$\tau$')
plt.grid(True)
plt.legend()
plt.show()
