import mysql.connector

db = mysql.connector.connect(host="localhost",database="remontdarbnica",user="root",password="123456")

print(db)