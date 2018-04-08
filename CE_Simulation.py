# -*- coding: utf-8 -*-
""" 
Milestone 2:
    Simulation of a CE economy

Course:
    Advanced Public Finance by Prof. Hendrik Rommerswil
    
Date:
    10. April
    
Authors:
    David Biasi

Description:
    The following code simulates a CE economy.
    It uses as an input
    The output is
    Analytical background
    Technical background
 
"""

# Install libraries numpy and scipy
import numpy as np
from scipy.optimize import minimize


# Individuals
"Here we define the population of our economy, individuals 1, ..., H as \
members of the class Individual"

class Individual:

    def __init__(self, factors, utility_parameters):
        "Initialize consumer with a name, list of factors and a matrix of \
        utility parameters"
        self.factors = factors
        self.utility_parameters = utility_parameters
                
    def utility(self, factors_supplied, goods_consumed):
        "This method returns the utitlity experienced by any individual given \
        the factors supplied and goods consumed by this individual. \
        It uses the utility function from the lecture slides"
        total_positive = 0
        total_negative = 0
        for g in range(len(G)):
            total_positive += self.utility_parameters['alpha'][g] * \
            (goods_consumed[g]) ^ self.utility_parameters['gamma']
        for f in range(len(F)):
            total_negative += self.utility_parameters['beta'] * \
            (factors_supplied[f]) ^ (self.utility_parameters['theta'][f] + 1) \
            / (self.utility_parameters['theta'][f] + 1)
        total_utility = total_positive - total_negative
        return total_utility
    

# Goods, factors, and technology
"Here we create a good class. Every good has as attributes the parameters for \
the production function, which we assume has a classical Cobb-Douglas form"

class Good:
    
    def __init__(self, psi, zeta):
        self.psi = psi
        self.zeta = zeta
        
    def produce(self, labour, capital):
        total_output = 0
        for i in range(len(F)):
            total_output += self.psi[i] * (labour) ^ (1 - self.zeta) \
            / (1 - self.zeta)
        return total_output

class Private(Good):
    def __init__(self):
        pass

class Public(Good):
    
    def __init__(self, externality):
        self.externality = externality
        pass


# Market optimisation



for i in population:
    


# Utility possibility fontier
        
def production(factors, good):
    pass


# Inputs

"Here we define the goods and factors of our economy"
Champangne = Good(0.5, 0.5)
Cigars = Good(0.4, 0.6)
Beer = Good(0.7, 0.2)
G = [Champangne, Cigars, Beer]
F = ['Labour', 'Capital']
TPF = 3
          
"Say 'Hi' to Milton and Karl, our two agents and our model's population"
Milton = Individual([2, 15], {'alpha': [7, 2, 1], 'beta': 2, 'gamma': 2, \
                    'sigma': 0.5, 'theta': [3, 1]})
Karl = Individual([10, 3], {'alpha': [1, 1, 5], 'beta': 3, 'gamma': 3, \
                  'sigma': 0.2, 'theta': [3, 2]})
P = [Milton, Karl]        






# Markets

class Market:
    def __init__(self, d, s):
        "Initialise market class with demand d and supply s"
        self.demand = d
        self.supply = s
    
    def equilibrium(self, d, s):
        pass

class Goods_market(Market):
    pass

class Factor_market(Market):
    pass

# Utility function

def utility_function():
    pass

# Goods and factors
class Good:
    
    def __init__(self):
        pass

class Factor:
    
    def __init__(self):
        pass
# Technology
        
    def production():
        pass


# Government
class Government:
    
    def __init__(self, p):
        "Initialise government class with policy p"
        self.policy = p



