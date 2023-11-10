import mysql.connector



db = mysql.connector.connect(host="localhost",database="new_schema",user="root",password="123123")

cursor = db.cursor()

cursor.execute("SELECT * FROM klients")


for x in cursor:
    print(x)