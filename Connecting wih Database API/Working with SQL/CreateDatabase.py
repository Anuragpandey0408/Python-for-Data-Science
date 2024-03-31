import mysql.connector  
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Anurag@2004"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE NewTest")
mydb.close()