# This code is computational adaptation of the model mentioned in the 
# Text by POTENTIAL THEORY IN GRAVITY AND MAGNETIC APPLICATIONS by Richard J. Blakely

# Garvity anamoly modelling using  

import numpy as np 
from matplotlib import pyplot as plt # Plotting
from tqdm import tqdm
np.seterr(divide = 'ignore') 


G = 6.673e-4 # Universal Gravitational Constant
E = 2.67 # Geological Density
C = G*E # Multiplication of gravitational constant and density
A = 1e-3 # Unit Conversion from m to Km
B = 10000 # Unit Conversion from mGal/Km to E



# Importing Data Frame

df_2 = np.genfromtxt("terrain.txt", dtype=float, encoding=None, delimiter=",")

# Length of the Array
L = np.array(df_2.shape)
L[0] = L[0] - 1
L[1] = L[1] - 1

foo_x = df_2[0:L[0], 0]
foo_y = df_2[0:L[0], 1]
foo_z = df_2[0:L[0], 2]

X = np.sort(np.unique(foo_x))
Y = np.sort(np.unique(foo_y))
Z = np.empty([X.size, Y.size])
i = 0

X_iter = np.array(np.mgrid[0:X.size])
Y_iter = np.array(np.mgrid[0:Y.size])
Z_iter = np.array(np.mgrid[0:foo_z.size])

# f = open("sorted_terrain.txt", "w")

for i_x in tqdm(X_iter):
    for i_y in Y_iter:
        for i_fx in Z_iter:
            if (X[i_x] == foo_x[i_fx] and Y[i_y] == foo_y[i_fx] ):
                Z[i_x, i_y] = foo_z[i_fx]
                # print(foo_z[i_z])
            else:
                continue

# for i_x in X_iter:
#     for i_y in Y_iter:
#          f.write("{}, {}, {} \n".format(X[i_x], Y[i_y], Z[i_x, i_y]))


# f.close()
# print(X)

# Computing number of Prisms used in the system
print("Number of Prism in the simulation: ", X.size*Y.size)

[xx ,yy] = np.meshgrid(X, Y)
# xx = np.transpose(xx)
# yy = np.transpose(yy)

Z = np.transpose(Z)

# #Plotting
fig = plt.figure()
ax = plt.axes(projection ='3d')

figure = ax.plot_surface(xx, yy, Z, cmap='PuBuGn')

# plt.show()

print("Define the observation plane in terms of z for example: 20 and bottom of the prism -10000")
z = 20 # float(input("Enter Z-Plane: "))
q = -10000 # float(input("Enter bottom of the prism: "))

x_pos = np.array([0, 0])
y_pos = np.array([0, 0])
z_pos = np.array([0, 0])

# Generating r array
r = np.empty([X_iter.ndim, Y_iter.ndim])
valuez = np.empty([X_iter.ndim, Y_iter.ndim])
# valuezz = np.empty([X_iter.ndim, Y_iter.ndim])
# gzz = np.empty([X_iter.ndim, Y_iter.ndim])
valz = np.empty([X_iter.ndim, Y_iter.ndim])
foo_gzz1 = np.empty([X_iter.ndim, Y_iter.ndim])
foo_gzz2 = np.empty([X_iter.ndim, Y_iter.ndim])
foo_gzz3 = np.empty([X_iter.ndim, Y_iter.ndim])



for i_x in tqdm(X_iter[:-1]):
    for i_y in Y_iter[:-1]:
        x_pos[0] = X[i_x]
        x_pos[1] = X[i_x + 1]
        y_pos[0] = Y[i_y]
        y_pos[1] = Y[i_y + 1]
        z_pos[0] = Z[i_y, i_x]
        z_pos[1] = q

        for i_xx in [0, 1]:
            for i_yy in [0, 1]:
                for i_zz in [0, 1]:
                    xx1 = (xx - x_pos[i_yy])**2
                    yy1 = (yy - y_pos[i_xx])**2
                    zz1 = (z - z_pos[i_zz])**2
                    r = np.sqrt(xx1 + yy1 + zz1)
                    if ((i_xx + i_yy + i_zz)%2 == 0):
                        s = 1
                    else:
                        s = -1
                        
                    foo_gzz1 = (z - z_pos[i_zz])*np.arctan((xx - x_pos[i_yy])*(yy - y_pos[i_xx])/ (r*(z - z_pos[i_zz])))
                    foo_gzz2 = (xx - x_pos[i_yy])*np.log((r + (yy - y_pos[i_xx])))
                    foo_gzz3 = (yy - y_pos[i_xx])*np.log(r + (xx - x_pos[i_yy]))
                    valuez = C*s*(foo_gzz1 - foo_gzz2 - foo_gzz3)
                    
                    if (np.isnan(foo_gzz1).any() or np.isnan(foo_gzz2).any() or np.isnan(foo_gzz3).any()):
                        print("i_x = {} i_y = {} i_xx = {} i_yy = {}".format(i_x, i_y, i_xx, i_yy))
                        # print(foo_gzz1)
                        
                    # valuezz = 0
                    # gzz = (gzz + valuezz)
                    valz = (valz + valuez)
                    

fig = plt.figure()
ax = plt.axes(projection ='3d')

figure = ax.plot_surface(xx, yy, valz - 150, cmap='YlGnBu_r')
plt.show()

