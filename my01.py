"""Create a database and table inside that database"""
import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="JJ62%3Q4Hd")
print(mydb)
cursor = mydb.cursor()
# cursor.execute("create database karan")

# s = "create table karan.softwareone3(emp_id int(10), emp_name varchar(80), emp_mail_id varchar(20), emp_sal int(6), " \
#     "emp_attendance int(3) ) "
# q1 = cursor.execute(s)

q2 = cursor.execute("select * from karan.softwareone1")
print(cursor.fetchall())
