import scipy.optimize

def coffein_extraction(unknowns):
    # Variables
    m3koff, m4koff, w3vann = unknowns
    
    # Inlet
    m1koff = 0.070
    m1vann = 100

    m2dkm = 50

    m1tot = m1vann + m1koff
    m2tot = m2dkm

    # Outlet
    m3vann = m1vann

    m4dkm = m2dkm

    w4dkm = 0.999
    w4koff = 0.001

    m4tot = m4koff + m4dkm
    m3tot = m3vann + m3koff


    w3koff = 1 - w3vann
    w1vann = (m1vann)/(m1tot)
    w1koff = (m1koff)/(m1tot)

    
    # Mass balances
        # Totalmassebalanse
    f1 = m1tot + m2tot - m3tot - m4tot
        #  Koffein komponentbalanse
    f2 = m1tot * w1koff - (m3tot * w3koff + m4tot * w4koff)

        #  Vann komponentbalanse
    f3 = m1tot * w1vann - (m3tot * w3vann)

    return(f1, f2, f3)

guesses = [0.07, 0.07, 1]
solution = scipy.optimize.root(coffein_extraction, guesses)
m3koff, m4koff, w3vann = solution.x
print(f"m3koff = {m3koff:.6f}")
print(f"m4koff = {m4koff:.6f}")
print(f"w3vann = {w3vann:.6f}")
