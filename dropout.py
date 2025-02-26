import numpy as np

class Dropout ():
    def __init__ (self, nInputs, alfa = 0.3):
        self.nInputs = nInputs
        self.alfa = alfa
        
    def FeedForward (self,inputs):
        c = np.random.choice(inputs.shape[0],int(self.alfa*inputs.shape[0]))
        for nn in c:
            inputs[nn] = 0
        return inputs
    
    def BackProp (self,inputs,errori):
        return errori