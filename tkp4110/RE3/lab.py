"""
RE3 - Hydrolysis of t-butyl chloride in a CSTR
Group R3, Felleslab TKP4110, 28.09.2026

Produces the 5 required plots and the 7 required quantities.

ASSUMPTIONS - flip these two and everything downstream updates.
Both are flagged in the report as open questions (see Discussion).
"""
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# Assumptions to verify against the lab manual
# ----------------------------------------------------------------------
N_PUMPS = 1       # 1 -> v0 = Qf ;  2 -> v0 = 2*Qf (two feed streams)
C_A0    = 0.025   # mol/L, t-BC concentration entering the reactor
                  # 0.0125 if two equal feeds dilute the 0.025 M stock 1:1

# ----------------------------------------------------------------------
# Fixed quantities
# ----------------------------------------------------------------------
V_REACTOR = 300.0        # mL
R_GAS     = 8.314        # J/(mol K)
M_TBC, RHO_TBC = 92.57, 0.851   # g/mol, g/mL
M_H2O, RHO_H2O = 18.02, 1.00
C_TBC_STOCK = 0.025      # mol/L in the tBC/MeOH feed flask
C_H2O_STOCK = 35.0       # mol/L in the water/MeOH feed flask
V_FLASK = 1.0            # L prepared of each feed


def Qf(rpm):
    """Pump calibration curve, mL/s."""
    return 0.0022 * rpm + 0.025


# ----------------------------------------------------------------------
# Raw run log  (run label, bath T, rpm, [(t_min, pH, T_reactor), ...])
# ----------------------------------------------------------------------
RUNS = [
    ("R1", 30, 80, [(3, 2.09, 27.2), (6, 2.03, 29.7), (9, 1.99, 29.7),
                    (12, 1.94, 29.7), (15, 1.91, 29.7), (18, 1.88, 29.6),
                    (21, 1.86, 29.6), (24, 1.86, 29.6)]),
    ("R2", 30, 60, [(3, 1.81, 29.7), (6, 1.83, 29.7), (9, 1.77, 29.7),
                    (12, 1.78, 29.7), (15, 1.75, 29.7), (18, 1.77, 29.7),
                    (21, 1.76, 29.7), (24, 1.76, 29.7)]),
    ("R3", 35, 80, [(3, 1.74, 32.8), (6, 1.75, 33.3), (9, 1.72, 33.5),
                    (12, 1.72, 33.6), (15, 1.72, 33.6)]),
    ("R4", 35, 60, [(3, 1.70, 33.8), (6, 1.70, 33.8), (9, 1.67, 33.9),
                    (12, 1.68, 33.9), (15, 1.67, 33.9), (18, 1.67, 33.9)]),
    ("R5", 40, 80, [(3, 1.64, 36.7), (6, 1.64, 37.4), (9, 1.63, 37.6),
                    (12, 1.64, 37.6), (15, 1.62, 37.6)]),
]

# ----------------------------------------------------------------------
# Reactant amounts used (solution preparation)
# ----------------------------------------------------------------------
n_tbc = C_TBC_STOCK * V_FLASK
m_tbc = n_tbc * M_TBC
V_tbc = m_tbc / RHO_TBC
n_h2o = C_H2O_STOCK * V_FLASK
m_h2o = n_h2o * M_H2O
V_h2o = m_h2o / RHO_H2O

print("=" * 62)
print("REACTANT AMOUNTS (per 1 L feed flask)")
print("=" * 62)
print(f"  t-BC   : {n_tbc:.4f} mol  = {m_tbc:7.3f} g = {V_tbc:7.3f} mL")
print(f"  water  : {n_h2o:.1f} mol    = {m_h2o:7.1f} g = {V_h2o:7.1f} mL")
print("  each diluted to 1000 mL with methanol in a volumetric flask")

# ----------------------------------------------------------------------
# Per-run steady-state analysis
# ----------------------------------------------------------------------
res = []
for label, bathT, rpm, log in RUNS:
    t = np.array([p[0] for p in log], float)
    pH = np.array([p[1] for p in log], float)
    Tr = np.array([p[2] for p in log], float)

    v0 = N_PUMPS * Qf(rpm)             # mL/s
    tau = V_REACTOR / v0 / 60.0        # min

    H = 10 ** (-pH)                    # mol/L
    X = H / C_A0                       # conversion
    C_out = C_A0 * (1 - X)             # outlet t-BC concentration

    pH_ss, T_ss = pH[-1], Tr[-1]
    X_ss = 10 ** (-pH_ss) / C_A0
    k = X_ss / (tau * (1 - X_ss))      # 1/min
    t_const = 1.0 / (1.0 / tau + k)    # approach-to-steady-state constant

    res.append(dict(label=label, bathT=bathT, rpm=rpm, t=t, pH=pH, Tr=Tr,
                    H=H, X=X, C_out=C_out, v0=v0, tau=tau, pH_ss=pH_ss,
                    T_ss=T_ss, X_ss=X_ss, k=k, t_const=t_const,
                    t_run=t[-1]))

print("\n" + "=" * 110)
print(f"ASSUMPTIONS: v0 = {N_PUMPS}*Qf,  C_A0 = {C_A0} M")
print("=" * 110)
hdr = (f"{'run':4}{'bath':>6}{'rpm':>5}{'T_rx':>7}{'v0':>8}{'tau':>8}"
       f"{'pH_ss':>7}{'[H+]':>9}{'X':>7}{'C_out':>8}{'k':>8}{'4*tc':>8}{'ran':>6}")
