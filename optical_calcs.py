# -*- coding: utf-8 -*-
"""
A module containing a number of functions used for performing common 
optical calculations

"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const
import seaborn as sns


sns.set_style('whitegrid')

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


def fresnel_refl(n1,n2,theta_i):
    """ Compute the fresnel reflections at a dielectric surface with incident
    index n1, and entering index n2, with incident angle theta_i (in radians).  
    Returns both the S and P polarized reflections. 
    """
    sterm1 = n1 * np.cos(theta_i)
    sterm2 = n2*np.sqrt(1 - ((n1/n2)*np.sin(theta_i))**2)
    Rs = ((sterm1 - sterm2)/(sterm1 + sterm2))**2
    
    pterm1 = n2*np.cos(theta_i)
    pterm2 = n1*np.sqrt(1 - ((n1/n2)*np.sin(theta_i))**2)
    Rp = ((pterm2 - pterm1)/(pterm2 + pterm1))**2
    
    #tested with 0 deg incidence, correct at 4% Reflection
    #T = 1 - R
    
    return Rs,Rp



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




if __name__ == "__main__":
    #test some functions here
    
    #test fresnel
    theta = np.linspace(0,np.pi/2,100)
    Rs,Rp = fresnel_refl(1,1.5,theta)
    
    plt.figure()
    plt.plot(np.rad2deg(theta),Rs, label = 'Rs')
    plt.plot(np.rad2deg(theta),Rp, label = 'Rp')
    plt.title('Fresenel Reflection vs. Angle of incidence')
    plt.xlabel('Angle (deg)')
    plt.ylabel('Reflection')
    plt.legend()
    plt.show()                                       
    