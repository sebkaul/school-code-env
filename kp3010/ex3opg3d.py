"""
McCabe-Thiele graphical solution for a linear-equilibrium absorber.

Assumes:
    - equilibrium line: Y = K * X       (straight, dilute regime)
    - operating line : straight in ratio coordinates (inert-based)
"""

import numpy as np
import matplotlib.pyplot as plt


# ---------- INPUT (Oppg 3d) ----------
G_tot   = 122.6     # total inlet gas [kmol/h]
L_tot   = 5880      # total inlet liquid [kmol/h]
y_in    = 0.05      # gas inlet mole fraction (bottom, y_{N+1})
y_out   = 0.005     # gas outlet mole fraction (top, y_1)
x_in    = 0.0       # liquid inlet mole fraction (top, x_0)
K       = 45        # equilibrium: Y = K X
# -------------------------------------


def frac_to_ratio(f):
    return f / (1 - f)


def step_off_stages(X0, Y1, XN, K, slope, intercept, max_stages=50):
    """
    Staircase from (X0, Y1) up to XN.
    Horizontal step: land on equilibrium curve  X = Y / K
    Vertical step  : land on operating line     Y = slope * X + intercept
    Returns list of (X, Y) vertices of the staircase.
    """
    verts = [(X0, Y1)]
    X, Y = X0, Y1
    stages = 0
    while X < XN and stages < max_stages:
        # horizontal: from operating line across to equilibrium
        X_new = Y / K
        verts.append((X_new, Y))
        if X_new >= XN:
            # last stage is fractional — measure how much of it we used
            frac = (XN - X) / (X_new - X)
            stages += frac
            break
        # vertical: up to operating line
        Y_new = slope * X_new + intercept
        verts.append((X_new, Y_new))
        X, Y = X_new, Y_new
        stages += 1
    return verts, stages


# --- convert inputs to ratios ---
X0     = frac_to_ratio(x_in)
Y1     = frac_to_ratio(y_out)
Y_Np1  = frac_to_ratio(y_in)

G_prime = G_tot * (1 - y_in)
L_prime = L_tot * (1 - x_in)

# XN from overall inert balance
XN = X0 + (G_prime / L_prime) * (Y_Np1 - Y1)

# operating line slope & intercept: Y = (L'/G') X + (Y1 - (L'/G') X0)
slope     = L_prime / G_prime
intercept = Y1 - slope * X0

# absorption factor for a sanity print
A = L_prime / (K * G_prime)

# --- step off ---
verts, N_stages = step_off_stages(X0, Y1, XN, K, slope, intercept)

print(f"G'         = {G_prime:.2f} kmol/h")
print(f"L'         = {L_prime:.2f} kmol/h")
print(f"X0, Y1     = {X0:.5f}, {Y1:.5f}")
print(f"XN, Y_N+1  = {XN:.5f}, {Y_Np1:.5f}")
print(f"L'/G'      = {slope:.3f}")
print(f"A          = {A:.3f}")
print(f"Stages (graphical) = {N_stages:.2f}  ->  round up to {int(np.ceil(N_stages))}")


# --- plot ---
X_grid = np.linspace(0, XN * 1.15, 200)
Y_eq   = K * X_grid
Y_op   = slope * X_grid + intercept

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(X_grid, Y_eq, label=f"Equilibrium: Y = {K}X", color="C0")
ax.plot(X_grid, Y_op, label=f"Operating: slope = {slope:.1f}", color="C1")

# staircase
xs = [v[0] for v in verts]
ys = [v[1] for v in verts]
ax.plot(xs, ys, "k-", lw=1)

# anchor points
ax.plot(X0, Y1, "ko"); ax.annotate("(X0, Y1) - top", (X0, Y1), textcoords="offset points", xytext=(8, -12))
ax.plot(XN, Y_Np1, "ko"); ax.annotate("(XN, Y_{N+1}) - bottom", (XN, Y_Np1), textcoords="offset points", xytext=(-100, 8))

ax.set_xlabel("X (mol A / mol inert liquid)")
ax.set_ylabel("Y (mol A / mol inert gas)")
ax.set_title(f"McCabe-Thiele — N ≈ {N_stages:.2f} stages   (A = {A:.2f})")
ax.legend()
ax.grid(True, alpha=0.3)

fig.savefig("mccabe_thiele.png", dpi=120, bbox_inches="tight")
plt.show()
