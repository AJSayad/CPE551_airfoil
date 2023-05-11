import numpy as np
import matplotlib.pyplot as plt

#domain and mesh set up in zeta plane
n=100 #grid points
xi = np.linspace(-1,1,n)
eta = np.linspace(-1,1,n)
XI,ETA = np.meshgrid(eta,xi)
zeta = XI + 1j*ETA
zeta0 = 0 
beta = np.arange(0,2*np.pi,0.01) #angle in zeta plane

#flow properties
alpha = 5*(np.pi/180) #angle of attack [radians]
u_inf = 1 #free stream velocity [m/s]
u = u_inf*np.cos(alpha) #x component of velocity
v = u_inf*np.sin(alpha) #y component of velocity
rho = 1.204 #air density [kg/m^3]

#generate a airfoil 1 in in zeta plane 
dx1 = 0.01 #shift in the x direction (change the sign of dx to flip direction
dy1 = 0.01 #shift in the left direction
dr1 = 0.01 #change in radius, set this equal to zero to get a flat plate in the z plane
r1 = 1
a1 = r1 + dr1; 
airfoil1 = -dx1 + 1j*dy1 + a1*np.exp(1j*beta)
gamma = 4*np.pi*u_inf*r1*np.sin(alpha) #Kutta condition for stagnation points

plt.figure(1)
plt.plot(airfoil1.real, airfoil1.imag); plt.title('Airfoil construction geometry in zeta plane')
angle = np.linspace(0,2*np.pi,n)
circle = r1*np.cos(angle) + 1j*np.sin(angle)
plt.plot(circle.real,circle.imag,'--r')
plt.show()

#domain and mesh set up in the z plane 
def z_plane(zeta):
    return zeta+r1**2/zeta #transform function to go from zeta plane to the z plane

z = z_plane(zeta)
x = np.real(z)
y = np.imag(z)

#mapping and plotting of airfoil 1 in z plane
plt.figure(2)
z_ellipse = z_plane(airfoil1)
plt.plot(z_ellipse.real,z_ellipse.imag); plt.title('Airfoil 1')
plt.show()

#plotting in the zeta plane
F_of_zeta = (u-1j*v)*(zeta-zeta0)+(u-1j*v)*(a1**2/(zeta-zeta0))+ 1j*(gamma/(2*np.pi))*np.log(gamma/a1);
plt.figure(3)
plt.contour(XI, ETA, F_of_zeta.imag,20); plt.title('Flow')
plt.show()

#generate a airfoil 2 in in zeta plane
dx2 = 0.15 #shift in the x direction (change the sign of dx to flip direction
dy2 = 0.15 #shift in the left direction
dr2 = 0.15 #change in radius, set this equal to zero to get a flat plate in the z plane
r2 = 1.05
a2 = r2 + dr2; 
airfoil2 = -dx2 + 1j*dy2 + a2*np.exp(1j*beta)

#mapping and plotting of airfoil 2 in z plane
plt.figure(3)
z_ellipse = z_plane(airfoil2)
plt.plot(z_ellipse.real,z_ellipse.imag); plt.title('Airfoil 2')
plt.show()