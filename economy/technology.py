import numpy as np
"""X=   [v1,v2,...vH,
                x11,x21,...,xG1,f11,f21,...fF1,
                x12,x22,...,xG2,f12,f22,...fF2,
                .
                .
                .
                x1H,x2H,...,xGH,f1H,f2H,...fFH,
                r11,r12,...,r1F,r21,r22,...,r2F,....,rG1,rG2,...,rGF,rV1,rV2,...,rVF]"""


class Technology(object):
    def __init__(self, parameters,i,env):
        'index=good index 0,...G-1'
        self.parameters=parameters
        self.i=i
        self.env=env

        """
        self.parameters['psis'] = parameters['psis']
        self.parameters['ksis'] = parameters['ksis'] --> Put it in class (Good)
        """
        
        self.index=index
        self.env=env
        
    def __call__(self,X):
        G=self.env['nog']
        F=self.env['nof']
        H=self.env['noc']
        n=H+(G+F)*H+i*F
        Prod_i=np.dot(self.parameters['psis']/(1-self.parameters['ksis']),np.power(X[n : n+F],1-self.parameters['ksis']))
        return Prod_i

