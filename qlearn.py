import numpy as np


peso_stare = 1
peso_muoversi = 0.8
Ricompense = np.ones((25,25)) * (-1)


def ApriVarco (c1,c2):
    Ricompense[c1,c2] = 1
    Ricompense[c2,c1] = 1
    
    
ApriVarco(0,1)
ApriVarco(2,1)
ApriVarco(2,7)
ApriVarco(6,7)
ApriVarco(6,11)
ApriVarco(6,11)
ApriVarco(10,11)
ApriVarco(12,11)
ApriVarco(16,11)
ApriVarco(12,17)
ApriVarco(22,17)
ApriVarco(22,23)
ApriVarco(24,23)
ApriVarco(17,18)
ApriVarco(13,18)
ApriVarco(13,8)
ApriVarco(9,8)
ApriVarco(9,14)
ApriVarco(19,14)
ApriVarco(9,4)
ApriVarco(3,4)
ApriVarco(15,20)
ApriVarco(21,20)

Qualita = np.zeros_like(Ricompense)
Qualita[4,4] = 100 # Formaggio = GOAL

def Bellman (stato, azione):
    global Ricompense,Qualita,peso_stare,peso_muoversi
    return peso_stare * Ricompense[stato,azione] + peso_muoversi * max (Qualita[azione,:])


def Addestramento (epoche=100):
    global Ricompense,Qualita
    for epoca in range (epoche):
        for stato in range(Ricompense.shape[0]):
            for azione in range(Ricompense.shape[1]):
                if Ricompense[stato,azione] != -1:
                    Qualita[stato,azione] = Bellman(stato,azione)
                    
Addestramento()