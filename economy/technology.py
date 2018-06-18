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
        
    def __call__(self,X,prod_help=0.0):
        G=self.env['G']
        F=self.env['F']
        H=self.env['H']
        n=H*(G+F)+self.i*F
        if self.i==0:
            Prod_i=np.dot(self.parameters['psis'],(X[n: n+F]+prod_help)**(self.env['ksis'][self.i]))/self.env['ksis'][self.i]
        else:
            Prod_i=np.dot(self.parameters['psis'],X[n: n+F]**(self.env['ksis'][self.i]))/self.env['ksis'][self.i]
        return Prod_i
