import numpy as np
from scipy.optimize import minimize
import numdifftools as nd
from math import log


H=input('number of consumers :') # H consumers <10
G=input('number of goods:')# G-1 private goods and 1 public good. number_of_goods=G+1.
n=H*(G-1) # Total consumption of private goods
budget=input('budget of consumers:') # Same budget for each individuals. Prices are normalized equal to one. 
print '\n'

# For consumer i : Ui(Xi1,Xi2,..,Xi(G-1),P1,P2,..,PH)=2(log(Xi1)+log(Xi2)+..+log(XiG))+log(P1+P2+..+PH)
def Social_Welfare(x,sign=1.0):
    #lengh x=H*G
    #x=[consumption of private good by consumer 1, consumption of private good by consumer 2,...,consumption of private goods by consumer C,consumption of public good]
    # =[X11,X12,..,X1(G-1),X21,X22,..X2(G-1),..,XH1,XH2,..XH(G-1),P1,P2,..PH]
    return sign*2*(sum([log(x[i]) for i in range(n)])+log(sum(x[n:]))) #Sum of utility functions

# Define a vector of H budget constraints
def constraint_function(x,budget,H,G): 
    res=[]
    for i in range(H):
        res.append(sum(x[i:i+G-1])+x[i+n]-budget) #Budget line
    return np.array(res)

# Maximize social welfare under budget constraints
def Social_Welfare_Maximization(H,G):
    x0=np.full(H*G,10,dtype=float)
    return minimize(Social_Welfare,x0,args=(-1.0),method='SLSQP',constraints=[{'type':'ineq','fun':lambda x:x},
                                                                              {'type':'eq','fun':lambda x:constraint_function(x,budget,H,G)}])



Social_Welfare_Maximization(H,G)

def u1(x,sign=1.0):
    return sign*(2*log(100-x[0])+log(x[0]+x[1]))
def u2(x,sign=1.0):
    return sign*(2*log(100-x[1])+log(x[0]+x[1]))

du1=nd.Gradient(u1)
du2=nd.Gradient(u2)

"""print minimize(u1,np.array([10.0,10.0]),args=(-1.0),method='SLSQP',constraints=[{'type':'eq','fun':lambda x:du1(x)[0]},
                                                                                {'type':'eq','fun':lambda x:du2(x)[1]},
                                                                                {'type':'ineq','fun':lambda x:x}])"""

""" minimize(lambda x:sum(x),np.array([10.0,10.0]),method='SLSQP',constraints=[{'type':'eq','fun':lambda x:[du1(x)[0],du2(x)[1]]}])"""

# Define the utility function of consumer i including the budget constraints : xi=budget-pi
def ui(i,sign=1.0):
    return lambda x:sign*(2*log(100-x[i])+log(sum(x)))

# List of the utility functions
def list_ui(H,sign=1.0):
    res=[]
    i=0
    for i in range(H):
        res.append(ui(i,sign))
    return res

"""
print list_ui(2)[0](np.array([1.0,15.0]))
print list_ui(2)[1](np.array([16.0,45.0]))
"""

# Derivative utility functions (useful for the constraints)
def dui(H,i,sign=1.0):
    return lambda x:nd.Gradient(list_ui(H,sign)[i])(x)

# List of the derivative utility functions
def list_dui(H,sign=1.0):
    res=[]
    for i in range(H):
        res.append(dui(H,i,sign))
    return res

"""print list_dui(2)[0](np.array([10.0,10.0]))"""

# ith derivative function of consumer i 
def dui_i(H,i):
    return lambda x:list_dui(H)[i](x)[i]

"""print dui_i(2,1)(np.array([10.0,10.0]))"""

# Define a vector of H constraints
def constraints(H,x):
    res=[]
    for i in range(H):
        res.append(dui_i(H,i)(x))
    return res

# Print the only solution to the linear equation problem 
Nash=minimize(lambda x:sum(x),np.full(H,10.0,dtype=float),method='SLSQP',constraints=[{'type':'ineq','fun':lambda x:x},
                                                                                 {'type':'eq','fun':lambda x:constraints(H,x)}])
print 'Social Optimum =', sum(Social_Welfare_Maximization(H,G)['x'][n:])
print Social_Welfare_Maximization(H,G)['x']
print '\n'
print 'Nash Equilibrium =', sum(Nash['x'])
print Nash['x']




