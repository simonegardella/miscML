import pickle
studenti = []

def Inserisci ():
    nome = input ('Inserisci il nome dello studente:')
    studenti.append (nome)

def Modifica ():
    global studenti
    Lista()
    try:
        n = int(input ('Quale studente vuoi modificare?'))
        if 0<= n < len (studenti):
            nuovonome = input (f'Come si chiama lo studente che prima hai nominato come {studenti[n]}:')
            if nuovonome != '':
                studenti[n]  = nuovonome  
        else:
            print ('La scelta che hai operato non è valida')
    except ValueError:
        print ('La scelta immessa non è un numero')
    
def Cancella ():
    global studenti
    Lista()
    try:
        n = int(input ('Quale studente vuoi cancellare?'))
        if 0<= n < len (studenti):
            print (f'Cancello lo studente {studenti[n]}')
            del studenti[n]
        else:
            print ('La scelta che hai operato non è valida')
    except ValueError:
        print ('La scelta immessa non è un numero')
        

def Lista ():
    print (' Lista degli studenti inseriti:')
    for i, studente in enumerate(studenti):
       print (i,studente) 
    print (' ---------')
    
    
def Ordina ():
    global studenti
    studenti.sort()
    Lista()
    
def CaricaDati ():
    global studenti
    try:
        studenti = pickle.load(open ('studenti.pk','rb'))
    except FileNotFoundError:
        print ('  >>>>  Il file non è stato ancora creato!!! Lo salverò all\'uscita del programma  <<<<')
def SalvaDati ():
    pickle.dump (studenti, open ('studenti.pk','wb'))

def _quit():
    pass

azioni = {'q':'Uscire dal programma',
          'i':'Insierire uno studente',
          'm':'Modificare uno studente',
          'c':'Cancellare uno studente',
          'l':'Mostrare tutti gli studenti',
          'o':'Ordina i nomi'}


funzioni = {'q':_quit,
            'i':Inserisci,
            'm':Modifica,
            'c':Cancella,
            'l':Lista,
            'o':Ordina}


def StampaMenu():
    print (' ***********************************************')
    print (' *  Menu principale dell\'anagrafica studenti  *')
    print (' ***********************************************')
    print ()
    for chiave in azioni.keys():
        print (f"{chiave} per {azioni[chiave]}")

def FiltraScelta(scelta):
    if not scelta in azioni.keys():
        print ()
        print (' >>>>>>>>>   La scelta immessa non è valida <<<<<<<<<' )
        
    else:
        funzioni[scelta]()
    
    print ("\n\n")

scelta = ""
CaricaDati()

while not scelta == 'q':
    StampaMenu()
    scelta = input ('Qaule azione vuoi eseguire?')
    FiltraScelta(scelta)
    
SalvaDati()
    