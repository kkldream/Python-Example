import RPi.GPIO as GPIO
import time
import readchar

PIN = [19, 26] 
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN[0], GPIO.OUT)
GPIO.setup(PIN[1], GPIO.OUT)
init = 8.5
l_pwm = GPIO.PWM(PIN[0], 60)
r_pwm = GPIO.PWM(PIN[1], 60)
l_pwm.start(0)
r_pwm.start(0)
try:
    print('Press Q to quit')
    print('---------------')
    while True:
        getch = readchar.readchar()
        if getch == 'q': break # 按 Q 跳出程式
        elif getch == '5':
            print('Stop')
            l_pwm.ChangeDutyCycle(0)
            r_pwm.ChangeDutyCycle(0)
        elif getch == '8':
            print('Forward')
            l_pwm.ChangeDutyCycle(init + 0.3)
            r_pwm.ChangeDutyCycle(init - 0.3)
        elif getch == '2':
            print('Back')
            l_pwm.ChangeDutyCycle(init - 0.3)
            r_pwm.ChangeDutyCycle(init + 0.3)
        elif getch == '6':
            print('Right')
            l_pwm.ChangeDutyCycle(init + 0.15)
            r_pwm.ChangeDutyCycle(init + 0.15)
        elif getch == '4':
            print('Left')
            l_pwm.ChangeDutyCycle(init - 0.15)
            r_pwm.ChangeDutyCycle(init - 0.15)
except KeyboardInterrupt:
    print('關閉程式')
finally:
    GPIO.cleanup()
    print('---------------')
    print('Stop program')