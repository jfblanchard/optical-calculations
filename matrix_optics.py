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

Todo: Put in the determinant check.



"""

import numpy as np
import matplotlib.pyplot as plt


class OpticalRay:
    
    def __init__(self,y,u):
        """ Define a ray for matrix optical calculations. 
            Todo: make this construct a ray grid and think about the best structure
            to store lots of rays (ex: millions)"""
            
        self.yu = np.zeros(shape = (2,1), dtype=float)
        self.yu[0] = y
        self.yu[1] = u
        self.energy = 1.0   
        


class OpticalSystem:
    
    def __init__(self):
        """Setup creates an empty list structure for rays, locations, and 
        system matricies
        """
        
        #initialize rays - at least get an empty list started
        self.start_rays = [] 
        self.locations = [0]  #new list of locations
        
        #start_rays.append(optical_ray(0,.1))   #chief and marginal rays
        #start_rays.append(optical_ray(.1,0))
        
        #initialize and store system matricies list 
        self.matricies= []     
        
        #stores all the ray parameters
        self.ray_matrix = np.zeros(1)
        
        
    def create_rayfan(self, ray_height, min_angle, max_angle, num):
        """ Create a rayfan with extents min_angle to max_angle, with num rays
        Todo: Add loop for ray_heights too
        """
          
        for i in np.linspace(self, ray_height, min_angle, max_angle, num):  #make a ray fan
            self.start_rays.append(OpticalRay(ray_height,i)) 


    def add_chief_and_marginal_rays(self):
        # add chief and marginal rays
        self.start_rays.append(OpticalRay(0,.1))   #need to know height of aperture
        self.start_rays.append(OpticalRay(.1,0))   #need to know height of object   
        
        
    def add_ray(self,y,u):
        """ Add an arbitrary ray at height y and angle u
        """
        self.start_rays.append(OpticalRay(y,u))
    
    
    def append_matrix(self, M):
        """Append a matrix to the system.
        """
        
        self.matricies.append(M)
        
     
    def update_system(self):
        """Progagate rays, recomputes entire system ray matrix
        """
        
        self.ray_matrix = np.zeros((len(self.start_rays),len(self.matricies)+1,2))
        #load starting rays:
        count = 0  #need a counter if iterating through objects
        for i in self.start_rays:
            self.ray_matrix[count,0,0] = i.yu[0]
            self.ray_matrix[count,0,1] = i.yu[1]
            count +=1
        
        #multiply by each matrix
        for i in range(len(self.start_rays)):
            for j in range(len(self.matricies)):
                self.ray_matrix[i][j+1] = np.dot(self.matricies[j], self.ray_matrix[i][j])
        
            

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
    
    d = dist/n   #reduced distance
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
    """Matrix to approximate a thin lens (no thickenss).  
    Singular input paramter is focal length.
    """
    
    A = 1
    B = 0
    C = -1/focal_length
    D = 1
    matrix = xfer_matrix(A, B, C, D)    
    
    return matrix
   



def plot_rays(ray_matx, loc):
    
    #to plot, we need cumulative distances.  Maybe make part of array later
    
    plt.figure()
    #draw optical axis
    x = [np.min(loc), np.max(loc)]
    y = [0,0]
    plt.plot(x,y,'--')
    
    for i in range(ray_matx.shape[0]):
        plt.plot(dist,ray_matx[i,:,0])     
        
    plt.title('Raytrace with Matrix Optics')
    plt.xlabel('Distance (m)')
    plt.ylabel('Ray height(m)')
    plt.show()


#def append_element(ele):
    


if __name__ == '__main__':
  
    system = OpticalSystem()
    system.add_chief_and_marginal_rays()
    system.add_ray(.05,.05)
    
    
    # populate the optical system with matricies
    d1 = xfer_free_space(1)  #create a matrix to propagate 1m
    system.matricies.append(d1)
    system.locations.append(1)
    
    #system.append(xfer_free_space(1))  #propagate another 1m
    l1 = thin_lens_matrix(.5)  #500mm thin lens
    system.matricies.append(l1)
    system.locations.append(0)
    
    d2 = xfer_free_space(1)  #propagate 1m
    system.matricies.append(d2)
    system.locations.append(1)
    
    system.update_system()
    ray_matx = system.ray_matrix
    dist = np.cumsum(system.locations)
    plot_rays(ray_matx,dist)

    print('final ray parameters: \n', str(ray_matx))
    
    # Tested with a .5m lens, correct in that a infintie image goes to zero
    # at 1m away, an on-axis point object is collimated, and a 
    
    
