import numpy as np
from utility import CESUtility, ExpectedUtility, Social_Welfare
from objects import Good,Factor
from economy import Economy
from agents import Consumer,Producer,SocialPlanner
from scipy.optimize import minimize
a=[0.3,0.3,0.4,2.0]
b=[0.4,0.3,0.3,2.0]
c=[0.3,0.4,0.3,2.0]
o=[1.0,1.0]

#The part is just for the introduction
print "Welcome to the ECON world of CE group! \n" \
      "This simulaton compute the general equilibrium of an economy in the presence of a public good (vaccination). \n" \
      "After having set up the economy, you will have to take the good decision in order to prevent the population from being infected."
raw_input()
print "Please follow us to set up all the details."
raw_input()

'''I'm asking the user to determine the 3 important numbers of ECON world.
These numbers determine the structure of ECON world.'''
number_of_goods   = int(input("Please enter the number of goods (the first good will be vaccination):"))
number_of_factors = int(input("Please enter the number of factors:"))
gamma = float(input("Please enter the gamma of your economy:"))
number_of_types = int(input("Please determine how many types of consumers(more than 1):"))
number_of_consumers_by_type=[]
for i in range(number_of_types):
    number_of_consumers_by_type.append(int(input('Please determine how many consumers(more than 1) in type %s:' % (i))))
total_number_of_consumers=int(sum(number_of_consumers_by_type))

print "\n Now let's set the parameters for goods"
raw_input()
Goods=[[]]*number_of_goods
for g in range(number_of_goods):
    if g==0:
        Goods[g]=Good(float(input('Please determine ksi for good %s(more than 1):' % (g))),'public')
    else:
        Goods[g]=Good(float(input('Please determine ksi for good %s(more than 1):' % (g))),'private')

print "\n Now let's set the parameters for factors"
raw_input()
Factors=[[]]*number_of_factors
for f in range(number_of_factors):
    Factors[f]=Factor(float(input('Please determine theta for factor %s(more than 1):' % (f))))

print "\n Now let's set the parameters for consumers"
raw_input()
alphas=[[]]*number_of_types
betas=np.zeros(number_of_types)
for ty in range(number_of_types):
    para=np.array(input('Please enter the alphas and beta for consumer type %s:' %(ty)))
    alphas[ty]=np.array(para[0:number_of_goods ])
    betas[ty]=para[number_of_goods]

print "\n Now let's set the parameters for producers"
raw_input()
psis=[[]]*number_of_goods 
for g in range(number_of_goods):
    psis[g]=np.array(input('Please enter the psis for the production of good %s:' %(g)))




ECO=Economy(gamma,number_of_goods,number_of_factors,number_of_types,number_of_consumers_by_type,total_number_of_consumers,Goods,Factors,alphas,betas,psis)
dictio_ECO=ECO()

maxi=ECO.SocialPlanner.maximization(0.0,0.0,0.0)
sick=0.5/(1+sum(maxi['x'][0:ECO.env['H']]))

def Conclusion(sick,maxi):
    print "RESULTS : \n" \
          "Total welfare : %s. \n" \
          "Consumption of vaccination : %s. \n" \
          "Total consumption of vaccination : %s. \n" \
          "Probability of getting sick : %s. \n" %(-maxi['fun'],maxi['x'][0:ECO.env['H']],sum(maxi['x'][0:ECO.env['H']]),sick)
Conclusion(sick,maxi)
raw_input()

print   "\n As a social planner you can implement different measures to both reduce the probability of getting sick and increase the total welfare. \n" \
        "Currently, the probability of getting sick is %s.\n" \
        "How do you want to act?" %(sick)
raw_input()

def action():
    act=input("If you want to implement penalities print P.\n"\
              "If you want to create a reward print R. \n" \
              "If you want to help production print H. \n" \
              "If you want to make a mix of these policies print M. \n" \
              "Your act : ")
    return act

def Give_penality(i):
        if i==0:
            print   "\n Let\'s see how implement penality policy can contribute to lower the probability of getting sick. \n" \
                    "You can remove point of utility in the part corresponding to non-vaccination in the expected utility functions of consumers. \n" \
                    "Choose a reasonable number according to the current total welfare value (%s)"%(maxi['fun'])
            raw_input()
            penality=float(input('Please try one level of penality :'))
            pmaxi=ECO.SocialPlanner.maximization(penality,0.0,0.0)
            psick=0.5/(1+sum(pmaxi['x'][0:ECO.env['H']]))
        else:
            penality=float(input('Please try one level of penality :'))
            pmaxi=ECO.SocialPlanner.maximization(penality,0.0,0.0)
            psick=0.5/(1+sum(pmaxi['x'][0:ECO.env['H']]))

        Conclusion(psick,pmaxi)

def Give_reward(i):
        if i==0:
            print   "\n Let\'s see how implement reward policy can contribute to lower the probability of getting sick. \n" \
                    "You can add point of utility in the part corresponding to vaccination in the expected utility functions of consumers. \n" \
                    "Choose a reasonable number according to the current total welfare value (%s)" %(maxi['fun'])
            raw_input()
            reward=float(input('Please try one level of reward :'))
            pmaxi=ECO.SocialPlanner.maximization(0.0,reward,0.0)
            psick=0.5/(1+sum(pmaxi['x'][0:ECO.env['H']]))
        else:
            reward=float(input('Please try one level of reward :'))
            pmaxi=ECO.SocialPlanner.maximization(0.0,reward,0.0)
            psick=0.5/(1+sum(pmaxi['x'][0:ECO.env['H']]))

        Conclusion(psick,pmaxi)

