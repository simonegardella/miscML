import csv


MiInteressa = ['N. Provvedimento','Data Provvedimento','Tipologia di accordo']

intestazioni = []
dati =[]
try:
    with open ('piene.csv','r',encoding='utf-8') as f:
        csvreader = csv.reader(f,delimiter=';')
        for riga in csvreader:
            if intestazioni ==[]: 
                intestazioni = riga # Mi trovol le intestazioni
            else:   
                if len (riga) == len (intestazioni):
                    dato =[]
                    for campo in MiInteressa: # per ogni intestazione che mi interessa
                        if campo in intestazioni:  # se esiste
                            indice = intestazioni.index(campo) # trovo la posizione dove il campo che mi interessa si trova
                            dato.append (riga[indice]) # aggiungi il valore all'indice che ho trovato
                    dati.append(dato) # Lo aggiungo alla mia lista
                    
                
    tipiaccordo = []

    for dato in dati:
        if not dato[-1] in tipiaccordo:
            tipiaccordo.append(dato[-1])
            
    for tipoaccordo in tipiaccordo:
        print (tipoaccordo, end =" => ")
        totale = 0
        for dato in dati:
            if dato[-1] == tipoaccordo:
                totale += 1
        print (totale)
except FileNotFoundError:
    print ("Non ho trovato il file delle piene!!!!")
