'''
Created on Apr 16, 2018

@author: Hendrik Rommeswinkel
'''
import numpy as np
from functions import FlexibleCrossProduct   

class CESUtility(object):
    def __init__(self, uparameters,i,env):
        self.env=self.env
        self.uparameters=uparameters
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

    def __call__(self, X): 
        '''
        i=0,1,2,...,H
        This makes the utility function a callable function
        '''
        G=self.env['nog']
        F=self.env['nof']
        H=self.env['noc']
        #Here we need to check if the passed parameters c are of the correct datatype
        n=H+self.i*(G+F)
        # r is the exponent inside of the sum. Careful: an elasticity close to zero currently breaks the code. (Requires case distinction)
        nog=len(self.uparameters['alphas'])
        U_goods=(np.dot(self.uparameters['alphas'], X[n : n+G]**self.uparameters['gamma']))**(1/self.uparameters['gamma'])
        U_factors=self.uparameters['beta']*np.sum(np.power(X[n+G : n+G+F],(1+self.uparameters['thetas']))/(1+self.uparameters['thetas']))
        
        #We need to scale and shift the utility function by the appropriate parameters
        U=U_goods-U_factors      
        return U

class ExpectedUtility(object):
    def __init__(self,Utility,extparameters,i,env):

        self.Utility=Utility
        self.extparameters=extparameters
        self.i=i
        self.env=env

        """
        self.extparameters['a'] = extparameters['a']
        self.extparameters['b'] = extparameters['b']
        self.extparameters['c'] = extparameters['c']
        self.extparameters['f'] = extparameters['f']
        
        """
        
    def _call__(self,X,ext):
        """ext=[v1,v2,...,v(H)]"""
        G=self.env['nog']
        F=self.env['nof']
        H=self.env['noc']
        p=self.extparameters['c']/(self.extparameters['a']*(X[self.i]+self.extparameters['b']*np.sum(ext))+1)
        EU=p*(self.Utility(X)-self.extparameters['f'])+(1-p)*self.Utility(X)
        return EU
