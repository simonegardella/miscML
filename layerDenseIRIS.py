import numpy as np
import math 
import random
from funzioniattivazione import * 
from dropout import * 
from matplotlib import pyplot as plt
import csv


    
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
        self.Perc = LayerDense (4,4,     Sigmoide, dSigmoide)
        self.Hidden1 = LayerDense (9,4,  Sigmoide, dSigmoide)
        self.Hidden2 = LayerDense (18,9, Sigmoide, dSigmoide)
        self.Hidden3 = LayerDense (5,18, Sigmoide, dSigmoide)
        self.Class = LayerDense (3,5,   Sigmoide,dSigmoide)

    def FeedForward (self,Inputs):
        o1 = self.Perc.FeedForward (Inputs)
        o2 = self.Hidden1.FeedForward (o1)
        o3 = self.Hidden2.FeedForward (o2)
        o4 = self.Hidden3.FeedForward (o3)
        output = self.Class.FeedForward (o4)
        return output

        
    def BackProp (self,Inputs, VA):
        
        o1 = self.Perc.FeedForward (Inputs)
        o2 = self.Hidden1.FeedForward (o1)
        o3 = self.Hidden2.FeedForward (o2)
        o4 = self.Hidden3.FeedForward (o3)
        output = self.Class.FeedForward (o4)
        
        errori = output- VA
        errori_class = self.Class.BackProp (o4,errori)
        errori_hidden3 = self.Hidden3.BackProp (o3,errori_class)
        errori_hidden2 = self.Hidden2.BackProp (o2,errori_hidden3)
        errori_hidden1 = self.Hidden1.BackProp (o1,errori_hidden2)
        _ = self.Perc.BackProp (Inputs, errori_hidden1)
        return errori ** 2
    
    
miaRete = Rete ()
predataset = []
with open ('iris.csv','r') as file:
    csvreader = csv.reader (file, delimiter=',', quotechar='"')
    for riga in csvreader:
        predataset.append(riga)
    
Dataset = []
for i, riga in enumerate(predataset):
    if i> 0 and len (riga) == 5:
        dato = [float(x) for x in riga[:4]]
        if riga[-1] =='Setosa':         # 1,0,0
            dato.append (1)
            dato.append (0)
            dato.append (0)
        if riga[-1] =='Versicolor':     # 0,1,0
            dato.append (0)
            dato.append (1)
            dato.append (0)
            
        if riga[-1] =='Virginica':      # 0,0,1            
            dato.append (0)
            dato.append (0)
            dato.append (1)
        Dataset.append(dato)
         
         

 
              
RDataset =  np.array(Dataset)

massimi = np.max (RDataset,axis=0)

Dataset = RDataset / massimi

batch_size= 1

ErroriMedi = []
for epoca in range (2000):
    random.shuffle(Dataset)  
    erroremedio = np.zeros (3)
    for dato in Dataset[:len(Dataset)//batch_size]:
        erroremedio = erroremedio +  miaRete.BackProp (dato[:4],np.array(dato[4:]))
    erroremedio = (erroremedio / len (Dataset) )** .5
    
    ErroriMedi.append (erroremedio)
    
    if epoca % 50 == 0:
        print (epoca, erroremedio)
    
    
plt.figure()
plt.plot (range (len(ErroriMedi)),ErroriMedi)
plt.show()


# Senza batch_size => 1950 [0.00380104 0.00380653 0.0038065 ]
# Con batch_size=8 => 1950 [0.00350677 0.0038725  0.00390462]

