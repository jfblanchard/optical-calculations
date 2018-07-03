# optical-tools
Set of functions for performing common optical computations.  Module descriptions below.

<h3>Optical_calcs.py</h3>

Module Functions
1. Diffraction limited spot size calculation.
2. Determine F-number from EFL and aperture diameter.
3. Calculate half angle from NA (numerical aperture).
4. Snells law to compute angle of refraction.
5. Irradiance in W/cm^2
6. Paraxial Optical Computations, which include:
- Object and Image distance calculations given EFL and magnification
- Thin lens image distance
- EFL of two thin lenses
- Thick lens EFL given two surface radii, index and center thickness
- Thin prism deviation


<h3>Matrix_optics.py</h3>

Matrix Functions
- Create an optical ray suitable for matrix propagation.
- General transfer matrix from (A, B, C, D) parameters
- Free space propagation matrix
- Refraction matrix
- Thin lens matrix
- Ray propagation function

<h3>read_ohara.py</h3>

Parse the ohara downloaded catalog (csv format), and creates a new cleaned up
data frame with glass type and sellmeier coeffs for all glass types.  Output 
in json and binary (pickled)formats.

Also prints out an interactive plot of the glass types.  Glass name and index are
displayed when hovered over with the cursor.


![Ohara Glass map](/images/ohara_glass_map.png)


* Currently uses Ohara file version 20171130
* Todo: Add Schott catalog

<h3>zernike.py</h3>

Plot Zernike polynomials.  Indexing uses the OSA/ANSI single index scheme.  Can plot the first 14 modes.

Some example screenshots below:

![Horizontal Tilt](/images/horiz_tilt.png)
![Defocus](/images/defocus.png)
![Horizontal Coma](/images/horiz_coma.png)
![Vertical Astigmatism](/images/vert_astigmatism.png)
![Oblique Trefoil](/images/oblique_trefoil.png)
![Vertical Quadrafoil](/images/vert_quadrafoil.png)









