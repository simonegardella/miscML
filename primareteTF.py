import tensorflow as tf
import numpy as np
X = np.random.random((1000,25,1))
Y = np.random.random ((1000,3))


modello = tf.keras.models.Sequential()
modello.add(tf.keras.Input (shape=X.shape [1:]))

modello.add (tf.keras.layers.Dense(32,activation='sigmoid'))
modello.add (tf.keras.layers.Dense(64,activation='sigmoid'))
modello.add (tf.keras.layers.Dense(16,activation='sigmoid'))
modello.add (tf.keras.layers.Flatten())
modello.add (tf.keras.layers.Dense(3,activation='sigmoid'))

modello.summary()


modello.compile(optimizer=tf.keras.optimizers.Adam(
    learning_rate=0.003),
  loss='mse',
  metrics=['accuracy'])

modello.fit (X,Y,epochs = 10)


predizione = modello.predict (np.random.random((2,25,1)))

print (predizione)