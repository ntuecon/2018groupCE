import numpy as np


class Economy:
    def __init__(self,gamma,number_of_goods,number_of_factors,number_of_types,number_of_consumers_by_type,total_number_of_consumers,Goods,Factors):
        self.gamma=gamma
        self.G=number_of_goods
        self.F=number_of_factors
        self.Ty=number_of_types
        self.HTy=number_of_consumers_by_type
        self.H=total_number_of_consumers
        self.Goods=Goods
        self.Factors=Factors

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
        self.env['ksis']=self.ksis
        self.env['thetas']=thetas

        #Here we create our consumers
        extparameters={'a':0.5}
        self.Consumers=[]
        for ty in range(self.number_of_types):
            uparameters={}
            uparameters['alphas']=self.alphas[ty]
            uparameters['beta']=self.betas[ty]
            if ty==0:
                for h in range(self.total_number_of_consumers):
                    self.Consumers.append(Consumer(uparameters,extparameters,h,self.env))
            else:
                n=int(sum([self.number_of_consumers_by_type[j] for j in range(ty)]))
                for h in range(n,n+self.number_of_consumers_by_type[ty]):
                    self.Consumers.append(Consumer(uparameters,extparameters,h,self.env))

        #Here we create our producers
        self.Producers=[]
        for g in range(self.number_of_goods):
            techparameters={}
            techparameters['psis']=psis[g]
            self.Producers.append(Producer(techparameters,g,self.env))

        
        #Here we create a social planner
        self.SocialPlanner=SocialPlanner(Consumers,Producers,self.env)

    def __call__(self,alphas,betas,psis):
        dictio={}
        dictio['env']=self.env
        dictio['Goods']=self.Goods
        dictio['Factors']=self.Factors
        dictio['Consumers']=self.Consumers
        dictio['Producers']=self.Producers
        dictio['SocialPlanner']=self.SocialPlanner

        dictio['alphas']=alphas
        dictio['betas']=betas
        dictio['psis']=psis

        return dictio

    

        
