import csv
f = open ('miofilecsv.csv','r')
mioreader = csv.reader(f,delimiter=',')

for riga in mioreader:
    print (riga)

f.close()