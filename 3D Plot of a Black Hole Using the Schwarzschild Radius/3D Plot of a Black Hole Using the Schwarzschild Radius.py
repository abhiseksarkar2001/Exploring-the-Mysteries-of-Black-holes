# -*- coding: utf-8 -*-
"""
3D Plot of a Black Hole Using the Schwarzschild Radius

@author: Abhisek Sarkar
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Parameters for the black hole
mass = 1.0 # mass of the black hole in solar masses

# Calculate the Schwarzschild radius of the black hole
rs = 2*mass*6.67e-11*2e30/(3e8)**2

# Define the shape of the black hole in 3D space
# Create spherical coordinates
u, v = np.linspace(0, 2 * np.pi, 100), np.linspace(0, np.pi, 100)
# Create the x, y, and z coordinates of the sphere
x = rs * np.outer(np.cos(u), np.sin(v))
y = rs * np.outer(np.sin(u), np.sin(v))
z = rs * np.outer(np.ones(np.size(u)), np.cos(v))

# Create a figure and axes for the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the black hole shape
ax.add_collection(Poly3DCollection([list(zip(x.flatten(), y.flatten(), z.flatten()))], alpha=.25, color='black'))

# Set the plot limits and labels
ax.set_xlim([-rs, rs]) # set limit to the radius of the black hole sphere
ax.set_ylim([-rs, rs]) # set limit to the radius of the black hole sphere
ax.set_zlim([-rs, rs]) # set limit to the radius of the black hole sphere
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()

