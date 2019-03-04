#Solution to Problem-10
#Import packages matploylib and numpy
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


#Set the functions so f(x), f(x**2) and f(2**x) and the x axis length up to 4 (Need to check this)
x = np.arange(0.0, 4.5, 0.5)
z = x
y = x**2
dy = 2**x

# Plot functions f(x), f(x**2) and f(2**x)
plt.plot(x, z)
plt.plot(x, y)
plt.plot(x, dy)
#Add a piont of intersection at (2, 4) and added a Blue circle to mark the intersection
plt.plot(2, 4, 'bo')

# Add title, and labels for x and y axis
plt.title('Hopefully the solution to problem 10...')
plt.xlabel('X or Horizontal axis')
plt.ylabel('Y or Vertical axis')

#Add grid lines True for yes and False for no
plt.grid(True)
#Add legends and placed the location in top left
plt.legend(['y = x', 'y = x^2', 'y = 2^x'], loc='upper left')

# Show the graph
plt.show()