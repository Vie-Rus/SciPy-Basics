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
#Optimization - Sub-package-----------------------------------------------------------------
    #Various optimization algorithms: uncontrained and constrained multivariate, minimization scalar functions, global optimization, least-square minization and curve-fitting functions,
        #minimizers of scalar univariate functions and finder of roots, algorithms to solve multivariate equation systems

    #Optimization
def Opfunc(x):
    return numpy.array([10*(x[1]-x[0]**2), (1-x[0])])

num12 = npy.array([5,5])
solve10 = least_squares(Opfunc, num12)
print("Optimization is:\n",solve10, "\n")
print("\n")                                             #Empty Space
