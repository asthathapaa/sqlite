import sqlite3
connection = sqlite3.connect('database.db')

db_astha = 'todo.db'
connection = sqlite3.connect(db_astha)
"""
connection.execute('drop table if exists staff')
print("Table staff Exists/Drop")
#creating Table
connection.execute('create table staff(ID int,Name text,Age int,Gender text)')
print("Table staff Created")
#insert Values
connection.execute('insert into staff(ID,Name,Age,Gender) values(0001,"Name at",21,"M")')
connection.execute('insert into staff(ID,Name,Age,Gender) values(0002,"Name st",28,"F")')
connection.execute('insert into staff(ID,Name,Age,Gender) values(0003,"Name ht",26,"M")')

connection.commit()
print("Rows are inserted in Table staff Created")

cursor = connection.cursor()

print("Displaying staff Created")
#cursor.execute('select * from staff')
#result = cursor.fetchall()
#result= cursor.fetchone()

result = connection.execute('select age from staff where age>25')
for rows in result:
    print(rows)"""


"""#creating Table
connection.execute('create table student(roll int,subject text,city text,phone text)')
print("Table student Created")"""
#insert values
connection.execute('insert into student(roll,subject,city,phone) values(" 001","eng","patan","redmi")')
connection.execute('insert into student(roll,subject,city,phone) values(" 002","sci","patan","iphone")')
connection.execute('insert into student(roll,subject,city,phone) values(" 003","math","patan","huwai")')


connection.commit()
print("Rows are inserted in Table student Created")

cursor = connection.cursor()

print("Displaying student Created")
cursor.execute('update student set city = "kathmandu" where phone="redmi"')
#result = cursor.fetchall()
#result= cursor.fetchone()

result = connection.execute('select * from student')
for rows in result:
    print(rows)
