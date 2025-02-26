from classeFile import *

NomiLibri = ['IPromessiSposi.txt','IPromessiSposiFake.txt']

Libri =[]

for nomelibro in NomiLibri:
    Libri.append(Libro(nomelibro))
    
for i,nomelibro in enumerate(NomiLibri):
    print ("Il libro {} ha {} capitoli".format(NomiLibri[i],len(Libri[i].capitoli)))




"""


PromessiSposi = Libro ('IPromessiSposi.txt')


if PromessiSposi.LibroCaricato:
    print ('Ci sono {} capitoli'.format(len(PromessiSposi.capitoli)))
    for i, capitolo in enumerate(PromessiSposi.capitoli):
        print ("Il capitolo {} finisce con '...{}'".format(i+1, capitolo[-30:]))
        
        
"""