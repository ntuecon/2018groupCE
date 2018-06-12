import numpy as np
def infect_Pr(Ind_Vaccin,People_of_Type):
    '''It's a Cobb-Douglas Form in the probability function.
    1.alpha is the C-D parameter, it's the weight between individual and sum
    2.Base-line probability means that even no consumption at all, there is
    still a infecting probability.
    3.'''
    Ind_Vaccin=np.array(Ind_Vaccin,dtype=float)
    People_of_Type=np.array(People_of_Type,dtype=float)
    Base_Pr=0.8
    Effect_Vaccin=3.0
    Weight=3.0
    gamma=1.0
    Total_Vaccin=np.dot(People_of_Type,Ind_Vaccin)
    return Base_Pr/(Effect_Vaccin*np.power(np.power(Ind_Vaccin,gamma)+Weight*np.power(Total_Vaccin,gamma),gamma)+1)
    #return Base_pr/(A*np.power(Ind_Vaccin,alpha)*np.power(Total_Vaccin,1-alpha)+1.0)

def Expected_Uti(utility,SocialPlan,People_of_Type,nt,ng,nf):
    utility=np.array(utility,dtype=float)
    ConsumerPlan=np.array(np.reshape(SocialPlan[0:nt*(ng+nf)],(nt,(ng+nf))),dtype=float)
    People_of_Type=np.array(People_of_Type,dtype=float)
    Health_dis=0.5
    Absolute_weak=2.0
    Ind_Vaccin=ConsumerPlan[:,0:1]
    Infect_Pr=infect_Pr(Ind_Vaccin,People_of_Type)
    EU=Infect_Pr*(Health_dis*utility-Absolute_weak)+(1-Infect_Pr)*utility
    return EU
