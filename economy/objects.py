'''
Created on Apr 16, 2018

@author: Hendrik Rommeswinkel
'''

class Good(object):
    '''
    classdocs
    '''

    def __init__(self, name, goodtype='private'):
        '''
        Constructor
        '''
        self.name = name
        self.goodtype = goodtype

class Factor(object):
    '''
    classdocs
    '''

    def __init__(self, name, factortype='private'):
        '''
        Constructor
        '''
        self.name = name
        self.factortype = factortype

class Bundle(object):
    '''
    A bundle is a numpy vector that contains a goods description
    '''
    pass


class Allocation(object):
    '''
    classdocs
    '''
    pass