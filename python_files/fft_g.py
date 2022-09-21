# Inverse FFT to obtain gradient tensor
# Where G_x is the FFT of g_x;
# Where G_y is the FFT of g_y;
# Where G_z is the FFT of g_z;

import numpy as np
from matplotlib import pyplot as plt

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

figure, ax = plt.subplots(3,3,figsize=(10,10),subplot_kw=dict(projection='3d'))

T_11 = A * fft_valz
inv_fft_T_11 = np.fft.ifft(T_11)
# ax[0][0] = plt.axes(projection ='3d')
ax[0][0].set_title('Gravity Gradient Component (1,1)')
ax[0][0].plot_surface(xx, yy, inv_fft_T_11,  cmap='YlOrRd')


T_12 = B * fft_valz
inv_fft_T_12 = np.fft.ifft(T_12)
# ax[0][1] = plt.axes(projection ='3d')
ax[0][1].set_title('Gravity Gradient Component (1,2)')
ax[0][1].plot_surface(xx, yy, inv_fft_T_12,  cmap='YlOrRd')




T_13 = C* fft_valz
inv_fft_T_13 = np.fft.ifft(T_13)
# ax[0][2] = plt.axes(projection ='3d')
ax[0][2].set_title('Gravity Gradient Component (1,3)')
ax[0][2].plot_surface(xx, yy, inv_fft_T_13,  cmap='YlOrRd')



T_21 = D* fft_valz
inv_fft_T_21 = np.fft.ifft(T_21)
# ax[1][0] = plt.axes(projection ='3d')
ax[1][0].set_title('Gravity Gradient Component (2,1)')
ax[1][0].plot_surface(xx, yy, inv_fft_T_21,  cmap='YlOrRd')



T_22 = E* fft_valz
inv_fft_T_22 = np.fft.ifft(T_22)
# ax[1][1] = plt.axes(projection ='3d')
ax[1][1].set_title('Gravity Gradient Component (2,2)')
ax[1][1].plot_surface(xx, yy, inv_fft_T_22,  cmap='YlOrRd')


T_23 = F* fft_valz
inv_fft_T_23 = np.fft.ifft(T_23)
# ax[1][2] = plt.axes(projection ='3d')
ax[1][2].set_title('Gravity Gradient Component (2,3)')
ax[1][2].plot_surface(xx, yy, inv_fft_T_23,  cmap='YlOrRd')


T_31 = G* fft_valz
inv_fft_T_31 = np.fft.ifft(T_31)
# ax[2][0] = plt.axes(projection ='3d')
ax[2][0].set_title('Gravity Gradient Component (3,1)')
ax[2][0].plot_surface(xx, yy, inv_fft_T_31,  cmap='YlOrRd')


T_32 = H* fft_valz
inv_fft_T_32 = np.fft.ifft(T_32)
# ax[2][0] = plt.axes(projection ='3d')
ax[2][1].set_title('Gravity Gradient Component (3,2)')
ax[2][1].plot_surface(xx, yy, inv_fft_T_32,  cmap='YlOrRd')


T_33 = I* fft_valz
inv_fft_T_33 = np.fft.ifft(T_33)
# ax[2][2] = plt.axes(projection ='3d')
ax[2][2].set_title('Gravity Gradient Component (3,3)')
ax[2][2].plot_surface(xx, yy, inv_fft_T_33,  cmap='YlOrRd')

plt.show()

