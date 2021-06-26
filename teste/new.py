import time


#CH1  CH2  CH3  CH4  CH5  
#P21  P22  P23  P24  P25
# 29   31   33   35   37
relay_pin = [29,31,33,35,37]


import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setmode(GPIO.BOARD)

#cred ca daca am pune GPIO.BOARD, atunci pinii ar fi de la 21 la 26

GPIO.setup(relay_pin[0], GPIO.OUT) #set Relay 1 output 
GPIO.setup(relay_pin[1], GPIO.OUT) #set Relay 2 output 
GPIO.setup(relay_pin[2], GPIO.OUT) #set Relay 3 output
GPIO.setup(relay_pin[3], GPIO.OUT) #set Relay 4 output 
GPIO.setup(relay_pin[4], GPIO.OUT) #set Relay 5 output 



while True:

    GPIO.output(relay_pin[0], GPIO.HIGH) #turn relay  on
    GPIO.output(relay_pin[1], GPIO.HIGH) #turn relay  on

    time.sleep(1)
    GPIO.output(relay_pin[0], GPIO.LOW) #turn relay  on
    GPIO.output(relay_pin[1], GPIO.LOW) #turn relay  on
    time.sleep(1)
