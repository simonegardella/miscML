def EPrimo(k):
    for i in range (2,k):
        if k % i == 0:
            return False
    return True

def stampaIPrimiNumeri(k):
    for i in range (k+1):
        if EPrimo(i):
            print (i)
            
            
