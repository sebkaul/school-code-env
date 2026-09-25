import numpy as np
import matplotlib.pyplot as plt

# EXPONENTIAL GROWTH MODEL – E. coli colony over time

# === EDIT THIS FOR EACH LAB ===
x = np.array([0, 21, 40, 60, 80, 90, 96])   # Tid
y = np.array([0.359, 0.376, 0.398, 0.449, 0.609, 0.681, 0.734])      # Absorbansmåling
# =================================

# Remove invalid zero entries for exponential fitting
mask = y > 0
x_fit_data = x[mask]
y_fit_data = y[mask]

# Fit exponential model: y = A * exp(kx)
# ln(y) = ln(A) + kx  → linear fit in log-space
ln_y = np.log(y_fit_data)
k, ln_A = np.polyfit(x_fit_data, ln_y, 1)

A = np.exp(ln_A)

# Generate smooth curve
x_model = np.linspace(min(x), max(x), 200)
y_model = A * np.exp(k * x_model)

# Plot
plt.figure()

plt.scatter(x, y, label="Målte verdier")

plt.plot(
    x_model,
    y_model,
    label=f"Eksponensiell kurve: y = {A:.4f}·e^({k:.4f}x)"
)

plt.xlabel("Tid [minutt]")
plt.ylabel("Absorbansmåling")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Numerical output
print(f"===== RESULTATER =====")
print(f"A = {A} (Initiell Verdi)")
print(f"k = {k} (Vekstkonstant)")
