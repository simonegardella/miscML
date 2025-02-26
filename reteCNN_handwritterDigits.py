import tensorflow as tf
import numpy as np
import random
import os
import cv2 # pip3 install opencv-python
import tqdm



def shuffle (ds,rs):
  for i in tqdm.tqdm(range (len(ds)//2)):
    e1 = random.randint(0,len(ds)-1)
    e2 = random.randint(0,len(ds)-1)
    dTemp = ds[e1].copy()
    rTemp = rs[e1].copy()
    ds[e1] = ds[e2].copy()
    rs[e1] = rs[e2].copy()
    ds[e2] = dTemp
    rs[e2] = rTemp
  return np.array(ds), np.array(rs)
cifre = [str(x) for x in range (10)]

Dataset = []
Resultset =[]

for cifra in cifre:
  for data in os.walk (f'./HandwrittenDigits/{cifra}/'):
    for file in data[-1]:
      immagine = cv2.imread (f'./HandwrittenDigits/{cifra}/{file}')
      immagine = cv2.cvtColor (immagine, cv2.COLOR_RGB2GRAY) /255
      Dataset.append (immagine)
      out = [0]* 10
      out[int(cifra)] = 1
      Resultset.append (out)
      
Dataset,Resultset = shuffle (Dataset,Resultset)
modello = tf.keras.models.Sequential()
modello.add (tf.keras.Input ((28,28,1)))
modello.add (tf.keras.layers.Conv2D( 64, 3, strides=(1, 1) ,padding = "same",activation='relu'))
modello.add (tf.keras.layers.MaxPooling2D(2,padding="same"))
modello.add (tf.keras.layers.Conv2D( 128, 2, strides=(1, 1) ,padding = "same",activation='relu'))
modello.add (tf.keras.layers.MaxPooling2D(2,padding="same"))
modello.add (tf.keras.layers.Conv2D( 256, 2, strides=(1, 1) ,padding = "same",activation='relu'))
modello.add (tf.keras.layers.MaxPooling2D(2,padding="same"))
modello.add (tf.keras.layers.Flatten())
modello.add (tf.keras.layers.Dense (128,activation='relu'))
modello.add (tf.keras.layers.Dropout(0.3))
modello.add (tf.keras.layers.Dense (10, activation ="softmax"))

modello.compile(optimizer='adam',
  loss='categorical_crossentropy',
  metrics=['accuracy'])

modello.summary()

modello.fit(Dataset,Resultset, epochs=500,batch_size=128)
