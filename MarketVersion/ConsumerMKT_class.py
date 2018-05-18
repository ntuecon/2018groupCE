class Consumer:
    """This class is the optimization of individual choice of consumer"""
    def __init__(self,alpha,beta,theta,GoodPrices,FacPrices):
        import numpy as np
        self.GoodPrices=np.array(GoodPrices)
        self.FacPrices=np.array(FacPrices)
        self.alpha=np.array(alpha)
        self.gamma=1.0
        self.rho=0.0
        self.beta=1.0*beta
        self.theta=1.0*np.array(theta)
        self.ng=len(self.alpha)
        self.nf=len(self.theta)

    def utility(self,GFvec,sign=1.0):
        from math import log
        import numpy as np
        """What's below is the linear algebra version of above equation"""
        """Objective function of consumer utility"""
        GFvec=np.array(GFvec[0:self.ng+self.nf])
        return sign*((self.alpha.dot(GFvec[0:self.ng]**self.gamma))**((1-self.rho)/self.gamma)-np.ones(len(self.theta)).dot(self.beta*GFvec[self.ng:(self.ng+self.nf)]**(self.theta+1)/(self.theta+1)))

    def cons(self):
        """
        1.Budget constraint
        2&3.Nonnegative criterias
        """
        import numpy as np
        return ({'type' : 'ineq',
                 'fun' : lambda goods: np.array(self.FacPrices.dot(GFvec[self.ng:(self.ng+self.nf)])-self.GoodPrices.dot(GFvec[0:self.ng]))},
                {'type' : 'ineq',
                 'fun' : lambda GFvec: GFvec})
    
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
        #GFvec=[[]]*(self.ng+self.nf)
        """res = minimize(self.utility, np.ones(self.ng+self.nf), args=(-1.0,),"""
        res = minimize(self.utility, [10.0]*(self.ng+self.nf), args=(-1.0,),
                       constraints=self.cons(), method='SLSQP', options={'disp': True})
        return res.x
