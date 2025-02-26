
import tensorflow as tf
import tensorflow_hub as hub
import cv2
import numpy as np
hubaddress = "https://tfhub.dev/tensorflow/faster_rcnn/resnet50_v1_640x640/1"
modello = hub.load(hubaddress)

immagineorig = cv2.imread ('persone1.png')
immagine = cv2.cvtColor(immagineorig.copy(),cv2.COLOR_BGR2RGB)
immagine_redim = cv2.resize(immagine,(640,640))

immagine_redim_1 = np.expand_dims(immagine_redim.copy(),axis=0)

output = modello (immagine_redim_1)


boxes   = output['detection_boxes'].numpy()[0]
confidenza  = output['detection_scores'].numpy()[0]
classi  = output['detection_classes'].numpy()[0]

for indice in range (len (confidenza)):
    if confidenza[indice]> 0.5:
        y1,x1,y2,x2 = boxes[indice]*640
        cv2.rectangle(immagine_redim,(int(x1),int(y1)),(int(x2),int(y2)),(0,255,0))
        
cv2.imshow ('Modello faster', immagine_redim)
cv2.waitKey(0)