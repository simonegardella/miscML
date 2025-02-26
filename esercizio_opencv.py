import cv2
import numpy as np


immagine = cv2.imread('quadrato.png')

immagineGray = cv2.cvtColor(immagine.copy(),cv2.COLOR_BGR2GRAY)
immagineCanny = cv2.Canny(immagineGray,50,150)

immaginefinta = np.zeros_like(immagine)

for y in range (immagineGray.shape[0]):
    for x in range (immagineGray.shape[1]):
        grigio = immagineGray [y,x]
        immaginefinta[y,x,:] = [grigio,grigio,grigio]

contorni, gerarchia = cv2.findContours(immagineCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

contorno  = contorni[0]
print (contorno)
lastpoint = contorno[0][0]
for punto in contorno:
    prossimopunto = punto[0]
    cv2.line (immagine,lastpoint,prossimopunto,(255,0,0),1)
    lastpoint = prossimopunto
    
cv2.line (immagine,lastpoint,contorno[0][0],(255,0,0),1)


cv2.imshow ('immagine',immagine)
cv2.imshow ('immaginegray',immagineGray)
cv2.imshow ('immagineCanny',immagineCanny)
cv2.imshow ('immagineFinta',immaginefinta)
cv2.waitKey(0)