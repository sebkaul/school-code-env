from scipy.integrate import tplquad
import numpy as np

f = lambda rho, phi, theta : rho**2 * np.sin(phi)

theta0 = 0
theta1 = np.pi/4
#r0 = 0
#r1 = 1
#z0 = lambda theta, r: -r
#z1 = lambda theta, r: r
phi0 = np.pi/4
phi1 = 3/4 * np.pi
rho0 = 0
rho1 = lambda theta, phi : 1/(np.sin(phi))

#polar = dblquad(f * r, theta, r)
#cylindrical = tplquad(f, theta0, theta1, r0, r1, z0, z1)
spherical = tplquad(f, theta0, theta1, phi0, phi1, rho0, rho1)

#print(polar)
#print(cylindrical)
print(spherical)

