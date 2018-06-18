import numpy as np
from utility import CESUtility, ExpectedUtility, Social_Welfare
from objects import Good,Factor
from economy import Economy
from agents import Consumer,Producer,SocialPlanner
from scipy.optimize import minimize

def set_up_economy(i):

    print "Please follow us to set up all the details."
    raw_input()

    '''I'm asking the user to determine the 3 important numbers of ECON world.
    These numbers determine the structure of ECON world.'''
    number_of_goods   = int(input("Please enter the number of goods (the first good will be vaccination):"))
    while number_of_goods<1:
        print 'You should have at least ONE good in economy.'
        number_of_goods   = int(input("Please enter the number of goods (the first good will be vaccination):"))
    number_of_factors = int(input("Please enter the number of factors:"))
    while number_of_factors<1:
        print 'You should have at least ONE factor in economy.'
        number_of_goods   = int(input("Please enter the number of goods (the first good will be vaccination):"))
    gamma = float(input("Please enter the gamma of your economy:"))
    while not gamma<1 or gamma==0:
        print 'Please make sure gamma is smaller than 1 and not equal to 0.'
        gamma = float(input("Please enter the gamma of your economy:"))
    number_of_types = int(input("Please determine how many types of consumers(more than 1):"))
    while number_of_types<1:
        print 'You should have at least ONE type of consumer in economy.'
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
            while Goods[g]<0:
                print 'ksi for good should not be smaller than 0.'
                Goods[g]=Good(float(input('Please determine ksi for good %s(more than 1):' % (g))),'public')
        else:
            Goods[g]=Good(float(input('Please determine ksi for good %s(more than 1):' % (g))),'private')
            while Goods[g]<0:
                print 'ksi for good should not be smaller than 0.'
                Goods[g]=Good(float(input('Please determine ksi for good %s(more than 1):' % (g))),'private')

    print "\n Now let's set the parameters for factors"
    raw_input()
    Factors=[[]]*number_of_factors
    for f in range(number_of_factors):
        Factors[f]=Factor(float(input('Please determine theta for factor %s(more than 1):' % (f))))
        while Factors[f]<0:
            print 'Theta should be greater than 0.'
            Factors[f]=Factor(float(input('Please determine theta for factor %s(more than 1):' % (f))))

    print "\n Now let's set the parameters for consumers"
    raw_input()
    alphas=[[]]*number_of_types
    betas=np.zeros(number_of_types)
    for ty in range(number_of_types):
        para=np.array(input('Please enter the alphas and beta for consumer type %s:' %(ty)))
        alphas[ty]=np.array(para[0:number_of_goods ])
        betas[ty]=para[number_of_goods]
        while not alphas[ty]>0 or np.sum(alphas[ty])!=1 or not betas[ty]>=0:
            print 'Make sure that alphas and beta are positive or that sum of alpha equals to 1.'
            para=np.array(input('Please enter the alphas and beta for consumer type %s:' %(ty)))
            alphas[ty]=np.array(para[0:number_of_goods ])
            betas[ty]=para[number_of_goods]

    print "\n Now let's set the parameters for producers"
    raw_input()
    psis=[[]]*number_of_goods 
    for g in range(number_of_goods):
        psis[g]=np.array(input('Please enter the psis for the production of good %s:' %(g)))
        while not psis[g]>0:
            print 'Make sure psis be positive.'
            psis[g]=np.array(input('Please enter the psis for the production of good %s:' %(g)))

    ECO=Economy(gamma,number_of_goods,number_of_factors,number_of_types,number_of_consumers_by_type,total_number_of_consumers,Goods,Factors,alphas,betas,psis)

    return ECO

def conclusion(ECO,maxi):
    print "\n" \
          "GENERAL EQUILIBRIUM : \n" \
          "Total welfare : %s. \n" \
          "Consumption of vaccination : %s. \n" \
          "Total consumption of vaccination : %s. \n" \
          "Probability of getting sick : %s. \n" %(-maxi['fun'],maxi['x'][0:ECO.env['H']],sum(maxi['x'][0:ECO.env['H']]),0.5/(1+sum(maxi['x'][0:ECO.env['H']])))


