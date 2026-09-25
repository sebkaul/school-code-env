import scipy.optimize

def sulphur_filtration(unknowns):
    # Variables
    m2, x2S, m3, m4, m5, m6 = unknowns
    
    # Inlet
    x1S = 0.050
    x1W = 1 - x1S
    m1 = 1.3

    # Outlet
    x3W = 1.0
    x5S = 1.0

    # Middle
    x4S = 0.600
    x4W = 1 - x4S

    x6S = 0.200
    x6W = 1 - x6S

    
    # Mass balances
        # Kontrollvolum 1
    f1 = m1 - m3 - m5
    f2 = m1 * x1S - m5 * x5S

        # Kontrollvolum 2
    f3 = m4 - m5 - m6
    f4 = m4 * x4W - m6 * x6W

        # Kontrollvolum 3
    f5 = m1 + m6 - m2
    f6 = m1 * x1S + m6 * x6S - m2 *x2S


    return(f1, f2, f3, f4, f5, f6)

guesses = [1, 1, 1, 1, 1, 1]
solution = scipy.optimize.root(sulphur_filtration, guesses)
m2, x2S, m3, m4, m5, m6 = solution.x
print(f"m2 = {m2:.6f}")
print(f"x2S = {x2S:.6f}")
print(f"m3 = {m3:.6f}")
print(f"m4 = {m4:.6f}")
print(f"m5 = {m5:.6f}")
print(f"m6 = {m6:.6f}")

