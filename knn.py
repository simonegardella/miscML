import numpy as np
import math
from collections import Counter

def distanza_euclidea(punto1, punto2):
    dist = 0.0
    for i in range (len(punto1)):
        dist += (punto1[i]-punto2[i])**2
    return dist**.5
    #return  np.sqrt(np.sum((punto1-punto2)**2))

def getKNN (train_data,train_labels,test_point, k):
    distanze =[]
    
    for i in range (len(train_data)):
        distanze.append ([distanza_euclidea(test_point,train_data[i]),train_labels[i]])
        
    distanze.sort (key = lambda dato:dato[0])
    vicini = distanze[:k]
    
    return [dato[1] for dato in vicini]
        
def prediciKNN (dataset, etichette, testset, k):
    predizioni = []
    for test_point in testset:
        vicini = getKNN(dataset,etichette, test_point,k)
        vicinoComune = Counter(vicini).most_common(1)[0][0]
        predizioni.append (vicinoComune)
    return predizioni
        
Dataset = [
    [5.1,3.5,1.4,.2],
    [4.9,3,1.4,.2],
    [5.8,2.7,5.1,1.9],
    [7.1,3,5.9,2.1]
]

ResultSet =[0,0,1,1]
testset = [
     [5,3.2,1.3,0.21],
     [6,2.5,4.9,2.0],
]

k = 3


print (prediciKNN (Dataset,ResultSet,testset,k))