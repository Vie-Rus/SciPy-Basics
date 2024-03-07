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
#Linear Algebra - Sub-Package--------------------------------------------------------------------
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