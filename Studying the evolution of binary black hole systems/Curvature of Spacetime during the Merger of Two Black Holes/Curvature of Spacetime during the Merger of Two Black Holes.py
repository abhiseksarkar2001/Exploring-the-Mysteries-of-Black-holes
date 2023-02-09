import numpy as np
import matplotlib.pyplot as plt

# Set up the grid for the simulation
N = 100
X, Y = np.meshgrid(np.linspace(-1, 1, N), np.linspace(-1, 1, N))

# Define the positions of the two black holes
x1, y1 = -0.5, 0.0
x2, y2 = 0.5, 0.0

# Define the mass of the two black holes
m1, m2 = 1.0, 1.0

# Define the velocity of the two black holes
vx1, vy1 = 0.0, 0.1
vx2, vy2 = 0.0, -0.1

# Compute the gravitational potential due to the two black holes
phi = -(m1 / np.sqrt((X - x1)**2 + (Y - y1)**2) +
        m2 / np.sqrt((X - x2)**2 + (Y - y2)**2))

# Add correction term to account for velocity of the black holes
phi += (m1 * (vx1 * (X - x1) + vy1 * (Y - y1)) +
        m2 * (vx2 * (X - x2) + vy2 * (Y - y2)))

# Plot the results
plt.imshow(phi, extent=(-1, 1, -1, 1), origin='lower')
plt.colorbar()

# Add a title to the plot
plt.title("Curvature of Spacetime during the Merger of Two Black Holes")

plt.show()
