import RPi.GPIO as GPIO
import time
import readchar
import cv2
# -----openCV-----
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 160)
cascade = cv2.CascadeClassifier('xml/cascade.xml')
# -----宣告GPIO腳位-----
right_motot_pin = [19, 26]
left_motot_pin = [6, 13]
GPIO.setmode(GPIO.BCM)
for i in range(2):
	GPIO.setup(left_motot_pin[i], GPIO.OUT)
	GPIO.setup(right_motot_pin[i], GPIO.OUT)
left_pwm_0 = GPIO.PWM(left_motot_pin[0],100)
left_pwm_1 = GPIO.PWM(left_motot_pin[1],100)
right_pwm_0 = GPIO.PWM(right_motot_pin[0],100)
right_pwm_1 = GPIO.PWM(right_motot_pin[1],100)

# -----馬達控制函式-----
# motor 輸入 0 控制左輪，輸入 1 控制右輪
# speed 輸入範圍 100 ~ -100
def motorWrite(motor, speed):
	if motor == 0:
		if speed == 0:
			left_pwm_0.stop()
			left_pwm_1.stop()
			GPIO.output(left_motot_pin[0],False)
			GPIO.output(left_motot_pin[1],False)
		elif speed > 0:
			left_pwm_1.stop()
			GPIO.output(left_motot_pin[1],False)
			left_pwm_0.start(speed)
		elif speed < 0:
			left_pwm_0.stop()
			GPIO.output(left_motot_pin[0],False)
			left_pwm_1.start(speed * -1)
	if motor == 1:
		if speed == 0:
			right_pwm_0.stop()
			right_pwm_1.stop()
			GPIO.output(right_motot_pin[0],False)
			GPIO.output(right_motot_pin[1],False)
		elif speed > 0:
			right_pwm_1.stop()
			GPIO.output(right_motot_pin[1],False)
			right_pwm_0.start(speed)
		elif speed < 0:
			right_pwm_0.stop()
			GPIO.output(right_motot_pin[0],False)
			right_pwm_1.start(speed * -1)

# -----主程式-----
try:
	while True:
		ret, img = cap.read()
		if ret == 1: break
	print(img.shape)
	while cap.isOpened():
		ret, img = cap.read()
		img = cv2.flip(img, -1)
		img = img[60:150, 0:160]
		grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		#faceRects = cascade.detectMultiScale(grey, scaleFactor = 1.1, minNeighbors = 5, minSize = (20,20), maxSize = (200,200))                                 
		faceRects = cascade.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 10)                                 
		x = 160
		for faceRect in faceRects:
			x, y, w, h = faceRect
			x = int(x + h / 2)
			y = int(y + w / 2)
			text = '(%d, %d)' %(x, y)
			cv2.putText(img, text, (150, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1, cv2.LINE_AA)
			cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
			#cv2.rectangle(img, (x - 10, y - 10), (x + w + 10, y + h + 10), (255, 0, 0), 2)
		cv2.imshow('Haar', img)  
		if x > 90:
			print('Left')
			motorWrite(0,60)
			motorWrite(1,-60)
			time.sleep(0.1)
			motorWrite(0,0)
			motorWrite(1,0)
		if x < 70:
			print('Right')
			motorWrite(0,-60)
			motorWrite(1,60)
			time.sleep(0.1)
			motorWrite(0,0)
			motorWrite(1,0)
		if cv2.waitKey(1)==ord('q'): break
except KeyboardInterrupt:
	print('關閉程式')
finally:
	GPIO.cleanup()
	print('---------------')
	print('Stop program')