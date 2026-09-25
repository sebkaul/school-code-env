import hashlib

# =============================================================================
# PART A: EQUILIBRIUM STAGE
# =============================================================================

def solve_equilibrium_stage(L_inert, G_inert, x_in, y_in, K):
    """
    Solves a single equilibrium stage.

    Inputs
    ------
    L_inert : inert liquid flowrate [kmol/h]
    G_inert : inert gas flowrate [kmol/h]
    x_in    : inlet liquid mole fraction
    y_in    : inlet gas mole fraction
    K       : equilibrium constant

    Outputs
    -------
    x_eq    : outlet liquid mole fraction
    y_eq    : outlet gas mole fraction
    """

    # ---- Step 1: Convert mole fractions to mole ratios:

    X_in = x_in/(1 - x_in)
    Y_in = y_in/(1 - y_in)

    # ------------

    # ---- Step 2: Combine solute component balance and equilibrium:
    # L' * X_in + G' * Y_in = L' * X_eq + G' * Y_eq
    # Y_eq = K * X_eq
    # to derive an expression for X_eq:

    X_eq = (L_inert*X_in + G_inert*Y_in)/(L_inert + K*G_inert)
    
    # ------------
    
    # ---- Step 3: Use X_eq to calculate Y_eq

    Y_eq = K * X_eq
    
    # ---- Step 4: Convert the equilibrium mole ratios back into mole fractions:

    x_eq = X_eq/(1 + X_eq)
    y_eq = Y_eq/(1 + Y_eq)

    # ------------

    return [x_eq, y_eq]


# =============================================================================
# EQUILIBRIUM STAGE: Testing if it works correctly
# =============================================================================

def test_solve_equilibrium_stage():
    G_in  = 150     # flow rate inlet gas [kmol/h]
    L_in  = 400     # flow rate inlet liquid [kmol/h]
    x_in  = 0       # mole fraction inlet liquid
    y_in  = 0.15    # mole fraction inlet gas
    K     = 0.893   # equilibrium constant

    G_inert = G_in*(1-y_in)
    L_inert = L_in*(1-x_in)

    [x_eq, y_eq] = solve_equilibrium_stage(L_inert, G_inert, x_in, y_in, K)

    print(f"x_eq = {x_eq:.5f}")
    print(f"y_eq = {y_eq:.5f}")


# Run this function to check if your implementation is correct
def check_implementation():
    [x,y] = solve_equilibrium_stage(1,2,0.01,0.2,1.5)
    solution_hash = "04bf1b8d0e45f910dcf1d74382226b39"
    answer_hash = hashlib.md5(str(round(x + y, 4)).encode()).hexdigest()
    #print(answer_hash); print(x + y)
    if answer_hash == solution_hash: print("Implementation looks good!\n")
    else: print("Implementation does not look complete yet\n")


if __name__ == "__main__":
    check_implementation()
    test_solve_equilibrium_stage()
