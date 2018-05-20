class Product:
    def __init__(self,psi,ksi,GoodPriceN,FacPrices):
        import numpy as np
        self.GoodPriceN=float(GoodPriceN)
        self.FacPrices=np.array(FacPrices)
        self.ksi=float(ksi)
        self.psi=np.array(psi)
        self.nf=len(FacPrices)

    def Tech(self,FacDemand,sign=1.0):
        import numpy as np
        FacDemand=np.array(FacDemand)
        return sign*(self.psi.dot(FacDemand**(1-self.ksi)/(1-self.ksi)))

    def Cost(self,FacDemand,sign=1.0):
        import numpy as np
        FacDemand=np.array(FacDemand)
        return self.FacPrices.dot(FacDemand)

    def Profit(self,FacDemand,sign=1.0):
        import numpy as np
        FacDemand=np.array(FacDemand)
        return self.GoodPriceN*self.Tech(FacDemand)-self.Cost(FacDemand)

    def Cons(self):
        import numpy as np
        return ({'type' : 'ineq',
                 'fun' : lambda FacDemand: np.array(self.GoodPriceN-self.Cost(FacDemand)/self.Tech(FacDemand))},
                {'type' : 'ineq',
                 'fun' : lambda FacDemand: FacDemand})

    def Profit_max(self):
        import numpy as np
        from scipy.optimize import minimize
        res = minimize(self.Profit, [10.0]*(self.nf), args=(-1.0,),
                       constraints=self.Cons(), method='SLSQP', options={'disp': False})
        GoodN = self.Tech(res.x)
        return np.append(GoodN,res.x)
