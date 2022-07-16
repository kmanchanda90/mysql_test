"""< >"""


import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="JJ62%3Q4Hd", db = "karan777")
print(mydb)
cursor = mydb.cursor()