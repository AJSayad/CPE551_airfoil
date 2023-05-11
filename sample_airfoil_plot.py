import matplotlib.pyplot as plt
import numpy as np

# Define the airfoil coordinates
x = np.array([1, 0.933, 0.75, 0.5, 0.25, 0.067, 0, 0.067, 0.25, 0.5, 0.75, 0.933, 1])
y = np.array([0, -0.005, -0.017, -0.033, -0.042, -0.033, 0, 0.045, 0.076, 0.072, 0.044, 0.013, 0])

# Plot the airfoil
plt.plot(x,y)

# Define the grid for the streamlines
Y,X = np.mgrid[-1:1:100j,-1:2:100j]

# Define the velocity field
U = -Y
V = X

# Add circulation to satisfy the Kutta condition
Gamma = -4*np.pi*V[50][50]
U = U + Gamma/(2*np.pi)*(Y/(X**2+Y**2))
V = V - Gamma/(2*np.pi)*(X/(X**2+Y**2))

# Mask the region inside the airfoil
mask = np.zeros(U.shape,dtype=bool)
mask[(X<1) & (X>0) & (Y<np.interp(X,x,y)) & (Y>-np.interp(X,x,-y))] = True
U = np.ma.array(U,mask=mask)
V = np.ma.array(V,mask=mask)

# Plot the streamlines
plt.streamplot(X,Y,U,V)

# Show the plot
plt.show()
