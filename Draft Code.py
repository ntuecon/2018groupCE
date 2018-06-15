
# EXT ADV
import numpy as np
from scipy.optimize import minimize
import numdifftools as nd
"""X=[v1,v2,x11,x21,f11,f21,x12,x22,f12,f22,r11,r12,r21,r22,r01,r02]"""
a1=[0.0,0.4,0.6]
a2=[0.0,0.5,0.5]
rgov=0.0
def U_1(X,sign=1.0):
    return sign*(((a1[0]+rgov)*X[0]**0.5+(a1[1]-rgov/2.0)*X[2]**0.5+(a1[2]-rgov/2.0)*X[3]**0.5)**2-X[4]**2-X[5]**2)
def U_2(X,sign=1.0):
    return sign*(((a2[0]+rgov)*X[1]**0.5+(a2[1]-rgov/2.0)*X[6]**0.5+(a2[2]-rgov/2.0)*X[7]**0.5)**2-X[8]**2-X[9]**2)

exp=0.5
h=0.0# Lower the probablity of falling sick at the social optimum
def tech_0(X):
    return ((X[10]+h)**exp+(X[11]+h)**exp)/(exp)

def tech_1(X):
    return (X[12]**exp+X[13]**exp)/(exp)

def tech_2(X):
    return (X[14]**exp+X[15]**exp)/(exp)



R=0.1
pgov=0.1
def EU_1(X,ext=2.0,sign=1.0):
    p=0.5/((X[0]+ext)+1)
    return sign*((1-p)*U_1(X)-p*pgov+(1-p)*R)
def EU_2(X,ext=2.0,sign=1.0):
    p=0.5/((X[1]+ext)+1)
    return sign*((1-p)*U_2(X)-p*pgov+(1-p)*R)


def EWelf(X,sign=1.0):
    return (EU_1(X,X[1],sign)+EU_2(X,X[0],sign))


X0=np.full(16,1,dtype=float)

Welfmax=minimize(EWelf,X0,args=(-1.0),method='SLSQP',constraints=[{'type':'eq','fun':lambda X:[tech_1(X)-X[2]-X[6],tech_2(X)-X[3]-X[7],tech_0(X)-X[0]-X[1]]},
                                                                {'type':'eq','fun':lambda X:[X[4]+X[8]-X[10]-X[12]-X[14],X[5]+X[9]-X[11]-X[13]-X[15]]},
                                                                {'type':'ineq','fun':lambda X:EU_1(X,X[1])},
                                                                {'type':'ineq','fun':lambda X:EU_2(X,X[0])},
                                                                  {'type':'eq','fun':lambda X:sum(X[0:5])+sum(X[7:9])-sum(X[5:7])-sum(X[7:9])},
                                                                  {'type':'ineq','fun':lambda X:X}])
print Welfmax
print tech_0(Welfmax['x'])

X_max=Welfmax['x']

o1=0.0
EU_1_max=minimize(EU_1,X0,args=(o1,-1.0),method='SLSQP',constraints=[{'type':'ineq','fun':lambda X:X[0]},
                                                                     {'type':'eq','fun':lambda X:X[1]},
                                                                     {'type':'ineq','fun':lambda X:X[2:6]},
                                                                     {'type':'eq','fun':lambda X:X[6:10]},
                                                                     {'type':'ineq','fun':lambda X:X[10:16]},
                                                                     {'type':'eq','fun':lambda X:tech_0(X)-X[0]},
                                                                     {'type':'eq','fun':lambda X:tech_1(X)-X[2]},
                                                                     {'type':'eq','fun':lambda X:tech_2(X)-X[3]},
                                                                     {'type':'eq','fun':lambda X:[X[4]-X[10]-X[12]-X[14],X[5]-X[11]-X[13]-X[15]]},
                                                                     {'type':'ineq','fun':lambda X:X[4]+X[5]-X[0]-X[2]-X[3]}])
EU_1_X=EU_1_max['x']
print EU_1_X

