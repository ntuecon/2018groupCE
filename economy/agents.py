'''
Created on Apr 16, 2018

@author: Hendrik Rommeswinkel
'''
import numpy as np
from scipy.optimize import minimize
from utility import Utility,Profit,GoodFactorUtility,CESUtility
from technology import LinearTechnology
from technology import DRSTechnology

class Agent(object):
    '''
    An agent contains an objective. When asked to optimize(), the agent maximizes the objective given constraints and bounds on the variables.
    '''
    def __init__(self, env, objective, constraints):
        '''
        Constructor
        '''
        self.objective = objective
        self.constraints = constraints
        #Perhaps the env should instead be an argument to optimize()?
        
        #In case an environment is provided, use this environment
        self.env = env
        #The problemsize needs to be manually rewritten in case it is not equal to 1
        self.problemsize = 1
    
    def optimize(self,bounds,constraints):
        #The env tells us how large the dimension of the initial guess has to be
        x0 = np.ones(self.problemsize)
        
        opt = minimize(self.objective, x0, method='SLSQP', bounds=bounds, constraints=constraints)
        if opt['success']==0:
            # If the optimization problem could not be solved, we need to raise an error.
            raise ValueError("Optimization problem could not be solved.")
        return opt['x']
    
class Consumer(Agent):
    '''
    A consumer is an agent who has a utility function as the objective and no internal constraints
    Setting env is required as there are both goods and factors to be chosen
    Constraints for the consumer need to be supplied by the economy
    '''
    def __init__(self,objective,uparameters,environment,budget):
        '''
        Constructor
        '''
        self.environment = environment
        self.problemsize = len(self.environment['goods']) + len(self.environment['factors'])
        if objective==CESUtility:
            self.objective = lambda c: -objective (uparameters)(c)
        elif objective==GoodFactorUtility:
            self.objective=lambda c:-objective (uparameters,environment)(c)
        else:
            self.objective=objective

        self.budget=budget


class Producer(Agent):
    '''
    A producer is an agent who has a technology as a constraint and maximizes payoffs
    
    The economy needs to supply prices
    '''
    def __init__(self, objective, technology, environment,parameters):
        '''
        Constructor
        '''
        self.parameters=parameters
        self.environment=environment
        if objective==Profit:
            self.objective=lambda c: Profit(self.parameters)(c,self.environment)
        else:
            self.objective = objective
        if technology == None:
            self.technology = DRSTechnology(self.environment)
        self.constraints = [{'type': 'ineq', 'fun':technology}]
        
        #In case an environment is provided, use this environment
        self.problemsize = len(self.environment['goods']) + len(self.environment['factors'])


        '''
        For a producer, optimization is slightly different since for a linear technology the optimum is not unique.
        '''
        """if self.technology==LinearTechnology:
            raise ValueError("No support for linear technologies yet")
        else:
            pass"""

        
        
class Government(Agent):
    '''
    The government maximizes a social welfare function. We assume a utilitarian SWF.
    '''
    def __init__(self, objective, env=None):
        '''
        Constructor
        '''
        self.objective = objective
        self.constraints = {}
        
        #In case an environment is provided, use this environment
        self.env = env
        #The problem size for the government is the number of consumers among who to do lump-sum transfers
        #We only need to redistribute a single good lump-sum for a well-behaved problem. More generally, we could redistribute all goods lump-sum.
        self.problemsize = len(self.env['consumers'])


env={'goods':['X1','X2'],'factors':[],'goodprices':[1,2],'factorprices':[1.5]}
prices=np.array([2.0,1.5,-1.5,-2.5])
iendowment=np.array([2,4,2,1])
MyConsumer=Consumer(CESUtility,
                    {'good':{'scale':1.0,'shift':0.0,'weights':np.array([1.0,2.0]),'exponent':1.0,'elasticity':0.5},
                    'factor':{'scale':1.0,'shift':0.0,'weights':np.ones(2,dtype=float),'exponent':1.0,'elasticity':0.5},
                    'scale':1.0,
                    'shift':0.0}['good'],
                    env,
                    10)

MyConsumer.optimize(None,{'type':'eq','fun':lambda x:sum(x*[1.0,2.0])-MyConsumer.budget})


                                       

