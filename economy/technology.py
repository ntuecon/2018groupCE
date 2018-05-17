'''
Created on Apr 16, 2018

@author: Hendrik Rommeswinkel
'''
import numpy as np
from functions import FlexibleCrossProduct
from utility import CESUtility


class Technology(object):
    '''
    classdocs
    '''
    def __init__(self, parameters):
        '''
        Constructor
        '''
        self.parameters = dict()
        """self.parameters.update(parameters)"""
    def __call__(self,c):
        '''
        This returns the constraint value. If the value is positive, the constraint is fulfilled.
        '''
        return 0
class LinearTechnology(object):
    '''
    classdocs
    '''
    def __init__(self, parameters):
        '''
        Constructor
        '''
        self.parameters = dict()
        self.parameters=parameters
        """self.parameters.update(parameters)"""
    def __call__(self,output,factors):
        '''
        This returns the constraint value. If the value is positive, the constraint is fulfilled.
        '''
        return output - FlexibleCrossProduct(self.parameters['linear'], factors)

class DRSTechnology(object):
    '''
    This technology has constant decreasing returns to scale
    '''
    def __init__(self, tech_parameters):
        '''
        Constructor
        '''
        self.tech_parameters = tech_parameters
        
    def __call__(self,factors):
        '''
        This returns the constraint value. If the value is positive, the constraint is fulfilled.
        '''
        #for the power, a flexible version also needs to be introduced in case we want changing exponents.
        return CESUtility(self.tech_parameters)(factors)
