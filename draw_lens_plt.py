# -*- coding: utf-8 -*-
"""
script to draw a homebrew 2D arc.  patches arc is not working for me.
Want to define the clear aperture and then draw the arc from those points
This is for drawing lenses.

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


mpl.rcParams['lines.linewidth'] = .5


def draw_arc(loc,R,sa):
    
    surf1_x, surf1_y = loc,0  #location of the surface, assume y=0 (optical axis)
    xc,yc = surf1_x + R, 0 #center of sphere  
    
    #setup theta ranges and step size
    theta_max = np.arcsin(sa/R)
    theta_min = -1 * theta_max  #symmetric about the origin    
    theta_steps = 100
    theta_vals = np.linspace(theta_min,theta_max,theta_steps)  
    
    x = np.zeros(len(theta_vals))
    y = np.zeros(len(theta_vals))
    
    for i in range(len(theta_vals)):
        x[i] = xc - R*np.cos(theta_vals[i])
        y[i] = yc - R*np.sin(theta_vals[i])
        
    plt.plot(x,y,'b')
    return x,y
    
def draw_lens(R1,R2,th,sa,loc):
    """ Draw a lens with radii R1 and R2, thickness th, and semi-aperture sa. 
    Todo:  need flats for concave surfaces.
    Need index
    Make a path instead?  Tyr this in draw_lens2
    """ 

    ax = plt.subplot(111)
    x1,y1 = draw_arc(loc,R1,sa)  #draw surface 1 at origin
    x2,y2 = draw_arc(loc+th,R2,sa) #draw surface 2 at th
    ax.plot([x1[0],x2[0]],[y1[0],y2[0]],'b')  #draw lower edge
    ax.plot([x1[-1],x2[-1]],[y1[-1],y2[-1]],'b')  #draw lower edge
    ax.set_aspect('equal')
    #plt.xlim(-20+loc,20+loc)
   

def draw_lens_path(loc, R1, R2, th, sa): 
    """ Draw a lens via path  """
    
    

def draw_triplet():
    """ Draw triplet from KDP """
    
    draw_lens(40.91,1e10,8.74,18.5,0) # element 1
    draw_lens(-55.65,1e10,2.78,14.5,19.8) # element 2
    draw_lens(107.56,-43.33,9.55,15.5,28.6) # element 3
    
    
if __name__ == "__main__":
    
    #example lenses
    plt.figure()
    draw_triplet()
    #calculate system length and scale accordingly.
    #draw_lens(-50,-20,4,10,10)  #later this will come from a spreadsheet, or cmd
    #draw_lens(50,-50,4,10,-10)  # actually, think of the data structure first. json?
                                # then the table can read from it, the plot can, 
                                # but want local datastructure too (not alwyas read and write from file.)
    #plt.axis('off')
    plt.tick_params(
        axis='both',         
        which='both',      # both major and minor ticks are affected
        bottom=False,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off  
        left=False,
        labelleft=False,
        labelbottom=False) # labels along the bottom edge are off
    
    plt.axis('equal')
    plt.show()
    
    # this is where I belong.
    
    
    
    