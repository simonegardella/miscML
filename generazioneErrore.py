nome = ''
cognome = ''
def setta (_nome, _cognome):
    global nome, cognome
    nome = _nome
    cognome = _cognome
    
def GeneraCI ():
    if nome =='' or cognome == '':
        raise Exception
    print ("Ecco la tua carta di identità ", nome,  cognome)
    
    
try:
    nome = input ('name:')
    cognome = input ('surname:')
    GeneraCI()
except:
    print ("you entered invalid data!!!!")