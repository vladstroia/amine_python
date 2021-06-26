import time

# import random


# #pt ads1115 (placa care citeste senzori de temp)
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)

import adafruit_ads1x15.ads1115 as ADS

from adafruit_ads1x15.analog_in import AnalogIn

ads1 = ADS.ADS1115(i2c)                   #prima placa ads1115
ads2 = ADS.ADS1115(i2c, address=0x49)     #pentru a doua placa



channel1 = AnalogIn(ads1, ADS.P0)
channel2 = AnalogIn(ads2, ADS.P0)
while True:
    print("ch1:         "+str(channel1.voltage))
    print("ch2:         " + str(channel2.voltage))
    time.sleep(1)
