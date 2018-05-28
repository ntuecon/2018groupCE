# -*- coding: utf-8 -*-
"""
Created on Sat May 26 2018

@author: David Biasi

This is a Test file that fixes the user inputs for test purposes
"""


#import ConsumerCES_class as Cons
#import ProducerCES as Pros
import WelfareCES as Soc
import numpy as np


"""Here we fix the type of consumers, number of goods, and number of factors
"""
nt_cons = int(2)
n_goods   = int(2)
n_factors = int(2)


"""Here are some parameters in CES utility but independent of individuals, 
goods and factors.
Make sure that gamma is <1 & !=0 and sigma is an element of (0,inf) & !=1
"""
gamma = 0.5
sigma = 0.3
ind_par = np.append(gamma, sigma)


"""Then, according to the number of consumer types, determine
the parameter of each type, including how many people that type is
um of alphas must be equal to 1 and beta must be positive.
"""
t_agent = [[0.3, 0.7, 0.3], [0.1, 0.9, 0.5]]
t_individuals = [[3], [4]]


"""Converting the the lists into np.arrays
"""
t_agent = np.array(t_agent, dtype=float)
t_individuals = np.array(t_individuals, dtype=float)

"""Analog, we fix the production parameters
"""
fac_sup = np.array([0.3, 0.5], dtype=float)

prod_par = [[0.9, 0.6, 2], [0.9, 0.7, 3]]

"""Again converting to np.array
"""
prod_par = np.array(prod_par, dtype=float)


"""Import all the parameters to the welfare function.
Please refer to the WelfareCES.py
"""
A = Soc.Social(t_agent, t_individuals, fac_sup, prod_par, ind_par)
#A.Welfare([1,1,1,1])
#A.Welfare([1,1,1,1,3,1,1,3,1,1])
#(g1,g2,f1,f2,p1,cf1,cf2,p2,cf1,cf2)

"""Use the function defined in the WelfareCES.py
"""
res = A.Welfare_max()
res

"""Print the results appropriately
"""

"""
for i in range(nt_cons):
    print "The "+str(i+1)+" type of agent consumes goods: "+np.array2string(Result[i*(n_goods+n_fac):i*(number_of_goods+number_of_factors)+number_of_goods])
    print "The "+str(i+1)+" type of agent supplys factors: "+np.array2string(Result[i*(number_of_goods+number_of_factors)+number_of_goods:(i+1)*(number_of_goods+number_of_factors)])

for i in range(n_goods):
    print "The "+str(i+1)+" good is produced at the number: "+np.array2string(Result[(Type_of_consumers)*(number_of_goods+number_of_factors)+i*(number_of_factors+1)])
    print "The "+str(i+1)+" good is needed following factors: "+np.array2string(Result[(Type_of_consumers)*(number_of_goods+number_of_factors)+i*(number_of_factors+1)+1:(Type_of_consumers)*(number_of_goods+number_of_factors)+(i+1)*(number_of_factors+1)])
"""
