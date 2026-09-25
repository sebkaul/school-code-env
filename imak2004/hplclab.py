import numpy as np
import matplotlib.pyplot as plt


def standardkurve(datasett):
    """
    datasett = liste med dict:
    [
        {"x": np.array([...]), "y": np.array([...]), "navn": "Uten inhibitor"},
        {"x": np.array([...]), "y": np.array([...]), "navn": "Med inhibitor"},
        ...
    ]
    """

    def lister(x, y):
        # Lineær regresjon y = a*x + b
        a, b = np.polyfit(x, y, 1)

        y_pred = a * x + b

        # R^2
        ss_res = np.sum((y - y_pred)**2)
        ss_tot = np.sum((y - np.mean(y))**2)
        r2 = 1 - (ss_res / ss_tot)

        # Krysningspunkter
        x_cross = -b / a
        y_cross = b

        return a, b, x_cross, y_cross, r2


    plt.figure()

    # Finn felles x-område
    x_min = min(d["x"].min() for d in datasett if len(d["x"]) > 0)
    x_max = max(d["x"].max() for d in datasett if len(d["x"]) > 0)

    x_fit = np.linspace(x_min, x_max, 300)

    print("===== RESULTATER =====\n")

    # Gå gjennom alle datasett
    for i, d in enumerate(datasett):
        x = d["x"]
        y = d["y"]
        navn = d["navn"]

        if len(x) == 0 or len(y) == 0:
            continue

        # Regresjon
        a, b, x_cross, y_cross, r2 = lister(x, y)

        # Linjer
        y_fit = a * x_fit + b
        x_extra = np.linspace(x_max, x_cross, 150)
        y_extra = a * x_extra + b

        # Plot datapunkter
        plt.scatter(x, y, label=navn)

        # Plot regresjonslinje
        plt.plot(x_fit, y_fit, label=f"{navn} (a = {a:.4f}, R² = {r2:.4f})")

        # Ekstrapolasjon
#         plt.plot(x_extra, y_extra, linestyle="--")

        # Krysningspunkter
#         plt.scatter(x_cross, 0, zorder=3,
#                     label=f"x-aksekryssing ({navn}) = {x_cross:.4f}")
#         plt.scatter(0, y_cross, zorder=3,
#                     label=f"y-aksekryssing ({navn}) = {y_cross:.4f}")

        # Skriv numeriske verdier
        print(f"--- {navn} ---")
        print(f"Stigningstall a = {a}")
        print(f"x-kryssing = {x_cross}")
        print(f"y-kryssing = {b}")
        print(f"R² = {r2}\n")


    # Akser ved null
    plt.axhline(0, linewidth=1)
    plt.axvline(0, linewidth=1)

    # Aksetekst
    plt.xlabel("x, Konsentrasjon [mg/L]")
    plt.ylabel("y, Areal [mAU*s]")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()



# =======================
# EKSEMPEL PÅ BRUK
# =======================

datasett = [
    {
        "x": np.array([5, 10, 15, 20]), # Konsentrasjon
        "y": np.array([83.99, 168.14, 252.74, 338.75]), # Areal
        "navn": "Koffein"
    },
    {
        "x": np.array([5, 10, 20, 30]), # Konsentrasjon
        "y": np.array([84.43, 132.26, 263.74, 376.36]), # Areal
        "navn": "Acesulfam K"
    }
]

standardkurve(datasett)

