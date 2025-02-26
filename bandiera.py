import cv2
import math
import numpy as np

bandiera = cv2.imread('bandiera.png')

bandiere = []
ymax, xmax = bandiera.shape[:2]
print (xmax)

step = 5
for angolo in range (0,360,step):

    nuovabandiera = np.ones ((ymax*2,xmax,3),dtype=np.uint8) *127
    
    
    for x in range (xmax):
        angolorad = (angolo+x/275 * 360)/180*math.pi  # angolo : angolorad = 180 : pi
        correttivoY = int(ymax/2 + math.sin (angolorad) * ymax/3)
        for cy in range (ymax):
            nuovabandiera[correttivoY +cy,x,:] = bandiera[cy,x,:]
    
    
    bandiere.append(nuovabandiera)
    


indice = 0
_quit = False
while not _quit and len (bandiere)> 0:
    
    cv2.imshow('Bandiera Italiana', bandiere[indice])
    indice +=1
    if indice == len (bandiere):
        indice = 0
    

    _quit = cv2.waitKey(1) == 27