# This piece of generates values usefull for Fourier Transfrom

import numpy as np
from matplotlib import pyplot as plt  # Plotting
from tqdm import tqdm
import cmath


# Importing Data Frame
df_1 = np.load("valz.npy")  # save the data(valz) as text file
xx = np.load("xx.npy")
yy = np.load("yy.npy")


K_xx = 1 / xx
K_yy = 1 / yy
fft_valz = np.fft.fft(np.ifft.fftshift(df_1))
# fft_valz = np.fft.fft(df_1)

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
