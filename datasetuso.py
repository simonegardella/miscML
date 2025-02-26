from dataset_tipo4 import *
import matplotlib.pyplot as plt



numero_classi = 2
mioDS = Dataset(numero_classi,100)
mioDS.shuffle()
plt.figure()
for i in range (numero_classi):
    x = []
    y= []
    for nelemento  in range (len (mioDS.X)):
        if mioDS.Y[nelemento,0] == i:
            x.append (mioDS.X[nelemento,0])
            y.append (mioDS.X[nelemento,1])
        
    plt.scatter (x,y)
plt.show()