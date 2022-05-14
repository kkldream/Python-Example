from imutils import face_utils
import dlib
import cv2

detector = dlib.simple_object_detector("detector.svm")
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
while True:
    ret, img = cap.read()
    if ret == 1: break
print(img.shape)
while(True):
    ret, img = cap.read()
    img = cv2.flip(img, 0)
    #img = img[160:320, 0:320]
    #img = cv2.resize(img, (120, 60))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fists = detector(gray, 1)
    for fist in fists:
        (x, y, w, h) = face_utils.rect_to_bb(fist)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
    img = cv2.flip(img,1)
    img = cv2.resize(img, (640, 320))
    cv2.imshow('Display', img)
    if cv2.waitKey(1)==ord('q'): break
cap.release()
cv2.destroyAllWindows()

