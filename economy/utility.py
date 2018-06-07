'''
Created on Apr 16, 2018

@author: Hendrik Rommeswinkel
'''
import numpy as np
from functions import FlexibleCrossProduct   
        return u

class CESUtility(object):
    def __init__(self, uparameters):
        self.parameters=parameters
        """X=   [v1,v2,...vH,
                x11,x21,...,xG1,f11,f21,...fF1,
                x12,x22,...,xG2,f12,f22,...fF2,
                .
                .
                .
                x1H,x2H,...,xGH,f1H,f2H,...fFH,
                r11,r12,...,r1F,r21,r22,...,r2F,....,rG1,rG2,...,rGF,rV1,rV2,...,rVF]"""
        
        """
        self.parameters['alphas'] = parameters['alphas']
        self.parameters['gamma'] = parameters['gamma']
        self.parameters['beta'] = parameters['exponent']
        self.parameters['thetas']=paramaters['thetas']
        """

    def __call__(self, X, i,env): 
        '''
        i=0,1,2,...,H
        This makes the utility function a callable function
        '''
        G=env['nog']
        F=env['nof']
        H=env['noc']
        #Here we need to check if the passed parameters c are of the correct datatype
        n=H+i*(G+F)
        # r is the exponent inside of the sum. Careful: an elasticity close to zero currently breaks the code. (Requires case distinction)
        nog=len(self.parameters['alphas'])
        u_goods=(np.dot(self.parameters['alphas'], X[(n) : (nog+1)]**self.parameters['gamma']))**(1/self.parameters['gamma'])
        u_factors=self.parameters['beta']*np.sum(np.power(X[nog+1:55],(1+self.parameters['thetas']))/(1+self.parameters['thetas']))
        
        #We need to scale and shift the utility function by the appropriate parameters
        u=u_goods-u_factors      
        return u

class ExpectedUtility(CESUtility):
    def __init__(self,uparameters,extparameters):
        
        self.uparameters=uparameters
        sefl.extparameters=extparameters

        
    def _call__(self,c,ext):
        EU=CESUtility(self.uparameters)(c)*(1-self.extparameters['c']/((c[0]*self.extparameters['gamma']+np.sum(ext**self.extparameters['gamma']))**(1/self.extparameters['gamma'])+1))

