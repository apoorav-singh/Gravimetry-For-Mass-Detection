# This piece of code performs fourier transform

import numpy as np 
from matplotlib import pyplot as plt # Plotting

# Importing Data Frame
df_1 = np.load('valz.npy') # save the data(valz) as text file
#print(df_1)

from tqdm import tqdm



# Importing Data Frame

df_2 = np.genfromtxt("terrain.txt", dtype=float, encoding=None, delimiter=",")
#print(df_2)

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

K_xx = 1/xx
K_yy = 1/yy

# save_k_x = np.save("k_x", K_xx)
# save_k_y = np.save("k_y", K_yy)

K = np.empty(K_xx.shape)
K = np.sqrt((K_yy**2 + K_xx**2))

fig = plt.figure() 
ax = plt.axes(projection ='3d')
L3 = np.abs(np.fft.fft(df_1))
figure = ax.plot_surface(K_xx, K_yy, L3,  cmap='YlGnBu_r')


plt.show()