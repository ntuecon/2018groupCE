import numpy as np
from scipy.optimize import minimize

import ConsumerCES_class as Cons
import ProducerCES as Pros


class Social:
    
    
    def __init__(self, Agent_Type, People_of_Type, Factor_sup,
                 Production_Par, InvPar):
        
        """Constructor
        """
        self.Agent_Type = Agent_Type
        self.People_of_Type = People_of_Type
        self.Factor_sup = Factor_sup
        self.nt = self.Agent_Type.shape[0]
        self.ng = self.Agent_Type.shape[1] - 1
        self.nf = self.Factor_sup.shape[0]
        self.Production_Par = Production_Par
        self.InvPar = InvPar

    def Welfare(self, SocialPlan, sign=1.0):
        
        """We use a utilitarian social welfare function, i.e. social welfare 
        simply equals the aggregate of individual utility levels. 
        The individual utility function is written in the ConsumerCES_class.py.
        """
        SocialPlan = np.array(SocialPlan[0:(self.nt*(self.ng+self.nf) + self.ng*(1+self.nf))],
                              dtype=float)
        People = [[]]
        utility = [[]] * self.nt
        for i in range(self.nt):
            People = Cons.Consumer(self.Agent_Type[i][0:self.ng],
                                   self.Agent_Type[i][self.ng],
                                   self.Factor_sup, self.InvPar[0],
                                   self.InvPar[1])
            utility[i] = People.utility(SocialPlan[i *(self.ng+self.nf) : (i + 1)*(self.ng + self.nf)])
        utility = np.array(utility)
        return sign * self.People_of_Type.dot(utility)

    def Technology(self, SocialPlan):
        
        """This function guarantees the goods variables in SocialPlan are
        consistent with facter variables under technology constraints. The
        technology is written in the ProducerCES.py
        """
        Product = [[]]
        NT = np.zeros((self.nt, self.nt), float)
        np.fill_diagonal(NT, self.People_of_Type)
        for i in range(self.ng):
            Product = Pros.Product(self.Production_Par[i][0:self.nf],
                                   self.Production_Par[i][self.nf])
            SocialPlan[self.nt*(self.ng+self.nf) + i*(1+self.nf)] = Product.Tech(SocialPlan[self.nt*(self.ng+self.nf) + i*(1+self.nf) + 1:self.nt*(self.ng + self.nf)+(i+1)*(1+self.nf)])
        ProSide = SocialPlan[self.nt*(self.ng+self.nf):]
        ProSide = np.reshape(ProSide,(self.ng,1+self.nf))
        TotalProduct = ProSide[:,0]
        ConSide = SocialPlan[0:self.nt*(self.ng+self.nf)]
        ConSide = np.reshape(ConSide,(self.nt,self.ng+self.nf))
        ConSide = np.sum(np.matmul(NT,ConSide),0)
        TotalConsume = ConSide[0:self.ng]
        return TotalProduct - TotalConsume
    
    def MarketClearance(self, SocialPlan):
        """This function calculate the indivual supply and consumption into
        the market supply and consumption. The operation logic is to sum all
        the variables(goods and factors) consumer or producer used.
        """
        NT = np.zeros((self.nt, self.nt), float)
        np.fill_diagonal(NT, self.People_of_Type)
        ConSide = SocialPlan[0:self.nt * (self.ng+self.nf)]
        ProSide = SocialPlan[self.nt * (self.ng+self.nf):]
        ConSide = np.reshape(ConSide, (self.nt, self.ng+self.nf))
        ConSide = np.sum(np.matmul(NT, ConSide), 0)
        ProSide = np.reshape(ProSide, (self.ng, 1+self.nf))
        ProSide = np.append(ProSide[:, 0], np.sum(ProSide[:, 1:], 0))
        return ConSide - ProSide

    def Constraint(self):
        
        return ({'type' : 'eq',
                 'fun' : lambda SocialPlan: self.Technology(SocialPlan)},
                {'type' : 'eq',
                 'fun' : lambda SocialPlan: self.MarketClearance(SocialPlan)},
                {'type' : 'ineq',
                 'fun' : lambda SocialPlan: SocialPlan})

    def Welfare_max(self):
        
        """Steps:
        1.The package of minimize can be use as maximize ,if the
        objective function is multiply by -1.
        2.Objective function is Social Welfare function.
        3."MarketClears" &"Technology" set as the constrain of optimization 
        problem.
        """
        res = minimize(self.Welfare, 
                       [50.0]*(self.nt*(self.ng+self.nf)+self.ng*(1+self.nf)), 
                       args = (-1.0,),
                       constraints = self.Constraint(), 
                       method = 'SLSQP', 
                       options = {'disp': True})
        return res.x
