'''
Created on Apr 16, 2018

@author: Hendrik Rommeswinkel
'''
import numpy as np

def FlexibleCrossProduct(a,b):
    '''
    This function corrects for different lengths of the c and the weight vector. It treats missing values as zero
    See https://stackoverflow.com/questions/27096966/multiply-array-of-different-size
    In the future, this function should be extended to allow for multiplication of goods vectors that skip goods, etc.
    '''
    return np.append(a,np.zeros(0 if (len(b) - len(a))<0 else (len(b) - len(a))))*np.append(b,np.zeros(0 if (len(a) - len(b))<0 else (len(a) - len(b))))

def externalities(X,noc):
    L=[[]]*noc
    EXT=[[]]*noc
    for i in noc:
        L[i]=[j for j in range(noc) if j!=i]
        EXT[i]=np.sum([X[j] for j in L[i]])
    return EXT
