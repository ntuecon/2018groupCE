'''
Created on Apr 16, 2018
@author: Hendrik Rommeswinkel
'''
import numpy as np
from scipy.optimize import minimize
from utility import CESUtility, ExpectedUtility, Social_Welfare
from technology import Technology
from scipy.optimize import minimize


class Consumer(object):
    
    def __init__(self,uparameters,extparameters,i,env):
        
        self.i=i
        self.uparameters=uparameters
        self.extparameters=extparameters
        self.env = env
        self.Utility = CESUtility(self.uparameters,self.i,self.env)
        self.ExpectedUtility=ExpectedUtility(self.Utility,self.extparameters,self.i,self.env)
        

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

    def maximization(self,penality,reward,prod_help):
        G=self.env['G']
        F=self.env['F']
        H=self.env['H']
        pbm_size=H*(G+F)+G*F
        X0=np.full(pbm_size,1,dtype=float)
        return minimize(self.objective,X0,args=(-1.0,penality,reward),method='SLSQP',constraints=[{'type':'eq','fun':lambda X:self.Technology_constraint(X,prod_help)},
                                                                                  {'type':'eq','fun':lambda X:self.Market_clearance(X)},
                                                                                  {'type':'ineq','fun':lambda X:X}])
