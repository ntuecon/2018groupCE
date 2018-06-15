import numpy as np

class Economy:
    def __init__(self,gamma,number_of_goods,number_of_factors,number_of_types,number_of_consumers):
        self.gamma=gamma
        self.nog=number_of_goods
        self.nof=number_of_factors
        self.noty=number_of_types
        self.noc=number_of_consumers

class Factor:
    def __init__(self,theta):
        self.theta=theta

class Good:
    def __init__(self,ksi,good_type):
        self.ksi=ksi
        self.good_type=good_type

def environment(Economy,Goods,Factors):
    env={}
    env['nog']=Economy.nog
    env['nof']=Economy.nof
    env['noty']=Economy.noty
    env['noc']=Economy.noc

    ksis=np.zeros(env['nog'])
    for g in range(env['nog']):
        ksis[g]=Goods[g].ksi
    env['ksis']=ksis

    thetas=np.zeros(env['nof'])
    for f in range(env['nof']):
        thetas[f]=Factors[f].theta
    env['thetas']=thetas

    return env

    

        
