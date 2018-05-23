#Environmnent
import numpy as np

class Environment(object):
    def __init__(self,Agent_Type,People_of_Type,Factor_sup,Production_Par):
        self.Agent_Type=Agent_Type
        self.People_of_Type=People_of_Type
        self.Factor_sup=Factor_sup
        self.Production_Par=Production_Par
        self.nt=self.Agent_Type.shape[0]
        self.ng=self.Agent_Type.shape[1]-1
        self.nf=self.Factor_sup.shape[0]

    def __call__(self):
        res={}
        res['Agent_Types']={}
        for i in range(self.nt):
            res['Agent_Types'][str(i)]=self.Agent_Type[i]

        res['Factor_sup']=self.Factor_sup

        res['Production_Pars']={}
        for i in range(self.ng):
            res['Production_Pars'][str(i)]=self.Production_Par[i]

        res['nc']={}
        for i in range(self.nt):
            res['nc'][str(i)]=self.People_of_Type[i]

        res['nt']=self.nt
        res['ng']=self.ng
        res['nf']=self.nf
        return res

Env=Environment(np.array([[1,2,3],[1,2,5]]),np.array([5,6]),np.array([1,1]),np.array([[1,2,3],[5,8,9]]))





