import numpy as np
import matplotlib.pyplot as plt

X= np.random.random(size=(200,2))
def distanza_euclidea(punto1, punto2):
    #return ((punto1[0]-punto2[0])**2 + (punto1[1]-punto2[1])**2)**.5
    return  np.sqrt(np.sum((punto1-punto2)**2))

def kmeans (Dataset, classi, massime_iterazioni = 100):
    centroidi = Dataset[np.random.choice(Dataset.shape[0],classi, replace=False)]
    i = 0
    while i <= massime_iterazioni:
        etichette = []
        for dato in Dataset:
            distanzedacentroide = []
            for centroide in centroidi:
                distanzedacentroide.append(distanza_euclidea(dato,centroide))
            etichetta = np.array (np.argmin(np.array(distanzedacentroide)))
            etichette.append (etichetta)
        etichette = np.array(etichette)    
        nuovicentroidi = np.array ([Dataset[etichette == i].mean (axis =0) for i in range (classi)])
        if np.all (centroidi == nuovicentroidi):
            break
        centroidi = nuovicentroidi
        i = i+1
    return centroidi, etichette,i

classi = 4
centroidi , etichette,iterazioni = kmeans (X,classi)
print ('Centroidi:',centroidi)
print ('Elementi:',etichette)
print ('Ottenuto in n. ',iterazioni,'iterazioni')

cluster1 = []
cluster2 = []
for i, dato in enumerate(X):
    if etichette[i] == 0:
        cluster1.append (dato)
    if etichette[i] == 1:
        cluster2.append (dato)
    
cluster1 = np.array(cluster1)
cluster2 = np.array(cluster2)
plt.figure()
plt.scatter(cluster1[:,0],cluster1[:,1])
plt.scatter(cluster2[:,0],cluster2[:,1])

plt.scatter([centroidi[0,0]],[centroidi[0,1]])
plt.scatter([centroidi[1,0]],[centroidi[1,1]])
plt.show()