o2=0.1
EU_2_max= minimize(EU_2,X0,args=(o2,-1.0),method='SLSQP',constraints=[{'type':'eq','fun':lambda X:X[0]},
                                                                       {'type':'ineq','fun':lambda X:X[1]},
                                                                       {'type':'eq','fun':lambda X:X[2:6]},
                                                                       {'type':'ineq','fun':lambda X:X[6:10]},
                                                                       {'type':'ineq','fun':lambda X:X[10:16]},
                                                                       {'type':'eq','fun':lambda X:tech_0(X)-X[1]},
                                                                       {'type':'eq','fun':lambda X:tech_1(X)-X[6]},
                                                                       {'type':'eq','fun':lambda X:tech_2(X)-X[7]},
                                                                       {'type':'eq','fun':lambda X:[X[8]-X[10]-X[12]-X[14],X[9]-X[11]-X[13]-X[15]]},
                                                                     {'type':'ineq','fun':lambda X:X[8]+X[9]-X[1]-X[6]-X[7]}])
EU_2_X=EU_2_max['x']
print EU_2_X

tot=EU_1_X+EU_2_X
print "RESULTS"
print 'SOCIAL OPTIMUM : \n','Total Welfare : ',-Welfmax['fun'],'\n','Total consumption of vaccination : ',sum(X_max[0:2]),'(%s)'%(X_max[0:2]),'\n','Probability of getting sick :',0.5/((X_max[0]+X_max[1])+1),'\n','Consumer 1 Consumption :',np.append(X_max[0],X_max[2:6]),'\n','Consumer 1 Utility : ',EU_1(X_max,X_max[1]),'\n','Consumer 2 Consumption : ',np.append(X_max[1],X_max[6:10]),'\n','Consumer 2 Utility : ',EU_2(X_max,X_max[0]),'\n \n'
print 'INDIVIDUAL MAX : \n','Total Welfare : ',EWelf(tot),'\n','Total consumption of vaccination',EU_1_max['x'][0]+EU_2_max['x'][1],'(%s)'%(np.append(EU_1_X[0],EU_2_X[1])),'\n','Probability of getting sick :',0.5/((EU_1_X[0]+EU_2_X[1])+1),'\n','Consumer 1 Consumption :',np.append(EU_1_X[0],EU_1_X[2:4]),'\n','Consumer 1 Utility : ',EU_1(tot,o1),'\n','Consumer 2 Consumption : ',np.append(EU_2_X[1],EU_2_X[6:8]),'\n','Consumer 2 Utility : ',EU_2(tot,o2)                                                                                     
"""
g=0.5
def p_sick_square(X,c_level):
    return (0.5/((X[0]+X[1])**(1/g)+1)-c_level)**2

X0=np.full(16,5,dtype=float)
print minimize(p_sick_square,X0,args=(0.05),method='SLSQP',constraints=[{'type':'ineq','fun':lambda X:X},
                                                      {'type':'eq','fun':lambda X: EWelf(X)+EWelf(tot)}])
"""

