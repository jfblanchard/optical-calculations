'''

Plot Zernike polynomials.  Uses the first 14 modes of OSA/ANSI indexing

3D ploting based on matplotlib example by Armin Moser: surface3d_radial_demo.py


'''

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np


# Define functions and corresponding labels.
# Using first 14 modes in OSA/ANSI indexing

Z_polys = ['1', 
           '2*R*np.sin(Theta)',
           '2*R*np.cos(Theta)',
           'np.sqrt(6)*R**2*np.sin(2*Theta)',
           'np.sqrt(3)*(2*R**2 - 1)',
           'np.sqrt(6)*R**2*np.cos(2*Theta)',
           'np.sqrt(8)*R**3*np.sin(3*Theta)',
           'np.sqrt(8)*(3*R**3 - 2*R)*np.sin(Theta)',
           'np.sqrt(8)*(3*R**3 - 2*R)*np.cos(Theta)',
           'np.sqrt(8)*R**3*np.cos(3*Theta)',
           'np.sqrt(10)*R**4*np.sin(4*Theta)',
           'np.sqrt(10)*(4*R**4 - 3*R**2)*np.sin(2*Theta)',
           'np.sqrt(5)*(6*R**4 - 6*R**2 + 1)',
           'np.sqrt(10)*(4*R**4 - 3*R**2)*np.cos(2*Theta)',
           'np.sqrt(10)*R**4*np.cos(4*Theta)',
          ]
                                   
Z_labels = [r'$Z^0_0 , Z_j = 1$, Piston',
            r'$Z^{-1}_1, Z_j = 2\rho sin(\theta),$  Vertical tilt ',
            r'$Z^{1}_1, Z_j = 2\rho cos(\theta),$  Horizontal tilt ',
            r'$Z^{-2}_2, Z_j = \sqrt{6} \rho^2 \sin{2\theta},$  Oblique Astigmatism ',
            r'$Z^{0}_2, Z_j = \sqrt{3} (2\rho^2 -1),$  Defocus',
            r'$Z^{2}_2, Z_j = \sqrt{6} \rho^2 \cos{2\theta},$  Vertical Astigmatism ',  
            r'$Z^{-3}_3, Z_j = \sqrt{8} \rho^3 \sin{3\theta},$  Vertical Trefoil ', 
            r'$Z^{-1}_3, Z_j = \sqrt{8} (3\rho^3 - 2\rho) \sin{\theta},$  Vertical coma ',     
            r'$Z^{1}_3, Z_j = \sqrt{8} (3\rho^3 - 2\rho) \cos{\theta},$  Horizontal coma ',     
            r'$Z^{3}_3, Z_j = \sqrt{8} \rho^3 \cos{3\theta},$  Oblique Trefoil ', 
            r'$Z^{-4}_4, Z_j = \sqrt{10} \rho^4 \sin{4\theta},$  Oblique Quadrafoil ',  
            r'$Z^{-2}_4, Z_j = \sqrt{10} (4\rho^4 - 3\rho^2) \sin{2\theta},$  Oblique Secondary Astigmatism ',      
            r'$Z^{0}_4, Z_j = \sqrt{5} (6\rho^4 - 6\rho^2 + 1),$  Primary Spherical ',     
            r'$Z^{2}_4, Z_j = \sqrt{10} (4\rho^4 - 3\rho^2) \cos{2\theta},$  Vertical Secondary Astigmatism ',    
            r'$Z^{4}_4, Z_j = \sqrt{10} \rho^4 \cos{4\theta},$  Vertical Quadrafoil ',      
            ]

def plot_zernikes(osa_index):
    """ can make plots up to index 14 (OSA/ANSI)
    """

    # Create the mesh in polar coordinates and compute corresponding Z.
    r = np.linspace(0, 1.25, 100)
    theta = np.linspace(0, 2*np.pi, 100)
    R, Theta = np.meshgrid(r, theta) 
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    Z = eval(Z_polys[osa_index])  #select polynomial
    
    # Express the mesh in the cartesian system.
    X, Y = R*np.cos(Theta), R*np.sin(Theta)

    plt.title(Z_labels[osa_index])
    ax.plot_surface(X, Y, Z, cmap=plt.cm.jet)
    ax.set_zlim(-2*np.pi, 2*np.pi)

    plt.show()


#plot each one.
for i in np.arange(0,15):
    plot_zernikes(i)
    
    
    
    
#zernike terms
#Z = 1                                       #Z0,0: Piston
#Z = 2*R*np.sin(Theta)                       #Z-1,1: Y, verical tilt
#Z = 2*R*np.cos(Theta)                       #Z1,1: X, horizontal tilt
#Z = np.sqrt(6)*R**2*np.sin(2*Theta)        #Z-2,2: Oblique Astigmatism
#Z = np.sqrt(3)*(2*R**2 - 1)                #Z0,2: Defocus
#Z = np.sqrt(6)*R**2*np.cos(2*Theta)        #Z2,2: Vertical Astigmatism
#Z = np.sqrt(8)*R**3*np.sin(3*Theta)         #Z-3,3 Vertical trefoil
#Z = np.sqrt(8)*(3*R**3 - 2*R)*np.sin(Theta)  #Z-1,3: Vertical Coma
#Z = np.sqrt(8)*(3*R**3 - 2*R)*np.cos(Theta)  #Z1,3: Horizontal Coma
#Z = np.sqrt(8)*R**3*np.cos(3*Theta)          #Z3,3: Oblique trefoil
#Z = np.sqrt(10)*R**4*np.sin(4*Theta)         #Z-4,4: Oblique quadrafoil
#Z = np.sqrt(10)*(4*R**4 - 3*R**2)*np.sin(2*Theta)  #Z-2,4: Oblique secondary astigmatism
#Z = np.sqrt(5)*(6*R**4 - 6*R**2 + 1)                 #Z0,4: Primary spherical
#Z = np.sqrt(10)*(4*R**4 - 3*R**2)*np.cos(2*Theta)   #Vertical secondary astigmatism
#Z = np.sqrt(10)*R**4*np.cos(4*Theta)                #Vertical quadrafoil
           


