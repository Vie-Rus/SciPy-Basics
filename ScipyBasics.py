# SciPy (Scientific Python) - written by V I E R U S
# July 18, 2022
# 
#--------------------------------------------------------------------
#Imports
import numpy as npy
import numpy
from scipy import linalg, integrate, special, signal, constants
from scipy.optimize import least_squares
from scipy.stats import norm, uniform
from numpy import poly1d


#Linear Algebra - Sub-package-------------------------------------------------------------------------------------
    #Linear Equations Ex: 2x+y=5; 4y-5x=7
num1 = npy.array([[2,1], [4,-5]])                     #input array
num2 = npy.array([[5],[7]])                           #"answers" to equation

solve1 = linalg.solve(num1, num2)
print("Basic Linear Equation:\n", solve1)             #Print 
print("\n")                                           #Empty Space


    #To check if solve1 is correct, plug it back into the equation, if they are 0 they are correct
print("Plug back into the equation:\n", num1.dot(solve1) - num2)
print("\n")                                             #Empty Space


    #Inverse of a matrix
num3 = npy.array([[1,2,3],[4,5,6],[3,4,3]])             #created a 3D matrix
solve2 = linalg.inv(num3)                               #Use the inv function to find inverse
print(f'Inverse of:\n{num3}\n\nis:\n {solve2}')         #print
print("\n")                                             #Empty Space


    #Singular Value Decomposition (svd) - product of two orthonormal matrices and a diagonal matrix
num4 = npy.array([[1,2,3],[4,5,6]])
solve3 = linalg.svd(num4)
print("Singular Value Decomposition:\n", solve3)
print("\n")                                             #Empty Space


    #Lower and Upper triangular matrices
num5 = npy.array([[1,2,3],[4,5,6]])
solve4 = linalg.lu(num5)
print("Lower and Upper Triangular Matrices:\n", solve4)
print("\n")                                             #Empty Space


    #Finding eigenvalues and eigenvectors
num6 = npy.array([[1,2,3],[4,5,6],[3,4,3]])
solve5vals, solve5vects = linalg.eig(num6)
print("Eigenvalues:\n", solve5vals, "\n\n")
print("Eigenvectors:\n", solve5vects)
print("\n")                                             #Empty Space


    #Polynominals - Sub-package
num7 = poly1d([1,3,5])
print("polynomial is:\n", num7, "\n")                         #prints: 1x^2 + 3x + 5


    #Polynominal where x has a value
print("polynomial is:\n", num7(7), "\n") 


    #Polynominal with the product with itself
print("polynomial is:\n", num7*num7,"\n") 


    #Polynominal with Integration
print("polynomial is:\n", num7.integ(k=4), "\n") 


    #Polynominal with differentiation
print("polynomial is:\n", num7.deriv()) 
print("\n")                                             #Empty Space


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


#Vectorization---------------------------------------------------------------------------------
    #Vectoriztion - converts a normal function into a vectorized function
def maximun (x,y):
    if(x>y):
        return print("Maximun Vectorize is X:\n", x)
    return print("Maximun Vectorize is Y:\n", y)

num9 = npy.vectorize(maximun)([1,-3,7,5],[8,-6,2,4])
print("\n")                                             #Empty Space


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


#Signal Processing - Sub-package--------------------------------------------------------------------------------
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


#Optimization - Sub-package--------------------------------------------------------------------------------
    #Various optimization algorithms: uncontrained and constrained multivariate, minimization scalar functions, global optimization, least-square minization and curve-fitting functions,
        #minimizers of scalar univariate functions and finder of roots, algorithms to solve multivariate equation systems

    #Optimization
def Opfunc(x):
    return numpy.array([10*(x[1]-x[0]**2), (1-x[0])])

num12 = npy.array([5,5])
solve10 = least_squares(Opfunc, num12)
print("Optimization is:\n",solve10, "\n")
print("\n")                                             #Empty Space


#Statics - Sub-package--------------------------------------------------------------------------------------
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


#Constant Unit - Sub-package----------------------------------------------------------------------------------
    #You can use Metric, Binary , Mass, Angle, Time, Length, Pressure, Area, Volume, Speed, Temperature, Energy, Power, and Force prefixes
    #To see all constants use dir
print(dir(constants))
print("\n\n")



print("END OF SCIPY BASIC")