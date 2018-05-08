# -*- coding: utf-8 -*-
"""
Created on May 02, 2018

@author: David Biasi
"""

import numpy as np

class Utility(object):
    '''
    Abstract parent class for the economy's utility functions
    '''
    
    def __init__(self, parameters = dict()):
        '''
        Constructor
        '''
        self.parameters = dict()
        #Utility functions can be shifted and scaled
        self.parameters['scale'] = float(1)
        self.parameters['shift'] = float(0)
        #Parameters should be supplied as a dictionary, this has to be checked for
        self.parameters.update(parameters)
    
    def __call__(self, c, env = None):
        '''
        This makes the utility function a callable function
        '''
        
        #Here we need to check if the passed parameters c are of the correct datatype
        
        #We need to scale and shift the utility function by the appropriate parameters
        u= self.parameters['scale'] * np.sum(c) + self.parameters['shift']        
        return u

class Cons_Util(Utility):
    '''
    A class for the individual utility of consumer; defines utility in the form
    of 
    '''
    
    def __init__(self, parameters):
        '''
        Constructor
        '''
        pass
    
    def __call__():
        '''
        Making the consumer utility function a callable function
        '''
        pass

class Profit(Utility):
    '''
    A class for the individual utility of consumers
    '''
    
    def __init__(self, parameters):
        '''
        Constructor
        '''
        pass
    
    def __call__():
        '''
        Making the profit function a callable function
        '''
        pass

class Soc_wel(Utility):
    '''
    A class for social welfare functions
    '''
    
    def __init__():
        '''
        Constructor
        '''
        pass
    
    def __call__():
        '''
        Making the social welfare function a callable function
        '''
        pass