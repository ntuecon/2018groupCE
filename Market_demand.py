price=input('Please detemine the market prices of [x,y]: ')
income=input('Please detemine the income of individual: ')
par=input('Please detemine the parameters of Cobb-Doglous[alpha1,alpha2]: ')
nper=input('Please determine the number of individuals: ')

import Consumer_class

Market_D=[0,0]
for i in range(nper):
    A=Consumer_class.Consumer(price,income,par)
    Market_D+=A.utility_max()

print Market_D
