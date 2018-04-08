# -*- coding: utf-8 -*-
"""
Created on Sun Apr 08 14:17:46 2018

@author: David Biasi
"""

# Initialisation
from sympy import *
import numpy as np
from scipy.optimize import minimize


# Variables
"These variables are global parameters for our simulation of the CES economy \
that are later filled with input"

Population = list()

Goods = list()

Factors = list()

gamma = ()

sigma = ()


# Classes
class Individual:
    
    "This class specifies the individuals of our population. Every individual \
    has a specific demand for goods and a specific supply of factors that is \
    later specified through the general equilibrium mechanism. The data input \
    needs to specify the utility parameters Alpha and Beta, however"  
    def __init__(self, supply, demand, alpha, beta):
        self.supply = supply #supply of each factor, list or np.array
        self.demand = demand # demand for each good, list or np.array
        self.alpha = alpha # fixed for each good, list or np.array
        self.beta = beta # fixed
    
    "The consume method returns the utility level of each consumer, given his \
    levels of factors supplied and goods consumed and the utitlity parameters \
    Alpha and Beta. The utility function takes the form as shown in the \
    lecture slides"
    def consume(self):
        pleasure = 0
        pain = 0
        for g in range(len(Goods)):
            pleasure += (self.alpha[g] * self.demand[g] ^ gamma) \
            ^ ((1 - sigma) / gamma)
        for f in range(len(Factors)):
            pain += self.beta * (self.supply[f]) ^ (Factors[f].theta - 1) \
            / (Factors[f].theta + 1)
        total = pleasure - pain
        return total


class Good:
    
    "This class specifies the properties of goods in our economy. Goods are \
    only differentiable in terms of the parameters they posses when they \
    feature in the models functions, which correspond to the parameters used \
    in the lecture slides"
    def __init__(self, psi, xi, mu, delta):
        self.psi = psi # fixed for every factor
        self.xi = xi # fixed
        self.mu = mu # obtained from solving the Lagrangian
        self.delta = delta # obtained from solving the Lagrangian
    
    "The produce method returns the quantity that is produced of a specific \
    good using a certain amount factors as production input. The production \
    function corresponds with the example from the lecture slides"
    def produce(self, factor_supply):
        total = 0
        for f in range(len(Factors)):
            total += self.psi[f] * (factor_supply[f] ^ (1 - self.xi)) \
            / (1 - self.xi)
        return total


class Factor:
    
    "The factor class, similiarly as the goods class, specifies every factor \
    in our economy in terms of the factor specififc function parameters"
    def __init__(self, theta, pi):
        self.theta = theta
        self.pi = pi


# Functions

"The following functions are taken from Tresch and the course lecture to \
compute the general equilibrium for our stylised CES economy"
def utility_func():    
    pass

def production_func():
    pass

def social_welfare_func():
    pass


# Market clearing
    

# Test Input



# Input
## Function parameters
## Individuals
## Goods
## Factors


# Optimisation

def equilibrium():
    pass

# Output