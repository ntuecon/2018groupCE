class Product:
    def __init__(self,psi,ksi):
        import numpy as np
        self.ksi=float(ksi)
        self.psi=np.array(psi)

    def Tech(self,FacDemand,sign=1.0):
        '''This is simply the technology function.'''
        import numpy as np
        FacDemand=np.array(FacDemand)
        return sign*(self.psi.dot(FacDemand**(1-self.ksi)/(1-self.ksi)))