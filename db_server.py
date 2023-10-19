import mysql.connector

db = mysql.connector.connect(host="localhost",database = "123", user="root",password=" ")
print(db)

#metode .cursor()

cursor = db.cursor()

#.execute()
#.execute(sql,dati)

#sql kods datu ievietošanai
sql = ("""
insert into klients (idnew_table,klienta_vards,klienta_uzvards,telefona_numurs)
values (%s,%s,%s,%s);
""")
#Ievietojamie dati
dati = (785,"asd","zxcf",23452324)

cursor.execute(sql,dati)

#Apstiprināšana
db.commit()
