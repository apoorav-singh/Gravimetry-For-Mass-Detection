# This is the code for the prism

import numpy as np
from matplotlib import pyplot as plt

# Defining X-axis and Y-axis

# x = np.arange(-10,10,0.3) # [m]
# y = np.arange(-10,10,0.3) # [m]
x = np.arange(-10,10,0.3) # [m]
y = np.arange(-10,10,0.3) # [m]

# Surface where data is computed
z = 5 # [m]

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


figure_1, ax_1 = plt.subplots(1, 1,figsize=(10,10),subplot_kw=dict(projection='3d'))
ax_1.set_title(r'$g_x$')
ax_1.set_xlabel("X")
ax_1.set_ylabel("Y")
ax_1.set_zlabel("Gravity anomaly in mGal")
ax_1.plot_surface(xx, yy, gx1,  cmap='YlOrRd')

figure_2, ax_2 = plt.subplots(1, 1,figsize=(10,10),subplot_kw=dict(projection='3d'))
ax_2.set_xlabel("X")
ax_2.set_ylabel("Y")
ax_2.set_zlabel("Gravity anomaly in mGal")
ax_2.set_title(r'$g_y$')
ax_2.plot_surface(xx, yy, gy1,  cmap='YlOrRd')

figure_3, ax_3 = plt.subplots(1, 1,figsize=(10,10),subplot_kw=dict(projection='3d'))
ax_3.set_xlabel("X")
ax_3.set_ylabel("Y")
ax_3.set_zlabel("Gravity anomaly in mGal")
ax_3.set_title(r'$g_z$')
ax_3.plot_surface(xx, yy, gz1,  cmap='YlOrRd')

# Saving Values
save_valz = np.save("valz", gz1)
xx = np.save("xx", xx)
yy = np.save("yy", yy)

plt.show()