# Inverse FFT to obtain gradient tensor
# Where G_x is the FFT of g_x;
# Where G_y is the FFT of g_y;
# Where G_z is the FFT of g_z;

import numpy as np

# Importing Data Frame

fft_valz = np.load("fft_valz.npy")
k_xx = np.load("k_xx.npy")
k_yy = np.load("k_yy.npy")
K_z = np.load("k_z.npy")
mod_k = np.load("mod_k.npy")
xx = np.load("xx.npy")
yy = np.load("yy.npy")

# Define all the tensor components
A = (-1 * k_xx ** 2) / mod_k
B = (-1 * k_xx * k_yy) / mod_k
C = -1j * k_xx
D = (-1 * k_xx * k_yy) / mod_k
E = (-1 * k_yy ** 2) / mod_k
F = -1j * k_yy
G = -1j * k_xx
H = -1j * k_yy
I = mod_k

# | A B C |
# | D E F |
# | G H I |


fft_T_11 = A * fft_valz
inv_fft_T_11 = np.fft.ifft(fft_T_11)
