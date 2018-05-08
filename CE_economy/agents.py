# -*- coding: utf-8 -*-
"""
Created on May 01, 2018

@author: David Biasi
"""

import numpy as np
from scipy.optimize import minimize
from CE_economy.utility import Utility, Cons_util, Profit, Soc_wel
from CE_economy.technology import Linear_tech, CD_tech

class Agent():
    '''
    Parent class for agents in the economy; agents optimise a specific goal 
    that is given by their respective utility functions
    '''
    
    def __init__(self, objective = Utility(), env = None):
        '''
        Constructor
        '''
        self.objective = objective
        self.constraints = []
    
    def optimise(self):
        '''
        This method returns the optimisation for the agent specific objective
        '''
        pass
    
class Consumer(Agent):
    '''
    Class for the consumers in our economy; maximises individual utility with 
    goods entering positively and factors entering negatively into the utility 
    function
    '''
    
    def __init__(self, objective = Cons_util(), alpha, beta, endowment):
        '''
        Constructor
        '''
        self.objective = objective
        self.alpha = alpha
        self.beta = beta
        self.endowment = endowment
    
class Producer(Agent):
    '''
    Class for the producers in our economy; maximises profit with revenue 
    entering positivley and factors entering negatively into the production 
    function
    '''
    
    def __init__(self, objective = Profit(), technology = None, env = None):
        '''
        Constructor
        '''
        self.objective = objective
        self.technology = technology
        self.env = env
        self.constraints = []

class Social_Planner(Agent):
    '''
    Class for the social planner in our economy; maximises social welfare which 
    is defined according to the utilitarian notion of welfare by simply summing 
    up individual utility levels at equal weight
    '''
    
    def __init__(self, objective = Soc_wel(), env = None):
        '''
        Constructor
        '''
        self.objective = objective
        self.env = env
        self.constraints = []