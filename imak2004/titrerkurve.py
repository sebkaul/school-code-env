import numpy as np
import matplotlib.pyplot as plt

def titration_curve(conc_acid, pKa, conc_base=0.1, vol_acid=0.05):
    Kw = 1e-14
    Ka = 10**(-pKa)
    Kb = Kw / Ka
    
    n_acid = conc_acid * vol_acid
    V_eq = n_acid / conc_base
    
    Vb = np.linspace(0, 2 * V_eq, 1000)
    pH = np.zeros(len(Vb))
    
    for i, vb in enumerate(Vb):
        if vb == 0: # Før tilsats av base
            H3O = (-Ka + np.sqrt(Ka**2 + 4*Ka*conc_acid)) / 2
            pH[i] = -np.log10(max(H3O, Kw))

        elif vb < V_eq: # Før ekvivalenspunkt
            total_vol = vol_acid + vb
            cHA = (conc_acid * vol_acid - conc_base * vb) / total_vol
            cA_minus = (conc_base * vb) / total_vol
            H3O = (-(Ka + cA_minus) + np.sqrt((Ka + cA_minus)**2 + 4*Ka*cHA)) / 2
            pH[i] = -np.log10(max(H3O, Kw))

        elif abs(vb - V_eq) < 1e-10: # Ekvivalenspunkt
            total_vol = vol_acid + vb
            cA_minus = n_acid / total_vol
            OH = np.sqrt(Kb * cA_minus)
            pOH = -np.log10(max(OH, Kw))
            pH[i] = 14 - pOH
            
        else: # Etter ekvivalenspunkt
            OH_excess = conc_base * (vb - V_eq) / (vol_acid + vb)
            pOH = -np.log10(OH_excess)
            pH[i] = 14 - pOH
    
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.plot(Vb * 1000, pH, 'b-', linewidth=2)
    ax.axhline(y=7, color='gray', linestyle='--', alpha=0.5)
    ax.axvline(x=V_eq * 1000, color='red', linestyle='--', alpha=0.5, label=f'Equivalenspunkt ({V_eq*1000:.1f} mL)')
    
    ax.set_xlabel('Volum NaOH tilsatt (mL)', fontsize=12)
    ax.set_ylabel('pH', fontsize=12)
    ax.set_title(f'Titrerkurve: Svak syre (pKa={pKa}) mot sterk base', fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)
    ax.set_xlim(0, Vb[-1] * 1000)
    ax.set_ylim(0, 14)
    
    plt.tight_layout()
    plt.savefig('titration_curve.png', dpi=150)
    plt.show()
    #print(V_eq)

titration_curve(conc_acid=0.1, pKa=4.76)
print("Saved to titration_curve.png")
