import mysql.connector as conn

"""Need to connect to MySQL Workbench"""
mydb = conn.connect(host="localhost", user="root", passwd="JJ62%3Q4Hd")  # connection variable
print(mydb)
"""If this ran successfully without any errors, it means the connection established successfully"""

cursor = mydb.cursor()  # pointer which 'll go through a table one-by-one and perform r/w opr: created a cursor
cursor.execute("show databases")  # execute the query
print(cursor.fetchall())  # show the results of the executed queries

"""Need to CTM above script"""
