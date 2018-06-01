# optical-tools
Set of functions for performing common optical computations.  It currently consists of a two python files: optical_calcs.py and matrix_optics.py.  

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







