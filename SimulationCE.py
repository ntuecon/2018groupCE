# -*- coding: utf-8 -*-
"""
Created on Sun Apr 08 14:17:46 2018

@author: David Biasi
"""

# Initialisation

# from sympy import * # not used in current code
import numpy as np
from scipy.optimize import minimize


# Variables
"These variables are global parameters for our simulation of the CES economy \
that are later filled with input"

Milton = None
Karl = None
Population = [Milton, Karl]
Beer = None
Champagne = None
Tobacco = None
Goods = [Beer, Champagne, Tobacco]
Labour = None
Capital = None
Factors = [Labour, Capital]
gamma = None
sigma = None


# Classes
"The classes defined here are essentially there to organise the input data \
in such a way that it can be used for the optimisation problem posed by our \
economic model. Hence, we divided the classes into the essential components \
of our economy, which are individuals, goods, and factors. The attributes are \
for the most part the mathemtical functional parameters that distinguish \
individual objects of a certain class from each other"

class Individual:
          
    def __init__(self, supply, demand, alpha, beta, endowment):
        "This class specifies the individuals of our population. Every \
        individual has a specific demand for goods and a specific supply of \
        factors that is later specified through the general equilibrium \
        mechanism. The data input needs to specify the utility parameters \
        Alpha and Beta, however"
        self.supply = supply #supply of each factor, np.array
        self.demand = demand # demand for each good, np.array
        self.alpha = alpha # fixed for each good, np.array
        self.beta = beta # fixed
        self.endowment = endowment # endowment with factors, np.array
    def consume(self):
        "The consume method returns the utility level of each consumer, given \
        his levels of factors supplied and goods consumed and the utitlity \
        parameters Alpha and Beta. The utility function takes the form as \
        shown in the lecture slides"
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
       
    def __init__(self, psi, xi, mu, delta, quant, raw):
        "This class specifies the properties of goods in our economy. Goods \
        are only differentiable in terms of the parameters they posses when \
        they feature in the models functions, which correspond to the \
        parameters used in the lecture slides"
        self.psi = psi # fixed for every factor
        self.xi = xi # fixed
        self.mu = mu # obtained from solving the Lagrangian
        self.delta = delta # obtained from solving the Lagrangian
        self.quant = quant # obtained from equilibrium
        self.raw = raw # resources used in the production function, np.array
                       # later obtained from optimisation
        
    def produce(self, factor_supply):
        "The produce method returns the quantity that is produced of a \
        specific good using a certain amount factors as production input. The \
        production function corresponds with the example from the lecture \
        slides"
        total = 0
        for f in range(len(Factors)):
            total += self.psi[f] * (factor_supply[f] ^ (1 - self.xi)) \
            / (1 - self.xi)
        return total


class Factor:
        
    def __init__(self, theta, pi, quant):
        "The factor class, similiarly as the goods class, specifies every \
        factor in our economy in terms of the factor specififc function \
        parameters"
        self.theta = theta # fixed
        self.pi = pi # obtained from solving Lagrangian
        self.quant = quant # obtained from equilibrium


# Functions

"The following functions are taken from Tresch and the course lecture to \
compute the general equilibrium for our stylised CES economy"

def utility_func(individual):    
    "The utility function for each individual. First, we create the variables \
    from the attributes that are specified for each good, and one np.array \
    that contains the theta parameters for each factor"
    h = individual # individual from Population
    V = h.supply # factor supply of h, np.array of length len(Factors)
    X = h.demand # good deman of h, np.array of length len(Goods)
    a = h.alpha # parameter of h, np.array of length len(Goods)
    b = h.beta # parameter of h
    t = np.array([])
    for f in range(len(Factors)):        
        t = np.append(t, Factors[f].theta)  
    return (sum(a[1:] * X[1:] ^ gamma ) ^ ((1 - sigma) / gamma)) \
            - (sum(b * (V[1:] ^ (t[1:] + 1)) / (t[1:] + 1)))


def production_func(good, ressources):
    "This function gives the output value for a particular good given a \
    specified input of factors. We follow the production function from the \
    course lecture. The variable good needs to be an element of the class \
    good, while resources specifies the quantities of factors from the list \
    of factors in our economy and is a np.array. We start by specifing the \
    the variables needed for the equation and then construct the production \
    function"
    g = good # good from Goods
    r = ressources # np.arry of length len(Factors)
    p = g.psi # parameter value for each good, np.arry of length len(Factors)
    x = g.xi # parameter value for each good
    return sum(p[1:] * ((r[1:] ^ (1 - x)) / (1 - x)))


def social_welfare_func(individuals):
    "For a number of specified individuals this function calculates the level \
    of social welfare among these individuals. The utility function used here \
    has a utilitarian form, i.e. the utility levels of all individuals are \
    summed up with equal weight. We start by creating an np.array that takes \
    the individual utility values and the sum over said array"
    H = individuals
    U = np.array([])
    for h in range(len(H)):
        U = np.append(U, utility_func(H[h]))
    return sum(U[1:])


