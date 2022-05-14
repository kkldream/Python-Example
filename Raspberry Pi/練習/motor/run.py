import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

cascade = cv2.CascadeClassifier('xml/cascade.xml')

while True:
    ret, img = cap.read()
    if ret == 1: break
print(img.shape)
while cap.isOpened():
    ret, img = cap.read()
    img = cv2.flip(img, -1)
    img = img[120:300, 0:320]
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #faceRects = cascade.detectMultiScale(grey, scaleFactor = 1.1, minNeighbors = 5, minSize = (20,20), maxSize = (200,200))                                 
    faceRects = cascade.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 10)                                 
    for faceRect in faceRects:
        x, y, w, h = faceRect
        x = int(x + h / 2)
        y = int(y + w / 2)
        text = '(%d, %d)' %(x, y)
        cv2.putText(img, text, (10, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        #cv2.rectangle(img, (x - 10, y - 10), (x + w + 10, y + h + 10), (255, 0, 0), 2)
    cv2.imshow('Haar', img)        
    if cv2.waitKey(1)==ord('q'): break

cap.release()
cv2.destroyAllWindows()
