import numpy as np
from utility import CESUtility, ExpectedUtility, Social_Welfare
from objects import Good,Factor
from economy import Economy
from agents import Consumer,Producer,SocialPlanner
from scipy.optimize import minimize
from simulation_functions import set_up_economy, conclusion,action,give_penalty,give_reward,help_prod

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
        
        name=input("Please give a name to your new economy (use string) : ")
        if type(name)!=str:
            name=input("\n" \
                       "Make sure you use a string to define the name. \n"\
                       "Please enter again the name of your new economy : ")
        names.append(name)

        print "Well done, you have created the new economy %s. \n" %(names[e])

        e=e+1
        
    elif act==1:

        if len(ECONOMIES)==0:
            print "Please set up an economy before"

        else:
            if len(ECONOMIES)==1:
                if input ("You have created only one economy. Please print 0 if you do want work on %s : " %(names[0]))==0:
                    act=action(ECONOMIES[0])
                else:
                    act='MENU'
            if len(ECONOMIES)>1:
                your_economies=str(names[0])
                for i in range(1,len(ECONOMIES)):
                    your_economies+=' or %s' %(names[i])
                name_eco=input("You have created %s economies. Do you want to work on %s? \n"\
                          "Please write the name (use string) of the economy you want to work on : " %(len(ECONOMIES),your_economies))
                if name_eco not in [name[i] for i in range(len(ECONOMIES))]:
                    name_eco=input("\n" \
                                   "Please enter a valid name. Make sure you use string. \n" \
                                   "Do you want to work on %s? \n" \
                                   "Please write the name of the economy you want to work on : " %(your_economies))
                for i in range(len(ECONOMIES)):
                    if names[i]==name_eco:
                        index_eco=i
                ECO=ECONOMIES[index_eco]
                act=action(ECO)
                
    elif act=='STOP':
        print "Thanks for partcipating to the simulation"

    else:
        act='MENU'
