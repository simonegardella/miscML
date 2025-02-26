for i in range (10):
    try:
        print (i,end ='\t')
        _ = i / (4-i)
    except ZeroDivisionError:
        print ()

print ()
try:
    print ('Apro')
    #raise Exception
    print ('Lavoro con un file')
    print ('Chiudo il file')
    
except:
    print ('Il file è corrotto')
    
finally:
    #print ('Chiudo il file')
    _ = 1
    # Clean up