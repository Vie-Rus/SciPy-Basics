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
#Statics - Sub-package---------------------------------------------------------------------------
    #Cumulative Distribution
num13 = norm.cdf(numpy.array([1,-1.,3,1,0,4,-6,2]))
print("Cumulative Distribution:\n", num13)
print("\n")                                             #Empty Space

    #Percentage Point
num14 = norm.ppf(0.6)
print("Percent point:\n", num14)
print("\n")                                             #Empty Space

    #Random Variant Sequence
num15 = norm.rvs(size=6)
print("Random variant sequence:\n", num15)
print("\n")                                             #Empty Space

    #Binomial Distribution
num16 = uniform.cdf([2,4,6,8], scale=3)
print("Binominal Distribution:\n", num16)
print("\n\n")                                             #Empty Space
