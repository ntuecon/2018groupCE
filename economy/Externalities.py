# Externalities : 2 goods, 2 consumers

import numpy as np
from agents import Consumer
from utility import GoodFactorUtility

class Utility_function(object):
    def __init__(self,parameters):
        self.parameters=parameters

    def __call__(self,c,env):
        return (self.parameters['good']['Z']+self.parameters['good']['gamma']*c[2])*c[0]-1/2*c[0]**2+c[1]
    


ConsumerA=Consumer(Utility_function,
                   {'good':{'scale':1.0,'shift':0.0,'Z':1,'gamma':0.0,'exponent':1.0},
                    'scale':1.0,
                    'shift':0.0},
                   {'goods':['X1','X2'],'factors':[],'number of externalities':1},
                   np.ones(2))

ConsumerB=Consumer(Utility_function,
                   {'good':{'scale':1.0,'shift':0.0,'Z':1,'gamma':1,'exponent':1.0},
                    'scale':1.0,
                    'shift':0.0},
                   {'goods':['X1','X2'],'factors':[],'number of externalities':1},
                   np.array([2,2]))
