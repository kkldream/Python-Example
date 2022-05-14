import RPi.GPIO as GPIO
import threading
import time
trigger_pin = [11,15,21,29]
echo_pin = [13,19,23,31]
ult_var = [0,0,0,0]
end = False
GPIO.setmode(GPIO.BOARD)
timeout = 5000
def get_distance(pin_num):
    GPIO.output(trigger_pin[pin_num], True)
    time.sleep(0.001)
    GPIO.output(trigger_pin[pin_num], False)
    count = timeout
    while GPIO.input(echo_pin[pin_num]) != True and count > 0:
        count = count - 1
    start = time.time()
    count = timeout
    while GPIO.input(echo_pin[pin_num]) != False and count > 0:
        count = count - 1
    finish = time.time()
    pulse_len = finish - start
    distance_cm = pulse_len * 340 *100 /2
    return distance_cm
def job(num):
    global ult_var
    while end==False:
        ult_var[num] = get_distance(num)
        time.sleep(0.1)
threads = []
for a in range(4):
    GPIO.setup(trigger_pin[a], GPIO.OUT)
    GPIO.setup(echo_pin[a], GPIO.IN)
    threads.append(threading.Thread(target = job, args = (a,)))
    threads[a].start()
try:
    while True:
        print('%d\t%d\t%d\t%d\n' %(ult_var[0],ult_var[1],ult_var[2],ult_var[3]))
        time.sleep(0.1)
finally:
    print('End')
    end=True