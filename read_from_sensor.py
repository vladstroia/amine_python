import time
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)

import adafruit_ads1x15.ads1115 as ADS

from adafruit_ads1x15.analog_in import AnalogIn

ads = ADS.ADS1115(i2c)

chan = AnalogIn(ads, ADS.P0)
#ads.gain = 2/3

while True:
    volt = chan.voltage
    temp = 200*(volt-0.8)/3
    print( volt, temp)
    time.sleep(1) 

