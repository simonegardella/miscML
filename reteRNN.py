import tensorflow as tf
import numpy as np
import math
import matplotlib.pyplot as plt

X= []

for x in range (1600):
    X.append (x/500*math.sin(x/180*math.pi)+x/200)
    
massimo = max (X)
    
lookback= 50
stride = 2
Xtrain = []
Ytrain = []
for i in range (lookback,len(X),stride):
    Xtrain.append (X[i-lookback:i-1])
    Ytrain.append (X[i])

Xtrain = np.array (Xtrain) /massimo
Ytrain = np.array (Ytrain) /massimo
Xtrain = np.reshape (Xtrain, (*Xtrain.shape,1))
Ytrain = np.reshape (Ytrain, (*Ytrain.shape,1))


modello = tf.keras.models.Sequential()
modello.add (tf.keras.Input (Xtrain.shape[1:]))
modello.add (tf.keras.layers.LSTM(128,return_sequences=False))
modello.add (tf.keras.layers.Dense (32))
modello.add (tf.keras.layers.Dropout(0.3))
modello.add (tf.keras.layers.Dense (1,activation='sigmoid'))


modello.compile(optimizer='adam',
                loss = 'mse',
                metrics=['accuracy'])


modello.summary()

modello.fit (Xtrain,Ytrain,epochs=25)


Xoriginale = []
Xpredetto = modello.predict (Xtrain)



plt.figure()
plt.plot (range (len(Ytrain)),Ytrain)
plt.plot (range (len(Xpredetto)),Xpredetto)
plt.show()
