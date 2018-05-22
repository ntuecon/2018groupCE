#This is main file
import ConsumerMKT_class as Cons
import ProducerMKT_class as Pros
import MarketPlaceMKT as Mark
import numpy as np

print "Welcome to the ECON world of CE group!(MarketVersion)"
raw_input()
print "Please follow us to set up all the details."
raw_input()

Type_of_consumers = int(input("Please determine how many types of consumers(more than 1):"))
number_of_goods   = int(input("Please enter the number of goods:"))
number_of_factors = int(input("Please enter the number of factors:"))

Agent_Type=[[]]*Type_of_consumers
People_of_Type=[[]]*Type_of_consumers

for i in range(Type_of_consumers):
    Agent_Type[i] = input("Please set the parameters of consumption of type"+str(i+1)+"(["+str(number_of_goods)+" for alpha,1 for beta]):")
    while sum(Agent_Type[i][0:number_of_goods])!=1 or Agent_Type[i][number_of_goods]<0:
        print '   Value error. Sum of alphas must be equal to 1 and beta must be positive. Please try again :'
        Agent_Type[i]=input("   Please set the parameters of consumption of type"+str(i+1)+"(["+str(number_of_goods)+" for alpha,1 for beta]):")
    People_of_Type[i] = int(input("Please determine how many people of this type are:"))

Agent_Type=np.array(Agent_Type,dtype=float)
People_of_Type=np.array(People_of_Type,dtype=float)

Factor_sup = np.array(input("Please set the parameters of factor supply(["+str(number_of_factors)+" for theta]):"),dtype=float)

while np.all(Factor_sup>np.zeros(number_of_factors))==False:
    print '   Value error. Thetas must be positive. Please try again :'
    Factor_sup = np.array(input("   Please set the parameters of factor supply(["+str(number_of_factors)+" for theta]):"),dtype=float)

Production_Par=[[]]*number_of_goods
for i in range(number_of_goods):
    Production_Par[i]=input("Please set the parameters of production of goods"+str(i+1)+"(["+str(number_of_factors)+" for psi,1 for ksi]):")
    while np.all(Production_Par[i][0:number_of_goods]>np.zeros(number_of_goods))==False or Production_Par[i][number_of_goods]<0:
        print '   Value error. Psis must be strictly positive and ksi must be positive. Please try again :'
        Production_Par[i]=input("   Please set the parameters of production of goods"+str(i+1)+"(["+str(number_of_factors)+" for psi,1 for ksi]):")

Production_Par=np.array(Production_Par,dtype=float)

'Give all the parameters to the welfare function'
A=Mark.Market(Agent_Type,People_of_Type,Factor_sup,Production_Par)

Prices=A.Price_Power()
Result=A.Equilibrium()

for i in range(Type_of_consumers):
    print "The "+str(i+1)+" type of agent consumes goods: "+np.array2string(Result[i*(number_of_goods+number_of_factors):i*(number_of_goods+number_of_factors)+number_of_goods])
    print "The "+str(i+1)+" type of agent supplys factors: "+np.array2string(Result[i*(number_of_goods+number_of_factors)+number_of_goods:(i+1)*(number_of_goods+number_of_factors)])

for i in range(number_of_goods):
    print "The "+str(i+1)+" good is produced at the number: "+np.array2string(Result[(Type_of_consumers)*(number_of_goods+number_of_factors)+i*(number_of_factors+1)])
    print "The "+str(i+1)+" good is needed following factors: "+np.array2string(Result[(Type_of_consumers)*(number_of_goods+number_of_factors)+i*(number_of_factors+1)+1:(Type_of_consumers)*(number_of_goods+number_of_factors)+(i+1)*(number_of_factors+1)])
