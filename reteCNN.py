import tensorflow as tf
import numpy as np
import random


x = np.random.random((100,28,28,1))
y = np.zeros ((100,10))
for y1 in range (y.shape[0]):
    y[y1,random.randint(0,9)] = 1


modello = tf.keras.models.Sequential()
modello.add (tf.keras.Input ((28,28,1)))
modello.add (tf.keras.layers.Conv2D( 32, 3, strides=(1, 1) ,padding = "same"))
modello.add (tf.keras.layers.MaxPooling2D(2,padding="same"))
modello.add (tf.keras.layers.Conv2D( 64, 2, strides=(1, 1) ,padding = "same"))
modello.add (tf.keras.layers.MaxPooling2D(2,padding="same"))
modello.add (tf.keras.layers.Flatten())
modello.add (tf.keras.layers.Dense (128))
modello.add (tf.keras.layers.Dense (10, activation ="softmax"))

modello.compile(optimizer='adam',
  loss='mse',
  metrics=['accuracy'])

modello.summary()

modello.fit(x, y, epochs=500)
