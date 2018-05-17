'''
Created on Apr 16, 2018

@author: Hendrik Rommeswinkel
'''
import numpy as np
from functions import FlexibleCrossProduct

class Utility(object):
    '''
    An abstract utility class
    '''

    def __init__(self, parameters):
        '''
        Constructor
        '''
        self.parameters = dict()
        #Utility functions can be shifted and scaled
        self.parameters['scale'] = parameters['scale']
        self.parameters['shift'] = parameters['shift']
        #Parameters should be supplied as a dictionary, this has to be checked for
        self.parameters.update(parameters) 
    def __call__(self, c, env):
        '''
        This makes the utility function a callable function
        '''
        
        #Here we need to check if the passed parameters c are of the correct datatype
        
        #We need to scale and shift the utility function by the appropriate parameters
        u= self.parameters['scale'] * np.sum(c) + self.parameters['shift']        
        return u

class CESUtility(Utility):
    '''
    Defines the utility function u = (sum_i a_i*c_i^r )^(a/r)
    Required parameters
    'elasticity' (float)
    'weights' (ndarray of floats)
    'exponent' (float)
    '''
    def __init__(self, parameters):
        '''
        Constructor
        '''
        #Parameters should be stored as a dictionary, this has to be checked for
        self.parameters = dict()
        #Utility functions can be shifted and scaled
        self.parameters['scale'] = parameters['scale']
        self.parameters['shift'] = parameters['shift']
        #The generalized CES function we use has three parameters. The elasticity of substitution, weights for each dimension, and an exponent
        self.parameters['elasticity'] = parameters['elasticity']
        self.parameters['weights'] = parameters['weights']
        self.parameters['exponent'] = parameters['exponent']

    def __call__(self, c):
        '''
        This makes the utility function a callable function
        '''
        
        #Here we need to check if the passed parameters c are of the correct datatype
        
        # r is the exponent inside of the sum. Careful: an elasticity close to zero currently breaks the code. (Requires case distinction)
        r = (1-self.parameters['elasticity'])/self.parameters['elasticity']
        
       
        u = np.sum(FlexibleCrossProduct(self.parameters['weights'], np.power(c,r)))
        u = np.power(u, self.parameters['exponent']/r)
        
        #We need to scale and shift the utility function by the appropriate parameters
        u= self.parameters['scale'] * u + self.parameters['shift']        
        return u

class GoodFactorUtility(Utility):
    '''
    Difference of two CESUtility functions over goods and factors
    Required parameters in two dictionaries 'good' and 'factor'
    'elasticity' (float)
    'weights' (ndarray of floats)
    'exponent' (float)
    '''

    def __init__(self, parameters):
        '''
        Constructor
        '''
        #Parameters should be stored as a dictionary, this has to be checked for
        self.parameters = dict()
        self.parameters['good']=dict()
        self.parameters['good']['scale'] = parameters['good']['scale']
        self.parameters['good']['shift'] = parameters['good']['shift']
        self.parameters['good']['elasticity'] = parameters['good']['elasticity']
        self.parameters['good']['weights'] = parameters['good']['weights']
        self.parameters['good']['exponent'] = parameters['good']['exponent']
        #The scale of the factor utility is negative as it is the disutility of providing the factor
        self.parameters['factor']=dict()
        self.parameters['factor']['scale'] = parameters['factor']['scale']
        self.parameters['factor']['shift'] = parameters['factor']['shift']
        self.parameters['factor']['elasticity'] = parameters['factor']['elasticity']
        self.parameters['factor']['weights'] = parameters['factor']['weights']
        self.parameters['factor']['exponent'] = parameters['factor']['exponent']
        #Utility functions can be shifted and scaled
        self.parameters['scale'] = parameters['scale']
        self.parameters['shift'] = parameters['shift']
        self.goodutility = CESUtility(self.parameters['good'])
        self.factorutility =  CESUtility(self.parameters['factor'])
        self.parameters.update(parameters)
        
        
    def __call__(self, c, env):
        '''
        This makes the utility function a callable function; it returns the utility of a numpy array
        of goods and factors
        '''
        
        #This reshapes the array such that we can access it using familiar field names
        cpart = []
        cpart.append(c[0:len(env['goods'])])
        if len(env['factors'])>0:
            cpart.append(c[len(env['goods']):])
        cpart=np.array(cpart)

        #The utility is simply the sum of the good and factor utilities.
        if len(env['factors'])>0:
            u=self.goodutility(cpart[0]) + self.factorutility(cpart[1])
        else:
            u=self.goodutility(cpart[0])
        #We need to scale and shift the utility function by the appropriate parameters
        u= self.parameters['scale'] * u + self.parameters['shift']        
        return u

class Profit(Utility):
    '''
    A general class for calculating the profit
    '''
    def __call__(self,env,c):
        '''
        This makes the utility function a callable function
        '''
        cpart = []
        cpart.append(c[0:len(env['goods'])])
        cpart.append(c[len(env['goods']):])
        cpart=np.array(cpart)
        
        #'scale' and 'shift' are not necessary here
        u= self.parameters['scale']*(np.sum(cpart[0]*env['goodprices'])-np.sum(cpart[1]*env['factorprices']))+self.parameters['shift']        
        return u
"""
MyGoodFactorUtility=GoodFactorUtility({})
MyGoodFactorUtility(np.array([2,3,1]),{"goods":['X1','X2'],'factors':['F1']})
parameters={'scale':1,'shift':0}
env={'goods':['X1','X2'],'factors':['F1','F1'],'goodprices':np.array([1,2]),'factorprices':np.array([3,3])}
MyProfit=Profit(parameters)
MyProfit(np.array([1,2,3,4]),env)
"""
