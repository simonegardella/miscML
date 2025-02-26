import numpy as np
import random
import math
import matplotlib.pyplot as plt


def Sigmoide (x):
    return 1/ (1+ math.exp (-x))
def dSigmoide (x):
    temp = Sigmoide(x)
    return temp * (1-temp)
    
class Neurone ():
    def __init__ (self,nInputs, fa = Sigmoide, dfa = dSigmoide):
        self.nInputs = nInputs
        self.w = np.random.random((self.nInputs))
        self.b = random.random()
        self.fa = fa
        self.dfa = dfa
        self.lr = 0.01
        
    def fNeurone (self, Inputs):
        return sum(self.w * Inputs) + self.b
    
    def FeedForward (self,Inputs):
        return self.fa (self.fNeurone (Inputs))
    
    def BackProp (self,Inputs, Errore):
        dw = 2 * Errore * self.dfa (self.fNeurone(Inputs)) * Inputs
        db = 2 * Errore * self.dfa (self.fNeurone(Inputs)) 
        
        Errori = 2 * Errore * self.dfa(self.fNeurone(Inputs))  * self.w
        self.w = self.w - dw * self.lr
        self.b = self.b - db * self.lr
        
        return Errori
    
    
class Rete ():
    def __init__ (self):
        self.N1 = Neurone(2)
        self.N2 = Neurone (2)
        self.N3 = Neurone (2)

    def FeedForward (self,Inputs):
        l1 =np.array([self.N1.FeedForward(Inputs),self.N2.FeedForward (Inputs)])
        return self.N3.FeedForward (l1)
        
    def BackProp (self,Inputs, VA):
        l1 =np.array([self.N1.FeedForward(Inputs),self.N2.FeedForward (Inputs)])
        o = self.N3.FeedForward (l1)
        
        Errore = o - VA
        erroreN1, erroreN2  = self.N3.BackProp (l1,Errore)
        _= self.N1.BackProp (Inputs,erroreN1)
        _= self.N2.BackProp (Inputs,erroreN2)
        return Errore ** 2
        
        
    
miaRete = Rete ()

Dataset = np.array([[0.2,0.3,0],[0.8,0.9,1],[0.7,0.8,1],[0.1,0.3,0]])
ErroriMedi = []
for epoca in range (100000):
    erroremedio = 0
    for dato in Dataset:
        erroremedio = erroremedio +  miaRete.BackProp (dato[:2],dato[2])
    erroremedio = math.sqrt(erroremedio / len (Dataset))
    
    ErroriMedi.append (erroremedio)
    
    
plt.figure()
plt.plot (range (len(ErroriMedi)),ErroriMedi)
plt.show()