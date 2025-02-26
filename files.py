f = open ('miotesto.txt')
righe = f.readlines()
f.close()


f = open ('risultato.txt','w')
for riga in righe:
    for k in range (2):
        f.write(riga)
        if riga[-1] != '\n':
            f.write ('\n')
        
f.close()

for riga in righe:
    if riga[-1] == '\n':
        riga = riga[:-1]
    print (riga)