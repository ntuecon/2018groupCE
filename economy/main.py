import numpy as np
from utility import CESUtility, ExpectedUtility, Social_Welfare
from objects import Good,Factor
from economy import Economy
from agents import Consumer,Producer,SocialPlanner
from scipy.optimize import minimize
from simulation_functions import set_up_economy, conclusion,action,give_penalty,give_reward,help_prod
a=[0.3,0.3,0.4,2.0]
b=[0.3,0.3,0.4,2.0]
c=[0.3,0.3,0.4,2.0]
o=[1.0,1.0]

act=0
ECONOMIES=[]
names=[]
e=0 # number of economies created
n=0 
while act!='STOP':
    #The part is just for the introduction
    if n==0:print "Welcome to the ECON world of CE group! \n"
    n=+1
    raw_input()
    act=input( "MENU OF THE SIMULATION : \n"\
               "If you want to set up a new economy print 0. \n" \
               "If you want to implement policies in one of your existing economies print 1. \n"\
               "If you want to stop the simulation print 'STOP'.\n"\
               "Your action : ")

    if act==0:
        NEW_ECO=set_up_economy(e)
        ECONOMIES.append(NEW_ECO)
        
        name=input("Please give a name to your new economy : ")
        if type(name)!=str:
            name=input("Make sure you use ' ' for the name. \n"\
                       "Please enter again the name of your new economy : ")
        names.append(name)

        print "Well done, you have created the new economy %s. \n" %(names[e])

        e=e+1
        
    elif act==1:

        if len(ECONOMIES)==0:
            print "Please set up an economy before"

        else:
            if len(ECONOMIES)==1:
                if input ("You have created only one economy. Please print 0 if you do want work on %s" %(names[0]))==0:
                    act=action(ECONOMIES[0])
            if len(ECONOMIES)>1:
                your_economies=names[0]
                for i in range(1,len(ECONOMIES)):
                    your_economies+='or %s' %(names(i))
                ECO=input("You have created %s economies. Do you want to work on your_economies? \n"\
                          "Please write the name of the economy you want to work on : ")
                act=action(ECO)
                
    elif act=='STOP':
        print "Thanks for partcipating to the simulation"

    else:
        act='MENU'

"""
    print "This simulaton compute the general equilibrium of an economy in the presence of a public good (vaccination). \n" \
          "After having set up the economy, you will have to take the good decision in order to prevent the population from being infected."
    raw_input()

    print   "\n As a social planner you can implement different measures to both reduce the probability of getting sick and increase the total welfare. \n" \
            "Currently, the probability of getting sick is %s.\n" \
            "How do you want to act?" %(sick)
raw_input()




    
    

act=action()
while act!='STOP':
    if act=='P':
        i=0
        A=0
        while A==0:
            give_penality(i)
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
            give_reward(i)
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
            help_prod(i)
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
            mix_policy(i)
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
