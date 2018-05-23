import numpy as np
from scipy.optimize import minimize
class Producer:
    def __init__(self,psi,ksi,environment):
        self.psi=psi
        self.ksi=ksi
        self.env=environment

    def __call__(self,FacDemand,sign=1.0):
        Production=np.zeros(self.env['ng'])         
        return sign*(sum(self.psi*FacDemand**(1-self.ksi)/(1-self.ksi)))
        

    def Tech(self,FacDemand,sign=1.0):
        FacDemand=np.array(FacDemand)
        return sign*(self.psi.dot(FacDemand**(1-self.ksi)/(1-self.ksi)))

    def Cost(self,FacDemand,sign=1.0):
        FacDemand=np.array(FacDemand)
        return self.FacPrices.dot(FacDemand)

    def Profit(self,FacDemand,sign=1.0):
        FacDemand=np.array(FacDemand)
        return self.GoodPriceN*self.Tech(FacDemand)-self.Cost(FacDemand)

    def Cons(self):
        '''The constraint of Shutdown Condition'''
        return ({'type' : 'ineq',
                 'fun' : lambda FacDemand: np.array(self.GoodPriceN-self.Cost(FacDemand)/self.Tech(FacDemand))},
                {'type' : 'ineq',
                 'fun' : lambda FacDemand: FacDemand})

    def Profit_max(self):
        from scipy.optimize import minimize
        res = minimize(self.Profit, [10.0]*(self.nf), args=(-1.0,),
                       constraints=self.Cons(), method='SLSQP', options={'disp': False})
        GoodN = self.Tech(res.x)
        return np.append(GoodN,res.x)
