#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np

def kramer_unsoldt_opacity(dens, Z, A, Zbar, Te, lmbda):
    """
    Computes the  Kramer-Unsoldt opacity [Zel’dovich & Raizer 1967 p 27]
    cf. Thèse de Tommaso
    
    Parameters:
    -----------
     dens: [ndarray] density in (g.cm⁻³)
     Z: [ndarray] atomic number 
     A: [ndarray] atomic mass
     Zbar: [ndarray] ionization
     Te: [ndarray] electron temperature (eV)
     lmdba: [ndarray] wavelength (nm)

    Returns:
    --------
     out: [ndarray] of the same shape as input containing the opacity [cm⁻¹]
    """
                                          # check sign here
    Ibar = 10.4*Z**(4./3) * (Zbar/Z)**2 / (1 - Zbar/Z)**(2./3)
    Ibar = np.fmax(Ibar, 6.0)
    y = 1240./(lmbda * Te)
    y1 = Ibar / Te
    Ni = dens * NA_CST / A
    #print Ibar, y, y1, Ni
    return np.fmax(7.13e-16* Ni * (Zbar + 1)**2 * np.exp(y - y1) / (Te**2*y**3), 1e-16)
