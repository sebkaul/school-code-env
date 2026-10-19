import numpy as np
import matplotlib.pyplot as plt

# =======================
# INPUT
# =======================
c_std = np.array([0.2, 0.4, 0.6, 0.8, 1.0])          # mg/mL BSA

A_par1 = np.array([0.203, 0.388, 0.518, 0.755, 0.838])
A_par2 = np.array([0.200, 0.432, 0.595, 0.784, 0.934])
A_blank = np.array([0.0])  # instrument nullstilt på blank

DF = 1  # ingen fortynning etter kolonnen

# {"navn": [A595 rør 1, (rør 2)]}
prover = {
    "Prøve 1": [0.076],
    "Prøve 2": [0.083],
}

# =======================
# BEREGNING
# =======================
blank = A_blank.mean()
y1 = A_par1 - blank
y2 = A_par2 - blank

# Regresjon på alle 10 punkter, tvunget gjennom origo: A = a*c
x = np.concatenate([c_std, c_std])
y = np.concatenate([y1, y2])
a = np.sum(x * y) / np.sum(x ** 2)

y_pred = a * x
R2 = 1 - np.sum((y - y_pred) ** 2) / np.sum((y - y.mean()) ** 2)

print("===== STANDARDKURVE =====")
print(f"A595 = {a:.4f} * c   (gjennom origo)")
print(f"R^2  = {R2:.4f}\n")

print("===== PRØVER =====")
print(f"{'Prøve':<10}{'A595':>8}{'c (mg/mL)':>12}  Merknad")

resultater = []
for navn, A in prover.items():
    A_korr = np.mean(A) - blank
    c = A_korr / a * DF
    if A_korr < y.min():
        merknad = "UNDER laveste standard"
    elif A_korr > y.max():
        merknad = "OVER høyeste standard"
    else:
        merknad = ""
    resultater.append((navn, A_korr, c))
    print(f"{navn:<10}{A_korr:>8.3f}{c:>12.4f}  {merknad}")

# =======================
# PLOT
# =======================
x_fit = np.linspace(0, c_std.max() * 1.05, 200)

fig, ax = plt.subplots(figsize=(6.5, 4.8))
ax.scatter(c_std, y1, marker="o", label="Standard, parallell 1")
ax.scatter(c_std, y2, marker="s", label="Standard, parallell 2")
ax.plot(x_fit, a * x_fit, "k-",
        label=f"$A_{{595}} = {a:.3f}\\,c$,  $R^2 = {R2:.4f}$")

for navn, A_korr, c in resultater:
    c_ror = A_korr / a
    ax.scatter(c_ror, A_korr, marker="x", s=80, zorder=3,
               label=f"{navn}: $c$ = {c:.3f} mg/mL")
    # hjelpelinjer ned til aksene
    ax.plot([c_ror, c_ror], [0, A_korr], ":", color="gray", lw=1)
    ax.plot([0, c_ror], [A_korr, A_korr], ":", color="gray", lw=1)

ax.set_xlabel("BSA-konsentrasjon (mg/mL)")
ax.set_ylabel("Absorbans ved 595 nm")
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=8, loc="upper left")
fig.tight_layout()
fig.savefig("bradford_curve.png", dpi=300)
plt.show()
