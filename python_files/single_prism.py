# This is the code for the prism

import numpy as np
from matplotlib import pyplot as plt

# Defining X-axis and Y-axis

x = np.arange(-10,10,0.1) # [m]
y = np.arange(-10,10,0.1) # [m]

# Surface where data is computed
z = 3 # [m]

# Density
d = 11.11 # [g/cc]

# Mesh
[xx, yy] = np.meshgrid(x, y)
A = 1e-3 # [m] to [km]

# Definig parameters for Prism model
x_pos = np.array([0, 2]) # [FirstCorner SecondCorner]
y_pos = np.array([0, 2]) # [FirstCorner SecondCorner]
z_pos = np.array([0, 2]) # [FirstCorner SecondCorner]

G = 6.67384e-3;   # Define Gravitational constant
c = G*d;  # multiplication of gravitational constant and density 

gz1 = np.empty(xx.shape)
gy1 = np.empty(xx.shape)
gx1 = np.empty(xx.shape)

for i in range(x_pos.size):
    for j in range(y_pos.size):
        for k in range(z_pos.size):
            r = ((xx-x_pos[i])**2 + (yy-y_pos[j])**2 + (z-z_pos[k])**2)**0.5;
            if (i+j+k)%2 == 0:
                s = -1
            else:
                s = 1
            gz = c*s*(((z-z_pos[k])*np.arctan(((xx-x_pos[i])*(yy-y_pos[j]))/((z-z_pos[k])*r))) - ((xx-x_pos[i])*np.log(r+(yy-y_pos[j])))-((yy-y_pos[j])*np.log(r+xx-x_pos[i])));
            gy = -c*s*((yy-y_pos[j]+0.01)*np.arctan(((z-z_pos[k])*(xx-x_pos[i]))/(((yy-y_pos[j]+0.01)*r))) - ((z-z_pos[k])*np.log(r+xx-x_pos[i])+(xx-x_pos[i])*np.log(r+z-z_pos[k])));
            gx = c*s*(((xx-x_pos[i])*np.arctan(((yy-y_pos[j]+0.01)*(z-z_pos[k]))/(((xx-x_pos[i])*r))) - ((yy-y_pos[j]+0.01)*np.log(r+(z-z_pos[k])))-((z-z_pos[k])*np.log(r+yy-y_pos[j]+0.01))));
            gz1 = gz1 + gz;
            gy1 = gy1 + gy;
            gx1 = gx1 + gx;


figure, ax = plt.subplots(1, 3,figsize=(10,10),subplot_kw=dict(projection='3d'))
# ax[0][0].set_title('Gx')
ax[0].plot_surface(A*xx, A*yy, gx1,  cmap='YlOrRd')

# ax[0][1].set_title('Gy')
ax[1].plot_surface(A*xx, A*yy, gy1,  cmap='YlOrRd')

# ax[0][2].set_title('Gz')
ax[2].plot_surface(A*xx, A*yy, gz1,  cmap='YlOrRd')

# Saving Values
save_valz = np.save("valz", gz1)
xx = np.save("xx", xx)
yy = np.save("yy", yy)

plt.show()