def Help_prod(i):

    if i==0:
        print   "\n Let\'s see how helping production of vaccination can contribute to lower the probability of getting sick. \n" \
                "You can add capital directly in the production function to help the production of vaccination. \n" \
                "Choose a reasonable number according to the current consumption of vaccination %s (total = %s)." %(maxi['x'][0:int(sum(env['noc']))],sum(maxi['x'][0:int(sum(env['noc']))]))
        raw_input()
        help_prod=float(input('Please try one value to boost production :'))
        pmaxi=ECO.SocialPlanner.maximization(0.0,0.0,help_prod)
        psick=0.5/(1+sum(pmaxi['x'][0:ECO.env['H']]))
    else:
        help_prod=float(input('Please try one value to boost production :'))
        pmaxi=ECO.SocialPlanner.maximization(0.0,0.0,help_prod)
        psick=0.5/(1+sum(pmaxi['x'][0:ECO.env['H']]))

    Conclusion(psick,pmaxi)

def Mix_policy(i):
    
    if i==0:
        print   "\n Let\'s see how a mix of the different policies can contribute to lower the probability of getting sick. \n" 
        raw_input()
        mix_policy=np.array(input('Please try three values (list) of penality, reward and helping production :'),dtype=float)
        if len(mix_policy)!=3:
            print 'Make you have a vector of three values.\n'
            mix_policy=np.array(input('Please try three values (list) of penality, reward and helping production :'),dtype=float)
        pmaxi=ECO.SocialPlanner.maximization(mix_policy[0],mix_policy[1],mix_policy[2])
        psick=0.5/(1+sum(pmaxi['x'][0:ECO.env['H']]))
    else:
        mix_policy=np.array(input('Please try three values (list) of penality, reward and helping production :'),dtype=float)
        if len(mix_policy)!=3:
            print 'Make you have a vector of three values.\n'
            mix_policy=np.array(input('Please try three values (list) of penality, reward and helping production :'),dtype=float)
        pmaxi=ECO.SocialPlanner.maximization(mix_policy[0],mix_policy[1],mix_policy[2])
        psick=0.5/(1+sum(pmaxi['x'][0:ECO.env['H']]))

    Conclusion(psick,pmaxi)
    
    

act=action()
while act!='STOP':
    if act=='P':
        i=0
        A=0
        while A==0:
            Give_penality(i)
            A=input('\n Do you want to continue? (YES=0/NO=1) : ')
            i+=1
        if A!=0:
            A=input('\n Do you want to try another policy print 0 or stop the simulation (print STOP)? : ')
            if A=='STOP':
                act=A
            else:
                raw_input() 
                act=action()
    elif act=='R':
        i=0
        A=0
        while A==0:
            Give_reward(i)
            A=input('\n Do you want to continue? (YES=0/NO=1) : ')
            i+=1
        if A!=0:
            A=input('\n Do you want to try another policy print 0 or stop the simulation (print STOP)? : ')
            if A==0:
                raw_input()
                act=action()
            else:
                act=A
    elif act=='H':
        i=0
        A=0
        while A==0:
            Help_prod(i)
            A=input('\n Do you want to continue? (YES=0/NO=1) : ')
            i+=1
        if A!=0:
            A=input('\n Do you want to try another policy print 0 or stop the simulation (print STOP)? : ')
            if A==0:
                raw_input()
                act=action()
            else:
                act=A
    elif act=='M':
        i=0
        A=0
        while A==0:
            Mix_policy(i)
            A=input('\n Do you want to continue? (YES=0/NO=1) : ')
            i+=1
        if A!=0:
            A=input('\n Do you want to try another policy print 0 or stop the simulation (print STOP)? : ')
            if A==0:
                raw_input()
                act=action()
            else:
                act=A
        
        
    
"""
gamma=0.5
number_of_goods=3
number_of_factors=2
number_of_types=3
number_of_consumers=[1,1,1]

E=Economy(gamma,number_of_goods,number_of_factors,number_of_types,number_of_consumers)
Goods=[]
for g in range(E.nog):
    if g==0:
        Goods.append(Good(0.5,'public'))
    else:
        Goods.append(Good(0.5,'private'))

Factors=[]
for f in range(E.nof):
    Factors.append(Factor(1.0))

Env=environment(E,Goods,Factors)

alphas_type0=a[0:E.nog]
beta_type0=a[E.nog]
uparameters_type0={'alphas':alphas_type0,'beta':beta_type0}

alphas_type1=b[0:E.nog]
beta_type1=b[E.nog]
uparameters_type1={'alphas':alphas_type1,'beta':beta_type1}

alphas_type2=c[0:E.nog]
beta_type2=c[E.nog]
uparameters_type2={'alphas':alphas_type2,'beta':beta_type2}

extparameters={'a':0.5,'b':1.0,'c':1.0,'d':0.0,'e':0.0}

Consumers=[Consumer(uparameters_type0,extparameters,0,Env),Consumer(uparameters_type1,extparameters,1,Env),Consumer(uparameters_type2,extparameters,2,Env)]

techparameters={'psis':np.full(Env['nof'],1,dtype=float)}

Producers=[]
for g in range(Env['nog']):
    Producers.append(Producer(techparameters,g,Env))

SocialWelfare=Social_Welfare(Consumers,Producers,Env)

SP=SocialPlanner(Consumers,Producers,Env)
maxi=SP.maximization()
print maxi
print 'Probability of getting sick : ',0.5/(1+sum(maxi['x'][0:sum(Env['noc'])]))
print 'Aggregate welfare : ',-maxi['fun']
"""

