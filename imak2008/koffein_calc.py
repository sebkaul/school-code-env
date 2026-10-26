"""Koffein HPLC – ekstern + intern kalibrering. Fyll inn arealene og kjør: python koffein_calc.py"""
import numpy as np
import matplotlib.pyplot as plt

# ---------- FYLL INN ----------
C_std = np.array([5.0, 10.0, 20.0, 50.0])       # mg/L
A_caf = np.array([115.63114, 227.51530, 455.50916, 1122.18372])    # koffein, standarder
A_isA = np.array([572.28571, 569.05554, 566.91431, 564.41687])     # ISTD A, standarder
A_isB = np.array([1014.99231, 1055.32312, 1005.53278, 1128.69702]) # ISTD B, standarder

P_caf = np.array([346.18164, 355.05508, 336.47821])     # koffein, prøve 1-3 (0 = ikke kjørt ennå)
P_isA = np.array([562.77997, 530.76770, 567.64954])
P_isB = np.array([1135.69202, 2532.07935, 1146.96887])

DF = 10                                         # fortynningsfaktor
deklarert = 320                                 # mg/L  ← FRA BOKSEN: mg/100 mL × 10
names = {"A": "Paracetamol", "B": "4-Hydroxy Benzosyre"}
# ------------------------------

ok = P_caf > 0                                  # bruk bare prøver som er kjørt
P_caf, P_isA, P_isB = P_caf[ok], P_isA[ok], P_isB[ok]
n = ok.sum()

def fit(x, y):
    a, b = np.polyfit(x, y, 1)
    r2 = np.corrcoef(x, y)[0, 1] ** 2
    return a, b, r2

curves = {
    "Ekstern": (A_caf, P_caf, "Areal koffein"),
    names["A"]: (A_caf / A_isA, P_caf / P_isA, f"A_koffein / A_{names['A']}"),
    names["B"]: (A_caf / A_isB, P_caf / P_isB, f"A_koffein / A_{names['B']}"),
}

fig, axs = plt.subplots(1, 3, figsize=(13, 4))
for ax, (label, (y, ys, ylab)) in zip(axs, curves.items()):
    a, b, r2 = fit(C_std, y)
    print(f"\n{label}:  y = {a:.4g}x + {b:.4g}   R² = {r2:.4f}")
    xx = np.linspace(0, 55, 100)
    ax.plot(C_std, y, "o", label="Standarder")
    ax.plot(xx, a * xx + b, "-", label=f"y = {a:.3g}x + {b:.3g}\nR² = {r2:.4f}")
    if n:
        c_vial = (ys - b) / a                   # konsentrasjon i målt løsning
        c = c_vial * DF                         # konsentrasjon i drikken
        for i, (cv, cd) in enumerate(zip(c_vial, c), 1):
            print(f"  Prøve {i}: {cv:.2f} mg/L i vial → {cd:.1f} mg/L i drikk")
        line = f"  Snitt: {c.mean():.1f} mg/L"
        if n > 1:
            s = c.std(ddof=1)
            line += f" ± {s:.1f}   RSD = {s/c.mean()*100:.2f} %"
        line += f"   gjenfinning = {c.mean()/deklarert*100:.1f} %"
        print(line)
        ax.plot(c_vial, ys, "s", color="red", label="Prøver")
    ax.set(title=label, xlabel="Koffein (mg/L)", ylabel=ylab)
    ax.legend()
fig.tight_layout()
fig.savefig("kalibreringskurver.png", dpi=200)

print()
for nm, A in [(names["A"], A_isA), (names["B"], A_isB)]:
    print(f"ISTD-areal i standarder, {nm:<20} RSD = {A.std(ddof=1)/A.mean()*100:.2f} %")

# Rs: fyll inn tR og w½ (min)
def Rs(t1, w1, t2, w2):
    return 1.18 * (t2 - t1) / (w1 + w2)
# print(Rs(tR_caf, w_caf, tR_isA, w_isA))
