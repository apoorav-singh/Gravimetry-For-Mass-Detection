# This is the code for the single prism Froward model
import numpy as np
from matplotlib import pyplot as plt
from math import *
import file_management
import surf2stl

# del_x = 0.87

# Defining X-axis and Y-axis
x = np.arange(-8, 8, 0.087) # [m unit]  
y = np.arange(-8, 8, 0.087) # [m unit]

conv_B = 1e5 # Multiply with conv_B for convert the unit m/s^2 to mGal


# Surface where data is computed
# z = 8.3 # [m unit]
z = float(input("Enter the depth of the object: "))
# Density
# d = 3889.096 # [Kg/m^3]
d = 1400 # [Kg/m^3]
# Mesh
[xx, yy] = np.meshgrid(x, y)
k_xx = 1 / xx # inverse of length in the unit m^-1
k_yy = 1 / yy
# ---------------------------------------------------------------
#
# Prism Model Calculation for Synthetic Data Generation.
#
# ---------------------------------------------------------------
# Definig parameters for Prism model
# x_pos = np.array([0 , 66.8 ]) # [FirstCorner SecondCorner]
# y_pos = np.array([0 , 7.1 ]) # [FirstCorner SecondCorner]
# z_pos = np.array([0 , 8.2 ]) # [FirstCorner SecondCorner]

x_pos = np.array([0 , 1.2 ]) # [FirstCorner SecondCorner]
y_pos = np.array([0 , 0.9 ]) # [FirstCorner SecondCorner]
z_pos = np.array([0 , 0.5 ]) # [FirstCorner SecondCorner]

