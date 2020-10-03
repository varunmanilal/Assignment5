import math
from Functions import *
#A function which gives the equation after multiplying coefficients with  the variables
def polyfunc(x,n,coeffs):
    p=0
    for i in (range(1,n+1)):
        if i==n:
            p+=coeffs[i-1]
        else:
            p+=math.pow(x,n-i)*coeffs[i-1]
    return p
#To make it compatible with other functions in library
def func(x):
    return polyfunc(x,n,coeffs)
#main function
def polyroot():
    global n,coeffs
    coeffs = [1,-3,-7,27,-18]
    n=5
    #alpha as the guess
    alpha=-1.5
    while n>1:
        (a,b)= laguerre(alpha,n,func)
        syndiv(coeffs,a)
        n-=1
polyroot()

#-3.0 is one of the root
#The coefficient matrix is  [1, -6.000000000005963, 11.000000000053667, -6.000000000226592, 7.155520620472089e-10]
#1.0 is one of the root
#The coefficient matrix is  [1, -4.999999999966837, 5.9999999998912, -1.0063594402254239e-10, 6.14916118020729e-10]
#2.0 is one of the root
#The coefficient matrix is  [1, -3.0000000000093126, 0.0, -1.0063594402254239e-10, 4.136442299799188e-10]
#3.0 is one of the root
#The coefficient matrix is  [1, 0.0, 0.0, -1.0063594402254239e-10, 1.1173639791135444e-10]