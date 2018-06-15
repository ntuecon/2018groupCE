import numpy as np
from utility import CESUtility, ExpectedUtility, Social_Welfare
from objects import Good,Factor
from agents import Consumer,Producer,SocialPlanner
from scipy.optimize import minimize


class Economy:
    def __init__(self,gamma,number_of_goods,number_of_factors,number_of_types,number_of_consumers_by_type,total_number_of_consumers,Goods,Factors,alphas,betas,psis):
        self.gamma=gamma
        self.G=number_of_goods
        self.F=number_of_factors
        self.Ty=number_of_types
        self.HTy=number_of_consumers_by_type
        self.H=total_number_of_consumers
        self.Goods=Goods
        self.Factors=Factors
        self.alphas=alphas
        self.betas=betas
        self.psis=psis

        self.ksis=[]
        for Good in self.Goods:
            self.ksis.append(Good.ksi)

        self.thetas=[]
        for Factor in self.Factors:
            self.thetas.append(Factor.theta)

        #Here we create the environment for consumers
        self.env={}
        self.env['gamma']=self.gamma
        self.env['G']=self.G
        self.env['F']=self.F
        self.env['Ty']=self.Ty
        self.env['HTy']=self.HTy
        self.env['H']=self.H
        self.env['ksis']=np.array(self.ksis)
        self.env['thetas']=np.array(self.thetas)

        #Here we create our consumers
        extparameters={'a':0.5}
        self.Consumers=[]
        for ty in range(self.Ty):
            uparameters={}
            uparameters['alphas']=self.alphas[ty]
            uparameters['beta']=self.betas[ty]
            if ty==0:
                for h in range(self.HTy[ty]):
                    self.Consumers.append(Consumer(uparameters,extparameters,h,self.env))
            else:
                n=int(sum([self.HTy[j] for j in range(ty)]))
                for h in range(n,n+self.HTy[ty]):
                    self.Consumers.append(Consumer(uparameters,extparameters,h,self.env))

        #Here we create our producers
        self.Producers=[]
        for g in range(self.G):
            techparameters={}
            techparameters['psis']=psis[g]
            self.Producers.append(Producer(techparameters,g,self.env))

        
        #Here we create a social planner
        self.SocialPlanner=SocialPlanner(self.Consumers,self.Producers,self.env)

    def __call__(self):
        dictio={}
        dictio['env']=self.env
        dictio['Goods']=self.Goods
        dictio['Factors']=self.Factors
        dictio['Consumers']=self.Consumers
        dictio['Producers']=self.Producers
        dictio['SocialPlanner']=self.SocialPlanner

        dictio['alphas']=np.array(self.alphas)
        dictio['betas']=np.array(self.betas)
        dictio['psis']=np.array(self.psis)

        return dictio
