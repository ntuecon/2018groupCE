import numpy as np
from scipy.optimize import minimize
        
class Consumer:
    """This class is the optimization of individual choice of consumer"""
    def __init__(self,alpha,beta,theta,environment):
        import numpy as np
        self.alpha=alpha
        self.gamma=0.5
        self.sigma=0.0
        self.beta=beta
        self.theta=theta
        self.env=environment

    def __call__(self,C,sign=1.0): #Utility
        return sign*(sum(self.alpha*(C[0:self.env['ng']]**self.gamma))**((1-self.sigma)/self.gamma)-self.beta*sum(C[self.env['ng']]**(self.theta+1)/(self.theta+1)))


    """def cons(self):
        
        1.Budget constraint
        2&3.Nonnegative criterias
    
        import numpy as np
        return ({'type' : 'ineq',
                 'fun' : lambda GFvec: self.budget(GFvec)},
                {'type' : 'ineq',
                 'fun' : lambda GFvec: GFvec})
    'fun' : lambda goods: np.array(self.FacPrices.dot(GFvec[self.ng:(self.ng+self.nf)])-self.GoodPrices.dot(GFvec[0:self.ng]))}
    
    def utility_max(self):
    

        1.The package of minimize can be use as maximize ,if the
        objective function is multiply by -1.
        2."cons" set as the constrain of optimization problem.
        3.If we use SLSQP method, the jacobian of objective function is necessary.
        The jacobian means the partial derivative of every independent variables. 
        #GFvec=[[]]*(self.ng+self.nf)
        res = minimize(self.utility, np.ones(self.ng+self.nf), args=(-1.0,),
        res = minimize(self.utility, [10.0]*(self.ng+self.nf), args=(-1.0,),
                       constraints=self.cons(), method='SLSQP', options={'disp': True})
        return res.x """
                
