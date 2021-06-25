import time
import random

import mysql.connector

#config relay hat
#CH1  CH2  CH3  CH4  CH5  
#P21  P22  P23  P24  P25
# 29   31   33   35   37
relay_pin = [29,31,33,35,37]

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


GPIO.setup(relay_pin[0], GPIO.OUT) #set Relay 1 output 
GPIO.setup(relay_pin[1], GPIO.OUT) #set Relay 2 output 
GPIO.setup(relay_pin[2], GPIO.OUT) #set Relay 3 output
GPIO.setup(relay_pin[3], GPIO.OUT) #set Relay 4 output 
GPIO.setup(relay_pin[4], GPIO.OUT) #set Relay 5 output 


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="caracter",
  database="Amine"
)

mycursor = mydb.cursor()


sql_rezistente = "SELECT * FROM Rezistente ORDER BY NumberId DESC LIMIT 1;"

#  CREATE TABLE Inputs (
#     NumberId int NOT NULL AUTO_INCREMENT,
#     TimeStamp varchar(256),
#     Temp1 float,
#     Temp2 float,
#     Temp3 float,
#     Temp4 float,
#     Temp5 float,
#     Temp6 float,
#     PRIMARY KEY (NumberId)
# );

while True:
    
    
    
    #nu inteleg de ce, dar asta trebuie sa fie aici
    mydb.commit()
    
    
    
    
    mycursor.execute(sql_rezistente)
    myresult = mycursor.fetchall()
    print("citire din tabelul Rezistente:   " )
    print(myresult)


    rezistente = str(myresult).strip("])").split(',')[2:]
    #returneaza un array cu valorile pe care trebuie sa le aiba rezistentele
    print(rezistente)    
    #pentru fiecare rezistenta verificam daca trebuie sa fie pornita sa oprita si o pornim/oprim  
    for i in range(len(rezistente)):
        # print(rezistente[i])
        # print(" 1")
        if rezistente[i] == " 1":
        # if "A" == "A":
          GPIO.output(relay_pin[i], GPIO.HIGH) #turn relay  on
          print("rezistenta:    " + str(i+1) + "    e pornita")
        else:
          GPIO.output(relay_pin[i], GPIO.LOW) 
          print("rezistenta:    " + str(i+1) + "    e oprita")

    time.sleep( 1 )




