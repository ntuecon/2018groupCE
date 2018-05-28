import numpy as np


class Product:
    
    def __init__(self, psi, ksi):
        
        """Constructor
        """
        self.ksi = ksi
        self.psi = psi

    def Tech(self, FacDemand, sign = 1.0):
        
        """This is simply the technology function
        """
        FacDemand = np.array(FacDemand, dtype = float)
        return (sign *
                (self.psi.dot(FacDemand**(1.0-self.ksi) / (1.0-self.ksi))))
