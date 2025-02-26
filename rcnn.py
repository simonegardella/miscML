# Feature extractor -> RPN
#                  +-> Classificatore

# Input 224 x 224 x 3
# 2000 x 1000 x 3 -> 224 x 224 x 3 

import tensorflow as tf

def featureExtractor ():
    inputs = tf.keras.Input (shape = (224,224,3))
    o1 = tf.keras.layers.Conv2D (64,(3,3),activation='relu',padding = "same")(inputs)
    o2 = tf.keras.layers.MaxPooling2D ((2,2))(o1)
    o3 = tf.keras.layers.Conv2D (128,(3,3),activation='relu',padding = "same")(o2)
    o4 = tf.keras.layers.MaxPooling2D ((2,2))(o3)
    o5 = tf.keras.layers.Conv2D (256,(3,3),activation='relu',padding = "same")(o4)
    o6 = tf.keras.layers.MaxPooling2D ((2,2))(o5)
    return tf.keras.models.Model (inputs,o6,name ='FeatureExtractor')


def RPN (feature_map):
    o1 = tf.keras.layers.Conv2D (256,(3,3), activation='relu',padding = "same")(feature_map)
    confidenza = tf.keras.layers.Conv2D (1, (1,1),activation = 'sigmoid',name='confidenza_rpn')(o1)
    boxes = tf.keras.layers.Conv2D (4, (1,1),activation = 'linear',name='boxes_rpn')(o1) # x1,y1,w,h
    return confidenza, boxes

def Classificatore (feature_map):
    o1 = tf.keras.layers.Flatten ()(feature_map)
    o2 = tf.keras.layers.Dense (1024,activation ='relu')(o1)
    o3 = tf.keras.layers.Dense (512,activation ='relu')(o2)
    classificazione = tf.keras.layers.Dense (20,activation ='softmax',name='classe')(o3) 
    box = tf.keras.layers.Dense (4,activation ='linear',name='BOX')(o3) 
    return classificazione,box
    
imageinput = tf.keras.Input (shape=(224,224,3))
FE = featureExtractor ()
feature_map = FE(imageinput)
confidenza, boxes = RPN (feature_map)
classe, box = Classificatore (feature_map)

modello = tf.keras.models.Model (imageinput,[confidenza, boxes,classe,box])
modello.compile (optimizer='adam', loss = ['binary_crossentropy','mse','categorical_crossentropy','mse'])

modello.summary()
    

    
