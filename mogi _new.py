# Implementation of the Mogi's Model

# Importing Packages
import numpy as np # Faster Arrays
import math # Mahtematical Expression
from matplotlib import pyplot as plt # Plotting


# Constant Declaration

G = 6.67*10**(-11) # Univeral Gravtiational Constant
M = 5.9742*10**(2) # Mass of the Anamoly [kg]
d = 10 # Depth of the Anamoly [m]

start  = -50.0 # Start point of the grid
end = 50.0 # End point of the grid
step = 0.5 # Step size
size = (end - start)/step # Declaration for the Array size



x_data = np.linspace(start,end,num=int(size))#|
                                             #| (x,y)
y_data = np.linspace(start,end,num=int(size))#|


# Removing Zero
for i in range(int(size)):
    if (x_data[i]*y_data[i] == 0):
        x_data[i] = 1e-6
        y_data[i] = 1e-6
         

x_1, y_1 = np.meshgrid(x_data, y_data) #| Mesh

r_data = np.empty([int(size), int(size)]) # Hold the r vector
g_data = np.empty([int(size), int(size)]) # Hold the accelearation anamoly

# Calculation
for i in range(int(size)):
    for j in range(int(size)):
        r_data[i][j] = (math. pow (math.sqrt(math.pow(x_1[i][j], 2) + math.pow(d, 2) + math.pow(y_1[i][j], 2)),3))
        g_data[i][j] = (G*M*d*10**(8))/(r_data[i][j]) 
        

# Plotting
fig = plt.figure()
ax = plt.axes(projection ='3d')

figure = ax.plot_surface(x_1, y_1, g_data, rstride=2, cstride=2,
                cmap='coolwarm', edgecolor='none')
fig.colorbar(figure)
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_zlabel(r"$\Delta g$")
ax.set_title('Gravitaional Anamoly using Mogi model')
fig.savefig('saved_figure-1000dpi.png', dpi = 600)
plt.show()


