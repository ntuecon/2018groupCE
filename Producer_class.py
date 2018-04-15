class Producer:
    """This class is the optimization of prodiuction choice of firm"""
    def __init__(self,Goodprices,Facprices,par):
        self.Goodprices=Goodprices
        self.par=par
        self.Facprices=Facprices

    def production(self,Quants,sign=1.0):
        from math import log
        """import numpy as np"""
        """uti = self.par[0]*log(self.goods[0])+self.par[1]*log(self.goods[1])"""
        """What's below is the linear algebra version of above equation"""
        """uti = self.par.dot(log(self.goods))"""
        """Production function"""
        return sign*((Quants[0])**self.par[0]+Quants[1]**self.par[1])

    def profit(self,Quants,sign=1.0):
        from math import log
        """import numpy as np"""
        """uti = self.par[0]*log(self.goods[0])+self.par[1]*log(self.goods[1])"""
        """What's below is the linear algebra version of above equation"""
        """uti = self.par.dot(log(self.goods))"""
        """Objective function of profit maximization"""
        return sign*(self.Goodprices*self.production(Quants)-self.Facprices[0]*Quants[0]-self.Facprices[1]*Quants[1])

    def cons(self):
        import numpy as np
        return ({'type' : 'ineq',
                 'fun' : lambda Quants: Quants})
    
    def profit_max(self):
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
                 'fun' : lambda Quants: Quants})
        res = minimize(self.profit, [10.0,10.0], args=(-1.0,),
                       constraints=self.cons(), method='SLSQP', options={'disp': True})
        if self.profit(res.x)<0:
            return [0,0]
        else:
            return res.x
