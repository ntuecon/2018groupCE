class Consumer:
    """This class is the optimization of individual choice of consumer"""
    def __init__(self,GoodPrices,GoodPar,income):
        self.GoodPrices=GoodPrices
        #self.FacPrices=FacPrices
        self.GoodPar=GoodPar
        #self.FacPar=FacPar
        self.income=income
        """goods=np.array([])"""

    def utility(self,goods,sign=1.0):
        from math import log
        """import numpy as np"""
        """Objective function of consumer utility"""
        return sign*(self.GoodPar[0]*log(goods[0])+self.GoodPar[1]*log(goods[1]))

    def cons(self):
        """
        1.Budget constraint
        2&3.Nonnegative criterias
        """
        import numpy as np
        return ({'type' : 'ineq',
                 'fun' : lambda goods: np.array(self.income-self.GoodPrices[0]*goods[0]-self.GoodPrices[1]*goods[1]),
                 'jac' : lambda goods: np.array([-self.GoodPrices[0],-self.GoodPrices[1]])},
                {'type' : 'ineq',
                 'fun' : lambda goods: np.array(goods[0])},
                {'type' : 'ineq',
                 'fun' : lambda goods: np.array(goods[1])})
    
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
                 'fun' : lambda goods: np.array(self.income-self.GoodPrices[0]*goods[0]-self.GoodPrices[1]*goods[1]),
                 'jac' : lambda goods: np.array([-self.GoodPrices[0],-self.GoodPrices[1]])},
                {'type' : 'ineq',
                 'fun' : lambda goods: np.array(goods[0])},
                {'type' : 'ineq',
                 'fun' : lambda goods: np.array(goods[1])})
        res = minimize(self.utility, [10.0,10.0], args=(-1.0,),
                       constraints=self.cons(), method='SLSQP', options={'disp': True})
        return res.x
