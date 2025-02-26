import math
import re
a = 5.5 # float 

b = 25 # int

miopi = math.pi

k ='oggi'


for elemento in k:
    print (elemento)

for i in range (len (k)):
    print (k[i])
    
    
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print (x)


miaLista = [a,b,miopi,k]
nuovalista = [miaLista,k,miaLista]
listapadre = [miaLista,nuovalista.copy(),a,b]

dizionario = {}

for i in range (15):
    dizionario[i] = i**2
    
for chiave in list(dizionario.keys())[-3:]:
     print (chiave, dizionario[chiave])   
