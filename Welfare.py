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
        #Technology Constraint
        Product=[[]]
        for i in range(self.ng):
            Product=Pros.Product(self.Production_Par[i][0:self.nf],self.Production_Par[i][self.nf])
            SocialPlan[self.nt*(self.ng+self.nf)+i*(1+self.nf)]=Product.Tech(SocialPlan[self.nt*(self.ng+self.nf)+i*(1+self.nf)+1:self.nt*(self.ng+self.nf)+(i+1)*(1+self.nf)])
        People=[[]]
        utility=[[]]*self.nt
        for i in range(self.nt):
            People=Cons.Consumer(self.Agent_Type[i][0:self.ng],self.Agent_Type[i][self.ng],self.Factor_sup)
            utility[i]=People.utility(SocialPlan[i*(self.ng+self.nf):(i+1)*(self.ng+self.nf)])
        utility=np.array(utility)
        return sign*self.People_of_Type.dot(utility)

    def MarketClears(self):
        import numpy as np
        #cons=({},)*(self.ng+self.nf+1)
        #for i in range(self.ng):
        #    cons[]
        #for i in range(self.ng,self.ng+self.nf+1):
        #
        NT=np.zeros((self.nt,self.nt),float)
        np.fill_diagonal(NT,self.People_of_Type)
        cons=({},)*(3)
        cons[0]={'type' : 'eq',
                 'fun' : lambda SocialPlan: np.reshape(SocialPlan[0:self.nt*(self.ng+self.nf)],(self.nt,self.))}
        cons[1]={'type' : 'eq',
                 'fun' : lambda SocialPlan: SocialPlan}
        cons[2]={'type' : 'ineq',
                 'fun' : lambda SocialPlan: SocialPlan}
        return cons

    def Welfare_max(self):
        import numpy as np
        from scipy.optimize import minimize
        """
        1.The package of minimize can be use as maximize ,if the
        objective function is multiply by -1.
        2."cons" set as the constrain of optimization problem.
        3.If we use SLSQP method.
        The jacobian means the partial derivative of every independent variables. 
        """
        #GFvec=[[]]*(self.ng+self.nf)
        """res = minimize(self.utility, np.ones(self.ng+self.nf), args=(-1.0,),"""
        res = minimize(self.Welfare, [10.0]*(self.nt*(self.ng+self.nf)+self.ng*(1+self.nf)), args=(-1.0,),
                       constraints=self.MarketClears(), method='SLSQP', options={'disp': True})
        return res.x
