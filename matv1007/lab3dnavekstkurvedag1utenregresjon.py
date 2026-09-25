import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 21, 40, 60, 80, 90, 96])   # Tid
y = np.array([0.359, 0.376, 0.398, 0.449, 0.609, 0.681, 0.734])  # Absorbansmåling

plt.figure()

plt.plot(
    x,
    y,
    marker="o",
    label="Målte verdier"
)

plt.xlabel("Tid [minutt]")
plt.ylabel("Absorbans [A]")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Optional numerical output
print("===== RESULTATER =====")
for xi, yi in zip(x, y):
    print(f"Tid: {xi} min  |  Absorbans: {yi}")
