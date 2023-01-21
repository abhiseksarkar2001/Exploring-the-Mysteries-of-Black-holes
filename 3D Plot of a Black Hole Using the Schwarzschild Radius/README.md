# 3D Plot of a Black Hole Using the Schwarzschild Radius
This code generates a 3D plot of a black hole using the Schwarzschild radius, which is a fundamental concept in the study of black holes. The code is based on the theory of general relativity and uses the 'mpl_toolkits.mplot3d.art3d.Poly3DCollection' class to create a 3D sphere that represents the black hole.

## Requirements
* Python 3
* Numpy
* Matplotlib

## Usage
Clone the repository and run the code using python.
git clone [https://github.com/abhiseksarkar2001/3d-black-hole-plot.git
cd 3d-black-hole-plot
python3 black_hole_plot.py](https://github.com/abhiseksarkar2001/Exploring-the-Mysteries-of-Black-holes/blob/main/3D%20Plot%20of%20a%20Black%20Hole%20Using%20the%20Schwarzschild%20Radius/3D%20Plot%20of%20a%20Black%20Hole%20Using%20the%20Schwarzschild%20Radius.py)

## Parameters
The mass of the black hole is defined as 1 solar mass, and the Schwarzschild radius is calculated using the mass of the black hole and the gravitational constant. The shape of the black hole is defined as a sphere with a radius equal to the Schwarzschild radius. A 3D sphere is created using 'mpl_toolkits.mplot3d.art3d'.'Poly3DCollection' class to create the 3D sphere. Then it is plotted on 3D plot using the 'add_collection' method of the 3D axes object. The transparency of the sphere is controlled using the alpha parameter and the color of the sphere is set using the color parameter. The limits of the plot are set to -rs to rs for all the axis, this will make the sphere to be plottedParameters
