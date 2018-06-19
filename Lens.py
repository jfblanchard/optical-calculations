# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 10:38:04 2018

Class to represent an optical lens.

Singlet for now.  maybe later subclass.

"""


import bpy


class Lens:
    """ Start with singlet, constant n, location at center.  
    
    Parameters
    ----------
    
    material: string
        Index of refraction (n).  
    radius1: float
        Radius of curvature for surface1
    radius2: float
        Radius of curvature for surface2
    semi-aper: float
        The semi-aperture (half diameter) of the lens
    location: 1x3 ndarray float
        The x,y,z location of the lens.  Currently center
        
    
    
    """
    
    def __init__(self, material='bk7', radius1, radius2, ct, semi_aper, loc, lens_type='singlet'):
        #what parameters do I want to initialize?  I.E. what does it consist of?
        #singlet, doublet, etc.  Singlet for now  
        #radius of curvature - should be a list becuase the size is not know
        #upon class creation.
        self.r[0] = radius1
        self.r[1] = radius2
        #index (n for now), or glass type
        self.material = material
        
        #index homogeneity, estimate of the bulk material variations in volume
        #would need a 3D index map
        #is there a way to measure this in practice?
        #location - how to define.  midway between outside.  "First" surface.
        #or center? (x,y,z) for now
        self.location = loc
        self.semi_aper = semi-aper
        self.ct = ct
        self.lens_type = lens_time  
        self.num_surfaces = len()
        #other drawing stuff (if mensiscus --- diameter of flat)
        
    
    def draw_mpl(self):
        """ Function to draw in matplotlib
        """
        
        pass   #unimplemented
        
    def draw_opengl(self):
        """Draw in opengl """
        
        pass  #unimplemented
        
                    
    def draw_blender_3D(r1,r2,ct, semi_aper):
        """ Draw the lens in blender.  Later send the object. 
        Uses two UV spheres and a cylinder.
        The lens is created via boolean CSG intersection modifier"""
        
        #calclulate sphere center separation to get the correct ct
        separation = r1 + r2 - ct 
        
        #add first sphere
        bpy.ops.mesh.primitive_uv_sphere_add(size=r1,location=(0,0,0))
        sphere1 = bpy.context.active_object  #most recently added object is current
        
        #add second sphere
        bpy.ops.mesh.primitive_uv_sphere_add(size=r2, location = (0,0,separation))
        sphere2 = bpy.context.active_object
        
        #add a cylinder
        bpy.ops.mesh.primitive_cylinder_add(radius=semi_aper,depth=ct,location=(0,0,(r1-ct)/2))
        cyl = bpy.context.active_object
        
        #CSG Intersect - Sphere1 and Sphere 2
        mod1 = sphere1.modifiers.new('CSG1','BOOLEAN')
        mod1.show_in_editmode = True
        mod1.object = sphere2
        mod1.operation = 'INTERSECT'
        #do I need to apply?
        #sphere2.hide = True   #or remove
        sphere2.select = True
        bpy.ops.object.delete()
        
        #CSG intersect - cylinder (to create lens diameter)
        mod2 = sphere1.modifiers.new('CSG2','BOOLEAN')
        mod2.show_in_editmode = True
        mod2.object = cyl
        mod2.operation = 'INTERSECT'
        #cyl.hide = True   #or remove  
        cyl.select = True
        bpy.ops.object.delete()
        
        
        
        
       
        
        
        

