import numpy as np
from utility import CESUtility, ExpectedUtility
from environment import Economy,Factor,Good,environment
from agents import Consumer,Producer

'''The part is just for the introduction.'''
print "Welcome to the ECON world of CE group!"
raw_input()
print "Please follow us to set up all the details."
raw_input()

'''I'm asking the user to determine the 3 important numbers of ECON world.
These numbers determine the structure of ECON world.'''
number_of_goods   = int(input("Please enter the number of goods (the first good will be a public good):"))
number_of_factors = int(input("Please enter the number of factors:"))
gamma = int(input("Please enter the gamma of your economy:"))
number_of_types = int(input("Please determine how many types of consumers(more than 1):"))
number_of_consumers=np.zeros(number_of_types)
for i in range(number_of_types):
    number_of_consumers[i] = int(input('Please determine how many consumers(more than 1) in type %s:' % (i)))

"""Here we build our economy"""
ECO=Economy(gamma,number_of_goods,number_of_factors,number_of_types,number_of_consumers)


print "Now let's set the parameters for goods"
raw_input()
Goods=[[]]*ECO.nog
for g in range(ECO.nog):
    if g==0:
        Goods[g]=Good(float(input('Please determine ksi for good %s(more than 1):' % (g))),'public')
    else:
        Goods[g]=Good(float(input('Please determine ksi for good %s(more than 1):' % (g))),'private')

print "Now let's set the parameters for factors"
raw_input()
Factors=[[]]*ECO.nof
for f in range(ECO.nof):
    Factors[f]=Factor(float(input('Please determine theta for good %s(more than 1):' % (f))))

"""Here we build our environment"""
env=environment(ECO,Goods,Factors)

print "Now let's set the parameters for consumers"
raw_input()
alphas=[[]]*env['noty']
betas=np.zeros(env['noty'])
for ty in range(env['noty']):
    para=np.array(input('Please enter the alphas and beta for consumer type %s:' %(ty)))
    alphas[ty]=np.array(para[0:env['nog']])
    betas[ty]=para[env['nog']]

print "Now let's set the parameters for producers"
raw_input()
psis=[[]]*env['nog']
for g in range(env['nog']):
    psis[g]=np.array(input('Please enter the psis for the production of good %s:' %(g)))


extparameters={'a':0.5,'b':1.0,'c':1.0,'d':0.0,'e':0.0}

"""Here we create our consumers"""
Consumers=[[]]*sum(env['noc'])
uparameters={}
for ty in range(env['noty']):
    uparameters['alphas']=alphas[ty]
    uparameters['beta']=betas[ty]
    if ty>0:
        n=sum([env['noc'][i] for i in range(ty-1)])
    else :
        n=0
    for h in range(n,n+env['noc']['ty']):
        Consumers[h]=Consumer(uparameters,extparameters,h,env)

"""Here we create our producers"""
Producers=[[]]*env['nog']
for g in range(env['nog']):
    techparameters={}
    techparameters['psis']=psis[g]
    Producers[g]=Producer(techparameters,g,env)

