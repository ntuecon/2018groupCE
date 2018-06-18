'''
This file containns the classes for the objects of our economy - mainly goods 
and factors, bundels and allocations are
This file is directly taken from Prof. Hendrik Rommeswinkel.

'''
class Factor:
    '''
    This is the factor class. Factors are defined by their parameter theta.
    '''
    def __init__(self,theta):
        '''
        This constructs the factors class
        '''
        self.theta=theta

class Good:
    '''
    This is the goods class.
    Goods are defined by their parameter ksi and type.
    '''
    def __init__(self,ksi,good_type):
        '''
        This constructs the goods class
        '''
        self.ksi=ksi
        self.good_type=good_type


class Bundle(object):
    '''
    A bundle is a description that contains a quantity for any good in the
    economy. Thus, it takes the form of (numpy) vector of length g whith g 
    being the number of goods in the economy.
    '''
    
    def __init__(self, number_of_goods, quantities):
        
        self.nog = number_of_goods
        self.q = quantities


class Allocation(object):
    '''
    An allocation is a description that assignes each consumer a number of any 
    particular good in the economy. Thus, it takes the form of a c x g matrix 
    where c is the number of consumers and g is the number of goods in the 
    economy.
    It is in a sense a list that contains the bundle for each consumer of our
    economy.
    '''
    
    def __init__(self, number_of_consumers, bundles):
        
        self.noc = number_of_consumers
        self.bundles = bundles
