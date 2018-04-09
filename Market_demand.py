import Consumer_class

price=input('Detemine the market prices of [x,y]: ')
income=input('Detemine the income of individual: ')
par=input('Detemine the parameters of Cobb-Doglous[alpha1,alpha2]: ')
nper=input('Determine the number of individuals: ')

A=Consumer(price,income,par)
Market_D=[0,0]
for i in range(nper):
    A=Consumer(price,income,par)
    Market_D+=A.utility_max()

