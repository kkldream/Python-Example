import time
import Adafruit_DHT
DHT_GPIO_PIN = 4
try:
    print('start')
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT_GPIO_PIN)
        print('溫度={0:0.1f}度C 濕度={1:0.1f}%'.format(temperature, humidity))
        time.sleep(0.01)
except KeyboardInterrupt:
    print('KeyboardInterrupt')
finally:
    print('finally')