G_1 = 6.67384e-11   # 6.674 \times 10^{−11} # Define Gravitational constant SI unit
c = G_1*d  # Multiplication of gravitational constant and density 
# ---------------------------------------------------------------
# Gravity anomaly calculation
#---------------------------------------------------------------
gz1 = np.empty(xx.shape)
gy1 = np.empty(xx.shape, dtype = 'complex_')
gx1 = np.empty(xx.shape, dtype = 'complex_')
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
# ---------------------------------------------------------------
#
# Using FFT generating the g_x and g_y values from g_z
#
# ---------------------------------------------------------------
fft_valz = np.fft.ifftshift(np.fft.fft2(np.fft.fftshift(gz1)))
mod_k = np.sqrt((k_yy ** 2 + k_xx ** 2))
# ---------------------------------------------------------------
#
#  gravity anomaly along x & y direction using  FFT model 
#
# ---------------------------------------------------------------
g_x=(-1j*k_xx)/mod_k
G_x = g_x * fft_valz     
fft_g_x = np.fft.ifftshift(np.fft.ifft2(np.fft.fftshift(G_x)))
g_y=(-1j*k_yy)/mod_k
G_y= g_y * fft_valz 
fft_g_y = np.fft.ifftshift(np.fft.ifft2(np.fft.fftshift(G_y)))
# Plotting gravity anomaly
figure_1, ax_1 = plt.subplots(1, 3,figsize=(16,9),subplot_kw=dict(projection='3d'))
ax_1[0].set_xlabel("X (m)",fontsize =15)
ax_1[0].set_ylabel("Y (m)",fontsize =15)
ax_1[0].set_zlabel(r'$G_x$' "(mGal)",fontsize =15)
ax_1[0].set_title("Horizontal Gravity anomaly "  r'$g_x$', fontsize =20)
ax_1[0].plot_surface(xx, yy, fft_g_x.real*conv_B,  cmap='plasma')
ax_1[1].set_xlabel("X (m)",fontsize =15)
ax_1[1].set_ylabel("Y (m)",fontsize =15)
ax_1[1].set_zlabel(r'$G_y$'"(mGal)",fontsize =15)
ax_1[1].set_title("Horizontal Gravity anomaly "r'$g_y$',fontsize =20)
ax_1[1].plot_surface(xx , yy, fft_g_y.real*conv_B,  cmap='plasma')
ax_1[2].set_xlabel("X (m)",fontsize =15)
ax_1[2].set_ylabel("Y(m)",fontsize =15)
ax_1[2].set_zlabel(r'$g_z$'"(mGal)",fontsize =15)
ax_1[2].set_title( "vertical Gravity anomaly "r'$g_z$',fontsize =20)
ax_1[2].plot_surface(xx, yy, gz1*conv_B,  cmap='plasma')
image_format, image_name = file_management.file_gen(depth = int(z), graph_save = "gravity_ana")
figure_1.savefig(image_name, format=image_format, dpi=1200)
# ---------------------------------------------------------------
#
#  Generating Gravity Gradient Tensor in Etvos
#
# ---------------------------------------------------------------
# Inverse FFT to obtain gradient tensor
# Where G_x is the FFT of g_x;
# Where G_y is the FFT of g_y;
# Where G_z is the FFT of g_z;
# unit conversion from mGal/m to E. 
conv_c = 1e5; 	
T_A = np.empty([3, 3, fft_valz.shape[0], fft_valz.shape[1]], dtype = 'complex_')
# Define all the tensor components
T_A[0][0][:][:] = (-1 * k_xx ** 2) / mod_k
T_A[0][1][:][:] = (-1 * k_xx * k_yy) / mod_k
T_A[0][2][:][:] = -1j * k_xx
T_A[1][0][:][:]= (-1 * k_xx * k_yy) / mod_k
T_A[1][1][:][:]= (-1 * k_yy ** 2) / mod_k
T_A[1][2][:][:]= -1j * k_yy
T_A[2][0][:][:]= -1j * k_xx
T_A[2][1][:][:]= -1j * k_yy
T_A[2][2][:][:]= mod_k
figure_2, ax_2 = plt.subplots(3,3,figsize=(16,9),subplot_kw=dict(projection='3d'))
T = np.empty([3, 3, fft_valz.shape[0], fft_valz.shape[1]], dtype = 'complex_')
inv_fft_T = np.empty([3, 3, fft_valz.shape[0], fft_valz.shape[1]], dtype = 'complex_')
for i in range(3):
    for j in range(3):
        T[i][j][:][:] = T_A[i][j][:][:]*fft_valz.real
        inv_fft_T[i][j][:][:] = np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(T[i][j][:][:])))
        ax_2[i][j].set_title('Gravity Gradient Component (1,1)')
        ax_2[i][j].plot_surface(xx, yy, (inv_fft_T[i][j][:][:].real*conv_c),  cmap='plasma')
image_format, image_name = file_management.file_gen(depth = int(z), graph_save = "GGT")
figure_2.savefig(image_name, format=image_format, dpi=1200)
# ---------------------------------------------------------------
#
#  Calculation of the Mass of the Anomaly using Inverse Model
#
# ---------------------------------------------------------------
size = x.shape  
T_xx1 = inv_fft_T[0][0].real
T_xy1 = inv_fft_T[0][1].real
T_yy1 = inv_fft_T[1][1].real
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
# ax.plot_surface(xx, yy, M_data , cmap = 'plasma')
cont = ax.contourf(xx, yy, M_data , cmap = 'plasma')
# Add a color bar which maps values to colors.
fig.colorbar(cont, shrink=0.5, aspect=5)

np.savetxt('mass.csv', M_data, delimiter=',')

print("Expected mass of the Anomaly is:{}".format(np.sum(M_data)))
ax.set_xlabel("x (m)",  fontsize = 15)
ax.set_ylabel("y (m)",  fontsize = 15)
ax.set_zlabel("M (kg)",  fontsize = 15)
ax.view_init(90, 0)
ax.set_title('Mass of the anomaly at depth of {} m'.format(z), fontsize = 20)
image_format, image_name = file_management.file_gen(depth = int(z), graph_save = "mass_anomaly")
fig.savefig(image_name, format=image_format, dpi=1200)
# surf2stl.write('3d-mdata.stl', xx, yy, 100*M_data)
# Mesh Generator
plt.show()
