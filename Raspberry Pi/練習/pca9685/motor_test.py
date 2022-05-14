import RPi.GPIO as GPIO
import time
import readchar
import Adafruit_PCA9685, time
pwm_angle = Adafruit_PCA9685.PCA9685()
pwm_speed = Adafruit_PCA9685.PCA9685()
def pwmAngle(pulse):
    global pwm_angle
    pwm_angle.set_pwm_freq(60)
    var = int(pulse / 100 * (300 - 500) + 500)
    pwm_angle.set_pwm(1, 0, var)
    print('pwmAngle:%d' %var)
def pwmSpeed(pulse):
    global pwm_speed
    pwm_speed.set_pwm_freq(500)
    var = 0
    if not pulse == 0: var = int(pulse / 100 * (4000 - 3580) + 3580)
    pwm_speed.set_pwm(0, 0, var)
    print('pwmSpeed:%d' %var)
try:
    print('Press Q to quit')
    print('---------------')
    while True:
        getch = readchar.readchar()
        if getch == 'q': break # 按 Q 跳出程式
        # -----停止-----
        elif getch == '5':
            print('Stop')
            pwmAngle(50)
            pwmSpeed(0)
        # -----前進-----
        elif getch == '8':
            print('Forward')
            pwmAngle(50)
            pwmSpeed(10)
        # -----後退-----
        elif getch == '2':
            print('Back')
            pwmAngle(50)
            pwmSpeed(10)
        # -----左旋-----
        elif getch == '4':
            print('Left')
            pwmAngle(0)
            #pwmSpeed(10)
        # -----右旋-----
        elif getch == '6':
            print('Right')
            pwmAngle(100)
            #pwmSpeed(10)
except KeyboardInterrupt:
    print('關閉程式')
finally:
    GPIO.cleanup()
    print('---------------')
    print('Stop program')