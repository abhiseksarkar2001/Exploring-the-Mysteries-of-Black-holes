# -*- coding: utf-8 -*-
"""
3D visualization of a particle's path around a black hole

@author: Abhisek
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the equations of motion for a particle in the spacetime
# around a black hole
def equations_of_motion(y, t, mass):
    r, theta, phi, p_r, p_theta, p_phi = y
    dydt = [p_r, p_theta, p_phi, -mass/(r**2), -p_r*p_theta/(r**2), 0]
    return dydt

# Parameters for the black hole and the particle
mass = 1.0 # mass of the black hole in solar masses
y0 = [8.0, np.pi/2, 0, 0.1, 0.1, 0.1] # initial conditions for the particle
t = np.linspace(0, 100, 100000) # time values to solve the equations for

# Solve the equations of motion using the odeint function
solution = odeint(equations_of_motion, y0, t, args=(mass,))

# Extract the position of the particle over time
r = solution[:, 0]
theta = solution[:, 1]
phi = solution[:, 2]

# Plot the path of the particle in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(r*np.sin(theta)*np.cos(phi), r*np.sin(theta)*np.sin(phi), r*np.cos(theta))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
