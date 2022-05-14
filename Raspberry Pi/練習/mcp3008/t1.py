import time
import Adafruit_GPIO.SPI, Adafruit_MCP3008

adc = Adafruit_MCP3008.MCP3008(spi=Adafruit_GPIO.SPI.SpiDev(0, 0))
 
try:
    print('start')
    while True:
        var = adc.read_adc(0)
        print(var)
        time.sleep(0.1)
except KeyboardInterrupt:
    print('KeyboardInterrupt')
finally:
    print('finally')