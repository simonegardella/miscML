import random
import math
import statistics as stats
import matplotlib.pyplot as plt


minimo = 1
massimo = 10000000

listatentativi =[]

tetnativimassimi = int(math.log2(massimo))+1
print (f"Il numero massimo di tentativi che impiegherò è {tetnativimassimi}")

for i in range (100):
    minimo = 1
    massimo = 10000000
    dado = random.randint(minimo,massimo)
    tentativi = 0
    valore = 0
    while dado != valore:
        valore = int ((minimo+massimo)/2)
        if valore > dado:
            #print ("Il numero immesso è più grande di quello del dado")
            massimo = valore -1
        if valore < dado:
            #print ("Il numero immesso è più piccolo di quello del dado")
            minimo = valore + 1
        tentativi+=1
        
    #print (f"Hai indovinato in {tentativi} tentativi")
    listatentativi.append (tentativi)
    
print ("Il numero medio di tentavi è ", stats.mean(listatentativi))

plt.figure()
plt.plot(range(0,len(listatentativi)),listatentativi)
plt.show()