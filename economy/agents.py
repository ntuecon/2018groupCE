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
        self.ExpectedUtility=ExpectedUtility(self.Utility, self.extparameters, 
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

    def __init__(self,consumers,producers,env):
        self.consumers=consumers
        self.producers=producers
        self.env=env
        self.objective=Social_Welfare(consumers,producers,env)

    def Technology_constraint(self,X,prod_help=0.0):
        G=self.env['G']
        F=self.env['F']
        H=self.env['H']
        res=[self.producers[0].Production(X,prod_help)-sum(X[0:H])]
        for g in range(1,G):
            res.append(self.producers[g].Production(X)-sum([X[H+g-1+i*(G-1+F)] for i in range(H)]))
        return res

    def Market_clearance(self,X):
        G=self.env['G']
        F=self.env['F']
        H=self.env['H']
        res=[]
        for f in range(F):
            res.append(sum([X[H+(G-1)*(i+1)+F*i+f] for i in range(H)])-sum([X[H*(G+F)+i*F+f] for i in range(G)]))
        return res

    def maximization(self,penalty,reward,prod_help):
        G=self.env['G']
        F=self.env['F']
        H=self.env['H']
        pbm_size=H*(G+F)+G*F
        X0=np.full(pbm_size,1,dtype=float)
        return minimize(self.objective,X0,args=(-1.0,penalty,reward),method='SLSQP',constraints=[{'type':'eq','fun':lambda X:self.Technology_constraint(X,prod_help)},
                                                                                  {'type':'eq','fun':lambda X:self.Market_clearance(X)},
                                                                                  {'type':'ineq','fun':lambda X:X}])
