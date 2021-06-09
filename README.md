# amine_python


Script care creeaza valori random de temperaturi si le scrie in baza de date mysql.



cum sa conectezi mai multe placi i2c la raspberry
https://www.instructables.com/Raspberry-PI-Multiple-I2c-Devices/







ADS1115 I2C addressing
You can setup the ADS1115 with one of four addresses, so you can place 4 ADS1115 chips on a single I2C bus:

    0x48, 0x49, 0x4a, 0x4b.

The addressing control is unusual in that you only need to use one input pin as the address control pin .

Normally you would need two inputs to switch between 4 addresses but the ADS1115 16-bit ADC uses a clever scheme. The single address input is sampled continuously and if you connect it to GND, VDD, SDA or SCL you can set the address from 0x48, 0x49, 0x4a, 0x4b respectively.
source : https://www.best-microcontroller-projects.com/ads1115.html
