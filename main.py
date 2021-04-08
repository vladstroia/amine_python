import time
import random

import mysql.connector

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

# ); CREATE TABLE Inputs (
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
    val = [round(random.uniform(20, 60), 2) for i in range (6)]
    
    #adaugam timestamp 
    mytime = time.asctime( time.localtime(time.time()) )
    val =  [mytime] + val
    print(val)
    mycursor.execute(sql, val)
    mydb.commit()
    time.sleep( 1 )












