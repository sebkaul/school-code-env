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

        # Krysningspunkter
        x_cross = -b / a
        y_cross = b
        return a, b, x_cross, y_cross


    plt.figure()

    # Finn felles x-område
    x_min = min(d["x"].min() for d in datasett)
    x_max = max(d["x"].max() for d in datasett)

    x_fit = np.linspace(x_min, x_max, 300)

    print("===== RESULTATER =====\n")

    # Gå gjennom alle datasett
    for i, d in enumerate(datasett):
        x = d["x"]
        y = d["y"]
        navn = d["navn"]

        # Regresjon
        a, b, x_cross, y_cross = lister(x, y)

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
                    label=f"x-aksekryssing = {x_cross:.4f}")
        plt.scatter(0, y_cross, zorder=3,
                    label=f"y-aksekryssing = {y_cross:.4f}")

        # Skriv numeriske verdier
        # print(f"--- {navn} ---")
        print(f"Gjennomsnittsverdier: {y}")
        print(f"Stigningstall a = {a}")
        print(f"x-kryssing = {x_cross}")
        print(f"y-kryssing = {b} \n")


    # Akser ved null
    plt.axhline(0, linewidth=1)
    plt.axvline(0, linewidth=1)

    # Aksetekst
    plt.xlabel("Konsentrasjon (mg/mL)")
    plt.ylabel("Absorbans")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()



# =======================
# EKSEMPEL PÅ BRUK
# =======================

datasett = [
    {
        "x": np.array([0.2, 0.4, 0.6, 0.8, 1.0]),
        "y": np.array([((0.229 + 0.176)/2), ((0.442 + 0.399)/2), ((0.627 + 0.548)/2), (0.785 + 0.762)/2, ((0.970 + 0.918)/2)]),
        "navn": "Gjennomsnitt av standard 1 og 2"
    }
]

standardkurve(datasett)
