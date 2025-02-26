import numpy as np
import math 
import random
from funzioniattivazione import * 
from dropout import * 
from matplotlib import pyplot as plt


    
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
    

class LayerDense():
    def __init__ (self,nNeuroni, nInputs, fa = Sigmoide, dfa = dSigmoide):
        self.nNeuroni = nNeuroni
        self.nInputs = nInputs
        self.Neuroni = np.array([Neurone (nInputs,fa, dfa) for i in range (nNeuroni)])
    def FeedForward(self, Inputs):
        return np.array ([self.Neuroni[i].FeedForward (Inputs) for i in range (self.nNeuroni)])
    def BackProp (self, Inputs, errori ):
        ErroriRitorno  =  np.zeros((self.nInputs))
        for i in range (self.nNeuroni):
            ErroriParziali = self.Neuroni[i].BackProp (Inputs, errori[i])
            for k in range (len (ErroriParziali)):
                ErroriRitorno[k] = ErroriRitorno[k] + ErroriParziali[k]
        return ErroriRitorno
        
        
class Rete ():
    def __init__ (self):
        self.Perc = LayerDense (2,2,Relu,dRelu)
        self.Hidden = LayerDense (5,2,Relu,dRelu)
        self.Class = LayerDense (2,5,Sigmoide,dSigmoide)

    def FeedForward (self,Inputs):
        o1 = self.Perc.FeedForward (Inputs)
        o2 = self.Hidden.FeedForward (o1)
        output = self.Class.FeedForward (o2)
        return output

        
    def BackProp (self,Inputs, VA):
        
        o1 = self.Perc.FeedForward (Inputs)
        o2 = self.Hidden.FeedForward (o1)
        output = self.Class.FeedForward (o2)
        
        errori = output- VA
        errori_class = self.Class.BackProp (o2,errori)
        errori_hidden = self.Hidden.BackProp (o1,errori_class)
        _ = self.Perc.BackProp (Inputs, errori_hidden)
        return errori ** 2
    
    
miaRete = Rete ()

Dataset = np.array([[0.2,0.3,0,1],[0.8,0.9,1,0],[0.7,0.8,1,0],[0.1,0.3,0,1]])
ErroriMedi = []
for epoca in range (10000):
    erroremedio = np.zeros (2)
    for dato in Dataset:
        erroremedio = erroremedio +  miaRete.BackProp (dato[:2],np.array(dato[2:]))
    erroremedio = (erroremedio / len (Dataset) )** .5
    
    ErroriMedi.append (erroremedio)
    
    if epoca % 50 == 0:
        print (epoca, erroremedio)
    
    
plt.figure()
plt.plot (range (len(ErroriMedi)),ErroriMedi)
plt.show()