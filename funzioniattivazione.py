import numpy as np
import math


a = 1
alfa = 0.01

# Classificatori

def Sigmoide (x):
    return 1/ (1+math.exp (-x))

def dSigmoide (x):
    sig = Sigmoide(x)
    return sig * (1-sig)

# Reti ricorrenti

def Tanh (x):
    return math.tanh(x)

def dTanh(x):
    tanh = Tanh(x)
    return 1- tanh**2

def Linear (x):
    global a
    return a* x

def dLinear (x):
    global a
    return np.ones_like(x)*a


# Reti Convoluzionali 
def Relu (x):
    if x <= 0:
        return 0
    else:
        return x
    
def dRelu (x):
    if x <= 0:
        return 0
    else:
        return 1

def leakyRelu (x):
    global alfa
    if x <= 0:
        return alfa * x
    else:
        return x
    
def dleakyRelu (x):
    global alfa
    if x <= 0:
        return alfa
    else:
        return 1
    
    
# Classificatore esclusivo
def SoftMax (X): # X = [.....]
    denominatore = 0
    X = np.array(X)-np.min (X)
    for x in X:
        denominatore += math.exp (x)
    return np.exp(np.array(X))/denominatore
    
        