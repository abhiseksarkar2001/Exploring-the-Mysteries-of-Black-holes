# -*- coding: utf-8 -*-
"""
Simulating the Path of a Photon Around a Black Hole using Null Geodesic Equations

@author: Abhisek Sarkar
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the null geodesic equations for a photon in the spacetime around a black hole
def null_geodesic_equations(y, t, mass):
    r, theta, phi, p_r, p_theta, p_phi = y
    dydt = [p_r, p_theta, p_phi, -mass/(r**2) + (mass*(p_theta**2 + p_phi**2))/(r**3), -p_r*p_theta/(r**2) - mass*np.cos(theta)/(r**3) + (mass*p_phi*np.cos(theta)*p_theta)/(r**4), -mass*np.sin(theta)*np.tan(phi)/(r**3) + (mass*p_phi*np.sin(theta)*p_theta)/(r**4)]
    return dydt

# Parameters for the black hole and the photon
mass = 1.0 # mass of the black hole in solar masses
y0 = [5.0, np.pi/2, 0, 0.1, 0.1, 0.1] # initial conditions for the photon
t = np.linspace(0, 100, 100000) # time values to solve the equations for

# Solve the null geodesic equations using the odeint function
solution = odeint(null_geodesic_equations, y0, t, args=(mass,), rtol=1e-9, atol=1e-9)

# Extract the position of the photon over time
r = solution[:, 0]
theta = solution[:, 1]
phi = solution[:, 2]

# Plot the path of the photon in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(r*np.sin(theta)*np.cos(phi), r*np.sin(theta)*np.sin(phi), r*np.cos(theta))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
