import cv2
import numpy as np

sciatore = cv2.imread('sciatore.jpg')

yMax, xMax = sciatore.shape[:2]
raggio = 10
_quit = False
x= xMax //2 - raggio
y= yMax //2 - raggio
deltaX = 1
deltaY = 1

pallina = np.ones((raggio*2,raggio*2,3), dtype=np.uint8)
cv2.circle(pallina,(raggio,raggio),raggio,(0,0,255),3)
yPallina, xPallina = pallina.shape[:2]


while not _quit:
    
    frame = sciatore.copy()
    frame[y:y+yPallina,x:x+xPallina,:] = pallina.copy()
    
    if x ==0 or x+xPallina == xMax-1:
        deltaX = -deltaX
    if y == 0 or y+yPallina == yMax-1:
        deltaY = -deltaY
    x += deltaX
    y += deltaY
    cv2.imshow('Mia finestra', frame)
    _quit = cv2.waitKey(1) == 27 # Carattere ESC