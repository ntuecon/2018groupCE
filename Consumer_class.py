class Consumer(object):
    def __init__(self,prices,goods,income,par):
        self.prices=prices
        self.goods=goods
        self.income=income
        self.par=par

    def utility(self,):
        from math import log
        uti = self.par[0]*log(self.goods[0])+self.par[1]*log(self.goods[1])
        return uti
