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
v_0 = 50.0 # L/min

# Calculate the reactor volume using the trapezoid rule
V_pfr = v_0 * cumulative_trapezoid(Ca0_over_rA, Xa, initial=0)
# Calculate the reactor volume for CSTR
V_cstr = v_0 * Xa * Ca0_over_rA

plt.figure(figsize=(10, 6))
plt.plot(Xa, V_pfr, 'b-', label='PFR Volume')
plt.plot(Xa, V_cstr, 'b-', label='CSTR Volume')

plt.xlabel('Xa')
plt.ylabel('V (L)')
plt.title('Reactor Volume as a Function of conversion')
plt.grid(True)
plt.legend()
plt.show()


