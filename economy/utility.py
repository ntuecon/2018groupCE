import numpy as np
from functions import FlexibleCrossProduct,externalities
from scipy.optimize import minimize

class CESUtility(object):
    def __init__(self, uparameters,i,env):
        self.env=env
        self.uparameters=uparameters
        self.i=i
        """X=   [v1,v2,...vH,
                x11,x21,...,xG1,f11,f21,...fF1,
                x12,x22,...,xG2,f12,f22,...fF2,
                .
                .
                .
                x1H,x2H,...,xGH,f1H,f2H,...fFH,
                r11,r12,...,r1F,r21,r22,...,r2F,....,rG1,rG2,...,rGF,rV1,rV2,...,rVF]"""
        
        """
        self.uparameters['alphas'] = uparameters['alphas']
        self.uparameters['beta'] = uparameters['beta']
        """

    def __call__(self, X): 
        '''
        i=0,1,2,...,H
        This makes the utility function a callable function
        '''
        G=self.env['G']
        F=self.env['F']
        H=self.env['H']
        n=H+self.i*(G-1+F)
        U_goods=((self.uparameters['alphas'][0]*X[self.i]**self.env['gamma']+np.dot(self.uparameters['alphas'][1:], X[n : n+G-1]**self.env['gamma'])))**(1/self.env['gamma'])
        U_factors=self.uparameters['beta']*np.sum(np.power(X[n+G-1 : n+G-1+F],(1+self.env['thetas']))/(1+self.env['thetas']))
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
        
        """  
    def __call__(self,X,ext,penalty=0.0,reward=0.0):
        
        G=self.env['G']
        F=self.env['F']
        H=self.env['H']
        p=self.extparameters['a']/(X[self.i]+np.sum(ext)+1)
        EU=(1-p)*self.Utility(X)-p*penalty+(1-p)*reward
        return EU


class Social_Welfare(object):

    def __init__(self,consumers,producers,env):
        self.consumers=consumers #list of consumers
        self.producers=producers #list of producer
        self.env=env

    def __call__(self,X,sign=1.0,penalty=0.0,reward=0.0):
        G=self.env['G']
        F=self.env['F']
        H=self.env['H']
        res=0
        for consumer in self.consumers:
            res+=consumer.ExpectedUtility(X,externalities(X,H)[consumer.i],penalty,reward)
        return sign*res