print(hdr)
print(f"{'':4}{'degC':>6}{'':5}{'degC':>7}{'mL/s':>8}{'min':>8}"
      f"{'':7}{'mol/L':>9}{'':7}{'mol/L':>8}{'1/min':>8}{'min':>8}{'min':>6}")
print("-" * 110)
for r in res:
    print(f"{r['label']:4}{r['bathT']:6}{r['rpm']:5}{r['T_ss']:7.1f}"
          f"{r['v0']:8.3f}{r['tau']:8.2f}{r['pH_ss']:7.2f}"
          f"{10**-r['pH_ss']:9.5f}{r['X_ss']:7.3f}"
          f"{C_A0*(1-r['X_ss']):8.5f}"
          f"{r['k']:8.4f}{4*r['t_const']:8.1f}{r['t_run']:6.0f}")

# ----------------------------------------------------------------------
# Arrhenius fit
# ----------------------------------------------------------------------
T_K = np.array([r['T_ss'] for r in res]) + 273.15
k_all = np.array([r['k'] for r in res])
inv_T = 1.0 / T_K
ln_k = np.log(k_all)

slope, intercept = np.polyfit(inv_T, ln_k, 1)
Ea = -slope * R_GAS / 1000.0
A_pre = np.exp(intercept)
r2 = np.corrcoef(inv_T, ln_k)[0, 1] ** 2

print("\n" + "=" * 62)
print("ARRHENIUS FIT  (all runs)")
print("=" * 62)
print(f"  Ea = {Ea:7.1f} kJ/mol")
print(f"  A  = {A_pre:.3e} 1/min")
print(f"  R2 = {r2:.4f}")

# ----------------------------------------------------------------------
# Plots
# ----------------------------------------------------------------------
colors = plt.cm.viridis(np.linspace(0, 0.85, len(res)))


def finish(ax, fname, legend=True):
    ax.grid(alpha=0.3)
    if legend:
        ax.legend(fontsize=8)
    ax.figure.tight_layout()
    ax.figure.savefig(fname, dpi=200)
    plt.close(ax.figure)


# 1. pH vs time
fig, ax = plt.subplots(figsize=(5.5, 3.8))
for r, c in zip(res, colors):
    ax.plot(r['t'], r['pH'], 'o-', color=c,
            label=f"{r['T_ss']:.1f} C, {r['rpm']} rpm")
ax.set_xlabel("Time [min]")
ax.set_ylabel("pH [-]")
finish(ax, "fig_pH_vs_time.png")

# 2. [H+] vs time
fig, ax = plt.subplots(figsize=(5.5, 3.8))
for r, c in zip(res, colors):
    ax.plot(r['t'], r['H'] * 1000, 'o-', color=c,
            label=f"{r['T_ss']:.1f} C, {r['rpm']} rpm")
ax.set_xlabel("Time [min]")
ax.set_ylabel(r"$[\mathrm{H}^+]$ [mmol/L]")
finish(ax, "fig_H_vs_time.png")

# 3. Conversion vs time
fig, ax = plt.subplots(figsize=(5.5, 3.8))
for r, c in zip(res, colors):
    ax.plot(r['t'], r['X'] * 100, 'o-', color=c,
            label=f"{r['T_ss']:.1f} C, {r['rpm']} rpm")
ax.set_xlabel("Time [min]")
ax.set_ylabel("Conversion X [%]")
finish(ax, "fig_X_vs_time.png")

# 4. Temperature vs conversion (steady state)
fig, ax = plt.subplots(figsize=(5.5, 3.8))
for rpm, mark in [(80, 'o'), (60, 's')]:
    sel = [r for r in res if r['rpm'] == rpm]
    if sel:
        ax.plot([r['T_ss'] for r in sel], [r['X_ss'] * 100 for r in sel],
                mark + '-', label=f"{rpm} rpm")
ax.set_xlabel("Reactor temperature [$^\\circ$C]")
ax.set_ylabel("Steady-state conversion X [%]")
finish(ax, "fig_T_vs_X.png")

# 5. Arrhenius
fig, ax = plt.subplots(figsize=(5.5, 3.8))
for rpm, mark in [(80, 'o'), (60, 's')]:
    sel = [r for r in res if r['rpm'] == rpm]
    if sel:
        ax.plot([1 / (r['T_ss'] + 273.15) for r in sel],
                [np.log(r['k']) for r in sel], mark, ms=7, label=f"{rpm} rpm")
xs = np.linspace(inv_T.min(), inv_T.max(), 50)
ax.plot(xs, slope * xs + intercept, 'k--',
        label=f"$E_a$={Ea:.0f} kJ/mol, $R^2$={r2:.3f}")
ax.set_xlabel("1/T [1/K]")
ax.set_ylabel(r"$\ln k$  [$\ln$(1/min)]")
finish(ax, "fig_arrhenius.png")

# ----------------------------------------------------------------------
# CSV for the appendix
# ----------------------------------------------------------------------
with open("re3_results.csv", "w") as f:
    f.write("run,bath_T_C,rpm,T_reactor_C,v0_mL_s,tau_min,pH_ss,"
            "H_molL,X,C_out_molL,k_per_min\n")
    for r in res:
        f.write(f"{r['label']},{r['bathT']},{r['rpm']},{r['T_ss']},"
                f"{r['v0']:.4f},{r['tau']:.3f},{r['pH_ss']},"
                f"{10**-r['pH_ss']:.6f},{r['X_ss']:.4f},"
                f"{C_A0*(1-r['X_ss']):.6f},{r['k']:.5f}\n")

print("\nWrote: re3_results.csv and 5 figures")
