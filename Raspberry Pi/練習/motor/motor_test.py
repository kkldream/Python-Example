import RPi.GPIO as GPIO
import time
import readchar

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
    print('Press Q to quit')
    print('---------------')
    while True:
        getch = readchar.readchar()
        if getch == 'q': break # 按 Q 跳出程式
        # -----停止-----
        elif getch == '5':
            print('Stop')
            motorWrite(0,0)
            motorWrite(1,0)
        # -----前進-----
        elif getch == '8':
            print('Forward')
            motorWrite(0,60)
            motorWrite(1,60)
        # -----後退-----
        elif getch == '2':
            print('Back')
            motorWrite(0,-60)
            motorWrite(1,-60)
        # -----左旋-----
        elif getch == '4':
            print('Left')
            motorWrite(0,-50)
            motorWrite(1,50)
        # -----右旋-----
        elif getch == '6':
            print('Right')
            motorWrite(0,50)
            motorWrite(1,-50)
        # -----左-前進-----
        elif getch == '7':
            print('Left-Forward')
            motorWrite(0,60)
            motorWrite(1,100)
        # -----右-前進-----
        elif getch == '9':
            print('Right-Forward')
            motorWrite(0,100)
            motorWrite(1,60)
        # -----左-後退-----
        elif getch == '1':
            print('Left-Back')
            motorWrite(0,-60)
            motorWrite(1,-100)
        # -----右-後退-----
        elif getch == '3':
            print('Right-Back')
            motorWrite(0,-100)
            motorWrite(1,-60)
except KeyboardInterrupt:
    print('關閉程式')
finally:
    GPIO.cleanup()
    print('---------------')
    print('Stop program')