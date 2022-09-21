# This piece of generates values usefull for Fourier Transfrom

import numpy as np
from matplotlib import pyplot as plt  # Plotting
from tqdm import tqdm
import cmath


# Importing Data Frame
df_1 = np.load("valz.npy")  # save the data(valz) as text file
# print(df_1)
df_2 = np.genfromtxt("terrain.txt", dtype=float, encoding=None, delimiter=",")
# print(df_2)

# Length of the Array
L = np.array(df_2.shape)
L[0] = L[0] - 1
L[1] = L[1] - 1

foo_x = df_2[0 : L[0], 0]
foo_y = df_2[0 : L[0], 1]
foo_z = df_2[0 : L[0], 2]

X = np.sort(np.unique(foo_x))
Y = np.sort(np.unique(foo_y))
Z = np.empty([X.size, Y.size])
i = 0

X_iter = np.array(np.mgrid[0 : X.size])
Y_iter = np.array(np.mgrid[0 : Y.size])
Z_iter = np.array(np.mgrid[0 : foo_z.size])

for i_x in tqdm(X_iter):
    for i_y in Y_iter:
        for i_fx in Z_iter:
            if X[i_x] == foo_x[i_fx] and Y[i_y] == foo_y[i_fx]:
                Z[i_x, i_y] = foo_z[i_fx]
                # print(foo_z[i_z])
            else:
                continue


# Computing number of Prisms used in the system
print("Number of Prism in the simulation: ", X.size * Y.size)
[xx, yy] = np.meshgrid(X, Y)
save_xx = np.save("xx", xx)
save_yy = np.save("yy", yy)


K_xx = 1 / xx
K_yy = 1 / yy
fft_valz = np.fft.fft(df_1)

mod_K = np.sqrt((K_yy ** 2 + K_xx ** 2))
shape_1 = mod_K.shape
K_z = np.empty(shape_1, dtype=complex)

for i in range(shape_1[0]):
    for j in range(shape_1[1]):
        K_z[i][j] = complex(0, mod_K[i][j])

save_k_x = np.save("k_xx", K_xx)
save_k_y = np.save("k_yy", K_yy)
save_K_z = np.save("k_z", K_z)
save_mod_K = np.save("mod_k", mod_K)
save_fft_valz = np.save("fft_valz", fft_valz)


plt.show()
