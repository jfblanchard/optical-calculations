# -*- coding: utf-8 -*-
"""
Geometrical imaging equations, Paraxial optical calculations

"""


import numpy as np
import scipy.constants as const


# Need to clarify some of these functions
#could break into newton imaging equations and gaussian imaging equations.
#newtons were derived in 1666 using similar triangles, referenced to focal planes.

    
def obj_dist_from_EFL_and_m(f,m):
    """Calculate object distance (z) from focal length (f) and magnification (m)
    """
    
    obj_dist = -1*((1-m)/m)*f
    return obj_dist
    # todo: clarify assumptions in terms of +/- distances.
    
    

def img_dist_from_EFL_and_m(f,m):
    """Calculate image distance (z') from focal length (f) and magnification (m)
    """
    
    img_dist = (1-m)*f
    return img_dist   
    # todo: clarify assumptions in terms of +/- distances.
    
    
    
def thin_lens_image_dist(obj_dist,efl):
    """Calculate the image distance given the object distance and efl.  Uses
    the thin lens equation 1/img + 1/obj = 1/f.  Returns same units.
    
    Parameters
    ----------
    obj_dist : float
        Distance to object
    efl : float
        Focal length of the thin lens
        
    Returns
    -------
    img_dist : float
        The image distance
    """  
    
    efl = float(efl)
    obj_dist = float(obj_dist)      #convert to float if int
    img_dist = 1/(1/efl - 1/obj_dist)
    return img_dist
    #todo: catch infinite case
    #todo: clarify parameters.  This is the distance in front of the focal pt.

    
def two_lens_EFL(f1,f2,d):
    """Calculate the focal length of two thin lenses sepatated by air.  The 
    units must match, and will return the same units.
    
    Parameters
    ----------
    f1 : float
        Focal length of lens 1
    f2 : float
        Focal length of lens 2
    d : float
        Separation distance between the two lenses
        
    Returns
    -------
    f : float
        The focal length of the two lens system
    """    
    
    phi1 = 1.0/f1
    phi2 = 1.0/f2
    phi = phi1 + phi2 -phi1*phi2*d

    return 1.0/phi
    
def thick_lens_EFL(R1,R2,t,n):
    """Calculate the focal length of a thick lens via geometrical method, 
    given the two surface radii, the center thickenss, and the index.  
    The units must match, and will return the same units.   
    
    Parameters
    ----------
    R1 : float
        Radius of surface 1
    R2 : float
        Radius of surface 2
    t : float
        Center thickenss of the lens
    n : float
        Index of refraction
        
    Returns
    -------
    f : float
        The focal length of the thick lens
    """  
    tau = t/n
    C1 = 1.0/R1
    C2 = 1.0/R2
    phi = (n-1.0)*(C1-C2 + (n-1)*C1*C2*tau)
    efl = 1.0/phi    
    
    return efl
    #test1 50,-50,10,1.5 matches Zemax exactly: 51.741
    #todo:  better way to convert units besides writing several if's

def thin_prism_deviation(angle, n):
    """Calculate the ray deviation caused by a thin prism given prism angle
        and index.
    
    Parameters
    ----------
    angle : float
        Angle of the prism (degrees or radians)
    n: float
        Index of refraction of the prism material at the wavelength of interest
        
    Returns
    -------
    d : float
        The ray deviation due to the prism (in units of input angle)
    """  
    d = -1*(n-1)*angle
    return d
