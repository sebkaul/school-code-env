import numpy as np
import hashlib

from equilibrium import solve_equilibrium_stage

# =============================================================================
# PART B - ABSORPTION COLUMN
# =============================================================================

def solve_column(L_in, G_in, x_in, y_in, K, N, tolerance=1e-4, max_iterations=1000):
    """
    A column is made up of several "stages" stacked one after another.
    At each stage, the liquid (x) and gas (y) mole fractions move toward
    equilibrium with each other.
    
    This script first guesses the mole fraction at each stage. Then it calls 
    solve_equilibrium_stage() once per stage to calculate the equilibrium and
    the mole fractions in the liquid and gas leaving that stage. After this,
    these mole fractions are then set as the new guess. As soon as the values 
    stop changing more than a small amount (the "tolerance"), we are done and 
    the  column has "converged"

    Inputs
    ------
    L_in        : inlet liquid flow [kmol/h]
    G_in        : inlet gas flow [kmol/h]
    x_in        : inlet liquid mole fraction
    y_in        : inlet gas mole fraction
    K           : equilibrium constant
    N           : number of stages
    tolerance   : how small the change between two iterations must be to call it "converged"
    max_iterations

    Outputs
    -------
    L       : Liquid flow rates [kmol/h] list: [0 .. N]
    G       : Gas flow rates [kmol/h] list: [0 .. N]
    x       : liquid mole fraction list: [0 .. N]
    y       : gas mole fraction list: [0 .. N]

    Liquid direction:
      top  ->                      bottom
      x[0] -> x[1] -> x[2] -> ... -> x[N]

    Gas direction:
      top                      <-  bottom
      y[0] <- y[1] <- y[2] <- ... <- y[N]

    Known:
        x[0] = x_in 
        y[N] = y_in
    """

    # ---- Step 1: Calculate inert flows:

    L_inert = (1 - x_in)*L_in 
    G_inert = (1 - y_in)*G_in

    # ------------

    # Start with simple guesses.
    # Every liquid mole fraction is guessed equal to the liquid feed value.
    # Every gas mole fraction is guessed equal to the gas feed value.
    x_guess = np.full((N + 1), x_in)
    y_guess = np.full((N + 1), y_in)

    converged = False  # To track if a solution is found
    
    # Start iterating
    for iteration in range(max_iterations + 1):
        # Create new arrays for the equilibrium mole fractions that we will calculate this iteration
        x_new = np.copy(x_guess)
        y_new = np.copy(y_guess)

        for n in range(0, N):  # The stage increases from n -> [0 .. n .. N]

            # ---- Step 2: Specify the mole fraction guess in the liquid and gas entering stage n

            x_in_stage = x_guess[n]
            y_in_stage = y_guess[n+1]

            # ------------

            # Solving the stage to calculate the mole fractions at equilibrium.
            [x_eq, y_eq] = solve_equilibrium_stage(L_inert, G_inert, x_in_stage, y_in_stage, K)

            # ---- Step 3: Saving the mole fractions of the streams exiting the stage (at equilibrium)

            x_new[n+1] = x_eq
            y_new[n] = y_eq

            # ------------

        # We find the largest relative change in any mole fraction between the old and new results.
        largest_relative_x_change = np.max(np.abs(x_new - x_guess) / x_guess)
        largest_relative_y_change = np.max(np.abs(y_new - y_guess) / y_guess)
        largest_relative_change = np.max([largest_relative_x_change, largest_relative_y_change])
        
        # If the largest change is small enough, a solution is found (converged).
        if largest_relative_change < tolerance:
            print(f"Solved! After {iteration} iterations")
            converged = True
            break  # Exit the for-loop

        # Otherwise, update the guess with the new mole fractions
        x_guess = x_new
        y_guess = y_new


    # ---- Step 4: Calculate the total flow rates in the column using the inert ones.

    L = L_inert/(1 - x_new)
    G = G_inert/(1 - y_new)

    # ------------

    return [L, G, x_new ,y_new, converged]


# =============================================================================
# COLUMN: Testing if it works correctly
# =============================================================================

# Run this function to check if your implementation is correct
def check_implementation():
    [_,_,x,y,_] = solve_column(50,40,0.01,0.1,0.8,10,1e-4,100)
    solution_hash = "6c7370745a084de84936676cf1967566"
    answer_hash = hashlib.md5(str(round(x[-1] + y[0], 4)).encode()).hexdigest()
    #print(answer_hash); print(x[-1], y[0], x[-1] + y[0])
    if answer_hash == solution_hash: print("Implementation looks good!\n")
    else: print("Implementation does not look complete yet\n")


if __name__ == "__main__":
    check_implementation()
