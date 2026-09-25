import numpy as np, pandas as pd, matplotlib.pyplot as plt

# --- constants ---
M = {"C16:0":270.46,"C18:0":298.51,"C18:1":296.50,"C18:2":294.48,"C18:3":292.46}
M_SBO, RHO_SBO = 875.1, 0.913      # g/mol, g/mL
M_BIOD, RHO_BIOD = 291.5, 0.891
M_IST = 25.0                        # mg of C17:0 added to each sample
FAME = list(M)

# --- data: GC areas (group R3) ---
areas = pd.DataFrame({
    "C16:0":[2428.6,2610.5,2569.5,2768.2,2602.0,2813.5,2846.4,3031.1,3272.2,2996.2,3155.9,3422.1],
    "C17:0":[3693.3,3747.1,3639.1,3554.6,3551.1,3529.1,3793.7,3616.8,3686.0,3525.4,3573.3,3535.3],
    "C18:0":[6344.0,6972.8,6840.2,7331.6,6738.7,7317.1,7334.6,8160.8,8317.8,7973.0,8433.4,9007.4],
    "C18:1":[4849.1,4824.5,4962.6,5123.2,5635.2,5773.4,5925.9,6142.0,6315.1,6919.5,7070.7,7185.0],
    "C18:2":[7791.5,9009.6,8930.0,9798.8,8257.6,9377.7,9087.6,10065.0,10508.5,9394.1,9965.3,10926.1],
    "C18:3":[1835.0,1952.3,1786.1,2053.8,1797.1,1933.9,2040.0,2100.1,2263.1,2085.0,2278.2,2351.7]})

t = np.array([3,4,5,6,7,8,9,12,15,18,23,28], float)              # min
m_sample = np.array([0.2515,0.2535,0.2519,0.2515,0.2554,0.2511,  # g
                     0.2472,0.2591,0.2573,0.2613,0.2480,0.2571])

# --- GC weight fractions ---
area_tot = areas.sum(axis=1)
w_gc = areas.div(area_tot, axis=0)                  # %w/w as seen by GC
w_biod_gc = w_gc[FAME].sum(axis=1)

# --- IST scaling: real fractions ---
w_ist_r = M_IST / (m_sample*1000 + M_IST)           # per-sample, NOT fixed 10%
w_biod_r = w_biod_gc / w_gc["C17:0"] * w_ist_r
w_sbo_r = 1 - w_biod_r - w_ist_r

# --- masses, volumes, concentrations ---
m_biod = w_biod_r * m_sample                        # g
m_sbo = w_sbo_r * m_sample
V = m_sbo/RHO_SBO + m_biod/RHO_BIOD                 # mL
C_sbo = (m_sbo/M_SBO) / (V/1000)                    # mol/L

# --- conversion ---
n_sbo0 = m_sample / M_SBO
X = (n_sbo0 - m_sbo/M_SBO) / n_sbo0

# --- selectivity (mole basis) ---
n_fame = pd.DataFrame({c: (w_gc[c]/w_biod_gc)*m_biod/M[c] for c in FAME})
S = n_fame.div(n_fame.sum(axis=1), axis=0) * 100

out = pd.DataFrame({"t_min":t, "m_sample_g":m_sample, "w_IST_R":w_ist_r,
                    "w_BIOD_R":w_biod_r, "w_SBOunc":w_sbo_r,
                    "C_SBO_molL":C_sbo, "X":X}).join(S.add_prefix("S_"))
out.to_csv("re1_results.csv", index=False)
print(out.round(4).to_string(index=False))

# --- plots ---
C0 = RHO_SBO/M_SBO*1000                             # mol/L, pure SBO
for name, y, lab in [("conversion", X*100, "Conversion [%]"),
                     ("order0", C_sbo, r"$C_{SBO}$ [mol/L]"),
                     ("order1", np.log(C0/C_sbo), r"$\ln(C_{A0}/C_A)$ [-]"),
                     ("order2", 1/C_sbo - 1/C0, r"$1/C_A - 1/C_{A0}$ [L/mol]")]:
    fig, ax = plt.subplots(figsize=(5,3.5))
    ax.plot(t, y, "o")
    if name != "conversion":
        p = np.polyfit(t, y, 1); r2 = np.corrcoef(t, y)[0,1]**2
        ax.plot(t, np.polyval(p, t), "-", label=f"slope={p[0]:.3e}, $R^2$={r2:.4f}")
        ax.legend()
    ax.set_xlabel("Time [min]"); ax.set_ylabel(lab); fig.tight_layout()
    fig.savefig(f"{name}.png", dpi=200)

fig, ax = plt.subplots(figsize=(5,3.5))
for c in FAME: ax.plot(t, S[c], "o-", label=c)
ax.set_xlabel("Time [min]"); ax.set_ylabel("Selectivity [mol %]")
ax.legend(fontsize=8); fig.tight_layout(); fig.savefig("selectivity.png", dpi=200)
