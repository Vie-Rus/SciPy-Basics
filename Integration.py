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
#Integration - Sub-package--------------------------------------------------------------
    #Single integration
num8f = lambda x:x**3
solve6A = integrate.quad(num8f,0,1)
print("Single integral value:\n", solve6A)
print("\n")                                             #Empty Space

    #Double Intergration 
num8f = lambda x,y:x**y
num8g = lambda x:x
num8h = lambda x:x**3
solve6B = integrate.dblquad(num8f,0,1, num8g, num8h)
print("Double integral value:\n", solve6B)
print("\n")                                             #Empty Space

