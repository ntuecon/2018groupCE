#This is main file
import ConsumerCES_class as Cons
import ProducerCES as Pros
import Welfare as Soc
import numpy as np

print "Welcome to the ECON world of CE group!"
raw_input()
print "Please follow us to set up all the details."
raw_input()
Type_of_consumers = int(input("Please determine how many types of consumers(more than 1):"))
number_of_goods = int(input("Please enter the number of goods:"))
number_of_factors =  int(input("Please enter the number of factors:"))

Agent_Type=[[]]*Type_of_consumers
People_of_Type=[[]]*Type_of_consumers
for i in range(Type_of_consumers):
    Agent_Type[i] = input("Please set the parameters of consumption of type"+str(i+1)+"(["+str(number_of_goods)+" for alpha,1 for beta]):")
    People_of_Type[i] = int(input("Please determine how many people of this type are:"))

Agent_Type=1.0*np.array(Agent_Type)
People_of_Type=1.0*np.array(People_of_Type)

Factor_sup = 1.0*np.array(input("Please set the parameters of factor supply(["+str(number_of_factors)+" for theta]):"))

Production_Par=[[]]*number_of_goods
for i in range(number_of_goods):
    Production_Par[i]=input("Please set the parameters of production of goods"+str(i+1)+"(["+str(number_of_factors)+" for psi,1 for ksi]):")

Production_Par=1.0*np.array(Production_Par)

'Give all the parameters to the welfare function'
A=Soc.Social(Agent_Type,People_of_Type,Factor_sup,Production_Par)
#A.Welfare([1,1,1,1])
#A.Welfare([1,1,1,1,3,1,1,3,1,1])
#(g1,g2,f1,f2,p1,cf1,cf2,p2,cf1,cf2)

A.Welfare_max()
