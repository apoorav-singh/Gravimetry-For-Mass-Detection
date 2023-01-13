# This is the code for the single prism Froward model
import numpy as np
from matplotlib import pyplot as plt
from math import *
# Defining X-axis and Y-axis

x = np.arange(-10,10,0.07) # [m unit]  
y = np.arange(-10,10,0.07) # [m unit]
conv_B = 1e5 # multiply with conv_B for convert the unit m/s^2 to mGal

# Surface where data is computed
z = 5  # [m unit]
# Density
d = 11.11*1e3 #[ SI ] # [kg/m^3]

# Mesh
[xx, yy] = np.meshgrid(x, y)
k_xx = 1 / xx # inverse of length in the unit m^-1
k_yy = 1 / yy

# Definig parameters for Prism model
x_pos = np.array([0, 2]) # [FirstCorner SecondCorner]
y_pos = np.array([0, 2]) # [FirstCorner SecondCorner]
z_pos = np.array([0, 2]) # [FirstCorner SecondCorner]

G_1 = 6.67384e-11   #6.67384e-3  #6.674×10−11 # Define Gravitational constant SI unit

c = G_1*d  # multiplication of gravitational constant and density 

gz1 = np.empty(xx.shape)
gy1 = np.empty(xx.shape)
gx1 = np.empty(xx.shape)

for i in range(x_pos.size):
    for j in range(y_pos.size):
        for k in range(z_pos.size):
            r = np.sqrt(((xx-x_pos[i])**2 + (yy-y_pos[j])**2 + (z-z_pos[k])**2))
            if (i+j+k)%2 == 0:
                s = 1
            else:
                s = -1
            gz = -c*s*((((xx-x_pos[i])*np.log(r+(yy-y_pos[j])))+((yy-y_pos[j])*np.log(r+xx-x_pos[i])-(z-z_pos[k])*np.arctan(((xx-x_pos[i])*(yy-y_pos[j]))/((z-z_pos[k])*r)))))
            gz1 = gz1 + gz
            
##################################### FFT of gravitional anomaly along z direction #################

fft_valz = np.fft.ifftshift(np.fft.fft2(np.fft.fftshift(gz1)))
mod_k = np.sqrt((k_yy ** 2 + k_xx ** 2))

################## gravity anomaly along x & y direction using  FFT model #######################
g_x=(-1j*k_xx)/mod_k
G_x = g_x * fft_valz     
fft_g_x = np.fft.ifftshift(np.fft.ifft2(np.fft.fftshift(G_x)))


g_y=(-1j*k_yy)/mod_k
G_y= g_y * fft_valz 
fft_g_y = np.fft.ifftshift(np.fft.ifft2(np.fft.fftshift(G_y)))

# Plotting gravity anomaly
figure_1, ax_1 = plt.subplots(1, 1,figsize=(10,10),subplot_kw=dict(projection='3d'))
ax_1.set_xlabel("X (m)",fontsize =15)
ax_1.set_ylabel("Y (m)",fontsize =15)
ax_1.set_zlabel(r'$G_x$' "(mGal)",fontsize =15)
ax_1.set_title("Horizontal Gravity anomaly"  r'$g_x$', fontsize =20)
ax_1.plot_surface(xx, yy, fft_g_x*conv_B,  cmap='gist_heat')

figure_2, ax_2 = plt.subplots(1, 1,figsize=(10,10),subplot_kw=dict(projection='3d'))
ax_2.set_xlabel("X (m)",fontsize =15)
ax_2.set_ylabel("Y (m)",fontsize =15)
ax_2.set_zlabel(r'$G_y$'"(mGal)",fontsize =15)
ax_2.set_title("Horizontal Gravity anomaly"r'$g_y$',fontsize =20)
ax_2.plot_surface(xx , yy, fft_g_y*conv_B,  cmap='gist_heat')

figure_3, ax_3 = plt.subplots(1, 1,figsize=(10,10),subplot_kw=dict(projection='3d'))
ax_3.set_xlabel("X (m)",fontsize =15)
ax_3.set_ylabel("Y(m)",fontsize =15)
ax_3.set_zlabel(r'$g_z$'"(mGal)",fontsize =15)
ax_3.set_title( "vertical Gravity anomaly "r'$g_z$',fontsize =20)
ax_3.plot_surface(xx, yy, gz1*conv_B,  cmap='gist_heat')

#######################  Gravity gradient tensor components in Evots####################################

# Inverse FFT to obtain gradient tensor
# Where G_x is the FFT of g_x;
# Where G_y is the FFT of g_y;
# Where G_z is the FFT of g_z;

conv_c = 1e5; # unit conversion from mGal/m to E. In the previous code km was used as the distance but meter is 
	          # considered in our calculation	

# Importing Data Frame

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

