#Learn optimization - The basics

"""Import the useful tools"""
import numpy as np
from scipy.optimize import minimize

#Optimization without constraint
"""Let's minimize g(x)=x²-2x+2. RESULT=1"""

"""Define g"""
def g(x):
    return x**2-2*x+2

"""Give a scalar (using np.array) x0 such as you think that min g=g(x0) (the value of x0 doesn't matter)"""
x0=np.array([2])

"""Compute the minimization :
    1. First argument : the function
    2. Second argument : an array """
min_g=minimize(g,x0)
print "Minimization of g \n",min_g,"\n \n"

#Optimization with constraints
"""Let's minimize h(x,y,z)=2x+2y+2z-1 under the constraint x²+y²+z²=3. RESULT=[1,1,1]"""

"""define h. x is an array with a lenght of 3"""
def h(x):
    return 2*x[0]+2*x[1]+2*x[2]-1

"""Give an array x0 with lenght 3"""
x0=np.array([-1,1,0])

"""Define the constraints (tuple of dictionnaries)(Here only one dictionary because one constraint) :
    1.The type of the constraint. "eq" for equality and "ineq" for inequality.
    2.The function of the constraint.
        -if the type is an equality then the constraint is the function equal to 0.
        -if the type is an inequality then the constraints is the function non-negative."""
cons={"type":"eq","fun":lambda x:x[0]**2+x[1]**2+x[2]**2-3}

"""Compute the minimization using SLSPQ method"""
min_h=minimize(h,x0,method="SLSQP",constraints=cons)
print "Minimization of h \n",min_h


