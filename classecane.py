import random
class Cane ():
    def __init__ (self, Nome=''):
        self.Nome = Nome
        self.Colore = ''
        self.Taglia = ''
        self.Razza = ''
        
        if random.random()< 0.5:
            self.verso = "Bau Bau"
        else:
            self.verso = "Wolf"
        
    def Abbaia (self):
        print (self.Nome +": "+ self.verso)
        
    def printRazza (self):
        print (self.Razza)
        
        
class Lagotto (Cane):
    def __init__ (self,Nome='',Eta=0):
        super().__init__(Nome)
        self.Eta = Eta
        self.Razza = 'Lagotto'
        
    def Abbaia (self):
        print (self.Nome+": Bau Bau Bau")
    def trovaTartufo (self):
        if random.random()< 0.5:
            print ("Lo ho trovato!!!")
        else:
            print ("Non ci sono riuscito")
        
        
ListaCani = [Cane (str(x)) for x in range (20)]

for cane in ListaCani:
    cane.Abbaia()
    
MioLagotto = Lagotto('Pippo')
    