import Adafruit_PCA9685, time
pwm = Adafruit_PCA9685.PCA9685()
servo_min = 300
servo_max = 500
pwm.set_pwm_freq(500)
def pwmWrite(channel, pulse): # channel:0~15 pulse:0~180
    var = int(pulse / 180 * (servo_max - servo_min) + servo_min)
    pwm.set_pwm(channel, 0, var)
    print(var)

channel = int(input('channel:'))
while True:
	var = int(input())
	#pwmWrite(channel, var)
	pwm.set_pwm(channel, 0, var)
	print(var)