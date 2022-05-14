from imutils import face_utils
import dlib, cv2, shutil, os, threading

def write_data(num):
	global file
	img = cv2.imread('photo/%s' %file[num])
	mat = detector(img, 1)
	if len(mat) >= 1:
		str = '  <image file=\'photo/%s\'>\n' %file[num]
		for i in range(len(mat)):
			(x, y, w, h) = face_utils.rect_to_bb(mat[i])
			str = str + '    <box top=\'%d\' left=\'%d\' width=\'%d\' height=\'%d\'/>\n' %(y, x, w, h)
			print('%d: %s: %d %d %d %d' %(len(file) - num, file[num], y, x, w, h))
		xml.write(str + '  </image>\n')
	else:
		shutil.move('photo/%s' %file[num], 'photo_fail')
def write_data_run(start, end):
	for i in range(start, end):
		write_data(i)

detector = dlib.simple_object_detector("detector.svm")

if not os.path.isdir('photo_fail'):
	print('mkdir photo_fail')
	os.mkdir('photo_fail')
    
file = os.listdir("photo")
xml = open('data.xml','w')
str = '\
<?xml version=\'1.0\' encoding=\'ISO-8859-1\'?>\n\
<?xml-stylesheet type=\'text/xsl\' href=\'image_metadata_stylesheet.xsl\'?>\n\
<dataset>\n\
<name>imglab dataset</name>\n\
<comment>Created by imglab tool.</comment>\n\
<images>\n'
xml.write(str)
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
	t[i] = threading.Thread(target=write_data_run,args=(start,end,))
	t[i].start()
	
start = len(file) // threading_num * threading_num
end = len(file)
write_data_run(start, end)

for i in range(8):
	while t[i].is_alive(): pass
str = '\
</images>\n\
</dataset>\n'
xml.write(str)
