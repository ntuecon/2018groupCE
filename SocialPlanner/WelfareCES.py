#import ConsumerCES_class as cons
class Social:
    def __init__(self,Agent_Type,People_of_Type,Factor_sup,Production_Par,InvPar):
        import ConsumerCES_class as Cons
        import ProducerCES as Pros
        import numpy as np
        self.Agent_Type=Agent_Type
        self.People_of_Type=People_of_Type
        self.Factor_sup=Factor_sup
        self.nt=self.Agent_Type.shape[0]
        self.ng=self.Agent_Type.shape[1]-1
        self.nf=self.Factor_sup.shape[0]
        self.Production_Par=Production_Par
        self.InvPar=InvPar
        self.People=[[]]*self.nt
        for i in range(self.nt):
            self.People[i]=Cons.Consumer(self.Agent_Type[:,0:self.ng][i],
                                         self.Agent_Type[:,self.ng:self.ng+1][i],
                                         np.outer(np.ones((self.nt,1),dtype=float),self.Factor_sup)[i],
                                         np.outer(np.ones((self.nt,1),dtype=float),self.InvPar[0])[i],
                                         np.outer(np.ones((self.nt,1),dtype=float),self.InvPar[1])[i])
        self.Firm=[[]]*self.ng
        for i in range(self.ng):
            self.Firm[i]=Pros.Product(self.Production_Par[:,0:self.nf][i],
                                      self.Production_Par[:,self.nf:self.nf+1][i])
#        self.People=np.apply_along_axis(Cons.Consumer,1,
#                                        self.Agent_Type[:,0:self.ng],
#                                        self.Agent_Type[:,self.ng:self.ng+1],
#                                        np.outer(np.ones((self.nt,1),dtype=float),self.Factor_sup),
#                                        np.outer(np.ones((self.nt,1),dtype=float),self.InvPar[0]),
#                                        np.outer(np.ones((self.nt,1),dtype=float),self.InvPar[1]))
#        self.Firm=np.apply_along_axis(Pros.Product,1,
#                                      self.Production_Par[:,0:self.nf],
#                                      self.Production_Par[:,self.nf:self.nf+1])

    def Welfare(self,SocialPlan,sign=1.0):
        '''The social welfare is simply the aggregation of individual utilitys.
        The individual utility is written in the ConsumerCES_class.py.'''
        import ConsumerCES_class as Cons
        import ProducerCES as Pros
        import numpy as np
        SocialPlan=np.array(SocialPlan[0:(self.nt*(self.ng+self.nf)+self.ng*(1+self.nf))],
                            dtype=float)
        utility=[[]]*self.nt
        for i in range(self.nt):
            utility[i]=self.People[i].utility(SocialPlan[i*(self.ng+self.nf):(i+1)*(self.ng+self.nf)])
        utility=np.array(utility)
        return sign*self.People_of_Type.dot(utility)

    def Technology(self,SocialPlan):
        '''This function guarantees the goods variables in SocialPlan are
        consistent with facter variables under technology constraints. The
        technology is written in the ProducerCES.py'''
        import ProducerCES as Pros
        import numpy as np
        NT=np.zeros((self.nt,self.nt),float)
        np.fill_diagonal(NT,self.People_of_Type)
        for i in range(self.ng):
            SocialPlan[self.nt*(self.ng+self.nf)+i*(1+self.nf)]=self.Firm[i].Tech(SocialPlan[self.nt*(self.ng+self.nf)+i*(1+self.nf)+1:self.nt*(self.ng+self.nf)+(i+1)*(1+self.nf)])
        ProSide=SocialPlan[self.nt*(self.ng+self.nf):]
        ProSide=np.reshape(ProSide,(self.ng,1+self.nf))
        TotalProduct=ProSide[:,0]
        ConSide=SocialPlan[0:self.nt*(self.ng+self.nf)]
        ConSide=np.reshape(ConSide,(self.nt,self.ng+self.nf))
        ConSide=np.sum(np.matmul(NT,ConSide),0)
        TotalConsume=ConSide[0:self.ng]
        return TotalProduct-TotalConsume
    
    def MarketClearance(self,SocialPlan):
        '''This function calculate the indivual supply and consumption into
        the market supply and consumption. The operation logic is to sum all
        the variables(goods and factors) consumer or producer used.'''
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
        2.Objective function is Social Welfare function.
        3."MarketClears" &"Technology" set as the constrain of optimization problem.
        """
        res = minimize(self.Welfare, [50.0]*(self.nt*(self.ng+self.nf)+self.ng*(1+self.nf)), args=(-1.0,),
                       constraints=self.Constraint(), method='SLSQP', options={'disp': True})
        return res.x
