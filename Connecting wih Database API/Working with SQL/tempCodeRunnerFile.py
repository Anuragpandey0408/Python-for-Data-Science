import mysql.connector  
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Anurag@2004"
)
mycursor = mydb.cursor()
mycursor.execute("select * from newtest.newtest_table")
for i in mycursor.fetchall():
    print(i)
mydb.close() 