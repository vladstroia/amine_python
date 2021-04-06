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

sql = "INSERT INTO Inputs VALUES (%s,%s,%s,%s,%s, %s)"
#  val = (1,2,3,4,5,6)




while True:
    val = [round(random.uniform(20, 60), 2) for i in range (6)]
    mycursor.execute(sql, val)
    mydb.commit()
    time.sleep( 1 )












