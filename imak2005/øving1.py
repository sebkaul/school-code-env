import numpy as np
import matplotlib.pyplot as plt


def lineweaver_burk_plot(datasett):
    """
    datasett = liste med dict:
    [
        {"x": np.array([...]), "y": np.array([...]), "navn": "Uten inhibitor"},
        {"x": np.array([...]), "y": np.array([...]), "navn": "Med inhibitor"},
        ...
    ]
    """

    def lineweaver_burk(x, y):
        # Lineær regresjon y = a*x + b
        a, b = np.polyfit(x, y, 1)

        # Krysningspunkter
        x_cross = -b / a        # = -1 / K_M
        y_cross = b            # = 1 / V_max

        return a, b, x_cross, y_cross


    plt.figure()

    # Finn felles x-område
    x_min = min(d["x"].min() for d in datasett)
    x_max = max(d["x"].max() for d in datasett)

    x_fit = np.linspace(x_min, x_max, 300)

    print("===== RESULTATER FRA LINEWEAVER–BURK =====\n")

    # Gå gjennom alle datasett
    for i, d in enumerate(datasett):
        x = d["x"]
        y = d["y"]
        navn = d["navn"]

        # Regresjon
        a, b, x_cross, y_cross = lineweaver_burk(x, y)

        # Linjer
        y_fit = a * x_fit + b
        x_extra = np.linspace(x_max, x_cross, 150)
        y_extra = a * x_extra + b

        # Plot datapunkter
        plt.scatter(x, y, label=navn)

        # Plot regresjonslinje
        plt.plot(x_fit, y_fit, label=f"{navn} (a = {a:.4f})")

        # Ekstrapolasjon
        plt.plot(x_extra, y_extra, linestyle="--")

        # Krysningspunkter
        plt.scatter(x_cross, 0, zorder=3,
                    label=f"-1/K_M ({navn}) = {x_cross:.4f}")
        plt.scatter(0, y_cross, zorder=3,
                    label=f"1/V_max ({navn}) = {y_cross:.4f}")

        # Skriv numeriske verdier
        print(f"--- {navn} ---")
        print(f"Stigningstall a = {a} (K_M / V_max)")
        print(f"x-kryssing = {x_cross}  (-1 / K_M)")
        print(f"y-kryssing = {b}  (1 / V_max)\n")


    # Akser ved null
    plt.axhline(0, linewidth=1)
    plt.axvline(0, linewidth=1)

    # Aksetekst
    plt.xlabel("x, 1/[S]")
    plt.ylabel("y, 1/V")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()



# =======================
# EKSEMPEL PÅ BRUK
# =======================

datasett = [
    {
        "x": 1 / np.array([1, 2, 4, 8]),
        "y": 1 / np.array([1.3, 2.0, 2.8, 3.5]),
        "navn": "Uten inhibitor"
    },
    {
        "x": 1 / np.array([1, 2, 4, 8]),
        "y": 1 / np.array([0.8, 1.2, 1.7, 2.2]),
        "navn": "Med inhibitor"
    }
]

lineweaver_burk_plot(datasett)
