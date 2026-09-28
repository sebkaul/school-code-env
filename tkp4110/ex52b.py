import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

V_max = 1.0291e-3 # mol/(L min)
K_m = 0.045304 # mol/L
S_0 = 0.0375 # Initial Conditions
t = np.linspace(0, 20, 200) #min

def residual(S, t, V_max):
    return K_m * np.log(S_0/S) + (S_0 - S) - V_max*t

def solve_S(t, V_max):
    S = np.zeros_like(t)
    guess = S_0
    for i, ti in enumerate(t):
        S[i] = fsolve(residual, guess, args=(ti, V_max))[0]
        guess = S[i]
    return S

S_base = solve_S(t, V_max)
S_2x   = solve_S(t, 2*V_max)

plt.plot(t, S_base, label='$V_{max}$')
plt.plot(t, S_2x, label='$2V_{max}$')
plt.xlabel('$t [min]$')
plt.ylabel('$C_S [mol/L]$')
plt.grid(alpha=.3)
plt.legend()
plt.show()

for label, S in [('E_t', S_base), ('2E_t', S_2x)]:
    print(f'{label}: C_S(20 min) = {np.interp(20, t, S):.5f} mol/L')
