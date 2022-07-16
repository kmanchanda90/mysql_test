"""Get specific column from a table"""
import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="JJ62%3Q4Hd")
cursor = mydb.cursor()
cursor.execute("select emp_id, emp_mail_id from karan.softwareone1")  # select * means select all the data
l = []
for i in cursor.fetchall():
    # print(i)   # one row in the form of a tuple
    l.append(i)

print(l)
print(type(l[0]))
# cursor.fetchall(): it returns all the data in the form of iterable object, thus, we can use for loop to get the data