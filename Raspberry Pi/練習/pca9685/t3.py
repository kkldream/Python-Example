import Adafruit_PCA9685, time, readchar
pwm = Adafruit_PCA9685.PCA9685()
servo_min = 130
servo_max = 600
pwm.set_pwm_freq(60)
def pwmWrite(channel, pulse): # channel:0~15 pulse:0~180
	var = int(pulse / 180 * (servo_max - servo_min) + servo_min)
	pwm.set_pwm(channel, 0, var)
	print(var)
def pwmSet(angle):
	pwmWrite(14, angle[0])
	pwmWrite(15, angle[1])
try:
	motor_angle = [45, 90]
	pwmWrite(14, motor_angle[0])
	pwmWrite(15, motor_angle[1])
	print('Press Q to quit')
	print('---------------')
	while True:
		getch = readchar.readchar()
		if getch == 'q': break # 按 Q 跳出程式
		elif getch == '0':
			motor_angle = [0, 0]
			pwmSet(motor_angle)
		elif getch == '5':
			motor_angle = [45, 90]
			pwmSet(motor_angle)
		elif getch == '8':
			motor_angle[0] = motor_angle[0] + 5
			motor_angle[1] = motor_angle[1] + 10
			pwmSet(motor_angle)
		elif getch == '2':
			motor_angle[0] = motor_angle[0] - 5
			motor_angle[1] = motor_angle[1] - 10
			pwmSet(motor_angle)
except KeyboardInterrupt:
	print('關閉程式')
finally:
	motor_angle = [0, 0]
	pwmSet(motor_angle)
	print('---------------')
	print('Stop program')