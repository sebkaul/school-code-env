import numpy as np
import matplotlib.pyplot as plt

m_cat = 1        # g catalyst
V_mol = 22400    # cm³/mol at STP

P  = np.array([1.200, 1.933, 4.800, 12.866, 25.132, 38.131])  # kPa
CO = np.array([0.670, 0.870, 1.201, 1.397, 1.697, 1.897])     # cm³ STP adsorbed

x = 1/P
y = 1/CO

slope, intercept = np.polyfit(x, y, 1)   # y = slope·x + intercept
R2 = np.corrcoef(x, y)[0, 1]**2

Vm = 1/intercept           # cm³ STP at monolayer
K  = intercept/slope       # kPa⁻¹
Ct = Vm/V_mol/m_cat        # mol sites / g_cat (1 CO = 1 site)

print(f"intercept={intercept:.4f}, slope={slope:.4f}, R²={R2:.4f}")
print(f"Vm={Vm:.3f} cm³, K={K:.3f} kPa⁻¹, Ct={Ct:.3e} mol/g")

xf = np.linspace(0, x.max()*1.05, 100)
plt.plot(x, y, 'bo', label='Data')
plt.plot(xf, slope*xf + intercept, 'r-',
         label=f'Fit: $y = {slope:.3f}x + {intercept:.3f}$, $R^2 = {R2:.3f}$')
plt.plot(0, intercept, 'k*', markersize=12,
         label=f'Intercept $1/V_m = {intercept:.3f}$ → $V_m = {Vm:.2f}$ cm³')

plt.xlabel(r'$1/P_{\mathrm{CO}}$ [kPa$^{-1}$]')
plt.ylabel(r'$1/V_{\mathrm{CO,ads}}$ [cm$^{-3}$]')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('langmuir_fit.pdf')
plt.show()
