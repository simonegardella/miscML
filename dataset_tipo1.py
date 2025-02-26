import numpy as np
import random 


class Dataset ():
    def __init__ (self, numero_classi,punti):
        self.classi = numero_classi
        self.X = ([])
        self.Y = np.array([])
        self.populate(punti)
        
    def populate (self,punti):
        self.X = []
        self.Y =[]
        separatore = 1/ self.classi

        while len (self.X) < punti:
            x = random.random()
            y= random.random()
        
            
            for classe in range(self.classi):
                if classe * separatore <= x  < (classe+1)* separatore and classe * separatore <= y  < (classe+1)* separatore:
                    self.X.append([x,y])
                    self.Y.append ([classe])
                    
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
    
            
            
        