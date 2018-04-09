class Consumer:
    """This class is the optimization of individual choice of consumer"""
    def __init__(self,prices,income,par):
        self.prices=prices
        self.income=income
        self.par=par

    def utility(self,goods,sign=1.0):
        from math import log
        """import numpy as np"""
        """uti = self.par[0]*log(self.goods[0])+self.par[1]*log(self.goods[1])"""
        """What's below is the linear algebra version of above equation"""
        """uti = self.par.dot(log(self.goods))"""
        """Objective function of consumer utility"""
        return sign*(self.par[0]*log(goods[0])+self.par[1]*log(goods[1]))

    def utility_deriv(self,goods,sign=1.0):
        import numpy as np
        from math import log
        """1st order derivative of objective function"""
        dudg0 = sign*(self.par[0]/goods[0])
        dudg1 = sign*(self.par[1]/goods[1])
        return np.array([ dudg0 , dudg1 ])
    
    def utility_max(self):
        import numpy as np
        from scipy.optimize import minimize
        """
        1.The package of minimize can be use as maximize ,if the
        objective function is multiply by -1.
        2."cons" set as the constrain of optimization problem.
        3.If we use SLSQP method, the jacobian of objective function is necessary.
        The jacobian means the partial derivative of every independent variables. 
        """
        cons = ({'type' : 'ineq',
                 'fun' : lambda goods: np.array(self.income-self.prices[0]*goods[0]-self.prices[1]*goods[1]),
                 'jac' : lambda goods: np.array([-self.prices[0],-self.prices[1]])})
        res = minimize(self.utility, [10.0,10.0], args=(-1.0,),
                       constraints=cons, method='SLSQP', options={'disp': True})
        return res.x

    def market_demand
