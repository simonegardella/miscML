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
        raggioseparatore = 0.5/ self.classi
        centrox, centroy = 0.5,0.5
        angolo = 0 # gradi

        while len (self.X) < punti:
            raggiopunto = random.random() * 0.5
            angolorad = angolo / 180 * math.pi
            classe = int(raggiopunto / raggioseparatore)
            self.X.append ([centrox+raggiopunto * math.cos(angolorad), centroy+ raggiopunto * math.sin (angolorad) ])
            self.Y.append ([classe])
            angolo +=1
            
            

                    
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
    
            
            
        