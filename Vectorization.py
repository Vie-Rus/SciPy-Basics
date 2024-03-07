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
#Vectorization---------------------------------------------------------------------------------
    #Vectoriztion - converts a normal function into a vectorized function
def maximun (x,y):
    if(x>y):
        return print("Maximun Vectorize is X:\n", x)
    return print("Maximun Vectorize is Y:\n", y)

num9 = npy.vectorize(maximun)([1,-3,7,5],[8,-6,2,4])
print("\n")                                             #Empty Space
