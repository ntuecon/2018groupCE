#Production
import numpy as np
from scipy.optimize import minimize

"""We are in a context of pure competition so the prices are given by the market"""

goods=np.array(["X1","X2"]) #Give a an axis of goods 
prices=np.array([5,10]) #Give a price for each good (axis)


def variable_cost_X1(x): #Give the variable cost function for the production of good X1
    return 2*x**2+4*x
def fixed_cost_X1(x):#Give the fixed cost function for the production of good X1
    return 0

def variable_cost_X2(x):#Give the variable cost function for the production of good X12
    return x**2+5*x
def fixed_cost_X2(x):#Give the fixed cost function for the production of good X1
    return 0

"""Create list of your variable cost functions and fixed cost functions"""
variable_cost_functions=[variable_cost_X1,variable_cost_X2]
fixed_cost_functions=[fixed_cost_X1,fixed_cost_X2]

"""This compute automatically the list of your average variable cost functions."""
def div_x(func): #Take a function func and return the function x-->func(x)/x
    return lambda x:(func(x)/float(x))

average_variable_cost_functions=[]
for i in range(len(goods)):
    average_variable_cost_functions.append(div_x(variable_cost_functions[i]))

        
   
"""This compute automatically the list of the closing thresold for the production of each good. We will use this list to determine which good produce."""
def compute_closing_thresolds():
    x=[1]
    res=[]
    for i in range(len(goods)):
        res.append(minimize(average_variable_cost_functions[i],x,method="SLSQP",constraints={"type":"ineq","fun":lambda x:x})["fun"])
    return res
closing_thresolds=compute_closing_thresolds()

"""I created this function because I didn't find a pre-build function like this in python. This function takes 2 arguments. list_of_func is a list of functions that take 1 scalar as input. x is an axis. The lenght of the list of functions has to be equal to the lenght of the axis x. This function return the sum of f0(x[0])+f1(x[1])+...+fn(x[n])."""
def sum_functions(list_of_func,x):
    res=0
    for i in range(len(list_of_func)):
        res+=list_of_func[i](x[i])
    return res

"""Create a class producer. Init the list of the variable cost functions, the list of the fixed cost functions and the list of the closing_thresolds."""
class Producer(object):
    def __init__(self,variable_cost_functions,fixed_cost_functions,closing_thresolds):
        self.variable_cost_functions=variable_cost_functions
        self.fixed_cost_functions=fixed_cost_functions
        self.closing_thresolds=closing_thresolds

    """We have to know which goods the Producer will produce in order to compute the cost function"""
    def goods_produced(self): # This function return the list of the good indexes that the Producer chooses to produce according to the closing thresold of each good
        index=[]
        for i in range(len(goods)):
            if self.closing_thresolds[i]<=prices[i]:
                index.append(i)
        return index
    def goods_non_produced(self):  #The list of the good indexes the Producer does'nt produce
        index=[]
        for i in range(len(goods)):
            if i not in self.goods_produced():
                index.append(i)
        return index

    """Now we know which goods to produce. Hence we can compute the variable cost function eliminating the variable cost function of the non-produced goods"""
    def variable_cost(self): 
        list_of_func=[] #First, this function build a list of function. If the good i is produced list_of_func[i] = variable cost function of good i. Else list_of_func[i] = function equal to 0.
        for i in range(len(goods)):
            if i in self.goods_produced():
                list_of_func.append(self.variable_cost_functions[i])
            else:
                list_of_func.append(lambda x:0)
        return lambda x:sum_functions(list_of_func,x) #The result is a function that takes one axis x as argument. This function will return the sum of the variable cost for the production of x[i] quantities of good i, if good i is produced

    """The same for the fixed cost function"""
    def fixed_cost(self):
        list_of_func=[]
        for i in self.goods_produced():
            list_of_func.append(self.fixed_cost_functions[i])
        return lambda x:sum_functions(list_of_func,x)

    def total_cost(self): #Compute the total cost function. One axis x as argument.
        return lambda x:self.variable_cost()(x)+self.fixed_cost()(x)

    def total_income(self): #Compute the total income function. One axis x as argument.
        return lambda x:sum([x[i]*prices[i] for i in self.goods_produced()])

    def profit(self): #Compute the total profit function. One axis x as argument and one scalar args for the maximization.
        return lambda x,args :args*(self.total_income()(x)-self.total_cost()(x))
    
    def pmaximization(self): #Compute the optimal production.

        """Define the constraints"""
        cons=({"type":"eq","fun":lambda x:[x[i] for i in self.goods_non_produced()]}, #Each good produced must have a positive quantity.
              {"type":"ineq","fun":lambda x:[x[i] for i in self.goods_produced()]}) #Each non-produced good must have a quantity equal to zero
        
        x0=np.ones(len(goods)) #Give an axis for the maximization
        
        pmax=minimize(self.profit(),x0,args=-1,method="SLSQP",constraints=cons) #Compute the maximization

        return pmax
                


Producer1=Producer(variable_cost_functions,fixed_cost_functions,closing_thresolds)
print "closing thresolds :",Producer1.closing_thresolds
Good_Produced=""
print "list of the produced goods indexes :",Producer1.goods_produced()
print "list ot the non produced goods indexes",Producer1.goods_non_produced()
print Producer1.pmaximization()
maxi=Producer1.pmaximization()
Conclusion="The optimal production for Producer1 is to produce "
for i in range(len(goods)):
    if i==0:
        Conclusion+="%s of %s " %(maxi["x"][i],goods[i])
    elif i==(len(goods)-1):
        Conclusion+="and %s of %s." %(maxi["x"][i],goods[i])
    else:
        Conclusion+=", %s of %s" %(maxi["x"][i],goods[i])
Conclusion+="Producer1 makes a profit equal to %s with a total income of %s and total costs of %s (fixed cost= %s and variable cost= %s" %(-maxi["fun"],Producer1.total_income()(maxi["x"]),Producer1.total_cost()(maxi["x"]),Producer1.fixed_cost()(maxi["x"]),Producer1.variable_cost()(maxi["x"]))
print Conclusion


