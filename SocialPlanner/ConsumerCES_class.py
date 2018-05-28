# from math import log
import numpy as np


class Consumer:
    
    """Description of consumer class
    """
    
    def __init__(self, alpha, beta, theta, gamma, sigma):
        
        """Constructor
        """
        self.alpha = np.array(alpha)
        self.gamma = gamma
        self.sigma = sigma
        self.beta = 1.0 * beta
        self.theta = 1.0 * np.array(theta)
        self.ng = len(self.alpha)
        self.nf = len(self.theta)

    def utility(self, GFvec, sign = 1.0):
        
        """This is delivers the function for the CES utility equation.
        Objective function of consumer utility
        """
        GFvec = np.array(GFvec[0:self.ng+self.nf], dtype=float)
        return sign*((self.alpha.dot(GFvec[0:self.ng]**self.gamma))**((1-self.sigma)/self.gamma)-np.ones(len(self.theta)).dot(self.beta*GFvec[self.ng:(self.ng+self.nf)]**(self.theta+1)/(self.theta+1)))