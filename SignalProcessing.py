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
#Signal Processing - Sub-package---------------------------------------------------------------
    #This involves: Generation, Analyzing, modifying various signals, designing, filtering, interpolation 1D(not the band) and 2D
    #Resampling
num10 = npy.linspace(-10,10,20)
solve7 = npy.abs(num10)
Resolve7 = signal.resample(solve7, 10)
print("Before sampling:\n", solve7,"\n")
print("After resampling:\n", Resolve7)
print("\n")                                             #Empty Space

    #Detrending - to remove linear element of the signal
num10 = npy.linspace(-10,10,20)
solve8 = npy.cos(num10)+num10
Desolve8 = signal.detrend(solve8)
print("Before detrending:\n", solve8, "\n")
print("After Detreading:\n", Desolve8)
print("\n")                                             #Empty Space

    #Ordered Filtering
num11 = npy.arange(20).reshape(4,5)
dom = npy.identity(3)
solve9 = signal.order_filter(num11, dom, 1)
print("Before Filtering", num11, "\n")
print("After Filtering", solve9, "\n")
print("\n")                                             #Empty Space
