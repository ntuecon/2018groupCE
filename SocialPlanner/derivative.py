import numpy as np
from scipy.misc import derivative

def partial_derivative(func, var=0, point=[]):
    args = point[:]
    def wraps(x):
        args[var] = x
        return func(*args)
    return derivative(wraps, point[var], dx = 1e-6)

def MRSh_hkhl(utility,k,l,point):
    

def MRSh_ikh1(utility_i,utility_h,k,l=0,point):


def MRT_