def lagrangian(individuals):
    "Now we use the base functions of our model to create the Lagrangian \
    which we can then optimise to compute the general equilibrium of our \
    economy"
    H = individuals
    G = Goods
    F = Factors
    return (social_welfare_func(H) +\
            sum(G[1:].mu * (G[1:].quant - production_func(G[1:], G[1:].raw))) +\
            sum(G[1:].delta * ((sum(H[1:].demand) - G[1:].quant))) +\
            sum(F[1:].pi * (sum(H[1:].supply) - sum(G[1:].raw))))



# Input

## Function parameters
"The user is prompted to define the global parameters for the utility \
function of our economy."

print 'First, you need to define the global parameters of the utility \
function used in our economy!'
gamma = input('Enter the value for the parameter Gamma for the utility \
               function of your economy: gamma = ')
sigma = input('Now specify the parameter Sigma: sigma = ')


## Factors
"The economy relies on two factors as production input: labour and capital. \
The following code prompts the user to specifiy the values for each of the \
factor parameters. Aftewards, we restate define the factors (as elemetens of \
the class factor of course), and restate the list of factors"

print 'Well done! Now, we can continue with the factors in our economy. \
The production inputs are labour and capital. You need to specify them.'
t_L = input('Please, specify the the parameter Theta for the factor Labour: \
            theta_L = ')
t_C = input('Please, specify the parameter Theta for the factor Capital: \
            theta_C = ')
Labour = Factor(t_L, np.array([]))
Capital = Factor(t_C, np.array([]))
Factors = [Labour, Capital]


## Goods
"Here the user is prompted to specify the goods of the economy. In this \
simple cas there are exactly three goods in total: Beer, Champagne and \
tobacco. First, we create empty variables for the variable Psi for every \
good, then we use a for loop to input a value for every good and every \
factor in the economy. We summarise the result into arrays for later use in \
in the functions. We then proceed with the inputs for the parameter Xi \
for every good. Then we summarise all inputs and restate the list of goods in \
our economy. The values obtained from solving the general equilibrium are \
specified only as blank arrays"


print 'We continue with the goods. Our economy is rather hedonistic: \
Our consumers only live on beer, champagne, and tobacco. \
In the following, you will specify their economic properties.'
p_B_L = None
p_B_C = None
p_C_L = None
p_C_C = None
p_T_L = None
p_T_C = None
all_p_names = ['p_B_L', 'p_B_C', 'p_C_L', 'p_C_C', 'p_T_L', 'p_T_C']
all_p = [p_B_L, p_B_C, p_C_L, p_C_C, p_T_L, p_T_C]
for i in range(len(all_p)):
    all_p[i] = float(input ('Please input the values for the variable p with \
         respect to the particular good and a specific factor: ' + \
         all_p_names[i] + ' = '))
p_B = np.array([p_B_L, p_B_C])
p_C = np.array([p_C_L, p_C_C])
p_T = np.array([p_T_L, p_T_C])



x_B = input('Please, specify the the parameter X for the good Beer: \
            x_B = ')
x_C = input('Please, specify the the parameter X for the good Champagne: \
            x_C = ')
x_T = input('Please, specify the the parameter X for the good Tobacco: \
            x_T = ')

Beer = Good(p_B, x_B, np.array([]), np.array([]))
Champagne = Good(p_C, x_C, np.array([]), np.array([]))
Tobacco = Good(p_T, x_T, np.array([]), np.array([]))
Goods = [Beer, Champagne, Tobacco]


## Individuals
"Say 'Hello' to the two players in our economy: Milton and Carl. The user is \
promted to input the parameter values for the two individuals. We creat the \
parameter Alpha for each good and individual and later summarise them in one \
array. The parameter Beta is also asked for for each individual. The supply \
and demand attributes, however, are only specified as empty arrays, as they \
are results of the general equilibrium solution. We finish this section by \
restatign the population."

while True:
    greeting = raw_input('Say hello to the two players in our economy, \
                             Milton and Carl! ')
    if greeting != 'Hello':
        print "Don't be rude!"
        continue
    else:
        break

print 'Now you need to specify their preferences. Alpha stands for the weight \
of the utility each individual enjoys from consuming a certain good, Beta for \
weight on the loss from having to provide for factors.'

a_M_B = input('Enter a value for the Alpha value of Milton for Beer: a_M_B = ')
a_M_C = input('Enter a value for the Alpha value of Milton for Champagne: \
              a_M_C = ')
a_M_T = input('Enter a value for the Alpha value of Milton for Tobacco: \
              a_M_T = ')
a_K_B = input('Enter a value for the Alpha value of Karl for Beer: a_K_B = ')
a_K_C = input('Enter a value for the Alpha value of Karl for Champagne: \
              a_K_C = ')
a_K_T = input('Enter a value for the Alpha value of Karl for Tobacco: \
              a_K_T = ')
a_M = np.array([a_M_B, a_M_C, a_M_T])
a_K = np.array([a_K_B, a_K_C, a_K_T])
b_M = input('Enter a value for the Beta value of Milton : b_M = ')
b_K = input('Enter a value for the Beta value of Karl : b_K = ')
Milton = Individual(np.array([]), np.array([]), a_M, b_M)
Karl = Individual(np.array([]), np.array([]), a_K, b_K)
Population = [Milton, Karl]

# Optimisation

equilibrium = minimize(lagrangian, Population, method='nelder-mead', \
                       options={'xtol': 1e-8, 'disp': True})





