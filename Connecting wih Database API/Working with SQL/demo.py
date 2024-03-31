import mysql.connector  
#this library is used for connect database and python

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Anurag@2004"
)

print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)