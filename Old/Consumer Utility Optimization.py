import numpy as np
from scipy.optimize import minimize

"""Input goods and prices"""
goods=np.array(["X1","X2"])
prices=np.array([3,4])

"""Build and print a GoodsPrices dictionnary to make it clear"""
GoodsPrices_dict={}
for i in range(len(goods)):
    GoodsPrices_dict[goods[i]]=prices[i]
print "Good prices: \n",GoodsPrices_dict

"""Create a class Economy with goods and fixed prices"""
class Economy(object):
    def __init__(self,goods,prices):
        self.goods=goods
        self.prices=prices

"""Define my_economy using the input at the beginning of the code"""
my_economy=Economy(goods,prices)

""" For all the program : Input x is a one axis of len(goods) quantities such as x[0] is the quantity of goods[0], x[1] the quantity of goods[1], etc"""


"""Define several utility functions. (***) """
def utility_function1(x,args):
    return args*x[1]*x[0]**1.5

def utility_function2(x,args):
    return args*x[0]*x[1]**1.5

"""Compute the total cost for a consumer that consume a quantity x[0] of goods[0], x[1] of goods[1], etc."""
def total_cost(x):
    total_cost=sum(prices*x)
    return total_cost


class Consumer(object): #Create Consumer class
    def __init__(self,budget,ufunction): #Give a budget and a utility function to the consumer
        self.budget=budget
        self.ufunction=ufunction
    def umaximization(self): #maximize the utility function of the consumer
        def cons(): #Define the constraint
            cons=({"type":"eq","fun":lambda x:self.budget-total_cost(x)}, #The budget line 
                  {"type":"ineq","fun":lambda x:x}) #Quantities can't be negative
            return cons
        x0=np.ones(len(goods)) #Give an axis for the maximization
        umax=minimize(self.ufunction,x0,args=-1,method="SLSQP",constraints=cons()) #Compute the maximization
        return umax


Consumer1=Consumer(100,utility_function1)
print "\n \n Consumer 1 maximization \n",Consumer1.umaximization()

Consumer2=Consumer(100,utility_function2)
print "\n \n Consumer 2 maximization \n",Consumer2.umaximization()
print "\n\n Consumer1 Utility max =",-Consumer1.umaximization()["fun"],"\n Consumer2 Utility max =",-Consumer2.umaximization()["fun"]
