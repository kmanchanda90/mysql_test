"""Insert data inside a table"""
import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="JJ62%3Q4Hd")
cursor = mydb.cursor()
temp_var = """insert into karan.softwareone1 values(8, "karan manchanda", 'km@gmail.com', 1000, 30)"""
cursor.execute(temp_var)
cursor.execute(temp_var)
cursor.execute(temp_var)
cursor.execute(temp_var)
cursor.execute(temp_var)
cursor.execute(temp_var)
cursor.execute(temp_var)
cursor.execute(temp_var)
cursor.execute(temp_var)
cursor.execute(temp_var)
mydb.commit()   # mandatory: always need to commit the changes
cursor.execute("select * from karan.softwareone1")  # select * means select all the data
for i in cursor.fetchall():
    print(i)
