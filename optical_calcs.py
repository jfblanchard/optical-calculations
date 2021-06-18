# -*- coding: utf-8 -*-
"""
A module containing a number of functions used for performing common 
optical calculations

"""

import numpy as np
import scipy.constants as const



def diff_limited_spot(wavelength, f,D):
    """Compute the diffraction limited spot size achievable by a lens of 
    focal length f, wavelength lambda, and collimated input beam diameter D.
    Units must match, and will return same in units.
    
    Parameters
    ----------
    wavelength : float
        The wavelength in microns
    f : float
        The focal length of the lens      
    D: float
        The diameter of the collimated input beam        
        
    Returns
    -------
    d: the diffraction limited spot size
    
    """  
    d = (4*wavelength*f)/(np.pi*D)
    return d
    

def fnum(efl,diameter):
    """Compute the F-number from the efl and diameter.  Both have to be the 
    same units.
    
    Parameters
    ----------
    efl : float
        The focal length of the lens
    diameter : float
        The diameter of the input beam (in the same units as efl)
        
    Returns
    -------
    fnum : float
        The fnumber of the system
    """
    fnum = efl/diameter
    return fnum
    
    
def half_angle_from_NA(na, n=1,deg=True):
    """Compute the half angle of the cone of light from the NA value.  From
    the equation NA = n x sin(theta). 
    
    Parameters
    ----------
    na : float
        The numerical aperture
    n : float (optional)
        The index of the material.  Default is 1.0 (air)
    deg : bool (optional)
        Return result in degrees or radians. Default is degrees.
        
    Returns
    -------
    theta : float
        The half angle of the cone of light in degrees
        
    """
    if deg==True:
        theta = np.rad2deg(np.arcsin(na/n))
    else:
        theta = np.arcsin(na/n)
        
    return theta 
    


def snells_law(n1,n2,theta1):
    """Compute the refracted ray angle (theta2) from index1,index2, 
        and angle in (theta1).  Angle must be in the range -90 to 90 deg  
    
    Parameters
    ----------
    n1 : float
        Index of medium for the entering ray
    n2 : float
        Index of the medium the ray is entering into.
    theta1 : float
        Incident ray angle (degrees) measured from normal to the surface        
        
    Returns
    -------
    theta2 : float
        The exiting angle of the ray after refraction (in degress),
        measured from the surface normal.
    """
    
    #need check for within -90 to 90 range, and handle it gracefully
    theta1rad = np.deg2rad(theta1)
    theta2rad = np.arcsin((n1/n2)*np.sin(theta1rad))
    theta2 = np.rad2deg(theta2rad)
    return theta2


def braggs_law():
    """Bragg's Law - unimplemented"""
    pass
    

def irradiance(power,diameter,units='mm'):
    """Compute the irradiance (power per unit area 'W/cm*2') on a surface.
    
    Parameters
    ----------
    power : float
        Power in watts
    diameter : float
        Spot size diameter in mm (default)
    units : String (optinal)
        units, valid = m,mm,um,nm
        
    Returns
    -------
    irrad : float
        The irradiance impinging on the surface in W/cm**2
    """
    
    if units == 'mm':
        d = .1*diameter
        area = np.pi * d
        
    irr = power/area
    return irr

def newton_wedge_fringe_sep(alpha, wavelength):
    """Calculate the separation between fringes for an optical flat with angle
    alpha."""
    
    d = wavelength/(2*np.sin(alpha))
    return d


def sag_depth(R,h):
    """ Calculate sag depth of a shphere at height h.  """
    
    if np.abs(h) > np.abs(R):
        print('height must be less than the raduis')
        return
    else:
        theta = np.arcsin(h/R)
        sag = R*(1-np.cos(theta))
        
    return sag

def abbe_number(nd, nF, nC):
    """ Compute the Abbe number (reciprocal dispersion).  Using the visible F, 
    d, and C lines:
        F(H):  486.1 nm
        d(He): 587.6 nm
        C(H):  656.3 nm
        
    nd, nF, and nC are the refractive indicies at each of these three lines.
    
    Todo: Alternately, select a glass type and compute these three n's.
    
    """
    V = (nd - 1)/(nF - nC)
    return V




