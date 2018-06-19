import ConsumerCES_class as Cons
import ProducerCES as Pros
import WelfareCES as Soc
import numpy as np

'''Here are some parameters in CES utility but independent of
individuals, goods and factors'''
'''Make sure that gamma is <1&!=0 and sigma is in (0,inf)&!=1'''
Gamma=0.5
Sigma=0.0
Inv_Par=np.append(Gamma,Sigma)
Shape_of_SWF=1.0

'''Here are parameters of vaccination.'''
DoVac=True
#Base_Pr=0.2
Effect_Vaccin=3.0
Weight_of_Total_Consumption=3.0
gamma=1.0
Badstate_discount=0.5
Absolute_Weakness=5.0
#Vac_Par=[DoVac,Base_Pr,Effect_Vaccin,Weight_of_Total_Consumption,gamma,
#         Badstate_discount,Absolute_Weakness]

Type_of_consumers=2
number_of_goods=2
number_of_factors=2
''' alphas & beta '''
Agent_Type=np.array([[0.4,0.6,0.8],
                     [0.2,0.8,0.3]])
People_of_Type=np.array([10,10])
'''thetas'''
Factor_sup=np.array([3,2])
'''psis&ksi'''
Production_Par=np.array([[11,12,0.8],
                         [12,3,0.5]])

BP=np.arange(0.,1.,0.05)
Welfare=[]
UA=[]
UB=[]
VacA=[]
VacB=[]
VacT=[]
for i in range(len(BP)):
    print str(i+1)
    Base_Pr=BP[i]
    Vac_Par=[DoVac,Base_Pr,Effect_Vaccin,Weight_of_Total_Consumption,gamma,
             Badstate_discount,Absolute_Weakness]
    A=Soc.Social(Agent_Type,People_of_Type,Factor_sup,Production_Par,Inv_Par,Vac_Par,Shape_of_SWF)
    Result=A.Welfare_max().x
    Consumer=np.reshape(Result[:Type_of_consumers*(number_of_goods+number_of_factors)],
                    (Type_of_consumers,number_of_goods+number_of_factors))
    Producer=np.reshape(Result[Type_of_consumers*(number_of_goods+number_of_factors):],
                    (number_of_goods,number_of_factors+1))
    VacA=np.append(VacA,Consumer[0][0])
    VacB=np.append(VacB,Consumer[1][0])
    VacT=np.append(VacT,Producer[0][0])
    Welfare=np.append(Welfare,A.Welfare(Result))
    UA=np.append(UA,A.People[0].utility(Consumer[0]))
    UB=np.append(UB,A.People[1].utility(Consumer[1]))

'''import matplotlib.pyplot as plt
plt.plot(BP, VacA, 'ro-',label='type 0')
plt.plot(BP, VacB, 'bo-',label='type 1')
plt.plot(BP, VacT, 'go-',label='Total')
plt.xlabel('Base Prob')
plt.ylabel('Consumption of Vaccin')
plt.title("Vaccination vs Base Probability")
plt.legend()
plt.show()'''

import matplotlib.pyplot as plt
'''fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('Base Prob')
ax1.set_ylabel('Social Welfare', color=color)
ax1.plot(BP, Welfare,label='SFW',color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend()
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Utility', color=color)
ax2.plot(BP, UA, 'o:',label='type 0',color=color)
ax2.plot(BP, UB, '^:',label='type 1',color='black')
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend()
#ax1.title("Utility vs Base Probability")
#fig.legend()
fig.tight_layout()
plt.savefig('Welfare-BasePro.png',format='png')
plt.show()
'''

import matplotlib.pyplot as plt
fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('Base Prob')
ax1.set_ylabel('Vaccin', color=color)
ax1.plot(BP, VacT,label='Total',color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend()
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Vaccin', color=color)
ax2.plot(BP, VacA, 'o:',label='type 0',color=color)
ax2.plot(BP, VacB, '^:',label='type 1',color='black')
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend()
#ax1.title("Utility vs Base Probability")
#fig.legend()
fig.tight_layout()
plt.savefig('Vaccin-BasePro.png',format='png')
plt.show()

#for i in range(Type_of_consumers):
#    print "The "+str(i+1)+" type of agent consumes goods: "+np.array2string(Result[i*(number_of_goods+number_of_factors):i*(number_of_goods+number_of_factors)+number_of_goods])
#    print "The "+str(i+1)+" type of agent supplys factors: "+np.array2string(Result[i*(number_of_goods+number_of_factors)+number_of_goods:
#                                                                                    (i+1)*(number_of_goods+number_of_factors)])
#
#for i in range(number_of_goods):
#    print "The "+str(i+1)+" good is produced at the number: "+np.array2string(Result[(Type_of_consumers)*(number_of_goods+number_of_factors)+i*(number_of_factors+1)])
#    print "The "+str(i+1)+" good is needed following factors: "+np.array2string(Result[(Type_of_consumers)*(number_of_goods+number_of_factors)+i*(number_of_factors+1)+1:                                                                                     (Type_of_consumers)*(number_of_goods+number_of_factors)+(i+1)*(number_of_factors+1)])
