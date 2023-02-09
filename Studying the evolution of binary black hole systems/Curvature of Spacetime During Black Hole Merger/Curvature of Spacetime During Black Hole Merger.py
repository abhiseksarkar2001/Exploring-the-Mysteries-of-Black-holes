import numpy as np
import matplotlib.pyplot as plt

def evolve_spacetime(grid_size, time_step, num_steps):
    # Initialize the spacetime grid
    spacetime = np.zeros((grid_size, grid_size, num_steps))
    
    # Set initial conditions for the two black holes
    initial_black_hole_positions = np.zeros((grid_size, grid_size))
    initial_black_hole_positions[grid_size//4, grid_size//4] = 1.0
    initial_black_hole_positions[3*grid_size//4, 3*grid_size//4] = 1.0
    spacetime[:,:,0] = initial_black_hole_positions
    
    for t in range(1, num_steps):
        # Evolve the spacetime grid using finite difference method
        spacetime[:,:,t] = spacetime[:,:,t-1] + time_step * spacetime_derivative(spacetime[:,:,t-1])
        
    return spacetime

def spacetime_derivative(spacetime):
    # Compute the derivative of the spacetime grid using finite difference method
    spacetime_derivative = np.zeros_like(spacetime)
    spacetime_derivative[1:-1, 1:-1] = (spacetime[2:, 1:-1] - spacetime[:-2, 1:-1]) / 2.0
    
    return spacetime_derivative

grid_size = 100
time_step = 0.01
num_steps = 1000
spacetime = evolve_spacetime(grid_size, time_step, num_steps)

# Plot the final spacetime grid
plt.imshow(spacetime[:,:,num_steps-1], cmap='gray')
plt.title("Curvature of Spacetime During Black Hole Merger")
plt.show()

