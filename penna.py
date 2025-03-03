class Penna ():
    def __init__ (self):
        self.colore = ''
    def Scrivi (self,testo):
        if self.colore != '':
            print (testo, end='')
    def ColoreRefill (self,colore):
        self.colore = colore
        
class BIC (Penna):
    def __init__(self):
        super().__init__()
        self.refill = 100
        
        
    def Scrivi(self, testo):
        if len(testo) > self.refill:
            testo = testo[:self.refill]  
        self.refill -= len(testo)
        return super().Scrivi(testo)
    
class BICaScatto (BIC):
    def __init__(self):
        super().__init__()
        self.colore = 'Blu'
        self.aperto = False
        
    def apri (self):
        self.aperto = True
    def chiudi (self):
        self.aperto = False
    def Scrivi(self, testo):
        if self.aperto:
            return super().Scrivi(testo)
        
Biro = BICaScatto()
testo = input ("Cosa devo scrivere?")


Biro.apri()



for i in range (300):
    Biro.Scrivi(testo)
    
    