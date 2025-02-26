import csv
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

predataset = []
with open ('iris.csv','r') as file:
    csvreader = csv.reader (file, delimiter=',', quotechar='"')
    for riga in csvreader:
        predataset.append(riga)
    
Dataset = []
ResultSet = []

for i, riga in enumerate(predataset):
    if i> 0 and len (riga) == 5:
        dato = [float(x) for x in riga[:4]]
        Dataset.append(dato)
        if riga[-1] =='Setosa':         # 1,0,0
            ResultSet.append ([1,0,0])
        if riga[-1] =='Versicolor':     # 0,1,0
            ResultSet.append ([0,1,0])
        if riga[-1] =='Virginica':      # 0,0,1            
            ResultSet.append ([0,0,1])
            
Dataset = np.array(Dataset)
ResultSet = np.array (ResultSet)

modello = tf.keras.models.Sequential()
modello.add (tf.keras.Input (shape = Dataset.shape[1:]))
modello.add (tf.keras.layers.Dense (16,activation='relu'))
modello.add (tf.keras.layers.Dense (8,activation='relu'))
modello.add (tf.keras.layers.Dense (ResultSet.shape[-1],activation='softmax'))


modello.compile (optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
#modello.compile (optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),....)
modello.summary()

modello.fit (Dataset,ResultSet,epochs = 100, batch_size=8)

plt.figure()
plt.plot(modello.history.epoch, modello.history.history['accuracy'])
plt.plot(modello.history.epoch, modello.history.history['loss'])

plt.show()




