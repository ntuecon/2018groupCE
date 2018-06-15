'''
Created on Apr 16, 2018

@author: Hendrik Rommeswinkel
'''
import numpy as np
from scipy.optimize import minimize
from utility import CESUtility, ExpectedUtility, Social_Welfare
from technology import Technology
class Consumer(object):
    
    def __init__(self,uparameters,extparameters,i,env):
        
        self.i=i
        self.uparameters=uparameters
        self.extparameters=extparameters
        self.env = env
        self.Utility = CESUtility(self.uparameters,self.i,self.env)
        self.Expected_Utility=Expected_Utility(self.Utility,self.extparameters,self.i,self.env)
        

class Producer(object):

    def __init__(self,parameters,i,env):
        self.i=i
        self.env=env
        self.parameters=parameters
        self.Production=Technology(self.parameters,self.i,self.env)

class SocialPlanner(object):

    def __init__(self,consumers,producers,env):
        self.consumers=consumers
        self.producers=producers
        self.env=env
        self.AggregateWelfare=Social_Welfare(consumers,producers,env)

    def constraints(self):
        pass
    def maximization(self):
        pass




                                       