"""
EU_1_max= minimize(EU_1,X0,args=(Welfmax['x'][1],-1.0),method='SLSQP',constraints=[{'type':'eq','fun':lambda X:-EU_2(X,X[0])+EU_2(Welfmax['x'],Welfmax['x'][0])},
                                                                               {'type':'eq','fun':lambda X:[tech_1(X)-X[2]-X[6],tech_2(X)-X[3]-X[7],tech_0(X)-X[0]-X[1]]},
                                                                {'type':'eq','fun':lambda X:[X[4]+X[8]-X[10]-X[12]-X[14],X[5]+X[9]-X[11]-X[13]-X[15]]},
                                                                {'type':'ineq','fun':lambda X:X}])
EU_1_X=EU_1_max['x']
print EU_1_X

EU_2_max= minimize(EU_2,X0,args=(Welfmax['x'][0],-1.0),method='SLSQP',constraints=[{'type':'eq','fun':lambda X:-EU_1(X,X[1])+EU_1(Welfmax['x'],Welfmax['x'][1])},
                                                                               {'type':'eq','fun':lambda X:[tech_1(X)-X[2]-X[6],tech_2(X)-X[3]-X[7],tech_0(X)-X[0]-X[1]]},
                                                                {'type':'eq','fun':lambda X:[X[4]+X[8]-X[10]-X[12]-X[14],X[5]+X[9]-X[11]-X[13]-X[15]]},
                                                                {'type':'ineq','fun':lambda X:X}])
EU_2_X=EU_2_max['x']
print EU_2_X

tot=np.append(EU_1_X+EU_2_X,X_max[10:])
tot[4:6]=X_max[4:6]
tot[8:10]=X_max[8:10]
print "RESULTS"
print 'SOCIAL OPTIMUM : \n','Total Welfare : ',-Welfmax['fun'],'\n','Total consumption of vaccination : ',sum(X_max[0:2]),'(%s)'%(X_max[0:2]),'\n','Probability of getting sick :',0.5/((X_max[0]**g+X_max[1]**g)**(1/g)+1),'\n','Consumer 1 Consumption :',np.append(X_max[0],X_max[2:6]),'\n','Consumer 1 Utility : ',EU_1(X_max,X_max[1]),'\n','Consumer 2 Consumption : ',np.append(X_max[1],X_max[6:10]),'\n','Consumer 2 Utility : ',EU_2(X_max,X_max[0]),'\n \n'
print 'INDIVIDUAL MAX : \n','Total Welfare : ',EWelf(tot),'\n','Total consumption of vaccination',EU_1_max['x'][0]+EU_2_max['x'][1],'(%s)'%(np.append(EU_1_X[0],EU_2_X[1])),'\n','Probability of getting sick :',0.5/((EU_1_X[0]**g+EU_2_X[1]**g)**(1/g)+1),'\n','Consumer 1 Consumption :',np.append(EU_1_X[0],EU_1_X[2:4]),'\n','Consumer 1 Utility : ',EU_1(tot,tot[1]),'\n','Consumer 2 Consumption : ',np.append(EU_2_X[1],EU_2_X[6:8]),'\n','Consumer 2 Utility : ',EU_2(tot,tot[0])                                                                                     
"""




