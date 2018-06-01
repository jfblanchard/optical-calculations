#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python scripts for performing matrix optics.  This method uses paraxial 
approximations (sin(a) ~= a), which is valid for angles < ~6 deg (.1 radians).

The rays and matricies are structued as numpy arrays (fast calculations)
embedded within a list structure for flexible adding and removing of items.

In most optical problems, the matrix determinants have a value of one, which
provides for a convenient check at the end of a calculation.

For now, launch only a marginal and chief ray

"""

import numpy as np
import matplotlib.pyplot as plt



def optical_ray(y,u):
    """ Define a ray for matrix optical calculations. 
        Todo: make this construct a ray grid and think about the best structure
        to store lots of rays (ex: millions)"""
        
    ray = np.zeros(shape = (2,1), dtype=float)
    ray[0] = y
    ray[1] = u
    
    return ray

    
def initialize_system():
    """Setup structure, creates an empty list.  Use lists for adding, then 
    convert to numpy arrays for computation.
    """
    
    #initialize rays
    start_rays = []  
    start_rays.append(optical_ray(0,.1))   #chief and marginal rays
    start_rays.append(optical_ray(.1,0))
    for i in range(10):
        start_rays.append(optical_ray(0.0,i/10.0 - .5))
    
    #initialize system list 
    system = []     
    
    #initialize locationations
    location = [0]
    
    return start_rays, system, location
    

def xfer_matrix(A,B,C,D):
    """Define a transfer matrix
    """
    matrix = np.zeros(shape=(2,2), dtype=float)
    matrix[0] = [A,B]
    matrix[1] = [C,D]
    
    return matrix


def xfer_free_space(dist, n=1):
    """Matrix representing a ray transfer through free space.  Distance and 
    index (n) are the input parameters.
    """
    d = dist/n #reduced distance
    matrix = xfer_matrix(1,d,0,1)    
    return matrix
 
    
def refraction_matrix(n1,n2,radius):
    """ Define a refraction matrix with index n1, index n2, and surface radius
    """
    A = 1
    B = 0
    C = -(n2 - n1)/radius
    D = 1
    matrix = xfer_matrix(A, B, C, D)    
    return matrix
    

def thin_lens_matrix(focal_length):
    """Matrix to approximate a thin lens.  Input paramter is focal length.
    """
    
    A = 1
    B = 0
    C = -1/focal_length
    D = 1
    matrix = xfer_matrix(A, B, C, D)    
    return matrix
    
 
def update_system(start_rays,system):
    """Called when the sytem changes, recomputes entire system ray matrix
    """
    
    ray_matrix = np.zeros((len(start_rays),len(system)+1,2))
    #load starting rays:
    for i in range(len(start_rays)):
        ray_matrix[i,0,0] = start_rays[i][0]
        ray_matrix[i,0,1] = start_rays[i][1]
    
    #multiply by each matrix
    for i in range(len(start_rays)):
        for j in range(len(system)):
            ray_matrix[i][j+1] = np.dot(system[j], ray_matrix[i][j])
    
    return ray_matrix

def plot_rays(ray_matx, loc):
    
    #to plot, we need cumulative distances.  Maybe make part of array later
    
    plt.figure()
    #draw optical axis
    x = [np.min(loc), np.max(loc)]
    y = [0,0]
    plt.plot(x,y,'--')
    
    for i in range(ray_matx.shape[0]):
        plt.plot(loc,ray_matx[i,:,0])
    plt.show()
        

if __name__ == '__main__':
    
    start_rays, system, location = initialize_system()
    print('initial rays: \n', str(start_rays))
    
    # populate the optical system with matricies
    d1 = xfer_free_space(1)  #create a matrix to propagate 1m
    system.append(d1)
    location.append(1)
    #system.append(xfer_free_space(1))  #propagate another 1m
    l1 = thin_lens_matrix(.5)  #500mm thin lens
    system.append(l1)
    location.append(0)
    d2 = xfer_free_space(1)  #propagate 1m
    system.append(d2)
    location.append(1)
    
    ray_matx = update_system(start_rays,system)
    cum_loc = np.cumsum(location)
    plot_rays(ray_matx,cum_loc)
    
    #multiply by each transfer matrix
    #for matx in system:
    #    ray = np.dot(matx,ray)
    
    print('final ray parameters: \n', str(ray_matx))
    
    
#Need a good way to add distances.
    
