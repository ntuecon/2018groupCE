#import ConsumerCES_class as cons
class Market:
    def __init__(self,Agent_Type,People_of_Type,Factor_sup,Production_Par):
        self.Agent_Type=Agent_Type
        self.People_of_Type=People_of_Type
        self.Factor_sup=Factor_sup
        self.nt=self.Agent_Type.shape[0]
        self.ng=self.Agent_Type.shape[1]-1
        self.nf=self.Factor_sup.shape[0]
        self.Production_Par=Production_Par

    def ConsSide(self,Prices,sign=1.0):
        import ConsumerMKT_class as Cons
        import numpy as np
        Prices=np.array(Prices[0:self.ng+self.nf])
        Peoples=[[]]
        ConDe=[[]]*self.nt
        for i in range(self.nt):
            People=Cons.Consumer(self.Agent_Type[i][0:self.ng],self.Agent_Type[i][self.ng],self.Factor_sup,Prices[0:self.ng],Prices[self.ng:self.ng+self.nf])
            ConDe[i]=People.utility_max()
        ConDe=np.array(ConDe)
        NT=np.zeros((self.nt,self.nt),float)
        np.fill_diagonal(NT,self.People_of_Type)
        ConDe=np.sum(np.matmul(NT,ConDe),0)
        return sign*ConDe

    def ProsSide(self,Prices,sign=1.0):
        import ProducerMKT_class as Pros
        import numpy as np
        Prices=np.array(Prices[0:self.ng+self.nf])
        Firms=[[]]
        ProDe=[[]]*self.ng
        for i in range(self.ng):
            Firm=Pros.Product(self.Production_Par[i,:self.nf],self.Production_Par[i,self.nf],Prices[i],Prices[self.ng:self.ng+self.nf])
            ProDe[i]=Firm.Profit_max()
        ProDe=np.array(ProDe)
        ProD=np.append(ProDe[:,0],np.sum(ProDe[:,1:],0))
        return sign*ProD

    def ExcessDemand(self,Prices,sign=1.0):
        import ConsumerMKT_class as Cons
        import ProducerMKT_class as Pros
        import numpy as np
        Prices=np.array(Prices[0:self.ng+self.nf])
        ExcessD=np.sum((self.ConsSide(Prices)-self.ProsSide(Prices))**2)
        return ExcessD

    def Constraint(self):
        import numpy as np
        return ({'type' : 'ineq',
                 'fun' : lambda Prices: Prices})

    def Price_Power(self):
        import numpy as np
        from scipy.optimize import minimize
        """
        1.The package of minimize can be use as maximize ,if the
        objective function is multiply by -1.
        2."MarketClears" set as the constrain of optimization problem.
        """
        res = minimize(self.ExcessDemand, [10.0]*(self.ng+self.nf),
                       method='Nelder-Mead', options={'disp': True})
        return res.x

    def Equilibrium(self):
        import numpy as np
        import ConsumerMKT_class as Cons
        import ProducerMKT_class as Pros
        Prices=self.Price_Power()
        Peoples=[[]]
        ConDe=[[]]*self.nt
        for i in range(self.nt):
            People=Cons.Consumer(self.Agent_Type[i][0:self.ng],self.Agent_Type[i][self.ng],self.Factor_sup,Prices[0:self.ng],Prices[self.ng:self.ng+self.nf])
            ConDe[i]=People.utility_max()
        ConDe=np.array(ConDe)
        np.reshape(ConDe,np.size(ConDe))
        Firms=[[]]
        ProDe=[[]]*self.ng
        for i in range(self.ng):
            Firm=Pros.Product(self.Production_Par[i,:self.nf],self.Production_Par[i,self.nf],Prices[i],Prices[self.ng:self.ng+self.nf])
            ProDe[i]=Firm.Profit_max()
        ProDe=np.array(ProDe)
        np.reshape(ProDe,np.size(ProDe))
        return np.append(ConDe,ProDe)
        
