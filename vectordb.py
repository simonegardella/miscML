from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams,Distance, PointStruct
from sentence_transformers import SentenceTransformer
#client = QdrantClient ("http://127.0.0.1:6333") # docker run -p 6333:6333 qdrant/qdrant
#client = QdrantClient (path='miodatabse.qdrant')
client = QdrantClient (":memory:")
nomeCollection = 'miei documenti'
documenti = [
"I modelli generativi stanno cambiando il modo in cui pensiamo all'intelligenza artificiale e alla creatività e hanno il potenziale per trasformare i settori, dai media alla finanza alla sanità.",
"I modelli generativi sono un fattore chiave per la creatività delle macchine, in quanto consentono loro di andare oltre ciò che hanno già visto e di creare qualcosa di nuovo.",
"Come per tutte le rivoluzioni tecnologiche, mi aspetto un impatto significativo sui posti di lavoro, ma è molto difficile prevedere esattamente quale sarà l'impatto... Credo che dall'altra parte ci saranno molti più posti di lavoro e che i posti di lavoro di oggi miglioreranno... Penso che sia importante capire e pensare al GPT-4 come a uno strumento, non a una creatura, che è facile confondere, ed è uno strumento su cui le persone hanno un grande controllo e su come lo usano. In secondo luogo, il GPT-4 e altri sistemi simili sono adatti a svolgere compiti, non lavori",
"L'intelligenza artificiale generativa è la chiave per risolvere alcuni dei più grandi problemi del mondo, come il cambiamento climatico, la povertà e le malattie. Ha il potenziale per rendere il mondo un posto migliore per tutti",
"L'IA generativa ha il potenziale per cambiare il mondo in modi che non possiamo nemmeno immaginare. Ha il potere di creare nuove idee, prodotti e servizi che renderanno la nostra vita più facile, più produttiva e più creativa. Ha anche il potenziale per risolvere alcuni dei maggiori problemi del mondo, come il cambiamento climatico, la povertà e le malattie. Il futuro dell'IA generativa è luminoso e sono entusiasta di vedere cosa ci riserverà",
"L'intelligenza artificiale generativa è il più potente strumento di creatività che sia mai stato creato. Ha il potenziale per scatenare una nuova era di innovazione umana",
"L'intelligenza artificiale generativa ha aperto possibilità entusiasmanti nel campo delle immagini e dei video. Le sue capacità di manipolazione e trasformazione offrono nuove strade per l'espressione artistica, la creazione di contenuti e la narrazione coinvolgente. Mentre questa tecnologia continua a evolversi, è essenziale sfruttare il suo potere in modo responsabile e garantire il suo impatto positivo sulla società.",
"In un mondo in cui ChatGPT e altre app di intelligenza artificiale possono fare molte cose che un tempo gli esseri umani dovevano fare da soli o dovevano assumere altri esseri umani per farle, la domanda come aggiungerò valore? diventa più importante che mai",
"Aristotele ha fondato o scoperto la logica osservando il mondo. ChatGPT pensa in modo logico. Perché? Perché nota tutta la logica nei dati del suo set di addestramento",
"L'intelligenza artificiale generativa ci sta insegnando che il modo in cui si parla è in realtà il codice stesso"
]
modello = SentenceTransformer ('sentence-transformers/all-MiniLM-L6-v2')
client.recreate_collection (collection_name=nomeCollection, vectors_config=VectorParams (size=384, 
                                                                    distance= Distance.COSINE ) )
vettori = []
for documento in documenti:
    vettori.append(modello.encode (documento).tolist()) 
client.upsert (collection_name=nomeCollection, points = [PointStruct(id =i, vector= vettori[i],
                                        payload={'testo': documenti[i]}) for i in range (len (documenti))]) 

while True:
    query = input ('dimmi cosa cerchi?')
    vettore_query = modello.encode (query).tolist()
    risultati = client.search (collection_name= nomeCollection, query_vector= vettore_query, limit = 2)
    for risultato in risultati:
        print ("{}, (score:{:.2f})".format (risultato.payload['testo'], risultato.score))