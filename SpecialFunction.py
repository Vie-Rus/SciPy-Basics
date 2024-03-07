# SciPy (Scientific Python) - written by V I E R U S
# July 18, 2022
#--------------------------------------------------------------------
#Imports
import numpy as npy
import numpy
from scipy import linalg, integrate, special, signal, constants
from scipy.optimize import least_squares
from scipy.stats import norm, uniform
from numpy import poly1d
#Special Functions--------------------------------------------------------------------------------
    #Provides exponential and trigonometric function
    #Calculate Gaussian Curve - ERF: erf()
    #Calcuate Gamma - Gamma: gamma()
    #Calcuate log of Gamma - Gammaln: gammaln()
    #Calcuate elliptic function - Eppilj: eppilj()
    #Repreents Nth order for the Bessel function - jn

    #Exponents
print("Exponents of 5^10:\n",special.exp10(5))
print("\n")                                             #Empty Space

    #Sin in degree format
print("Sin in Degree format:\n",special.sindg(90))
print("\n")                                             #Empty Space

    #Cos in degree format
print("Cos in degree format:\n",special.cosdg(30))
print("\n")                                             #Empty Space
