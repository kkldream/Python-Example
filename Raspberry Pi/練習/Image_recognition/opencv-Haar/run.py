import cv2
import sys

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

cascade = cv2.CascadeClassifier('xml/cascade.xml')

while True:
    ret, img = cap.read()
    if ret == 1: break
print(img.shape)
while cap.isOpened():
    ret, img = cap.read()
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faceRects = cascade.detectMultiScale(grey, scaleFactor = 1.1, minNeighbors = 5)                                 
    for faceRect in faceRects:
        x, y, w, h = faceRect        
        cv2.rectangle(img, (x - 10, y - 10), (x + w + 10, y + h + 10), (255, 0, 0), 2)
    cv2.imshow('Haar', img)        
    if cv2.waitKey(1)==ord('q'): break

cap.release()
cv2.destroyAllWindows()
