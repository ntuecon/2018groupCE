'''
Created on Apr 16, 2018

@author: Hendrik Rommeswinkel
'''
import numpy as np
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> parent of c52d92e... Merge branch 'Utility'
from functions import FlexibleCrossProduct,externalities
=======
from functions import FlexibleCrossProduct,externality
from scipy.optimize import minimize
>>>>>>> Final-Projet

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
        nog=len(self.uparameters['alphas'])
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
    def __call__(self,X,ext,penality=0.0,reward=0.0):
        
        G=self.env['G']
        F=self.env['F']
        H=self.env['H']
        p=self.extparameters['a']/((X[self.i]+np.sum(ext))**(1/0.5)+1)
        EU=(1-p)*(self.Utility(X)+reward)+p*(self.Utility(X)-penality)
        return EU


class Social_Welfare(object):

    def __init__(self,consumers,producers,env):
        self.consumers=consumers #list of consumers
        self.producers=producers #list of producer
        self.env=env

    def __call__(self,X,sign=1.0,penality=0.0,reward=0.0):
        G=self.env['G']
        F=self.env['F']
        H=self.env['H']
        res=0
<<<<<<< HEAD
        for consumer in consumers:
            res+=consumer.Expected_Utility(X,X[0:H])
        return res
<<<<<<< HEAD
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
=======
        for consumer in self.consumers:
            res+=consumer.ExpectedUtility(X,externality(X,H,consumer.i),reward,penality)
        return sign*res
    
    

        
        
    
        
        
        
>>>>>>> Final-Projet
=======
>>>>>>> parent of c52d92e... Merge branch 'Utility'
