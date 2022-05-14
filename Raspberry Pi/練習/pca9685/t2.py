import Adafruit_PCA9685, time
pwm = Adafruit_PCA9685.PCA9685()
servo_min = 130
servo_max = 600
pwm.set_pwm_freq(60)
def pwmWrite(channel, pulse): # channel:0~15 pulse:0~180
    var = int(pulse / 180 * (servo_max - servo_min) + servo_min)
    pwm.set_pwm(channel, 0, var)
    print(var)
while True:
    pwmWrite(15, 0)
    time.sleep(1)
    pwmWrite(15, 180)
    time.sleep(1)