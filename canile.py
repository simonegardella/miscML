from  classecane import *


class Canile ():
    def __init__ (self,numerocani):
        self.ListaCani = [Cane (str(x)) for x in range (numerocani)]
        
    def __len__ (self):
        return len (self.ListaCani)
    
    def __add__ (self,cane):
        self.ListaCani.append(cane)

        
canileCorsoML = Canile (20)

"""

for i in range (len(canileCorsoML.ListaCani)):
    print (canileCorsoML.ListaCani[i].Nome)
    
"""