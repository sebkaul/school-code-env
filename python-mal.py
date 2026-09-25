import numpy as np
import matplotlib.pyplot as plt

# LINEWEAVER BURK PLOT

# === EDIT THIS FOR EACH LAB ===
x = np.array([1, 2, 3, 4, 5])          # Prøve tilsatt
y = np.array([2.3, 3.1, 4.0, 4.8, 5.6])  # Absorbans
# =============================

### MERK:
# x = 1/[S]
# y = 1/V
#
# a = K_M / V_max
# b = 1 / V_max
# x_intercept = -1 / K_M
# y_intercept = 1 / V_max

# Linear regression using ORDINARY LEAST SQUARES
a, b = np.polyfit(x, y, 1)             # y = a*x + b

# x-intercept (y = 0)
x_cross = -b / a                       # = -1/K_M

# Generate x ranges
x_min = min(x)
x_max = max(x)

x_fit = np.linspace(x_min, x_max, 100)
y_fit = a * x_fit + b

# Extrapolate toward x-intercept
x_extra = np.linspace(x_max, x_cross, 100)
y_extra = a * x_extra + b

# PLOTTING
plt.figure()

# Data and model
plt.scatter(x, y, label="Målte Verdier")

plt.plot(
    x_fit, y_fit,
    label=f"Lineær regresjon, \nStigningstall = {a:.4f}"
)

plt.plot(
    x_extra, y_extra,
    linestyle="--",
    label="Ekstrapolasjon"
)

# Axes at zero
plt.axhline(0, linewidth=1)
plt.axvline(0, linewidth=1)

# Intercepts
plt.scatter(
    x_cross, 0,
    zorder=3,
    label=f"x-kryssing, -1/K_M = {x_cross:.4f}"
)

plt.scatter(
    0, b,
    zorder=3,
    label=f"y-kryssing, 1/V_max = {b:.4f}"
)

# Labels and layout
plt.xlabel("x, 1/[S]")
plt.ylabel("y, 1/V")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()


# Numerical output
print(f"Slope a = {a} (K_M / V_max)")
print(f"x-kryssing = {x_cross} (-1 / K_M)")
print(f"y-kryssing = {b} (1 / V_max)")

