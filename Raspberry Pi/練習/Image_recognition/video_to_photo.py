import cv2, time, sys, os
if len(sys.argv) <= 2:
	print('Use: python3 %s [Video] [Folder]' %sys.argv[0])
	exit()
elif not os.path.isfile(sys.argv[1]):
	print('No find %s' %sys.argv[1])
	exit()
elif not os.path.isdir(sys.argv[2]):
	print('mkdir %s' %sys.argv[2])
	os.mkdir(sys.argv[2])
cap = cv2.VideoCapture(sys.argv[1])
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
photo_num = 0
while(True):
	ret, frame = cap.read()
	if not ret: exit()
	str = '%s/%d.jpg' %(sys.argv[2], photo_num)
	print('Save:%s' %str)
	cv2.imwrite(str, frame)
	frame = cv2.resize(frame, (int(360/cap.get(cv2.CAP_PROP_FRAME_HEIGHT)*cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 360))  
	cv2.imshow('frame', frame)
	photo_num = photo_num + 1
	if cv2.waitKey(1)==ord('q'): break
cap.release()
cv2.destroyAllWindows()