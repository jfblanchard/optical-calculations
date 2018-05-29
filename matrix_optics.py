#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Python module for performing matrix optics.

In most optical problems, the matrix determinants have a value of one, which
provides for a convenient check at the end of a calculation.

Todo: Put in the determinant check.
Todo: Analyze structure.  Maybe classes instead of functions.

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
    #a class would include a description
   
    
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
   
    
def propagate_ray(matrix,ray):
    """Propagate a ray by computing the dot product with a 2D matrix"""
    
    result = np.dot(matrix,ray)
    return result
    

if __name__ == '__main__':
    
    #used for test case:
    y,u = 0.0, 1
    ray = optical_ray(y,u)   #create a ray with height 0m  and angle .1 radians
    print('initial ray parameters: (', str(ray[0]), ',', str(ray[1]), ')')
    
    #make the system (a list) and populate with matricies
    system = []
    d1 = xfer_free_space(1)  #propagate 1m
    system.append(d1)
    l1 = thin_lens_matrix(.5)  #500mm thin lens
    system.append(l1)
    d2 = xfer_free_space(1)  #propagate 1m
    system.append(d2)
    
    #multiply by each transfer matrix
    for matx in system:
        ray = propagate_ray(matx,ray)
    
    print('final ray parameters: (', str(ray[0]), ',', str(ray[1]), ')')
    
    
#
    
