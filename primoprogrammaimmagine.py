import cv2
import numpy as np

immagine = cv2.imread('panorama.jpg')

immagineBN = cv2.cvtColor(immagine, cv2.COLOR_BGR2GRAY)
immagineBN = cv2.blur(immagineBN,(5,5))

thr1 = 100
thr2 = 200
_quit = False
# font
font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (800, 50)

# fontScale
fontScale = 1
 
# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2

#cv2.imshow ('mywin',immagine)

cv2.imshow ('bn',immagineBN)

sprite = np.zeros ((100,100,3),dtype=np.uint8)

while not _quit:
    edges = cv2.Canny(immagineBN,thr1,thr2)
    contours, hierarchy = cv2.findContours(edges,  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    
    
    newcontours = []
    for contorno in contours:
        if cv2.contourArea(contorno) > 30:
            newcontours.append (contorno)
    
    immaginenuova = cv2.drawContours(immagine.copy(), newcontours, -1, (0, 255, 0), 3) 
    
    edges = cv2.putText(edges, "{} {} {}".format(thr1,thr2,len(contours)), org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
 
    x = (immaginenuova.shape[1] - sprite.shape[1] )//2
    y = (immaginenuova.shape[0] - sprite.shape[0] ) // 2
 
    print (y, y+sprite.shape[0], x, x+sprite.shape[1])
 
    immaginenuova[y:y+sprite.shape[0] ,x:x+sprite.shape[1] ,: ] = sprite
    cv2.imshow ('mywin',immaginenuova)
    
    

    
    cv2.imshow ('edges',edges)
    carattere = cv2.waitKey(1)
    quit = carattere == 27

    if carattere == 43:
        thr1 += 1
    if carattere == 45:
        thr1 -= 1
    if carattere == 65:
        thr2 += 1
    if carattere == 83:
        thr2 -= 1
