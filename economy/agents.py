'''
This file creates classes for the agents of our economy.
These are the consumers, the producers, and the social planner.
This file utilitses sum of the code supplied by Prof. Hendrik Rommeswinkel, 
but modifies it to fit our needs.
'''

import numpy as np
from scipy.optimize import minimize

from utility import CESUtility, ExpectedUtility, Social_Welfare
from technology import Technology


class Consumer(object):
    '''
    This is the consumer class. 
    A consumer is an object that is defined by its utility and some extra 
    parameters, his index, and an environment containing additional global 
    parameters.
    '''
    
    def __init__(self, uparameters, extparameters, i, env):
        '''
        This constructs the consumer classs.
        '''
        
        self.i = i
        self.uparameters = uparameters
        self.extparameters = extparameters
        self.env = env
        self.Utility = CESUtility(self.uparameters,self.i,self.env)
        self.Expected_Utility=Expected_Utility(self.Utility, self.extparameters, 
                                               self.i, self.env)
        

class Producer(object):
    '''
    This is the producer class. 
    A producer is an object that is defined by his parameters, his index, and 
    an environment containing additional global parameters.
    '''

    def __init__(self, parameters, i, env):
        '''
        This constructs the producer class.
        '''
        
        self.i = i
        self.env = env
        self.parameters = parameters
        self.Production = Technology(self.parameters, self.i, self.env)

class SocialPlanner(object):
    '''
    This is the SocialPlanner class. 
    The SocialPlanner is an object that is defined by the consumers and 
    producers of the economy, and an environment containing additional global 
    parameters.
    '''
    

    def __init__(self, consumers, producers, env):
        '''
        This constructs the SocialPlanner class.
        '''
        
        self.consumers = consumers
        self.producers = producers
        self.env = env
        self.AggregateWelfare = Social_Welfare(consumers, producers, env)

    def constraints(self):
        pass
    
    def maximization(self):
        pass




                                       

