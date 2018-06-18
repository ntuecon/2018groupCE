'''
This file contains the economy class of our model. 
Purpose of this class is to create an object that containes all information 
needed to define our economic model.
'''


import numpy as np
from scipy.optimize import minimize

import economy
from utility import CESUtility, ExpectedUtility, Social_Welfare
from objects import Good, Factor
from agents import Consumer, Producer, SocialPlanner


class Economy(object):
    '''
    This is the Economy class. The purpose of the class is to consolidate all 
    the information that defines our model into one object.
    For that reason, we first define the class with all the relevant 
    constiutents of our economy as attributes.
    '''
    
    def __init__(self, gamma, number_of_goods, number_of_factors, number_of_types, 
                 number_of_consumers_by_type, total_number_of_consumers, Goods, 
                 Factors, alphas, betas, psis):
        '''
        This constructs the economy class.
        It defines all attributes and creates lists for the parameters ksi and 
        theta.
        '''
        
        #Here we define all the class attributes
        self.gamma = gamma
        self.G = number_of_goods
        self.F = number_of_factors
        self.Ty = number_of_types
        self.HTy = number_of_consumers_by_type
        self.H = total_number_of_consumers
        self.Goods = Goods
        self.Factors = Factors
        self.alphas = alphas
        self.betas = betas
        self.psis = psis

        #Here we create a class attribute for the ksi parameter
        self.ksis = [] #First define the class attribute ksis as an empty list
        for Good in self.Goods: #We proceed to fill the list with
            self.ksis.append(Good.ksi) #With the ksis contained in the Goods
        
        #Analog to ksi, we create a class attribute containing the theta
        self.thetas = [] 
        for Factor in self.Factors:
            self.thetas.append(Factor.theta)

        #Here we create the environment for consumers
        self.env = {} #First create an empty dictionary
        self.env['gamma'] = self.gamma #Then we add all parameters to the env
        self.env['G'] = self.G
        self.env['F'] = self.F
        self.env['Ty'] = self.Ty
        self.env['HTy'] = self.HTy
        self.env['H'] = self.H
        self.env['ksis'] = np.array(self.ksis)
        self.env['thetas'] = np.array(self.thetas)

        #Here we create our consumers
        extparameters={'a':0.5}
        self.Consumers = []
        for ty in range(self.Ty):
            uparameters={}
            uparameters['alphas']=self.alphas[ty]
            uparameters['beta']=self.betas[ty]
            if ty==0:
                for h in range(self.HTy[ty]):
                    self.Consumers.append(Consumer(uparameters,extparameters,h,self.env))
            else:
                n = int(sum([self.HTy[j] for j in range(ty)]))
                for h in range(n, n+self.HTy[ty]):
                    self.Consumers.append(Consumer(uparameters, extparameters, 
                                                   h, self.env))

        #Here we create our producers
        self.Producers = []
        for g in range(self.G):
            techparameters = {}
            techparameters['psis'] = psis[g]
            self.Producers.append(Producer(techparameters, g, self.env))

        
        #Here we create a social planner
        self.SocialPlanner = SocialPlanner(self.Consumers, self.Producers, 
                                           self.env)

    def __call__(self):
        '''
        This makes the Economy class a callable function.
        The return value is a dictionary that contains all relevant elements 
        and parameters of our model.
        For that reason, we first create an empty dictionary.
        Then we add the data defining our economy.
        Finally, we return the newly created dictonary.
        '''
        
        dictio = {} #First we create an empty dictonary
        
        dictio['env'] = self.env #Then we add all the information to the env
        dictio['Goods'] = self.Goods
        dictio['Factors'] = self.Factors
        dictio['Consumers'] = self.Consumers
        dictio['Producers'] = self.Producers
        dictio['SocialPlanner'] = self.SocialPlanner
        dictio['alphas'] = np.array(self.alphas)
        dictio['betas'] = np.array(self.betas)
        dictio['psis'] = np.array(self.psis)


        return dictio
