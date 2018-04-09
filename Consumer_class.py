class Consumer(object):
    """This class is the optimization of individual choice of consum"""
    def __init__(self,prices,income,par):
        self.prices=prices
        """self.goods=[]"""
        self.income=income
        self.par=par


    def utility(self,sign=-1.0):
        from math import log
        """import numpy as np"""
        """uti = self.par[0]*log(self.goods[0])+self.par[1]*log(self.goods[1])"""
        """What's below is the linear algebra version of above equation"""
        """uti = self.par.dot(log(self.goods))"""
        return sign*(self.par[0]*np.log(self.goods[0])+self.par[1]*np.log(self.goods[1]))

    def utility_deriv(self,sign=-1.0):
        from math import log
        """from numpy import .dot"""
        dudg0 = sign*(self.par[0]/self.goods[0])
        dudg1 = sign*(self.par[1]/self.goods[1])
        return np.array([dudg0,dudg1])

    def utility_max(self):
        from scipy.optimize import minimize
        import numpy as np
        cons = ({'type' : 'eq',
                 'fun': lambda x: np.array(self.prices[0]*self.goods[0]+self.prices[1]*self.goods[1]-self.income),
                 'jac': lambda x: np.array(self.priese[0],0)})
        res = minimize(utility, [1.0,1.0], args=(-1.0,), jac=utility_deriv,
                       constraints=cons, method='SLSQP', options={'disp':True})
        return res

