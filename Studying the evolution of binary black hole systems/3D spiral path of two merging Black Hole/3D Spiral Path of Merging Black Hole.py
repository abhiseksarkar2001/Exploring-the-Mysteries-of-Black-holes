import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters for the black holes
mass_1 = 10**6
mass_2 = 10**6
separation = 1
G = 6.67430 * 10**-11 # Gravitational constant

# Define the number of points to plot
N = 10000

# Calculate the gravitational force
def grav_force(m1, m2, r):
    return G * m1 * m2 / r**2

# Generate the 3D spiral path for the first black hole
t = np.linspace(0, 50, N)
r = separation / 2 * np.exp(-t/10)
x1 = r * np.sin(t)
y1 = r * np.cos(t)
z1 = t

# Generate the 3D spiral path for the second black hole
x2 = -x1
y2 = -y1
z2 = z1

# Plot the two merging spiral paths
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x1, y1, z1, 'red')
ax.plot(x2, y2, z2, 'blue')

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Spiral Path of Merging Black Holes')

# Show the plot
plt.show()

