import mysql.connector

mydb = mysql.connector.connect(host="localhost", user='root', passwd="tyro@1234",database="detectiveconan")

mycursor = mydb.cursor()

# mycursor.execute("show databases")

mycursor.execute("select * from student")

# result = mycursor.fetchall()
result = mycursor.fetchone()

for i in result:
	print(i)

