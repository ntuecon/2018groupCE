import numpy as np
def infect_Pr(Ind_Vaccin,People_of_Type,Vac_Par):
    '''It's a Cobb-Douglas Form in the probability function.
    1.alpha is the C-D parameter, it's the weight between individual and sum
    2.Base-line probability means that even no consumption at all, there is
    still a infecting probability.
    3.parameters=[Baseline_Pr,Effect_Vaccin,Weight,gamma]'''
    Ind_Vaccin=np.array(Ind_Vaccin,dtype=float)
    People_of_Type=np.array(People_of_Type,dtype=float)
    Base_Pr=Vac_Par[0]
    Effect_Vaccin=Vac_Par[1]
    Weight=Vac_Par[2]
    gamma=Vac_Par[3]
    Total_Vaccin=np.dot(People_of_Type,Ind_Vaccin)
    return np.array(Base_Pr/(Effect_Vaccin*
                             np.power(np.power(Ind_Vaccin,gamma)+Weight*np.power(Total_Vaccin,gamma),1/gamma)+
                              1))
    #return Base_pr/(A*np.power(Ind_Vaccin,alpha)*np.power(Total_Vaccin,1-alpha)+1.0)

def Expected_Uti(utility,SocialPlan,People_of_Type,Vac_Par,nt,ng,nf):
    utility=np.array(utility,dtype=float)
    ConsumerPlan=np.array(np.reshape(SocialPlan[0:nt*(ng+nf)],(nt,(ng+nf))),dtype=float)
    People_of_Type=np.array(People_of_Type,dtype=float)
    Health_dis=Vac_Par[4]
    Absolute_weak=Vac_Par[5]
    Ind_Vaccin=ConsumerPlan[:,0:1]
    Infect_Pr=infect_Pr(Ind_Vaccin,People_of_Type,Vac_Par)
    EU=Infect_Pr*(Health_dis*utility-Absolute_weak)+(1-Infect_Pr)*utility
    return EU
