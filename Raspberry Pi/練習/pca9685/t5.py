import Adafruit_PCA9685, time, readchar
pwm = Adafruit_PCA9685.PCA9685()
servo_min = 130
servo_max = 600
pwm.set_pwm_freq(60)

class Servo_motor():
	def __init__(self, pin_1, pin_2):
		self.pwm = Adafruit_PCA9685.PCA9685()
		pwm.set_pwm_freq(60)
		self.pin = [pin_1, pin_2]
		self.max = 600
		self.min = 130
		self.angle = [45, 90]
		self.set_all()
	def set_one(self, channel, pulse): # channel:0~15 pulse:0~180
		var = int(pulse / 180 * (servo_max - servo_min) + servo_min)
		self.pwm.set_pwm(channel, 0, var)
	def set_all(self):
		self.set_one(self.pin[1], self.angle[1])
		self.set_one(self.pin[0], self.angle[0])
		print(self.angle)
	def set_angle(self, angle_1, angle_2):
		self.angle = [angle_1, angle_2]
		self.set_all()
	def add_angle(self, var):
		self.angle[0] = self.angle[0] + var
		if self.angle[0] > 90: self.angle[0] = 90
		elif self.angle[0] < 0: self.angle[0] = 0
		self.angle[1] = self.angle[1] + var * 2
		if self.angle[1] > 180: self.angle[1] = 180
		elif self.angle[1] < 0: self.angle[1] = 0
		self.set_all()
	def add_on_angle(self, var):
		self.angle[0] = self.angle[0] + var
		if self.angle[0] > 180: self.angle[0] = 180
		elif self.angle[0] < 0: self.angle[0] = 0
		self.set_all()
	def add_under_angle(self, var):
		self.angle[1] = self.angle[1] + var * 2
		if self.angle[1] > 180: self.angle[1] = 180
		elif self.angle[1] < 0: self.angle[1] = 0
		self.set_all()
		
try:
	pwm = Servo_motor(14, 15);
	pwm.set_angle(45, 90)
	print('Press Q to quit')
	print('---------------')
	while True:
		getch = readchar.readchar()
		if getch == 'q': break # 按 Q 跳出程式
		elif getch == '0':
			pwm.set_angle(0, 0)
		elif getch == '5':
			pwm.set_angle(45, 90)
		elif getch == '8':
			pwm.add_angle(5)
		elif getch == '2':
			pwm.add_angle(-5)
		elif getch == '7':
			pwm.set_angle(120, 160)
		elif getch == '4':
			pwm.set_angle(30, 100)
		elif getch == '1':
			pwm.set_angle(30, 60)
		elif getch == '6':
			for _ in range(3):
				pwm.set_angle(30, 100)
				time.sleep(0.5)
				pwm.set_angle(30, 60)
				time.sleep(0.5)
				pwm.set_angle(120, 160)
				time.sleep(0.5)
			pwm.set_angle(45, 90)
		
except KeyboardInterrupt:
	print('關閉程式')
finally:
	pwm.set_angle(0, 0)
	print('---------------')
	print('Stop program')