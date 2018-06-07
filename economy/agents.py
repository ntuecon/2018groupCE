'''
Created on Apr 16, 2018

@author: Hendrik Rommeswinkel
'''
import numpy as np
from scipy.optimize import minimize
from utility import CESUtility, ExpectedUtility
class Consumer(object):
    
    def __init__(self,i,environment, uparameters):
        
        self.i=i
        self.uparameters=uparameters
        self.extparameters=extparameters
        self.env = env
        self.Utility = CESUtility(self.uparameters,self.i,self.env)
        self.Expected_Utility=Expected_Utility(self.Utility,self.extparameters,self.i,self.env)
        

class Producer(object):
    pass

        
        
class Government(object):
    pass




                                       