def give_penalty(ECO,maxi,i):
        if i==0:
            print   "\n Let\'s see how implement penalty policy can contribute to lower the probability of getting sick. \n" \
                    "You can remove point of utility in the part corresponding to non-vaccination in the expected utility functions of consumers. \n" \
                    "Choose a reasonable number according to the current total welfare value (%s)"%(-maxi['fun'])
            raw_input()
            penality=float(input('Please try one level of penality :'))
            pmaxi=ECO.SocialPlanner.maximization(penality,0.0,0.0)
        else:
            penality=float(input('Please try one level of penality :'))
            pmaxi=ECO.SocialPlanner.maximization(penality,0.0,0.0)

        conclusion(ECO,pmaxi)

def give_reward(ECO,maxi,i):
        if i==0:
            print   "\n Let\'s see how implement reward policy can contribute to lower the probability of getting sick. \n" \
                    "You can add point of utility in the part corresponding to vaccination in the expected utility functions of consumers. \n" \
                    "Choose a reasonable number according to the current total welfare value (%s)" %(-maxi['fun'])
            raw_input()
            reward=float(input('Please try one level of reward :'))
            pmaxi=ECO.SocialPlanner.maximization(0.0,reward,0.0)
        else:
            reward=float(input('Please try one level of reward :'))
            pmaxi=ECO.SocialPlanner.maximization(0.0,reward,0.0)

        conclusion(ECO,pmaxi)

def help_prod(ECO,maxi,i):

    if i==0:
        print   "\n Let\'s see how helping production of vaccination can contribute to lower the probability of getting sick. \n" \
                "You can add capital directly in the production function to help the production of vaccination. \n" \
                "Choose a reasonable number according to the current consumption of vaccination %s (total = %s)." %(maxi['x'][0:ECO.env['H']],sum(maxi['x'][0:ECO.env['H']]))
        raw_input()
        help_prod=float(input('Please try one value to boost production :'))
        pmaxi=ECO.SocialPlanner.maximization(0.0,0.0,help_prod)
    else:
        help_prod=float(input('Please try one value to boost production :'))
        pmaxi=ECO.SocialPlanner.maximization(0.0,0.0,help_prod)

    conclusion(ECO,pmaxi)

def mix_policy(ECO,maxi,i):
    
    if i==0:
        print   "\n Let\'s see how a mix of the different policies can contribute to lower the probability of getting sick. \n" 
        raw_input()
        mix_policy=np.array(input('Please try three values (list) of penalty, reward and helping production :'),dtype=float)
        if len(mix_policy)!=3:
            print 'Make you have a vector of three values.\n'
            mix_policy=np.array(input('Please try three values (list) of penalty, reward and helping production :'),dtype=float)
        pmaxi=ECO.SocialPlanner.maximization(mix_policy[0],mix_policy[1],mix_policy[2])
    else:
        mix_policy=np.array(input('Please try three values (list) of penalty, reward and helping production :'),dtype=float)
        if len(mix_policy)!=3:
            print 'Make you have a vector of three values.\n'
            mix_policy=np.array(input('Please try three values (list) of penalty, reward and helping production :'),dtype=float)
        pmaxi=ECO.SocialPlanner.maximization(mix_policy[0],mix_policy[1],mix_policy[2])

    conclusion(ECO,pmaxi)


actions={'P':give_penalty,'R':give_reward,'H':help_prod,'M':mix_policy}
def action(ECO):

    maxi=ECO.SocialPlanner.maximization(0.0,0.0,0.0)
    conclusion(ECO,maxi)

    act=0

    while act!='MENU':
        act=input("If you want to implement penalties print P.\n"\
                  "If you want to create a reward print R. \n" \
                  "If you want to help production print H. \n" \
                  "If you want to make a mix of these policies print M. \n" \
                  "Your act : ")
        i=0
        A=0
        while A==0:
            actions[act](ECO,maxi,i)
            A=input('\n Do you want to continue? (YES=0/NO=1) : ')
            i+=1
        if A!=0:
            act=input('\n Do you want to try another policy print 0 or go back to the menu of the simulation (print MENU)? : ')
            if act=='MENU':
                return act
    
