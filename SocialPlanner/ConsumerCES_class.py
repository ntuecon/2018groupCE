class Consumer:
    def __init__(self,alpha,beta,theta):
        import numpy as np
        self.alpha=np.array(alpha)
        self.gamma=0.5
        self.rho=0.0
        self.beta=1.0*beta
        self.theta=1.0*np.array(theta)
        self.ng=len(self.alpha)
        self.nf=len(self.theta)

    def utility(self,GFvec,sign=1.0):
        from math import log
        import numpy as np
        """What's below is the linear algebra version of CES utility equation."""
        """Objective function of consumer utility"""
        GFvec=np.array(GFvec[0:self.ng+self.nf])
        return sign*((self.alpha.dot(GFvec[0:self.ng]**self.gamma))**((1-self.rho)/self.gamma)-np.ones(len(self.theta)).dot(self.beta*GFvec[self.ng:(self.ng+self.nf)]**(self.theta+1)/(self.theta+1)))
