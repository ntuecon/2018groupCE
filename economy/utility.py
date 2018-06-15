'''
Created on Apr 16, 2018

@author: Hendrik Rommeswinkel
'''
import numpy as np
<<<<<<< HEAD
from functions import FlexibleCrossProduct,externalities

class CESUtility(object):
    def __init__(self, uparameters,i,env):
        self.env=self.env
        self.uparameters=uparameters
        """X=   [v1,v2,...vH,
                x11,x21,...,xG1,f11,f21,...fF1,
                x12,x22,...,xG2,f12,f22,...fF2,
=======

class Utility(object):
    
    def __init__(self, parameters):
        
        """This constructs the utility class
        X =    [v1,v2,...vH,
                x11,x21,...,x1G,f11,f12,...f1F,
                x21,x22,...,x2G,f21,f22,...f2F,
>>>>>>> Utility
                .
                .
                .
                xH1,xH2,...,xHG,fH1,fH2,...fHF,
                r11,r12,...,r1F,r21,r22,...,r2F,....,rG1,rG2,...,rGF,
                rV1,rV2,...,rVF]
        
<<<<<<< HEAD
        """
        self.uparameters['alphas'] = uparameters['alphas']
        self.uparameters['beta'] = uparameters['beta']
=======
        self.parameters['alpha'] = parameters['alpha']
        self.parameters['gamma'] = parameters['gamma']
        self.parameters['beta'] = parameters['exponent']
        self.parameters['theta'] = paramaters['theta']
>>>>>>> Utility
        """
        self.parameters = parameters

<<<<<<< HEAD
    def __call__(self, X): 
        '''
        i=0,1,2,...,H
        This makes the utility function a callable function
        '''
        G=self.env['nog']
        F=self.env['nof']
        H=self.env['noc']
        n=H+self.i*(G+F)
        nog=len(self.uparameters['alphas'])
        U_goods=((self.uparameters['alphas'][0]*X[i]**self.env['gamma']+np.dot(self.uparameters['alphas'][1:], X[n : n+G]**self.env['gamma'])))**(1/self.env['gamma'])
        U_factors=self.uparameters['beta']*np.sum(np.power(X[n+G : n+G+F],(1+self.env['thetas']))/(1+self.env['thetas']))
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
        self.extparameters['e']=extaparameters['e']
        
        """  
    def _call__(self,X,ext):
        """ext=[v1,v2,...,v(H)]"""
        G=self.env['nog']
        F=self.env['nof']
        H=self.env['noc']
        p=self.extparameters['a']/(self.extparameters['b']*(X[self.i]+externalities(X,self.env['noc'])[self.i])+1)
        EU=p*(self.extparameters['c']*self.Utility(X)+self.extparameters['d'])+(1-p)*(self.Utility(X)-self.extparameters['e'])
        return EU


class Social_Welfare(object):

    def __init__(self,consumers,producers,env):
        self.consumers=consumers #list of consumers
        self.producers=producers #list of producer
        self.env=env

    def __call__(X):
        G=self.env['nog']
        F=self.env['nof']
        H=self.env['noc']
        res=0
        for consumer in consumers:
            res+=consumer.Expected_Utility(X,X[0:H])
        return res
=======

    def __call__(self, X, i, env): 
        
        """This makes the utility function a callable function
        i = 0, 1, 2, ..., H
        """
        G = env['n_goods']
        F = env['n_factors']
        H = env['n_consumers']
        
        # Here we need to check if the passed parameters c are of the correct 
        # datatype
        # We define a float that lets us access the relevant line in our matrix
        # X depending on the index of the individual
        n = H + i*(G+F) 
        # Next we compute the utility derived from the goods consumed and the
        # disutility from the factors supplied
        # Functions taken from the lecture slides
        u_goods = np.dot(self.parameters['alpha'], (X[n:(G+n)] ** self.parameters['gamma'])) ** (1/self.parameters['gamma'])
        u_factors = self.parameters['beta'] * np.sum(np.power(X[(n+G): (n+G+F)], (1+self.parameters['theta'])) / (1+self.parameters['theta']))
        
        # Goods factor positively, factors factor negatively into the utility 
        # function
        u = u_goods - u_factors      
        return u


class Expected_Utility(object):
    
    def __init__(self, X, i, Utility, parameters):
        self.X = X
        self.i = i
        self.Utility = Utility 
        self.parameters = parameters

        
    def _call__(self, X, i, parameters, env):
        H = env['n_consumers']
        p = self.parameters['c'] / (self.parameters['a']*(self.X[self.i] + self.parameters['b']*np.sum[self.X[0:H]]) + 1)
        u_ill = self.parameters['e'] * self.Utility(X, i, env) - self.parameters['f']
        u_health = self.Utility(X, i, env)
        EU = p * u_ill + (1 - p)*u_health
        return EU
>>>>>>> Utility
