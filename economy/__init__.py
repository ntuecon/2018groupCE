'''
Created on Apr 16, 2018

@author: Hendrik Rommeswinkel
'''
import numpy as np
from scipy.optimize import minimize
from agents import Consumer, Producer
from utility import GoodFactorUtility,CESUtility,Profit
class Economy(object):
    '''
    classdocs
    '''

    def __init__(self, goods, factors, consumers, producers):
        '''
        Constructor
        '''
        self.consumers = consumers
        self.producers = producers
        self.environment={}
        self.environment['goods']=goods
        self.environment['factors']=factors
    
    def squaredExcessDemand(self, prices):
        '''
        This function calculates the excess demand
        '''
        #It is convenient to have negative factor prices
        """goodsfactorbounds = [(0,None)]*(len(self.environment['goods'])+len(self.environment['factors']))"""
        x0=np.ones(len(self.environment['goods'])+len(self.environment['factors']))
        ed = np.zeros(len(self.environment['goods'])+len(self.environment['factors']))
        for consumer in self.consumers:
            ed+=consumer.optimize(None,constraints=[{'type': 'eq', 'fun': lambda x:sum(x*prices)-consumer.budget},
                                                    {'type':'ineq','fun':lambda x:x}])
        for producer in self.producers:
            producer.environment['goodprices']=prices[0:len(producer.environment['goods'])]
            producer.environment['factorprices']=prices[len(producer.environment['factors'])]
            ed-=producer.optimize(None,[{'type':'ineq','fun':lambda x:x}])
        ed=np.array(ed)
        return np.sum(ed*ed)
            
    def equilibriate(self):
        #We have prices and wages equal to the number of goods and factors
        x0=np.full(len(self.environment['goods'])+len(self.environment['factors']),2.0)
        x1 = np.ones(len(self.environment['goods'])+len(self.environment['factors']),dtype=float)
        #Problems could arise in case some prices are zero, possibly we need to move from using a 0 bound to using exponential prices
        """goodsfactorbounds = ([(0,None)]*(len(self.environment['goods']))).extend([(None,0)]*len(self.environment['factors']))"""
        sol = minimize(self.squaredExcessDemand, x0, method='SLSQP',
                       constraints=[{'type':'ineq','fun':lambda x:x[0:len(self.environment['goods'])]},
                                    {'type':'ineq','fun':lambda x: x[len(self.environment['goods']):]}])
        #A problem could arise since the minimum is not unique. This requires normalizing one price.
        #We can optimize this by supplying the Jacobian to speed up calculations.
        #This function should return a dictionary of prices, allocations, utilities, etc.
        return {'prices':sol['x'], 'excessdemand':sol['fun']}

env={'goods':['X1','X2'],'factors':[]}
goods=['X1','X2']
factors=[]
uparameters_1={'good':{'scale':1.0,'shift':0.0,'weights':np.array([1.0,4.0]),'exponent':1.0,'elasticity':0.5},
                    'factor':{'scale':1.0,'shift':0.0,'weights':np.ones(2,dtype=float),'exponent':2.0,'elasticity':0.5},
                    'scale':1.0,
                    'shift':0.0}
uparameters_2={'good':{'scale':1.0,'shift':0.0,'weights':np.ones(2,dtype=float),'exponent':2.0,'elasticity':0.5},
                    'factor':{'scale':1.0,'shift':0.0,'weights':np.ones(2,dtype=float),'exponent':1.0,'elasticity':0.5},
                    'scale':2.0,
                    'shift':0.0}
Consumer1=Consumer(CESUtility,
                   uparameters_1['good'],
                   env,
                   150)
Consumer2=Consumer(CESUtility,
                   uparameters_2['good'],
                   env,
                   100)
prodparameters={'scale':1.0,'shift':1.0,'exponent':0.5}
Producer1=Producer(Profit,
                   None,
                   env,
                   prodparameters)
                   
MyEconomy=Economy(env['goods'],env['factors'],[Consumer1,Consumer2],[Producer1])
print MyEconomy.equilibriate()
