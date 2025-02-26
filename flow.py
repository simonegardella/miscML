import cv2
vc = cv2.VideoCapture(0)
while True:
    frame = vc.read()
    cv2.imshow('Video',frame[1])
    cv2.waitKey(1)