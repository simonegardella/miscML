import numpy as np
import random 
import math


class Dataset ():
    def __init__ (self, numero_classi,punti):
        self.classi = numero_classi
        self.X = ([])
        self.Y = np.array([])
        self.populate(punti)
        
    def populate (self,punti):
        self.X = []
        self.Y =[]
        centrox, centroy = 0.5,0.5

        raggio = 0.0001
        angolototale = 360 + 180
        raggioaggiunto = (0.5 - raggio ) / angolototale
    
        while (len (self.X)/2 < punti):
            for angolo in range (0,angolototale):
                angolorad = angolo / 180 * math.pi 
                for classe in range (self.classi):
                    angoloclasse =classe * 360/self.classi /180 * math.pi
                    rumore = random.random () * 0.1/self.classi
                
                    self.X.append ([centrox+(raggio+rumore) * math.cos(angolorad+ angoloclasse), centroy+ (raggio+rumore) * math.sin (angolorad+angoloclasse) ])
                    self.Y.append ([classe])
                raggio += raggioaggiunto
            
        step = len(self.X) //punti
        
        Xtemp = []
        Ytemp = []
        for indice in range (0, len(self.X),step):
                Xtemp.append (self.X[indice])
                Ytemp.append (self.Y[indice])
                
        self.X = Xtemp.copy()
        self.Y = Ytemp.copy()
        
        
        self.X = np.array(self.X)
        self.Y = np.array(self.Y)
        
    def shuffle (self,iter = 100):
        for i in range (iter):
            x1 = random.randint(0,self.X.shape[0]-1)
            x2 = random.randint(0,self.X.shape[0]-1)
            dato = self.X[x1,:]
            self.X[x1,:] = self.X[x2,:]
            self.X[x2,:] = dato
            
            dato = self.Y[x1,:]
            self.Y[x1,:] = self.Y[x2,:]
            self.Y[x2,:] = dato
    
            
            
        