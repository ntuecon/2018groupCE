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
        nog=len(self.environment['goods'])
        nof=len(self.environment['factors'])
        ed = np.zeros(nog+nof)
        for consumer in self.consumers:
            ed+=consumer.optimize(None,constraints=[{'type':'eq', 'fun': lambda x:-sum(x*prices)},
                                                    {'type':'ineq','fun':lambda x:x}])
        for producer in self.producers:
            producer.environment['goodprices']=prices[0:nog]
            producer.environment['factorprices']=prices[nog:]
            ed-=producer.optimize(None,constraints=[{'type':'ineq','fun':lambda x:x},
                                                    {'type':'ineq','fun':lambda x:producer.technology(x[nog:])-producer.technology(producer.fact_endowment)}])
        ed=np.array(ed)
        return np.sum(ed*ed)
            
    def equilibriate(self):
        #We have prices and wages equal to the number of goods and factors
        nog=len(self.environment['goods'])
        nof=len(self.environment['factors'])
        x0=np.zeros(nog+nof)
        x0[0:nog]=np.full(nog,3,dtype=float)
        x0[nog:]=np.full(nof,-2,dtype=float)
        #Problems could arise in case some prices are zero, possibly we need to move from using a 0 bound to using exponential prices
        sol = minimize(self.squaredExcessDemand, x0, method='SLSQP',
                       constraints=[{'type':'ineq','fun':lambda x:x[0:nog]},
                                    {'type':'ineq','fun':lambda x:-x[nog:]}])
        #A problem could arise since the minimum is not unique. This requires normalizing one price.
        #We can optimize this by supplying the Jacobian to speed up calculations.
        #This function should return a dictionary of prices, allocations, utilities, etc.
        return {'prices':sol['x'], 'excessdemand':sol['fun']}

env={'goods':['X1','X2'],'factors':['F1','F2']}
goods=['X1','X2']
factors=['F1','F2']
uparameters_1={'good':{'scale':1.0,'shift':0.0,'weights':np.array([1.0,4.0]),'exponent':1.0,'elasticity':0.5},
               'factor':{'scale':1.0,'shift':0.0,'weights':np.array([1.0,4.0]),'exponent':1.0,'elasticity':0.5},
               'scale':1.0,
               'shift':0.0}
uparameters_2={'good':{'scale':1.0,'shift':0.0,'weights':np.array([4.0,2.0]),'exponent':1.0,'elasticity':0.5},
               'factor':{'scale':1.0,'shift':0.0,'weights':np.array([3.0,4.0]),'exponent':1.0,'elasticity':0.5},
               'scale':1.0,
               'shift':0.0}
Consumer1=Consumer(GoodFactorUtility,
                   uparameters_1,
                   env,
                   15)
Consumer2=Consumer(GoodFactorUtility,
                   uparameters_2,
                   env,
                   10)
tech_parameters={'scale':1.0,'shift':1.0,'exponent':1.0,'elasticity':2.0,'weights':[4.0,6.0]}
Producer1=Producer(Profit,
                   None,
                   tech_parameters,
                   env,
                   [2.0,6.0])
                   
MyEconomy=Economy(goods,factors,[Consumer1,Consumer2],[])
print MyEconomy.equilibriate()
