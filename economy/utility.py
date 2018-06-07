'''
Created on Apr 16, 2018

@author: Hendrik Rommeswinkel
'''
import numpy as np

class Utility(object):
    
    def __init__(self, parameters):
        
        """This constructs the utility class
        X =    [v1,v2,...vH,
                x11,x21,...,x1G,f11,f12,...f1F,
                x21,x22,...,x2G,f21,f22,...f2F,
                .
                .
                .
                xH1,xH2,...,xHG,fH1,fH2,...fHF,
                r11,r12,...,r1F,r21,r22,...,r2F,....,rG1,rG2,...,rGF,
                rV1,rV2,...,rVF]
        
        self.parameters['alpha'] = parameters['alpha']
        self.parameters['gamma'] = parameters['gamma']
        self.parameters['beta'] = parameters['exponent']
        self.parameters['theta'] = paramaters['theta']
        """
        self.parameters = parameters


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
    
    def __init__(self, Utility, parameters):
        self.Utility = Utility 
        self.parameters = parameters

        
    def _call__(self, X, i, parameters, env):
        H = env['n_consumers']
        p = self.parameters['c'] / (self.parameters['a']*(self.Utility.X[self.Utilitiy.i] + self.parameters['b']*np.sum[self.Utility.X[0:H]]) + 1)
        u_ill = self.parameters['e'] * self.Utility() - self.parameters['f']
        u_health = self.Utility()
        EU = p * u_ill + (1 - p)*u_health
        return EU
