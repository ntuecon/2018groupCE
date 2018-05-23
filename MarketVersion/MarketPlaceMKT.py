#import ConsumerCES_class as cons
import numpy as np
from scipy.optimize import minimize
from ConsumerCES_original import Consumer
from EnvironmentMKT_class import Environment
from ProducerMKT_class import Producer

Env=Environment
class Market:
    def __init__(self,environment):
        self.env=environment

    def Square_Excess_Demand(self,prices):
        res=np.zeros(self.env['ng']+self.env['nf'])
        theta=self.env['Factor_sup']
        for i in range(self.env['nt']):
            alpha=self.env['Agent_Types'][str(i)][0:self.env['ng']]
            beta=self.env['Agent_Types'][str(i)][self.env['ng']]
            People_i=Consumer(alpha,beta,theta,self.env)
            C_vec0=np.full(self.env['ng']+self.env['nf'],1,dtype=float)
            res+=minimize(People_i,C_vec0,args=(-1.0),method='SLSQP',constraints=[{'type':'eq','fun':lambda x:sum((x*prices)[self.env['ng']:])-sum((x*prices)[0:self.env['ng']])},
                                                                                  {'type':'ineq','fun':lambda x:x}])['x']*self.env['nc'][str(i)]
        Prod_max=np.zeros(self.env['ng']+self.env['nf'])
        for i in range(self.env['ng']):
            psi=self.env['Production_Pars'][str(i)][0:self.env['ng']]
            ksi=self.env['Production_Pars'][str(i)][self.env['ng']]
            Production_i=Producer(psi,ksi,self.env)
            P_Vec0=np.full(self.env['nf'],1,dtype=float)
            Prod_max=np.zeros(self.env['ng']+self.env['nf'])
            Prod_max[self.env['ng']:]+=minimize(Production_i,P_Vec0,args=(-1.0),method='SLSQP',constraints=[{'type':'ineq','fun':lambda x:x},
                                                                                                            {'type':'ineq','fun':lambda x:Production_i(x)*prices[i]-sum(x*prices[self.env['ng']:])}])['x']
            Prod_max[i]=-minimize(Production_i,P_Vec0,args=(-1.0),method='SLSQP',constraints=[{'type':'ineq','fun':lambda x:x},
                                                                                              {'type':'ineq','fun':lambda x:Production_i(x)*prices[i]-sum(x*prices[self.env['ng']:])}])['fun']
        res-=Prod_max
        return np.sum(res)**2

    def Price_Equilibrium(self):
        p0=np.full(self.env['ng']+self.env['nf'],10,dtype=float)
        return minimize(self.Square_Excess_Demand,p0,method='SLSQP',constraints={'type':'ineq','fun':lambda x:x})

    def __call__(self,prices):
        pass

        
