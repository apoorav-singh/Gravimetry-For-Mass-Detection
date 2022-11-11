# Inverse FFT to obtain gradient tensor
# Where G_x is the FFT of g_x;
# Where G_y is the FFT of g_y;
# Where G_z is the FFT of g_z;
con_A = 10**-3; # unit conversion from m to km
conv_B = 1000; # unit conversion from mGal/km to E

import numpy as np
from matplotlib import pyplot as plt
from scipy.io import savemat

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
inv_fft_T_11 = np.fft.ifftshift(np.fft.fft(np.fft.ifftshift(T_11)))
phase_11 = np.arctan(inv_fft_T_11.imag/inv_fft_T_11.real)

# ax[0][0] = plt.axes(projection ='3d')
ax[0][0].set_title('Gravity Gradient Component (1,1)')
ax[0][0].plot_surface(xx, yy, inv_fft_T_11.real,  cmap='YlOrRd')
# ax[0][0].plot_surface(xx, yy, phase_11)


T_12 = B * fft_valz
inv_fft_T_12 = np.fft.ifftshift(T_12)
phase_12 = np.arctan(inv_fft_T_12.imag/inv_fft_T_12.real)
# ax[0][1].plot_surface(xx, yy, phase_12)
# ax[0][1] = plt.axes(projection ='3d')
ax[0][1].set_title('Gravity Gradient Component (1,2)')
ax[0][1].plot_surface(xx, yy, inv_fft_T_12.real,  cmap='YlOrRd')




T_13 = C* fft_valz
inv_fft_T_13 = np.fft.fftshift(np.fft.ifft(np.fft.ifftshift(T_13)))
# ax[0][2] = plt.axes(projection ='3d')
ax[0][2].set_title('Gravity Gradient Component (1,3)')
phase_13 = np.arctan(inv_fft_T_13.imag/inv_fft_T_13.real)
# ax[0][2].plot_surface(xx, yy, phase_13)
ax[0][2].plot_surface(xx, yy, inv_fft_T_13.real,  cmap='YlOrRd')
# ax[0][2].plot_surface(xx, yy, inv_fft_T_13.real)


T_21 = D* fft_valz
inv_fft_T_21 = np.fft.fftshift(np.fft.ifft(np.fft.ifftshift(T_21)))
# ax[1][0] = plt.axes(projection ='3d')
phase_21 = np.arctan(inv_fft_T_21.imag/inv_fft_T_21.real)
# ax[1][0].plot_surface(xx, yy, phase_21)
ax[1][0].set_title('Gravity Gradient Component (2,1)')
ax[1][0].plot_surface(xx, yy, inv_fft_T_21.real,  cmap='YlOrRd')
# ax[1][0].plot_surface(xx, yy, inv_fft_T_21.real)


T_22 = E* fft_valz
inv_fft_T_22 = np.fft.fftshift(np.fft.ifft(np.fft.ifftshift(T_22)))
phase_22 = np.arctan(inv_fft_T_22.imag/inv_fft_T_22.real)
# ax[1][1].plot_surface(xx, yy, phase_22)
# ax[1][1] = plt.axes(projection ='3d')
ax[1][1].set_title('Gravity Gradient Component (2,2)')
ax[1][1].plot_surface(xx, yy, inv_fft_T_22.real,  cmap='YlOrRd')
# ax[1][1].plot_surface(xx, yy, inv_fft_T_22.real)

T_23 = F* fft_valz
inv_fft_T_23 = np.fft.fftshift(np.fft.ifft(np.fft.ifftshift(T_23)))
phase_23 = np.arctan(inv_fft_T_23.imag/inv_fft_T_23.real)
# ax[1][2].plot_surface(xx, yy, phase_23)
# ax[1][2] = plt.axes(projection ='3d')
ax[1][2].set_title('Gravity Gradient Component (2,3)')
ax[1][2].plot_surface(xx, yy, inv_fft_T_23.real,  cmap='YlOrRd')
# ax[1][2].plot_surface(xx, yy, inv_fft_T_23.real)

