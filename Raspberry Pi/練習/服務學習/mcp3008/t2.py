import spidev
import time
import os

# open SPI bus
spi = spidev.SpiDev()
spi.close()
spi.open(0,0)

# read SPI data from  MCP3008 , Channel must be 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

# Define sensor channels
sw_ch = 0
vx_ch = 1
vy_ch = 2

# Define delay between readings
delay = 0.5

while True:

  # Read the joystick position data
  vx_pos = ReadChannel(vx_ch)
  print ReadChannel(0)
  # Wait time
  time.sleep(delay)