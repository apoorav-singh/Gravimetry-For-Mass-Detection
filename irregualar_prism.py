# This code is computational adaptation of the model mentioned in the 
# Text by POTENTIAL THEORY IN GRAVITY AND MAGNETIC APPLICATIONS by Richard J. Blakely

# Garvity anamoly modelling using  

from math import *
import numpy as np 
from matplotlib import pyplot as plt # Plotting
import pandas as pd # For file handeling 
import logging
from tqdm import tqdm


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# Importing Data Frame
df_1 = pd.read_csv("terrain.txt")

foo_x = np.array(df_1.iloc[0:-1,0])
foo_y = np.array(df_1.iloc[0:-1,1])
foo_z = np.array(df_1.iloc[0:-1,2])

X = np.sort(np.unique(foo_x))
Y = np.sort(np.unique(foo_y))
Z = np.empty([X.size, Y.size])
i = 0

X_iter = np.array(np.mgrid[0:X.size])
Y_iter = np.array(np.mgrid[0:Y.size])
Z_iter = np.array(np.mgrid[0:foo_x.size])

f = open("sorted_terrain.txt", "w")

for i_x in tqdm(X_iter):
    for i_y in Y_iter:
        for i_fx in Z_iter:
                if (X[i_x] == foo_x[i_fx] and Y[i_y] == foo_y[i_fx] ):
                    Z[i_x, i_y] = foo_z[i_fx]
                    # print(foo_z[i_z])
                else:
                    continue

for i_x in X_iter:
    for i_y in Y_iter:
         f.write("{}, {}, {} \n".format(X[i_x], Y[i_y], Z[i_x, i_y]))


f.close()
print(foo_z)

# Computing number of Prisms used in the system
print("Number of Prism in the simulation: ", X.size*Y.size)

[xx ,yy] = np.meshgrid(X, Y)

# Plotting
fig = plt.figure()
ax = plt.axes(projection ='3d')

figure = ax.plot_surface(np.transpose(xx), np.transpose(yy), Z)

plt.show()



