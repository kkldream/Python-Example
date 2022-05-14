import RPi.GPIO as GPIO
import time

channel = 11 #管脚40，参阅树莓派引脚图，物理引脚40对应的BCM编码为21

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

while True:
    print(GPIO.input(channel))
    time.sleep(1)