# -*- coding: utf-8 -*-
"""
Created on May 02, 2018

@author: David Biasi
"""

import numpy as np

class Technology(object):
    '''
    Technology class
    '''
    
    def __init__(self, parameters):
        '''
        Constructor
        '''
        self.parameters = dict()
        self.parameters.update(parameters)
    
    def __call__(self, c):
        '''
        This returns
        '''
        return 0


class Cobb_Douglas_tech(Technology):
    '''
    This is a classical CES production function as proposed by Solow et al.;
    it assumes that production only relies on two factors, labour and capital, 
    and on total factor productivity: 
    Q = F * (a * K^r + (1 - a) * L^r) ^ (1/r)
    where Q is the quantitiy of output,
    K is capital input,
    L is labour input,
    F is total factor productivity,
    a is the share factor, and
    s = 1/(1 - r) is the elasticity of substition with r = (s -1)/s.
    With r = 1 we get a linear or perfect substition function,
    with r --> 0 we get a Cobb-Douglas-Production function, and
    with r --> - infinity we get a Leontief or perfect complements production 
    function.
    '''
    
    def __init__(self, parameters, special = None):
        '''
        Constructor
        '''
        parameters = dict()
        self.parameters['a'] = float()
        self.parameters['F'] = float()
        self.parameters['s'] = np.zeros(len(goods)) #goods vector needs to be defined somewhere
        self.parameters['r'] = (self.parameters['s'] - 1) / self.parameters['s']
        self.parameters.update(parameters)
    
    def __call__(self, capital, labour):
        '''
        Making the Cobb-Douglas-function a callable function
        '''
        K = self.capital
        L = self.labour
        q = self.parameters['F'] * (self.parameters['a'] * K^self.parameters['r'])\
        + (1 - self.parameters['a'] * L^self.parameters['r']) ^ (1/self.parameters['r'])
        return q

class CES_tech(Technology):
    '''
    This function takes the form of the general CES production function:
    Q = F * [sum_i=1_n a_i X_i^r](1/r)
    where Q is the quantity of output for a particular good,
    F is the total factor productivity,
    a_i is the share parameter of output for factor i with sum_i=1_n a_i = 1,
    X_i is the quantity of input for factor i,
    s = 1 / (1 - r) is the elasticity of substitution
    '''
    
    def __init__(self, parameters):
        '''
        Constructor
        '''
        parameters = dict()
        self.parameters['a'] = np.array() #of len(factors); maybe list? 
        self.parameters['F'] = float()
        self.parameters['s'] = np.zeros(len(goods)) #goods vector needs to be defined
        self.paremeters['r'] = (self.parameters['s'] - 1) / self.parameters['s']
        self.parameters.update(parameters)
    
    def __call__(self, X):
        '''
        Making the general CES function a callable function
        '''
        X = np.array()
        q = 0
        for i in len(X):
            q += self.parameters['a'][i] * (X[i] ^ self.parameters['r'])
        q = q ^ (1/self.parameters['r'])
        return q
        