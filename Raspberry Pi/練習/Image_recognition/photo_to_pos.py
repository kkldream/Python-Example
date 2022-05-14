from imutils import face_utils
import dlib, cv2, os, sys, threading

def photo_to_pos(num):
	global file
	str = '%s/%s'%(sys.argv[1], file[num])
	img = cv2.imread(str)
	fists = detector(img, 1)
	n = 0
	for fist in fists:
		img_copy = img.copy()
		(x, y, w, h) = face_utils.rect_to_bb(fist)
		pos_x = x + int(w / 2)
		pos_y = y + int(h / 2)
		if h > w: img_copy = img_copy[pos_y - int(h / 2):pos_y + int(h / 2), pos_x - int(h / 2):pos_x + int(h / 2)]
		else: img_copy = img_copy[pos_y - int(w / 2):pos_y + int(w / 2), pos_x - int(w / 2):pos_x + int(w / 2)]
		img_copy = cv2.resize(img_copy, (50,50))
		str = '%s%d-%s'%(sys.argv[2], n, file[num])
		cv2.imwrite(str, img_copy)
		n = n + 1
		print(str)
def photo_to_pos_run(start, end):
	for i in range(start, end):
		photo_to_pos(i)
if len(sys.argv) != 3:
	print('Use: python3 %s [From folder] [To folder]' %sys.argv[0])
	exit()
elif not os.path.isdir(sys.argv[1]):
	print('No find %s' %sys.argv[1])
	exit()
elif not os.path.isdir(sys.argv[2]):
	print('mkdir %s' %sys.argv[2])
	os.mkdir(sys.argv[2])

detector = dlib.simple_object_detector("detector.svm")
file = os.listdir(sys.argv[1])
num = 0
threading_num = 8
t = [threading.Thread(),
     threading.Thread(),
     threading.Thread(),
     threading.Thread(),
     threading.Thread(),
     threading.Thread(),
     threading.Thread(),
     threading.Thread()]
	 
for i in range(threading_num):
	start = len(file) // threading_num * i
	end = start + len(file) // threading_num
	t[i] = threading.Thread(target=photo_to_pos_run,args=(start,end,))
	t[i].start()
	
start = len(file) // threading_num * threading_num
end = len(file)
photo_to_pos_run(start, end)
