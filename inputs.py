
import time

# import random

import mysql.connector

# #pt ads1115 (placa care citeste senzori de temp)
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)

import adafruit_ads1x15.ads1115 as ADS

from adafruit_ads1x15.analog_in import AnalogIn

ads1 = ADS.ADS1115(i2c)                   #prima placa ads1115
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
    AnalogIn(ads1, ADS.P0), AnalogIn(ads1, ADS.P1),
    AnalogIn(ads1, ADS.P2), AnalogIn(ads1, ADS.P3),
    AnalogIn(ads2, ADS.P0), AnalogIn(ads2, ADS.P1),
    ]















#conexiunea la baza de date
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="caracter",
  database="Amine"
)

mycursor = mydb.cursor()


# sql querry string
sql = ("INSERT INTO Inputs (TimeStamp, Temp1,Temp2,Temp3,Temp4,Temp5,Temp6) "
 "VALUES (%s, %s,%s,%s,%s,%s, %s)"
)
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
    # 6 valori random intr-o lista
    # val = [round(random.uniform(20, 60), 2) for i in range (6)]
    
    #val este lista cu cele 6 temperaturi
    #prin channel.voltage citim tensiunea inregistrata pe fiecare canal si apoi facem calculele necesare pt a gasi temperatura  
    val = [round(200*(channel.voltage - 0.8)/3, 2) for channel in channels]
    #functia "round" rotunjeste numarul la doua zecimale



    #scriem in tabelul Inputs valorile citite de senzorii de temp
    #adaugam timestamp 
    mytime = time.asctime( time.localtime(time.time()) )
    val =  [mytime] + val
    print("scriere in tabelul Inputs:   ")
    print(val)
    mycursor.execute(sql, val)
    mydb.commit()



    time.sleep( 1 )












