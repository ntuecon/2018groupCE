def Vaccinate_Pr(Ind_Vaccin,People_of_Type):
    '''It's a Cobb-Douglas Form in the probability function.
    1.alpha is the C-D parameter, it's the weight between individual and sum
    2.Base-line probability means that even no consumption at all, there is
    still a infecting probability.
    3.'''
    import numpy as np
    Ind_Vaccin=np.array(Ind_Vaccin,dtype=float)
    People_of_Type=np.array(People_of_Type,dtype=float)
    alpha=0.2
    Base_pro=0.3
    A=3
    Total_Vaccin=People_of_Type.dot(Ind_Vaccin)
    return Base_pro/(A*np.power(Ind_Vaccin,alpha)*np.power(Total_Vaccin,1-alpha)+1.0)

def Expected_Uti(utility,SocialPlan,People_of_Type,nt,ng,nf):
    import numpy as np
    utility=np.array(utility,dtype=float)
    ConsumerPlan=np.array(np.reshape(SocialPlan[nt*(ng+nf)],(nt,(ng+nf))),dtype=float)
    People_of_Type=np.array(People_of_Type,dtype=float)
    Health_dis=0.4
    Absolute_weak=2.0
    Ind_Vaccin=ConsumerPlan[:,0:1]
    Infect_Pr=Vaccinate_Pr(Ind_Vaccin,People_of_Type)
    EU=Infect_Pr*(Health_dis*utility-Absolute_weak)+(1-Infect_Pr)*utility
    return EU