T_31 = G* fft_valz
inv_fft_T_31 = np.fft.fftshift(np.fft.ifft(np.fft.ifftshift(T_31)))
phase_31 = np.arctan(inv_fft_T_31.imag/inv_fft_T_31.real)
# ax[2][0].plot_surface(xx, yy, phase_31)
# ax[2][0] = plt.axes(projection ='3d')
ax[2][0].set_title('Gravity Gradient Component (3,1)')
ax[2][0].plot_surface(xx, yy, inv_fft_T_31.real,  cmap='YlOrRd')
# ax[2][0].plot_surface(xx, yy, inv_fft_T_31.real)

T_32 = H* fft_valz
inv_fft_T_32 = np.fft.fftshift(np.fft.ifft(np.fft.ifftshift(T_32)))
phase_32 = np.arctan(inv_fft_T_32.imag/inv_fft_T_32.real)
# ax[2][1].plot_surface(xx, yy, phase_32)
# ax[2][0] = plt.axes(projection ='3d')
ax[2][1].set_title('Gravity Gradient Component (3,2)')
ax[2][1].plot_surface(xx, yy, inv_fft_T_32.real,  cmap='YlOrRd')
# ax[2][1].plot_surface(xx, yy, inv_fft_T_32.real)

T_33 = I* fft_valz
inv_fft_T_33 = np.fft.fftshift(np.fft.ifft(np.fft.ifftshift(T_33)))
phase_33 = np.arctan(inv_fft_T_33.imag/inv_fft_T_33.real)
# ax[2][2].plot_surface(xx, yy, phase_33)
# ax[2][2] = plt.axes(projection ='3d')
ax[2][2].set_title('Gravity Gradient Component (3,3)')
ax[2][2].plot_surface(xx, yy, inv_fft_T_33.real,  cmap='YlOrRd')
# ax[2][2].plot_surface(xx, yy, inv_fft_T_33.real)


# in_ch = input("Do you wish to save the generated data in .mat format(MATLAB) (y/n): ")

# if (in_ch == "y"):
#     xx_mat={'xx':xx}
#     savemat("xx.mat", xx_mat)
#     yy_mat={'yy':yy}
#     savemat("yy.mat", yy_mat) 
#     inv_fft_T_11_mat = {'T_11':inv_fft_T_11.real}
#     savemat("inv_fft_T_11.mat",  inv_fft_T_11_mat)
#     inv_fft_T_12_mat = {'T_12':inv_fft_T_12.real}
#     savemat("inv_fft_T_12.mat",  inv_fft_T_12_mat)
#     inv_fft_T_13_mat = {'T_13':inv_fft_T_13.real}
#     savemat("inv_fft_T_13.mat",  inv_fft_T_13_mat)
#     inv_fft_T_21_mat = {'T_21':inv_fft_T_21.real}
#     savemat("inv_fft_T_21.mat",  inv_fft_T_21_mat)
#     inv_fft_T_22_mat = {'T_22':inv_fft_T_22.real}
#     savemat("inv_fft_T_22.mat",  inv_fft_T_22_mat)
#     inv_fft_T_23_mat = {'T_23':inv_fft_T_23.real}
#     savemat("inv_fft_T_23.mat",  inv_fft_T_23_mat)
#     inv_fft_T_31_mat = {'T_31':inv_fft_T_31.real}
#     savemat("inv_fft_T_31.mat",  inv_fft_T_31_mat)
#     inv_fft_T_32_mat = {'T_32':inv_fft_T_32.real}
#     savemat("inv_fft_T_32.mat",  inv_fft_T_32_mat)
#     inv_fft_T_33_mat = {'T_33':inv_fft_T_33.real}
#     savemat("inv_fft_T_33.mat",  inv_fft_T_33_mat)
# else:
#     pass

plt.show()

