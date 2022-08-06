import numpy as np
from matplotlib import pyplot as plt
from math import *


rho = 1e6 # [SI] Density
R = 10 # [SI] Radius of the anomaly
x_i = 1000
z_i = 100

# Anomaly is assumed to be spherical

# ----------------------------------------

# Anamoly Function 

def f_an(R, rho, x, z):
    G = 6.6743e-11 # [SI]
    # Universal Gravitational Constant
    C = (4/3)*G*pi*R**3*rho*z
    return C*(1/(x**2 + z**2)**1.5)

# ----------------------------------------

x = np.linspace(-300, 300, x_i) # One direction in a plane [x]
z = np.array([60])# np.linspace(0, 60, z_i) # Depth
g_v = np.empty([x.size])

# ----------------------------------------


for i in range(x.size):
    g_v[i] = f_an(R, rho, x[i], z)

plt.plot(x, g_v)
plt.grid(1)
plt.show()