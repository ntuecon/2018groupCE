'''
This file creates the environment for our model, i.e. it takes all the relevant 
global and constant parameters of our model and stores them in one dictionary 
that can then easily be accessed when we need to perform calcualtions.
For this reason, we first creat one class for the economy, goods, and factors 
of our model. Instances of these classes contain all relevant parameters.
We then define a function that extracts the relevant parameters from instances 
of these classes and stores them comprehensivly in one environment dictonary.
'''


import numpy as np


class Economy(object):
    '''
    This creates the economy class for tour model.
    The economy takes some global parameters of the utility and technology 
    function and parameters concerning the number and the types of goods 
    and factors aswell as the number of consumers of our economy.
    This parameters are fixed for all calculations in our model.
    '''
    
    def __init__(self, gamma, number_of_goods, number_of_factors, 
                 number_of_types, number_of_consumers):
        '''
        This constructs the class.
        An economy is defined through the global parameter gamma and 
        information about the goods, factors, and consumers of our model.
        '''
        
        self.gamma = gamma
        self.nog = number_of_goods
        self.nof = number_of_factors
        self.noty = number_of_types
        self.noc = number_of_consumers


class Factor(object):
    '''
    This creates the class for the factors in our economy.
    Factors are defined with respect to their parameters in the 
    utiltiy and technology function.
    '''
    
    def __init__(self, theta):
        '''
        This constructs the class.
        Factors only take the parameter theta.
        '''
        
        self.theta = theta


class Good(object):
    '''
    This creates the class for the goods in our economy.
    As factors, goods are defined with respect to their parameters in the 
    utiltiy and technology function.
    '''
    
    def __init__(self, ksi, good_type):
        '''
        This constructs the class.
        Goods take the parameters ksi and good_type.
        '''
        
        self.ksi = ksi
        self.good_type = good_type


def environment(Economy, Goods, Factors):
    '''
    This defines the environment fuction.
    Its arguments are instances of the Economy, Goods, and Factor class.
    It the takes the relevant parameters from the relevant parameters form
    these objects and transfers them into a newly created env dictonary.
    This way we can later easily access the global constituents of our model 
    for the economy.
    The fuction returns the env dictonary.
    '''
    
    env = {} #An empty dictonary for the environment variables is created
    env['nog'] = Economy.nog #Number of goods
    env['nof'] = Economy.nof #Number of factors
    env['noty'] = Economy.noty #Number of types of consumers
    env['noc'] = Economy.noc #Number of consumers

    ksis = np.zeros(env['nog']) #An empty array for the ksi parameters is created
    for g in range(env['nog']): #We fill the array with the parameters
        ksis[g] = Goods[g].ksi
    env['ksis'] = ksis #The array is added to the dictonary

    thetas = np.zeros(env['nof']) #Analogto the ksis, we add the theta parameters
    for f in range(env['nof']):
        thetas[f] = Factors[f].theta
    env['thetas'] = thetas
    
    return env #Finally, this returns the env dictonary

    

        
