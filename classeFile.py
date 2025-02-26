class Libro ():
    def __init__ (self,nomefile = ''):
        self.capitoli = []
        self.LibroCaricato = False
        if nomefile != '':
            self.CaricaLibro(nomefile)
        
    def CaricaLibro (self,nomefile):
        try:
            with open (nomefile,'r') as f:
                corpus = f.readlines()   
                buffer = ""
                for riga in corpus:
                    if 'CAPITOLO ' in riga:
                        # svuotare il buffer
                        if buffer != '':
                            self.capitoli.append (buffer[:-1])
                        buffer = ""
                    elif riga != '\n':
                        buffer += riga
                        
                if buffer != '':
                    self.capitoli.append (buffer[:-1])
                    buffer = ''
                self.LibroCaricato = True 
        except FileNotFoundError:
            print ('Il file non esiste')
            self.LibroCaricato = False
        except:
            print ('Per un errore generico non sono riuscito a carica il libro')
            self.LibroCaricato = False
  