a= 5
b = int (input ('num:'))

try:
    print (a/b)
except ZeroDivisionError:
    print ("Divisione per zero")
    try:
        print (a/b)
    except:
        print ("Errore nell'except")
except IndexError :
    print ("Errore generico")