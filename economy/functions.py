'''
This file contains the some global functions for our economy.
The first one is taken from the code supplied by Prof. Hendrik Rommeswinkel and
is concerned with the calculation of the cross product of two vectors.
The second one deals with the calculation of externalities.
'''
import numpy as np

def FlexibleCrossProduct(a, b):
    '''
    This function corrects for different lengths of the c and the weight vector. 
    It treats missing values as zero.
    See https://stackoverflow.com/questions/27096966/multiply-array-of-different-size
    In the future, this function should be extended to allow for multiplication
    of goods vectors that skip goods, etc.
    '''
    return np.append(a,np.zeros(0 if (len(b) - len(a))<0 else (len(b) - len(a))))*np.append(b,np.zeros(0 if (len(a) - len(b))<0 else (len(a) - len(b))))

def externalities(X, H):
    '''
    This is the externalities function. Its input is the number of consumers
    and a array X
    First we create to empty list of lists that are multiplied with the number 
    of consumers to determine the appropriate length.
    Then we iterate over the two newly created elements for the number of 
    consumers to fille the externalites matrix, which the function returns in 
    the end.
    '''
    L = [[]] * H
    EXT = [[]] * H
    for i in range(H):
        L[i] = [j for j in range(H) if j != i]
        EXT[i] = np.sum([X[j] for j in L[i]])
    return EXT
