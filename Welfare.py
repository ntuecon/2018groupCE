#import ConsumerCES_class as cons
class Social:
    def __init__(self,Agent_Type,People_of_Type,Factor_sup,Production_Par):
        self.Agent_Type=Agent_Type
        self.People_of_Type=People_of_Type
        self.Factor_sup=Factor_sup
        self.nt=self.Agent_Type.shape[0]
        self.ng=self.Agent_Type.shape[1]-1
        self.nf=self.Factor_sup.shape[0]
        self.Production_Par=Production_Par
        #super(Social, self).__init__(alpha,beta,theta)
        #self.gamma=1.0
        #self.rho=0.0
        #self.ng=len(self.alpha)
        #self.nf=len(self.theta)

    def Welfare(self,SocialPlan,sign=1.0):
        import ConsumerCES_class as Cons
        import ProducerCES as Pros
        import numpy as np
        SocialPlan=np.array(SocialPlan[0:(self.nt*(self.ng+self.nf)+self.ng*(1+self.nf))])
        People=[[]]
        utility=[[]]*self.nt
        for i in range(self.nt):
            People=Cons.Consumer(self.Agent_Type[i][0:self.ng],self.Agent_Type[i][self.ng],self.Factor_sup)
            utility[i]=People.utility(SocialPlan[i*(self.ng+self.nf):(i+1)*(self.ng+self.nf)])
        utility=np.array(utility)
        return sign*self.People_of_Type.dot(utility)

    def Technology(self,SocialPlan):
        import ProducerCES as Pros
        import numpy as np
        Product=[[]]
        NT=np.zeros((self.nt,self.nt),float)
        np.fill_diagonal(NT,self.People_of_Type)
        for i in range(self.ng):
            Product=Pros.Product(self.Production_Par[i][0:self.nf],self.Production_Par[i][self.nf])
            SocialPlan[self.nt*(self.ng+self.nf)+i*(1+self.nf)]=Product.Tech(SocialPlan[self.nt*(self.ng+self.nf)+i*(1+self.nf)+1:self.nt*(self.ng+self.nf)+(i+1)*(1+self.nf)])
        ProSide=SocialPlan[self.nt*(self.ng+self.nf):]
        ProSide=np.reshape(ProSide,(self.ng,1+self.nf))
        TotalProduct=ProSide[:,0]
        ConSide=SocialPlan[0:self.nt*(self.ng+self.nf)]
        ConSide=np.reshape(ConSide,(self.nt,self.ng+self.nf))
        ConSide=np.sum(np.matmul(NT,ConSide),0)
        TotalConsume=ConSide[0:self.ng]
        return TotalProduct-TotalConsume
    
    def MarketClearance(self,SocialPlan):
        import numpy as np
        NT=np.zeros((self.nt,self.nt),float)
        np.fill_diagonal(NT,self.People_of_Type)
        ConSide=SocialPlan[0:self.nt*(self.ng+self.nf)]
        ProSide=SocialPlan[self.nt*(self.ng+self.nf):]
        ConSide=np.reshape(ConSide,(self.nt,self.ng+self.nf))
        ConSide=np.sum(np.matmul(NT,ConSide),0)
        ProSide=np.reshape(ProSide,(self.ng,1+self.nf))
        ProSide=np.append(ProSide[:,0],np.sum(ProSide[:,1:],0))
        return ConSide-ProSide

    def Constraint(self):
        import numpy as np
        #cons=({},)*(self.ng+self.nf+1)
        #for i in range(self.ng):
        #    cons[]
        #for i in range(self.ng,self.ng+self.nf+1):
        #
        return ({'type' : 'eq',
                 'fun' : lambda SocialPlan: self.Technology(SocialPlan)},
                {'type' : 'eq',
                 'fun' : lambda SocialPlan: self.MarketClearance(SocialPlan)},
                {'type' : 'ineq',
                 'fun' : lambda SocialPlan: SocialPlan})

    def Welfare_max(self):
        import numpy as np
        from scipy.optimize import minimize
        """
        1.The package of minimize can be use as maximize ,if the
        objective function is multiply by -1.
        2."MarketClears" set as the constrain of optimization problem.
        """
        res = minimize(self.Welfare, [100.0]*(self.nt*(self.ng+self.nf)+self.ng*(1+self.nf)), args=(-1.0,),
                       constraints=self.Constraint(), method='SLSQP', options={'disp': True})
        return res.x
