# -*- coding: utf-8 -*-
"""
Created on Thu Jun 07 10:09:33 2018

@author: David Biasi
"""

class Thing(object):
    
    def __init__(self, parameters):
        
        self.parameters = parameters
        
        
class Good(Thing):
    
    def __init__(self, xi):
        
        self.xi = xi


class Factor(Thing):
    
    def __init__(self, theta):
        
        self.theta = theta


class Inventory(object):
    
    def __init__(self, Goods, Factors):
        self.Goods = list()
        self.Factors = list()