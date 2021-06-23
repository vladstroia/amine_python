import time
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)

import adafruit_ads1x15.ads1115 as ADS

from adafruit_ads1x15.analog_in import AnalogIn

ads1 = ADS.ADS1115(i2c)
ads2 = ADS.ADS1115(i2c, address=0x49)     #pentru a doua placa

#ST1
# ads1_chan_0 = AnalogIn(ads1, ADS.P0)    #canalul 0 de pe placa 1
# #ST2
# ads1_chan_1 = AnalogIn(ads1, ADS.P1)    #canalul 1 de pe placa 1
# ads1_chan_2 = AnalogIn(ads1, ADS.P2)    #
# ads1_chan_3 = AnalogIn(ads1, ADS.P3)    #
# ads2_chan_0 = AnalogIn(ads1, ADS.P0)    #canalul 0 de pe placa 2
# #ST6
# ads2_chan_1 = AnalogIn(ads1, ADS.P1)    #canalul 1 de pe placa 2



# am grupat ce era mai sus intr-un vector
channels = [
          AnalogIn(ads1, ADS.P0),[AnalogIn(ads1, ADS.P1),
          [AnalogIn(ads1, ADS.P2),[AnalogIn(ads1, ADS.P3),
          [AnalogIn(ads2, ADS.P0),[AnalogIn(ads2, ADS.P1),
          ]




while True:
    # volt_st1 = ads1_chan_1.voltage
    # temp_st1 = 200*(volt_volt_st1-0.8)/3
    # print( volt_st1, temp_st1)
    # time.sleep(1) 

    val = [200*(channels[i].voltage - 0.8)/3 for i in range(channels)]