figure, ax = plt.subplots(3,3,figsize=(10,10),subplot_kw=dict(projection='3d'))

T_11 = A * fft_valz
inv_fft_T_11 = np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(T_11)))
phase_11 = np.arctan(inv_fft_T_11.imag/inv_fft_T_11.real)
ax[0][0].set_title('Gravity Gradient Component (1,1)')
ax[0][0].plot_surface(xx, yy, (inv_fft_T_11*conv_c),  cmap='gist_heat')

T_12 = B * fft_valz
inv_fft_T_12 = np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(T_12)))
phase_12 = np.arctan(inv_fft_T_12.imag/inv_fft_T_12.real)
ax[0][1].set_title('Gravity Gradient Component (1,2)')
ax[0][1].plot_surface(xx, yy, (inv_fft_T_12*conv_c),  cmap='gist_heat')

T_13 = C* fft_valz
inv_fft_T_13 = np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(T_13)))
ax[0][2].set_title('Gravity Gradient Component (1,3)')
phase_13 = np.arctan(inv_fft_T_13.imag/inv_fft_T_13.real)
ax[0][2].plot_surface(xx, yy, (inv_fft_T_13*conv_c),  cmap='gist_heat')

T_21 = D* fft_valz
inv_fft_T_21 = np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(T_21)))
phase_21 = np.arctan(inv_fft_T_21.imag/inv_fft_T_21.real)
ax[1][0].set_title('Gravity Gradient Component (2,1)')
ax[1][0].plot_surface(xx, yy, (inv_fft_T_21*conv_c), cmap='gist_heat')

T_22 = E* fft_valz
inv_fft_T_22 = np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(T_22)))
phase_22 = np.arctan(inv_fft_T_22.imag/inv_fft_T_22.real)
ax[1][1].set_title('Gravity Gradient Component (2,2)')
ax[1][1].plot_surface(xx, yy,  (inv_fft_T_22*conv_c),  cmap='gist_heat')

T_23 = F* fft_valz
inv_fft_T_23 = np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(T_23)))
phase_23 = np.arctan(inv_fft_T_23.imag/inv_fft_T_23.real)
ax[1][2].set_title('Gravity Gradient Component (2,3)')
ax[1][2].plot_surface(xx, yy,  (inv_fft_T_23*conv_c),  cmap='gist_heat')

T_31 = G* fft_valz
inv_fft_T_31 = np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(T_31)))
phase_31 = np.arctan(inv_fft_T_31.imag/inv_fft_T_31.real)
ax[2][0].set_title('Gravity Gradient Component (3,1)')
ax[2][0].plot_surface(xx, yy, (inv_fft_T_31*conv_c),  cmap='gist_heat')

T_32 = H* fft_valz
inv_fft_T_32 = np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(T_32)))
phase_32 = np.arctan(inv_fft_T_32.imag/inv_fft_T_32.real)
ax[2][1].set_title('Gravity Gradient Component (3,2)')
ax[2][1].plot_surface(xx, yy, (inv_fft_T_32*conv_c),  cmap='gist_heat')

T_33 = I* fft_valz
inv_fft_T_33 = np.fft.ifftshift(np.fft.ifft2(np.fft.fftshift(T_33)))
phase_33 = np.arctan(inv_fft_T_33.imag/inv_fft_T_33.real)
ax[2][2].set_title('Gravity Gradient Component (3,3)')
ax[2][2].plot_surface(xx, yy, inv_fft_T_33*conv_c, cmap='gist_heat')

############################ Mass of the anomaly using inverse model ###########################################
size = x.shape  
T_xx1 = inv_fft_T_11.real
T_xy1 = inv_fft_T_12.real
T_yy1 = inv_fft_T_22.real
G_x = fft_g_x.real
G_y = fft_g_y.real
G_z = gz1

g_data = np.empty([size[0], size[0]])   
T_data = np.empty([size[0], size[0]])       
M_data = np.empty([size[0], size[0]])



for i in range(size[0]):
    for j in range(size[0]):
        g_data[i][j]=(((G_x[i][j].real)**2 + (G_y[i][j].real)**2 + (G_z[i][j].real)**2))**1.5
        T_data[i][j]= ((T_xx1[i][j].real + T_yy1[i][j].real - sqrt((T_xx1[i][j].real - T_yy1[i][j].real)**2 + 4*(T_xy1[i][j].real)**2)))**2
        M_data[i][j] = 4*(g_data[i][j]) /(G_1*T_data[i][j])  

fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.plot_surface(xx, yy, M_data , cmap = 'plasma')


ax.set_xlabel("x (m)",  fontsize = 15)
ax.set_ylabel("y (m)",  fontsize = 15)
ax.set_zlabel("M (kg)",  fontsize = 15)
# ax.set_zlim(0, 100000)
ax.set_title('Mass of the anomaly', fontsize = 20)
plt.show()
