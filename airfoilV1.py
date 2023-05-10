import numpy as np
import matplotlib.pyplot as plt

n = 100  # grid points
# domain and mesh set up in zeta plane
xi = np.linspace(-1, 1, n)
eta = np.linspace(-1, 1, n)
XI, ETA = np.meshgrid(eta, xi)
zeta = XI + 1j * ETA
zeta0 = 1
beta = np.arange(0, 2 * np.pi + 0.01, 0.01)  # angle in zeta plane

# flow properties
alpha = 5 * (np.pi / 180)  # angle of attack [radians]
u_inf = 1  # free stream velocity [m/s]
u = u_inf * np.cos(alpha)  # x component of velocity
v = u_inf * np.sin(alpha)  # y component of velocity
rho = 1.204  # air density [kg/m^3]
c = 1

# domain and mesh set up in the z plane
x = np.linspace(-1, 1, n)
y = np.linspace(-1, 1, n)
X, Y = np.meshgrid(x, y)


def z_plane(zeta):
    return zeta + c ** 2 / zeta


z = z_plane(zeta)

# generate a circle in zeta plane with slightly larger radius than circle
dc = 0.1  # set this equal to zero to get a flat plate in the z plane
a = c + dc
circle = a * np.exp(1j * beta)

# sample mapping and plotting the ellipse
plt.figure(1)
z_ellipse = z_plane(circle)
plt.plot(z_ellipse.real, z_ellipse.imag)
plt.title('Z-plane')
plt.axis('equal')

# plotting in the zeta plane
plt.figure(2)
F_of_zeta = (u - 1j * v) * (zeta - zeta0)
plt.contour(XI, ETA, F_of_zeta.imag)
plt.title('Zeta-plane')
plt.hold(True)
angle = np.linspace(0, 2 * np.pi, n)
p = dc * np.cos(angle)
k = dc * np.sin(angle)
plt.plot(p, k, 'k', linewidth=2)
plt.hold(False)

# plotting in the z plane
plt.figure(3)
F_of_z = z_plane(F_of_zeta)
plt.contour(X, Y, F_of_z.imag)
plt.title('Z-plane')
plt.axis('equal')
