Width = 1440
Height = 1080

import cv2, time, sys, os
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, Width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, Height)
if not cap.isOpened():
    print('VideoCapture is not open')
    exit()
elif len(sys.argv) <= 1:
    print('Use: python3 %s [Folder]' %sys.argv[0])
    exit()
elif not os.path.isdir(sys.argv[1]):
    print('mkdir %s' %sys.argv[1])
    os.mkdir(sys.argv[1])
switch = 0
photo_num = 0
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, -1)
    show_frame = cv2.resize(frame, (int(300 * Width / Height), 300))
    cv2.imshow('frame', show_frame)
    key = cv2.waitKey(1)
    if not key == -1:
        if key == ord('t'): switch = not switch
        if key == ord('q'): break
    if switch == 1:
        str = '%s/%s-%d.jpg' %(sys.argv[1], time.strftime("%Y%m%d-%H%M%S", time.localtime()), photo_num)
        print('Save:%s' %str)
        cv2.imwrite(str, frame)
        photo_num = photo_num + 1
cap.release()
cv2.destroyAllWindows()
