from column import solve_column
import matplotlib.pyplot as plt

def main():
    G_in  = 100     # flow rate inlet gas [kmol/h]
    L_in  = 120     # flow rate inlet liquid [kmol/h]
    x_in  = 0.001   # mole fraction inlet liquid
    y_in  = 0.20    # mole fraction inlet gas
    n_st  = 5       # number of stages
    K     = 1.5
    tolerance = 1e-4
    max_iterations = 1000

    [L, G, x, y, converged] = solve_column(L_in, G_in, x_in, y_in, K, n_st, tolerance, max_iterations)

    if not converged:
        # Checking if a solution was found
        print("The calculation did not converge; Try increasing the maximum number of iterations")
        return

    # Plotting the results
    xplot = list(range(0, n_st + 1))
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))
    ax1.plot(xplot,x,label='x (liquid)')
    ax1.plot(xplot,y,label='y (gas)')
    ax1.legend()
    ax1.set(xlabel="Stage number \n (top   ---->   bottom)", ylabel="Mole fraction of A")

    ax2.plot(xplot,L,label='L (liquid)')
    ax2.plot(xplot,G,label='G (gas)')
    ax2.legend()
    ax2.set(xlabel="Stage number \n (top   ---->   bottom)", ylabel="Flow rate [kmol/h]")

    # Use this if you want to save the plots
    fig.savefig("plot.png")


    print(f"\nGas outlet (y[0]) = {y[0]:.4f}")
    print(f"Requirement      : y[0] <= 0.025")
    print("PASS" if y[0] <= 0.025 else "FAIL")    

    plt.show()


if __name__ == "__main__":
    main()

