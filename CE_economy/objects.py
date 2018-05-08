# -*- coding: utf-8 -*-
"""
Created on May 01, 2018

@author: David Biasi
"""

class Good(object):
    '''
    Parent class for all goods in the economy
    '''
    
    def __init__(self, name, goodtype = 'private', externality, parameters):
        '''
        Constructor
        '''
        self.name = name
        self.goodtype = goodtype
        parameters = dict()
        self.parameters = parameters
        externality = float()
        # Here we create a dummy variable that can later be used to factor
        # externalities into the utility functions depending on whether a good
        # is public or private
        if goodtype == 'private':
            self.parameters['c'] = float(0)
        elif goodtype == 'public':
            self.parameters['c'] = float(1)
        else:
            print 'Error: goodtype needs to be either public or private'
            break


class Factor(object):
    '''
    Parent class for all factors in the economy
    '''

    def __init__(self, name, factortype='private', externality, parameters):
        '''
        Constructor
        '''
        self.name = name
        self.factortype = factortype
        parameters = dict()
        self.parameters = parameters
        externality = float()
        self.externality = externality
        # Here we create a dummy variable that can later be used to factor
        # externalities into the utility functions depending on whether a factor
        # is public or private
        if factortype == 'private':
            self.parameters['c'] = float(0)
        elif factortype == 'public':
            self.parameters['c'] = float(1)
        else:
            print 'Error: factortype needs to be either public or private'
            break

class Bundle(object):
    '''
    A bundle is a numpy vector that contains a goods description
    '''
    pass


class Allocation(object):
    '''
    Description goods and factors allocated to indiviuals in the economy
    '''
    pass