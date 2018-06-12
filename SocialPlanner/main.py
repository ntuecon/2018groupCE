#This is main file
import ConsumerCES_class as Cons
import ProducerCES as Pros
import WelfareCES as Soc
import numpy as np

'''The part is just for the introduction.'''
print "Welcome to the ECON world of CE group!"
raw_input()
print "Please follow us to set up all the details."
raw_input()

'''I'm asking the user to determine the 3 important numbers of ECON world.
These numbers determine the structure of ECON world.'''
Type_of_consumers = int(input("Please determine how many types of consumers(more than 1):"))
number_of_goods   = int(input("Please enter the number of goods:"))
number_of_factors = int(input("Please enter the number of factors:"))

'''Here are some parameters in CES utility but independent of
individuals, goods and factors'''
'''Make sure that gamma is <1&!=0 and sigma is in (0,inf)&!=1'''
Gamma=0.5
Sigma=0.0
Inv_Par=np.append(Gamma,Sigma)

'''Then, according to the numbers of consumer type, I'm asking user to determine
the parameter of each type, including how many people that type is.'''
Agent_Type=[[]]*Type_of_consumers
People_of_Type=[[]]*Type_of_consumers
for i in range(Type_of_consumers):
    Agent_Type[i] = input("Please set the parameters of consumption of type"+str(i+1)+"(["+str(number_of_goods)+" for alpha(sum of alphas is 1),1 for beta]):")
    while (sum(Agent_Type[i][0:number_of_goods])!=1.0 or not np.all(Agent_Type[i][0:number_of_goods]>0.0)) or Agent_Type[i][number_of_goods]<=0.0 or len(Agent_Type[i])!=(number_of_goods+1):
        print 'Value error. Sum of alphas must be equal to 1 and beta must be positive. Please try again :'
        Agent_Type[i] = input("Please set the parameters of consumption of type"+str(i+1)+"(["+str(number_of_goods)+" for alpha,1 for beta]):")
    People_of_Type[i] = int(input("Please determine how many people of this type are:"))

'''Cuz the input parameter is the List data type, I transfer the List into the
numpy array for sake of algebra operation.'''
Agent_Type=np.array(Agent_Type,dtype=float)
People_of_Type=np.array(People_of_Type,dtype=float)

'''The producer part is all the same as above.'''
Factor_sup = np.array(input("Please set the parameters of factor supply(["+str(number_of_factors)+" for theta]):"),dtype=float)
while not np.all(Factor_sup>=0) or len(Factor_sup)!=number_of_factors:
    print 'Value error. Thetas cannot be negative. Please try again :'
    Factor_sup = np.array(input("Please set the parameters of factor supply(["+str(number_of_factors)+" for theta]):"),dtype=float)

Production_Par=[[]]*number_of_goods
for i in range(number_of_goods):
    Production_Par[i]=input("Please set the parameters of production of goods"+str(i+1)+"(["+str(number_of_factors)+" for psi,1 for ksi]):")
    while not np.all(Production_Par[i][0:number_of_goods]>0) or not (Production_Par[i][number_of_goods]>=0.0 and Production_Par[i][number_of_goods]<1.0) or len(Production_Par[i])!=(number_of_factors+1):
        print 'Value error. Psis must be strictly positive and ksi must be positive. Please try again :'
        Production_Par[i]=input("Please set the parameters of production of goods"+str(i+1)+"(["+str(number_of_factors)+" for psi,1 for ksi]):")

Production_Par=np.array(Production_Par,dtype=float)


"""Import all the parameters to the welfare function.
Please refer to the WelfareCES.py."""
A=Soc.Social(Agent_Type,People_of_Type,Factor_sup,Production_Par,Inv_Par)

'''Use the function defined in the WelfareCES.py.'''
Result=A.Welfare_max()

'''Print the results appropriately'''
for i in range(Type_of_consumers):
    print "The "+str(i+1)+" type of agent consumes goods: "+np.array2string(Result[i*(number_of_goods+number_of_factors):i*(number_of_goods+number_of_factors)+number_of_goods])
    print "The "+str(i+1)+" type of agent supplys factors: "+np.array2string(Result[i*(number_of_goods+number_of_factors)+number_of_goods:(i+1)*(number_of_goods+number_of_factors)])

for i in range(number_of_goods):
    print "The "+str(i+1)+" good is produced at the number: "+np.array2string(Result[(Type_of_consumers)*(number_of_goods+number_of_factors)+i*(number_of_factors+1)])
    print "The "+str(i+1)+" good is needed following factors: "+np.array2string(Result[(Type_of_consumers)*(number_of_goods+number_of_factors)+i*(number_of_factors+1)+1:(Type_of_consumers)*(number_of_goods+number_of_factors)+(i+1)*(number_of_factors+1)])