"""
# EXT ADV LOG
import numpy as np
from scipy.optimize import minimize
import numdifftools as nd
from math import exp
a1=[0.2,0.1,0.7]
a2=[0.4,0.2,0.4]
rg=0.0 # Pointless Here
def U_1(X,sign=1.0):
    return sign*(((a1[0]+rg)*X[0]**0.5+(a1[1]-rg/2)*X[2]**0.5+(a1[2]-rg/2)*X[3]**0.5)**2-X[4]**2-X[5]**2)
def U_2(X,sign=1.0):
    return sign*(((a2[0]+rg)*X[1]**0.5+(a2[1]-rg/2)*X[6]**0.5+(a2[2]-rg/2)*X[7]**0.5)**2-X[8]**2-X[9]**2)

e=0.5
h=0.0 # Lower the probablity of falling sick at the social optimum
def tech_0(X):
    return ((X[14]+h)**e+(X[15]+h)**e)/(e)

def tech_1(X):
    return (X[10]**e+X[11]**e)/(e)

def tech_2(X):
    return (X[12]**e+X[13]**e)/(e)
 

g=0.5
rgov=0.0
pgov=0.5
def EU_1(X,ext=1.0,sign=1.0):
    p=exp(-(X[0]+ext)**4)
    return sign*((1-p)*(U_1(X)+rgov)+p*(U_1(X)-pgov))
def EU_2(X,ext=1.0,sign=1.0):
    p=exp(-(X[1]+ext)**4)
    return sign*((1-p)*(U_2(X)+rgov)+p*(U_2(X)-pgov))



def EWelf(X,sign=1.0):
    return (EU_1(X,X[1],sign)+EU_2(X,X[0],sign))


X0=np.full(16,1,dtype=float)

Welfmax=minimize(EWelf,X0,args=(-1.0),method='SLSQP',constraints=[{'type':'eq','fun':lambda X:[tech_1(X)-X[2]-X[6],tech_2(X)-X[3]-X[7],tech_0(X)-X[0]-X[1]]},
                                                                {'type':'eq','fun':lambda X:[X[4]+X[8]-X[10]-X[12]-X[14],X[5]+X[9]-X[11]-X[13]-X[15]]},
                                                                {'type':'ineq','fun':lambda X:EU_1(X,X[1])},
                                                                {'type':'ineq','fun':lambda X:EU_1(X,X[1])}])
print Welfmax
print tech_0(Welfmax['x'])

X_max=Welfmax['x']


EU_1_max=minimize(EU_1,X0,args=(X_max[1],-1.0),method='SLSQP',constraints=[{'type':'ineq','fun':lambda X:tech_0(X_max)-X[0]},
                                                                               {'type':'ineq','fun':lambda X:tech_1(X_max)-X[2]},
                                                                               {'type':'ineq','fun':lambda X:tech_2(X_max)-X[3]},
                                                                               {'type':'ineq','fun':lambda X:X_max[0]+sum(X_max[2:4])-X[0]-X[2]-X[3]},
                                                                               {'type':'eq','fun':lambda X:[X[i] for i in range(4,16)]},
                                                                               {'type':'ineq','fun':lambda X:[X[i] for i in range(2,4)]},
                                                                               {'type':'ineq','fun':lambda X:X[0]},
                                                                               {'type':'eq','fun':lambda X:X[1]}])
EU_1_X=EU_1_max['x']
print EU_1_X


EU_2_max= minimize(EU_2,X0,args=(X_max[0],-1.0),method='SLSQP',constraints=[{'type':'ineq','fun':lambda X:tech_0(X_max)-X[1]},
                                                                               {'type':'ineq','fun':lambda X:tech_1(X_max)-X[6]},
                                                                               {'type':'ineq','fun':lambda X:tech_2(X_max)-X[7]},
                                                                               {'type':'ineq','fun':lambda X:X_max[1]+sum(X_max[6:8])-X[1]-X[6]-X[7]},
                                                                               {'type':'eq','fun':lambda X:[X[i] for i in range(2,6)]},
                                                                               {'type':'eq','fun':lambda X:[X[i] for i in range(8,16)]},
                                                                               {'type':'ineq','fun':lambda X:[X[i] for i in range(6,8)]},
                                                                               {'type':'ineq','fun':lambda X:X[1]},
                                                                               {'type':'eq','fun':lambda X:X[0]}])
EU_2_X=EU_2_max['x']
print EU_2_X

tot=np.append(EU_1_X+EU_2_X,X_max[10:])
tot[4:6]=X_max[4:6]
tot[8:10]=X_max[8:10]
print "RESULTS"
print 'SOCIAL OPTIMUM : \n','Total Welfare : ',-Welfmax['fun'],'\n','Total consumption of vaccination : ',sum(X_max[0:2]),'(%s)'%(X_max[0:2]),'\n','Probability of getting sick :',exp((-(X_max[0]+X_max[1])**4)),'\n','Consumer 1 Consumption :',np.append(X_max[0],X_max[2:6]),'\n','Consumer 1 Utility : ',EU_1(X_max,X_max[1]),'\n','Consumer 2 Consumption : ',np.append(X_max[1],X_max[6:10]),'\n','Consumer 2 Utility : ',EU_2(X_max,X_max[0]),'\n \n'
print 'INDIVIDUAL MAX : \n','Total Welfare : ',EWelf(tot),'\n','Total consumption of vaccination',EU_1_max['x'][0]+EU_2_max['x'][1],'(%s)'%(np.append(EU_1_X[0],EU_2_X[1])),'\n','Probability of getting sick :',exp((-(EU_1_X[0]+EU_2_X[1])**4)),'\n','Consumer 1 Consumption :',np.append(EU_1_X[0],EU_1_X[2:4]),'\n','Consumer 1 Utility : ',EU_1(tot,tot[1]),'\n','Consumer 2 Consumption : ',np.append(EU_2_X[1],EU_2_X[6:8]),'\n','Consumer 2 Utility : ',EU_2(tot,tot[0])"""

                                                                

